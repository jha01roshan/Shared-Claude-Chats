# Borrowing without types implementation review

- Source: https://claude.ai/share/05c0f205-b4a2-435e-a33c-cfeb3ce2de8e
- Author: Jamie
- Created: 2026-04-20
- Messages: 2

---

## Human

Look for bugs in https://raw.githubusercontent.com/jamii/jams/refs/heads/main/0007-borrowing-without-types/lib.zig. Use https://www.scattered-thoughts.net/writing/borrow-checking-without-type-checking as a reference to understand the purpose. Bear in mind that that post is a few days out of date - the provenance is no longer stored on a second stack but in the ref itself.

---

## Assistant

Let me fetch both the code and the reference post.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Now let me analyze the code carefully with the blog post as context. I'll focus on semantics, not style.

Here are the bugs and issues I found:

---

### 1. Double-free on error paths in `evalPatternOwned` (nested destructuring with owned refs)

When `evalPatternOwned` processes a tuple pattern, it iterates through elements and copies each one (including ref pointers) to new stack allocations. If a *later* sub-pattern fails, the *earlier* ones have already been pushed onto `c.stack` with copies of heap pointers. Back in `evalPattern`, the `errdefer item.deinit()` fires and calls `freeRefs` on the original item, freeing the heap data. But the already-pushed sub-patterns still hold the same pointers and will be freed again when the stack is eventually cleaned up (via `deinitStacks`).

Concrete trigger:

```
let [a, [b, c]] = [ref(1), 2]
```

Trace:
- `evalPatternOwned` for `a` succeeds: copies the `ref(1)` pointer to a new stack slot and pushes `a`.
- `evalPatternOwned` for `[b, c]` fails: `checkKind` expects `.tuple` but gets `.number`.
- `errdefer item.deinit()` fires in `evalPattern`, calling `freeRefs` on the original tuple → frees the heap allocation behind `ref(1)`.
- `a` is still on `c.stack` holding the same (now-freed) pointer.
- When `deinitStacks` later pops `a` and calls `a.deinit()` → `freeRefs` → double-free.

The analogous `evalPatternRef` case (the `.ref` branch in `evalPattern`) has a similar partial-push problem. If `evalPatternRef` succeeds for the first element of a tuple but fails on a later one, the first element's `splitBorrow`/`share` was already applied and a new ref was already pushed. The `defer item.deinit()` drops the original borrow, but the partial sub-refs remain on the stack with their ref-count adjustments, and their cleanup during error recovery may produce incorrect ref-count states (though this is less severe since it doesn't cause a use-after-free, just wrong counts during teardown).

**Fix:** Add cleanup for already-pushed sub-patterns on failure. One approach is to record `c.stack.len` before the loop in the `.tuple` branch of `evalPatternOwned`, and on error, pop and deinit everything pushed since then before returning.

---

### 2. Uninitialised provenance for `ref_any`'s second word

A `ref_any` has word size 2 (pointer + type_id). When created:

```zig
// in the .ref_any builtin:
const ref = Value.allocStack(Type.internRefAny());
ref.setRefElem(target);
ref.getProvenance().?.* = .owned;
```

`allocStack` `@memset`s the provenance slice to `undefined` (in debug), then `getProvenance()` writes only the *first* provenance slot (at `word_offset 0`). The second slot — corresponding to the stored `TypeId` word — is left as uninitialised garbage.

This second slot is never directly *interpreted* via `getRefIndexes` (which only returns `word_offset=0` for refs), so it doesn't cause incorrect behaviour today. But it *is* blindly copied by `copyProvenance` and `std.mem.copyForwards` in `stackCompact`. If you ever add debug checks that scan the full provenance slice, or if the uninitialised bits happen to look like a valid `Provenance` to a future check, this becomes a real problem.

**Fix:** After setting the ref provenance, also set the second word to `.not_a_ref`:

```zig
ref.getProvenance().?.* = .owned;
// For ref_any (word size 2), mark the type-id word's provenance too:
if (ref.type_id.getWordSize() > 1) {
    Value.getProvenanceSlice(ref).?[1] = .not_a_ref;
}
```

