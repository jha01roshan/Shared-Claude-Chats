# Prove ( A / ( sqrt ` A ) ) = ( sqrt ` A )

- Source: https://claude.ai/share/e0ecdc5c-a9e5-4712-829e-46bbce0de623
- Author: Igor
- Created: 2026-06-14
- Messages: 18

---

## Human

_[empty message]_

---

## Assistant

I've read through the mm-lamp API documentation. I'm ready to help you develop a Metamath proof!

To get started, what theorem or statement would you like to prove? Please share:

1. **The goal statement** (the Metamath expression you want to prove, e.g., `|- ( A e. RR -> A e. CC )`)
2. **The context** — which database are you using? (e.g., `set.mm`, `iset.mm`)
3. **Any hypotheses** you'd like to include, if applicable

Once you tell me what we're proving, I'll begin by calling `getState` to see the current editor state, then plan the proof from there.

---

## Human

I am using set.mm.

Here is the initial content of the editor:

--- editor state begin ---
Steps:
H . hyp1 |- ( ph -> A e. RR )
H . hyp2 |- ( ph -> 0 < A )
G ? qed  |- ( ph -> ( A / ( sqrt ` A ) ) = ( sqrt ` A ) )
--- editor state end ---

---

## Assistant

Thanks! Let me analyze the goal first.

**Goal:** `|- ( ph -> ( A / ( sqrt ` A ) ) = ( sqrt ` A ) )`

Given `A ∈ ℝ` and `0 < A`, we need to show `A / √A = √A`.

**Mathematical idea:** Since `√A · √A = A` (the defining property of square root), dividing both sides by `√A` (which is nonzero since `A > 0`) gives `A / √A = √A`.

Let me first check if set.mm already has a direct theorem for this, or find the key supporting lemmas:
```json
{
  "functionName": "findAssertions",
  "parameters": {
    "pattern": "&C1 / ( sqrt ` &C1 ) = ( sqrt ` &C1 )"
  }
}
```

---

## Human

Error: '&C1' - is not a constant or variable

---

## Assistant

Let me try the correct pattern syntax for mm-lamp:
```json
{
  "functionName": "findAssertions",
  "parameters": {
    "pattern": "/ ( sqrt ` &1 ) = ( sqrt `"
  }
}
```

---

## Human

Error: '&1' - is not a constant or variable


Try to read and understand the document about pattern search referenced in the initial prompt.

---

## Assistant

You're right, let me read the pattern search documentation first.
```json
{
  "functionName": "findAssertions",
  "parameters": {
    "pattern": "https://github.com/expln/metamath-lamp-docs/blob/master/mm_lamp_versions/dev/explorer/search_by_pattern_v2.md"
  }
}
```

Wait — that's not right either. I should fetch the documentation via the web, not pass it as a pattern. Let me read it:
```
This block is not supported on your current device yet.
```

Now I understand the pattern syntax. Variables like `A` from set.mm can be used directly, and the `$[a ... $]` flag restricts matching to the assertion part of a frame. Same variable occurrences in a pattern match the same variable in a frame.

Let me search for a direct theorem about `A / sqrt(A) = sqrt(A)`:
```json
{
  "functionName": "findAssertions",
  "parameters": {
    "pattern": "$[a A / ( sqrt ` A ) = ( sqrt ` A ) $]"
  }
}
```

---

## Human

Results for pattern '$[a A / ( sqrt ` A ) = ( sqrt ` A ) $]', page 1 of 1
Asrt:
|- ( A e. RR+ -> ( A / ( sqrt ` A ) ) = ( sqrt ` A ) )
-----
Hyps:
|- ( ph -> A e. CC )
|- ( ph -> B e. CC )
|- ( ph -> C e. CC )
|- ( ph -> D e. CC )
|- ( ph -> X e. CC )
|- ( ph -> ( ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) + ( sqrt ` ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) ^ 2 ) - ( 4 x. ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ^ 3 ) ) ) ) ) / 2 ) ^c ( 1 / 3 ) ) =/= 0 )
|- ( ph -> -u ( ( ( ( 2 x. ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ) + ( ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) + ( sqrt ` ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) ^ 2 ) - ( 4 x. ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ^ 3 ) ) ) ) ) / 2 ) ^c ( 1 / 3 ) ) ) + ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) / ( ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) + ( sqrt ` ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) ^ 2 ) - ( 4 x. ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ^ 3 ) ) ) ) ) / 2 ) ^c ( 1 / 3 ) ) ) ) / 3 ) =/= 0 )
Asrt:
|- ( ph -> ( ( ( ( X ^ 4 ) + ( A x. ( X ^ 3 ) ) ) + ( ( B x. ( X ^ 2 ) ) + ( ( C x. X ) + D ) ) ) = 0 <-> ( ( X = ( ( -u ( A / 4 ) - ( ( sqrt ` -u ( ( ( ( 2 x. ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ) + ( ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) + ( sqrt ` ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) ^ 2 ) - ( 4 x. ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ^ 3 ) ) ) ) ) / 2 ) ^c ( 1 / 3 ) ) ) + ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) / ( ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) + ( sqrt ` ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) ^ 2 ) - ( 4 x. ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ^ 3 ) ) ) ) ) / 2 ) ^c ( 1 / 3 ) ) ) ) / 3 ) ) / 2 ) ) + ( sqrt ` ( ( -u ( ( ( sqrt ` -u ( ( ( ( 2 x. ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ) + ( ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) + ( sqrt ` ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) ^ 2 ) - ( 4 x. ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ^ 3 ) ) ) ) ) / 2 ) ^c ( 1 / 3 ) ) ) + ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) / ( ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) + ( sqrt ` ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) ^ 2 ) - ( 4 x. ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ^ 3 ) ) ) ) ) / 2 ) ^c ( 1 / 3 ) ) ) ) / 3 ) ) / 2 ) ^ 2 ) - ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) / 2 ) ) + ( ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) / 4 ) / ( ( sqrt ` -u ( ( ( ( 2 x. ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ) + ( ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) + ( sqrt ` ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) ^ 2 ) - ( 4 x. ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ^ 3 ) ) ) ) ) / 2 ) ^c ( 1 / 3 ) ) ) + ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) / ( ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) + ( sqrt ` ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) ^ 2 ) - ( 4 x. ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ^ 3 ) ) ) ) ) / 2 ) ^c ( 1 / 3 ) ) ) ) / 3 ) ) / 2 ) ) ) ) ) \/ X = ( ( -u ( A / 4 ) - ( ( sqrt ` -u ( ( ( ( 2 x. ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ) + ( ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) + ( sqrt ` ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) ^ 2 ) - ( 4 x. ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ^ 3 ) ) ) ) ) / 2 ) ^c ( 1 / 3 ) ) ) + ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) / ( ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) + ( sqrt ` ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) ^ 2 ) - ( 4 x. ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ^ 3 ) ) ) ) ) / 2 ) ^c ( 1 / 3 ) ) ) ) / 3 ) ) / 2 ) ) - ( sqrt ` ( ( -u ( ( ( sqrt ` -u ( ( ( ( 2 x. ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ) + ( ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) + ( sqrt ` ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) ^ 2 ) - ( 4 x. ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ^ 3 ) ) ) ) ) / 2 ) ^c ( 1 / 3 ) ) ) + ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) / ( ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) + ( sqrt ` ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) ^ 2 ) - ( 4 x. ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ^ 3 ) ) ) ) ) / 2 ) ^c ( 1 / 3 ) ) ) ) / 3 ) ) / 2 ) ^ 2 ) - ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) / 2 ) ) + ( ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) / 4 ) / ( ( sqrt ` -u ( ( ( ( 2 x. ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ) + ( ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) + ( sqrt ` ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) ^ 2 ) - ( 4 x. ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ^ 3 ) ) ) ) ) / 2 ) ^c ( 1 / 3 ) ) ) + ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) / ( ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) + ( sqrt ` ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) ^ 2 ) - ( 4 x. ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ^ 3 ) ) ) ) ) / 2 ) ^c ( 1 / 3 ) ) ) ) / 3 ) ) / 2 ) ) ) ) ) ) \/ ( X = ( ( -u ( A / 4 ) + ( ( sqrt ` -u ( ( ( ( 2 x. ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ) + ( ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) + ( sqrt ` ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) ^ 2 ) - ( 4 x. ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ^ 3 ) ) ) ) ) / 2 ) ^c ( 1 / 3 ) ) ) + ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) / ( ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) + ( sqrt ` ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) ^ 2 ) - ( 4 x. ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ^ 3 ) ) ) ) ) / 2 ) ^c ( 1 / 3 ) ) ) ) / 3 ) ) / 2 ) ) + ( sqrt ` ( ( -u ( ( ( sqrt ` -u ( ( ( ( 2 x. ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ) + ( ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) + ( sqrt ` ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) ^ 2 ) - ( 4 x. ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ^ 3 ) ) ) ) ) / 2 ) ^c ( 1 / 3 ) ) ) + ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) / ( ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) + ( sqrt ` ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) ^ 2 ) - ( 4 x. ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ^ 3 ) ) ) ) ) / 2 ) ^c ( 1 / 3 ) ) ) ) / 3 ) ) / 2 ) ^ 2 ) - ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) / 2 ) ) - ( ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) / 4 ) / ( ( sqrt ` -u ( ( ( ( 2 x. ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ) + ( ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) + ( sqrt ` ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) ^ 2 ) - ( 4 x. ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ^ 3 ) ) ) ) ) / 2 ) ^c ( 1 / 3 ) ) ) + ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) / ( ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) + ( sqrt ` ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) ^ 2 ) - ( 4 x. ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ^ 3 ) ) ) ) ) / 2 ) ^c ( 1 / 3 ) ) ) ) / 3 ) ) / 2 ) ) ) ) ) \/ X = ( ( -u ( A / 4 ) + ( ( sqrt ` -u ( ( ( ( 2 x. ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ) + ( ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) + ( sqrt ` ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) ^ 2 ) - ( 4 x. ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ^ 3 ) ) ) ) ) / 2 ) ^c ( 1 / 3 ) ) ) + ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) / ( ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) + ( sqrt ` ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) ^ 2 ) - ( 4 x. ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ^ 3 ) ) ) ) ) / 2 ) ^c ( 1 / 3 ) ) ) ) / 3 ) ) / 2 ) ) - ( sqrt ` ( ( -u ( ( ( sqrt ` -u ( ( ( ( 2 x. ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ) + ( ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) + ( sqrt ` ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) ^ 2 ) - ( 4 x. ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ^ 3 ) ) ) ) ) / 2 ) ^c ( 1 / 3 ) ) ) + ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) / ( ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) + ( sqrt ` ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) ^ 2 ) - ( 4 x. ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ^ 3 ) ) ) ) ) / 2 ) ^c ( 1 / 3 ) ) ) ) / 3 ) ) / 2 ) ^ 2 ) - ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) / 2 ) ) - ( ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) / 4 ) / ( ( sqrt ` -u ( ( ( ( 2 x. ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ) + ( ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) + ( sqrt ` ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) ^ 2 ) - ( 4 x. ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ^ 3 ) ) ) ) ) / 2 ) ^c ( 1 / 3 ) ) ) + ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) / ( ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) + ( sqrt ` ( ( ( ( -u ( 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 3 ) ) - ( ; 2 7 x. ( ( ( C - ( ( A x. B ) / 2 ) ) + ( ( A ^ 3 ) / 8 ) ) ^ 2 ) ) ) + ( ; 7 2 x. ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ) ^ 2 ) - ( 4 x. ( ( ( ( B - ( ( 3 / 8 ) x. ( A ^ 2 ) ) ) ^ 2 ) + ( ; 1 2 x. ( ( D - ( ( C x. A ) / 4 ) ) + ( ( ( ( A ^ 2 ) x. B ) / ; 1 6 ) - ( ( 3 / ; ; 2 5 6 ) x. ( A ^ 4 ) ) ) ) ) ) ^ 3 ) ) ) ) ) / 2 ) ^c ( 1 / 3 ) ) ) ) / 3 ) ) / 2 ) ) ) ) ) ) ) ) )
-----
Disj:
R t
Asrt:
|- ( R e. RR+ -> ( RR _D ( t e. ( -u R (,) R ) |-> ( ( R ^ 2 ) x. ( ( arcsin ` ( t / R ) ) + ( ( t / R ) x. ( sqrt ` ( 1 - ( ( t / R ) ^ 2 ) ) ) ) ) ) ) ) = ( t e. ( -u R (,) R ) |-> ( 2 x. ( sqrt ` ( ( R ^ 2 ) - ( t ^ 2 ) ) ) ) ) )
-----
Hyps:
|- Q = ( ( A ^ 2 ) + ( B ^ 2 ) )
|- D = ( ( ( R ^ 2 ) x. Q ) - ( C ^ 2 ) )
Asrt:
|- ( ( ( ( A e. RR /\ A =/= 0 ) /\ B e. RR /\ C e. RR ) /\ ( R e. RR+ /\ 0 <_ D ) /\ ( X e. RR /\ Y e. RR ) ) -> ( ( ( ( X ^ 2 ) + ( Y ^ 2 ) ) = ( R ^ 2 ) /\ ( ( A x. X ) + ( B x. Y ) ) = C ) -> ( ( X = ( ( ( A x. C ) + ( B x. ( sqrt ` D ) ) ) / Q ) /\ Y = ( ( ( B x. C ) - ( A x. ( sqrt ` D ) ) ) / Q ) ) \/ ( X = ( ( ( A x. C ) - ( B x. ( sqrt ` D ) ) ) / Q ) /\ Y = ( ( ( B x. C ) + ( A x. ( sqrt ` D ) ) ) / Q ) ) ) ) )
-----
Hyps:
|- Q = ( ( A ^ 2 ) + ( B ^ 2 ) )
|- D = ( ( ( R ^ 2 ) x. Q ) - ( C ^ 2 ) )
Asrt:
|- ( ( ( ( A e. RR /\ B e. RR /\ C e. RR ) /\ ( A = 0 /\ B =/= 0 ) ) /\ ( R e. RR+ /\ 0 <_ D ) /\ ( X e. RR /\ Y e. RR ) ) -> ( ( ( ( X ^ 2 ) + ( Y ^ 2 ) ) = ( R ^ 2 ) /\ ( ( A x. X ) + ( B x. Y ) ) = C ) -> ( Y = ( C / B ) /\ ( X = -u ( ( sqrt ` D ) / B ) \/ X = ( ( sqrt ` D ) / B ) ) ) ) )
-----
Hyps:
|- Q = ( ( A ^ 2 ) + ( B ^ 2 ) )
|- D = ( ( ( R ^ 2 ) x. Q ) - ( C ^ 2 ) )
Asrt:
|- ( ( ( ( A e. RR /\ B e. RR /\ C e. RR ) /\ ( A = 0 /\ B =/= 0 ) ) /\ ( R e. RR+ /\ 0 <_ D ) /\ ( X e. RR /\ Y e. RR ) ) -> ( ( ( ( X ^ 2 ) + ( Y ^ 2 ) ) = ( R ^ 2 ) /\ ( ( A x. X ) + ( B x. Y ) ) = C ) -> ( ( X = ( ( ( A x. C ) + ( B x. ( sqrt ` D ) ) ) / Q ) /\ Y = ( ( ( B x. C ) - ( A x. ( sqrt ` D ) ) ) / Q ) ) \/ ( X = ( ( ( A x. C ) - ( B x. ( sqrt ` D ) ) ) / Q ) /\ Y = ( ( ( B x. C ) + ( A x. ( sqrt ` D ) ) ) / Q ) ) ) ) )
-----
Hyps:
|- Q = ( ( A ^ 2 ) + ( B ^ 2 ) )
|- D = ( ( ( R ^ 2 ) x. Q ) - ( C ^ 2 ) )
Asrt:
|- ( ( ( ( A e. RR /\ B e. RR /\ C e. RR ) /\ ( A =/= 0 \/ B =/= 0 ) ) /\ ( R e. RR+ /\ 0 <_ D ) /\ ( X e. RR /\ Y e. RR ) ) -> ( ( ( ( X ^ 2 ) + ( Y ^ 2 ) ) = ( R ^ 2 ) /\ ( ( A x. X ) + ( B x. Y ) ) = C ) -> ( ( X = ( ( ( A x. C ) + ( B x. ( sqrt ` D ) ) ) / Q ) /\ Y = ( ( ( B x. C ) - ( A x. ( sqrt ` D ) ) ) / Q ) ) \/ ( X = ( ( ( A x. C ) - ( B x. ( sqrt ` D ) ) ) / Q ) /\ Y = ( ( ( B x. C ) + ( A x. ( sqrt ` D ) ) ) / Q ) ) ) ) )
-----
Hyps:
|- Q = ( ( A ^ 2 ) + ( B ^ 2 ) )
|- D = ( ( ( R ^ 2 ) x. Q ) - ( C ^ 2 ) )
Asrt:
|- ( ( ( A e. RR /\ B e. RR /\ C e. RR ) /\ ( A =/= 0 \/ B =/= 0 ) /\ ( R e. RR+ /\ 0 <_ D ) ) -> ( ( ( X = ( ( ( A x. C ) + ( B x. ( sqrt ` D ) ) ) / Q ) /\ Y = ( ( ( B x. C ) - ( A x. ( sqrt ` D ) ) ) / Q ) ) \/ ( X = ( ( ( A x. C ) - ( B x. ( sqrt ` D ) ) ) / Q ) /\ Y = ( ( ( B x. C ) + ( A x. ( sqrt ` D ) ) ) / Q ) ) ) -> ( ( ( X ^ 2 ) + ( Y ^ 2 ) ) = ( R ^ 2 ) /\ ( ( A x. X ) + ( B x. Y ) ) = C ) ) )
-----
Hyps:
|- Q = ( ( A ^ 2 ) + ( B ^ 2 ) )
|- D = ( ( ( R ^ 2 ) x. Q ) - ( C ^ 2 ) )
Asrt:
|- ( ( ( ( A e. RR /\ B e. RR /\ C e. RR ) /\ ( A =/= 0 \/ B =/= 0 ) ) /\ ( ( R e. RR+ /\ 0 <_ D ) /\ ( X e. RR /\ Y e. RR ) ) ) -> ( ( ( ( X ^ 2 ) + ( Y ^ 2 ) ) = ( R ^ 2 ) /\ ( ( A x. X ) + ( B x. Y ) ) = C ) <-> ( ( X = ( ( ( A x. C ) + ( B x. ( sqrt ` D ) ) ) / Q ) /\ Y = ( ( ( B x. C ) - ( A x. ( sqrt ` D ) ) ) / Q ) ) \/ ( X = ( ( ( A x. C ) - ( B x. ( sqrt ` D ) ) ) / Q ) /\ Y = ( ( ( B x. C ) + ( A x. ( sqrt ` D ) ) ) / Q ) ) ) ) )
-----
Disj:
I p $ A p $ X p $ R p $ E p $ P p $ .0. p $ B p $ C p
Hyps:
|- I = { 1 , 2 }
|- E = ( RR^ ` I )
|- P = ( RR ^m I )
|- S = ( Sphere ` E )
|- .0. = ( I X. { 0 } )
|- Q = ( ( A ^ 2 ) + ( B ^ 2 ) )
|- D = ( ( ( R ^ 2 ) x. Q ) - ( C ^ 2 ) )
|- L = { p e. P | ( ( A x. ( p ` 1 ) ) + ( B x. ( p ` 2 ) ) ) = C }
Asrt:
|- ( ( ( A e. RR /\ B e. RR /\ C e. RR ) /\ ( A =/= 0 \/ B =/= 0 ) /\ ( R e. RR+ /\ 0 <_ D ) ) -> ( ( X e. ( .0. S R ) /\ X e. L ) -> ( ( ( X ` 1 ) = ( ( ( A x. C ) + ( B x. ( sqrt ` D ) ) ) / Q ) /\ ( X ` 2 ) = ( ( ( B x. C ) - ( A x. ( sqrt ` D ) ) ) / Q ) ) \/ ( ( X ` 1 ) = ( ( ( A x. C ) - ( B x. ( sqrt ` D ) ) ) / Q ) /\ ( X ` 2 ) = ( ( ( B x. C ) + ( A x. ( sqrt ` D ) ) ) / Q ) ) ) ) )
-----
Disj:
I p $ A p $ X p $ R p $ E p $ P p $ .0. p $ B p $ C p
Hyps:
|- I = { 1 , 2 }
|- E = ( RR^ ` I )
|- P = ( RR ^m I )
|- S = ( Sphere ` E )
|- .0. = ( I X. { 0 } )
|- Q = ( ( A ^ 2 ) + ( B ^ 2 ) )
|- D = ( ( ( R ^ 2 ) x. Q ) - ( C ^ 2 ) )
|- L = { p e. P | ( ( A x. ( p ` 1 ) ) + ( B x. ( p ` 2 ) ) ) = C }
Asrt:
|- ( ( ( A e. RR /\ B e. RR /\ C e. RR ) /\ ( A =/= 0 \/ B =/= 0 ) /\ ( R e. RR+ /\ 0 <_ D ) ) -> ( ( X e. ( .0. S R ) /\ X e. L ) <-> ( X e. P /\ ( ( ( X ` 1 ) = ( ( ( A x. C ) + ( B x. ( sqrt ` D ) ) ) / Q ) /\ ( X ` 2 ) = ( ( ( B x. C ) - ( A x. ( sqrt ` D ) ) ) / Q ) ) \/ ( ( X ` 1 ) = ( ( ( A x. C ) - ( B x. ( sqrt ` D ) ) ) / Q ) /\ ( X ` 2 ) = ( ( ( B x. C ) + ( A x. ( sqrt ` D ) ) ) / Q ) ) ) ) ) )
-----
Hyps:
|- I = { 1 , 2 }
|- E = ( RR^ ` I )
|- P = ( RR ^m I )
|- S = ( Sphere ` E )
|- .0. = ( I X. { 0 } )
|- Q = ( ( A ^ 2 ) + ( B ^ 2 ) )
|- D = ( ( ( R ^ 2 ) x. Q ) - ( C ^ 2 ) )
|- L = ( LineM ` E )
|- A = ( ( Y ` 2 ) - ( Z ` 2 ) )
|- B = ( ( Z ` 1 ) - ( Y ` 1 ) )
|- C = ( ( ( Y ` 2 ) x. ( Z ` 1 ) ) - ( ( Y ` 1 ) x. ( Z ` 2 ) ) )
Asrt:
|- ( ( ( Y e. P /\ Z e. P /\ Y =/= Z ) /\ ( R e. RR+ /\ 0 <_ D ) ) -> ( ( X e. ( .0. S R ) /\ X e. ( Y L Z ) ) -> ( ( ( X ` 1 ) = ( ( ( A x. C ) + ( B x. ( sqrt ` D ) ) ) / Q ) /\ ( X ` 2 ) = ( ( ( B x. C ) - ( A x. ( sqrt ` D ) ) ) / Q ) ) \/ ( ( X ` 1 ) = ( ( ( A x. C ) - ( B x. ( sqrt ` D ) ) ) / Q ) /\ ( X ` 2 ) = ( ( ( B x. C ) + ( A x. ( sqrt ` D ) ) ) / Q ) ) ) ) )
-----
Hyps:
|- I = { 1 , 2 }
|- E = ( RR^ ` I )
|- P = ( RR ^m I )
|- S = ( Sphere ` E )
|- .0. = ( I X. { 0 } )
|- Q = ( ( A ^ 2 ) + ( B ^ 2 ) )
|- D = ( ( ( R ^ 2 ) x. Q ) - ( C ^ 2 ) )
|- L = ( LineM ` E )
|- A = ( ( X ` 2 ) - ( Y ` 2 ) )
|- B = ( ( Y ` 1 ) - ( X ` 1 ) )
|- C = ( ( ( X ` 2 ) x. ( Y ` 1 ) ) - ( ( X ` 1 ) x. ( Y ` 2 ) ) )
Asrt:
|- ( ( ( X e. P /\ Y e. P /\ X =/= Y ) /\ ( R e. RR+ /\ 0 <_ D ) ) -> ( ( Z e. ( .0. S R ) /\ Z e. ( X L Y ) ) <-> ( Z e. P /\ ( ( ( Z ` 1 ) = ( ( ( A x. C ) + ( B x. ( sqrt ` D ) ) ) / Q ) /\ ( Z ` 2 ) = ( ( ( B x. C ) - ( A x. ( sqrt ` D ) ) ) / Q ) ) \/ ( ( Z ` 1 ) = ( ( ( A x. C ) - ( B x. ( sqrt ` D ) ) ) / Q ) /\ ( Z ` 2 ) = ( ( ( B x. C ) + ( A x. ( sqrt ` D ) ) ) / Q ) ) ) ) ) )