The same issue applies in `stackPushRef`, which always creates a known ref (`Type.internRef`), so it's only word-size 1 and this doesn't bite there. But if `stackPushRef` were ever generalised to handle `ref_any`, it would inherit the bug.

---

### 3. `with_new_stack` creates duplicate dummy items when `owner == lender`

When transferring borrowed/shared refs to the new stack, the code always creates *two* dummy stack items — one for `owner` and one for `lender`:

```zig
const owner = c.stack.len;
stackPushEmptyTuple(stacks_old.stack.items[ref_provenance.owner].expr_id);
const lender = c.stack.len;
stackPushEmptyTuple(stacks_old.stack.items[ref_provenance.lender].expr_id);
```

When `ref_provenance.owner == ref_provenance.lender` (which is the common case for a direct borrow), this creates two separate dummies where one would do. More importantly, if *multiple* refs in the closure share the same owner/lender pair in the old stack, each gets its *own* pair of dummies. This means refs that should be tracked against the same variable are now tracked against independent variables, which can allow operations that should conflict. For example, two refs that borrow from the same outer variable should prevent sharing from that variable, but with independent dummies each only sees its own borrow.

**Fix:** Maintain a map from old-stack index → new-stack dummy index, and reuse dummies for the same owner/lender.

---

### 4. `with_new_stack` doesn't call `result.deinit()` — relies on `deinitStacks` to not double-free

After:
```zig
const result = c.stack.pop();
errdefer result.deinit();
```

On the success path, `result` is never deinit'd — its data (including owned-ref heap pointers) is copied to `result_old` on the old stack, then the new stack is torn down via `c.deinitStacks()`. This is *correct* because `result` was popped from the stack items, so `deinitStacks` won't touch it, and the heap pointers are now owned by `result_old`.

However, `result.value`'s ref pointers are still live in the new `stack_data` when `allocator.free(compiler.stack_data)` runs. If the allocator does any use-after-free detection on the freed `stack_data` block, it could flag these dangling pointers. More critically, if `deinitStacks` fails to pop all items cleanly (e.g. due to a debug assert in an intermediate item's `deinit`), the error handling could leave `result` leaking its heap data.

This isn't a bug per se, but it's fragile. A safer pattern would be to null out `result`'s ref pointers after copying them to `result_old`, similar to how `.move` uses `setRefsToNull`.

---

### 5. `calculateWordOffsets` returns `&.{}` for closures — inconsistent with tuples

```zig
fn calculateWordOffsets(@"type": Type) []usize {
    switch (@"type") {
        .number, .ref, .closure => return &.{},
        .tuple => |tuple| { ... }
    }
}
```

Closures share the same in-memory layout as tuples (captures are stored contiguously), and `makeRefIndexes` / `calculateWordSize` both handle closures by iterating `getElems()`. But `calculateWordOffsets` returns empty for closures. This is currently safe because closures are always accessed via `getClosureCaptures()` which returns a tuple-typed view, so `getWordOffset` is only ever called on the tuple type. But if anyone ever calls `getWordOffset` on a closure type directly, they'd get an out-of-bounds panic. It's an internal consistency issue that could bite during future refactoring.

---

### 6. Minor: `freeRefs` treats `.not_a_ref` as `unreachable` — but `ref` builtin's check accepts it

In the `ref`/`ref_any` builtin:
```zig
for (arg0.value.type_id.getRefIndexes()) |ref_index| {
    const lease = arg0.value.getRefAtIndex(ref_index).getProvenance().?.lease;
    switch (lease) {
        .not_a_ref, .owned => {},  // <-- accepts not_a_ref
        .borrowed, .shared => { return fail(...); },
    }
}
```

A ref position with `.not_a_ref` provenance is silently accepted here, which masks a bug elsewhere (a ref index should *always* have a ref provenance). If this ever triggers, it means something upstream failed to initialise provenance, and silently allowing it could lead to a heap leak (the ref would be treated as non-existent and never freed).

---

The most impactful bug is **#1** (the double-free in `evalPatternOwned`), which is a real memory safety issue triggered by runtime type mismatches in destructuring patterns that contain owned refs.