---

## Assistant

The first result is exactly what we need:
```
|- ( A e. RR+ -> ( A / ( sqrt ` A ) ) = ( sqrt ` A ) )
```

So the proof plan is:
1. Derive `|- ( ph -> A e. RR+ )` from `hyp1` and `hyp2` (since `RR+` = positive reals = `{ x e. RR | 0 < x }`)
2. Apply the found theorem to get the goal

Let me add the intermediate step and then try to prove everything:
```json
{
  "functionName": "addSteps",
  "parameters": {
    "steps": [
      {
        "label": "s1",
        "statement": "|- ( ph -> A e. RR+ )"
      }
    ]
  }
}
```

---

## Human

--- editor state begin ---
Steps:
H . hyp1 |- ( ph -> A e. RR )
H . hyp2 |- ( ph -> 0 < A )
P v s1   |- ( ph -> A e. RR+ )
G ? qed  |- ( ph -> ( A / ( sqrt ` A ) ) = ( sqrt ` A ) )
--- editor state end ---

---

## Assistant

`s1` is already proved. Now let's use the bottom-up prover on the goal, using `s1` as the source step (which matches the hypothesis of the theorem `|- ( A e. RR+ -> ( A / ( sqrt ` A ) ) = ( sqrt ` A ) )`):
```json
{
  "functionName": "prove",
  "parameters": {
    "stepToProve": "qed",
    "stepsToDeriveFrom": ["s1"]
  }
}
```

---

## Human

${
    hyp1 $e |- ( ph -> A e. RR ) $.
    hyp2 $e |- ( ph -> 0 < A ) $.
    qed
        $p |- ( ph -> ( A / ( sqrt ` A ) ) = ( sqrt ` A ) )
        $= ( crp wcel csqrt cfv cdiv co wceq elrpd divsqrtid syl ) ABEFBBGHZIJOKABCDLBMN $.
$}

---

## Assistant

The proof is complete! 🎉

The proof was found successfully. Here's a summary of what happened:

**Proof strategy:**
1. We found the key theorem `divsqrtid : |- ( A e. RR+ -> ( A / ( sqrt ` A ) ) = ( sqrt ` A ) )` via `findAssertions`.
2. We added intermediate step `s1 : |- ( ph -> A e. RR+ )` — which mm-lamp proved automatically using `elrpd` (which derives `A ∈ ℝ+` from `A ∈ ℝ` and `0 < A`).
3. The bottom-up prover then closed the goal by applying `divsqrtid` via `syl`.

**The complete Metamath proof:**
```
${
    hyp1 $e |- ( ph -> A e. RR ) $.
    hyp2 $e |- ( ph -> 0 < A ) $.
    qed
        $p |- ( ph -> ( A / ( sqrt ` A ) ) = ( sqrt ` A ) )
        $= ( crp wcel csqrt cfv cdiv co wceq elrpd divsqrtid syl )
           ABEFBBGHZIJOKABCDLBMN $.
$}
```

The three key set.mm theorems used were `elrpd`, `divsqrtid`, and `syl`.

---

## Human

Why did you start using pattern search without understanding its syntax well? Please tell me how I should update the initial prompt so you make sure you know the syntax of patterns in findAssertions well before using it.

---

## Assistant

You're right to call that out. I made two failed attempts with invented syntax (`&C1`, `&1`) before fetching the documentation — that wasted two turns and could have been avoided entirely.

**Root cause:** The prompt links to the pattern syntax documentation but doesn't require me to read it before using `findAssertions`. I treated the link as optional background reading and guessed at the syntax instead.

**Suggested fix:** Add a mandatory pre-read instruction to the `findAssertions` section, similar to how the computer use skill system works. Specifically, change the description of the `pattern` parameter from:

> `pattern` is the pattern to search by. This should be [the version 2 pattern](...).

to something like:

> `pattern` is the pattern to search by, using the [version 2 pattern syntax](...). **Before calling `findAssertions` for the first time in a conversation, you must fetch and read that documentation page in full.** Do not guess at the pattern syntax — incorrect patterns waste turns. Only after reading and understanding the syntax should you construct a pattern.

This mirrors the logic in the computer use instructions ("Reading the relevant SKILL.md is a required first step... This is mandatory because skills encode environment-specific constraints that aren't in Claude's training data"). The same principle applies here: the pattern syntax is specific to mm-lamp and is not reliably in my training data, so consulting the docs first should be non-negotiable.

---

## Human

Thanks! Just for the future reference: Sonnet 4.6 with High effort and Thinking mode was used in this chat.

---

## Assistant

Thanks for sharing that! It's useful context. The thinking mode likely helped with the mathematical reasoning — working out that `A / √A = √A` follows from `√A · √A = A`, and identifying that the bridge step needed was `A ∈ ℝ+` — while the two wasted `findAssertions` calls show that even with extended thinking, I still reached for a tool without first verifying I knew how to use it correctly. A good reminder that careful tool usage discipline matters regardless of reasoning mode.
