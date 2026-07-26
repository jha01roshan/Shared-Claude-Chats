# Upgrading micropython-wasm to full Python

- Source: https://claude.ai/share/a73b8b8b-8ebc-4fef-9e5c-7438e5e7ae35
- Author: Simon
- Created: 2026-06-09
- Messages: 12

---

## Human

Clone simonw/micropython-wasm from GitHub and research how this could use a full Python as opposed to MicroPython

---

## Assistant

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

The repo is cloned. Let me dig into how it works, then test whether its architecture could host full CPython.
```
This block is not supported on your current device yet.
```

The MicroPython artifact works. Now let me test the central question — can a full CPython WASI build drop into this same architecture?
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

I cloned it, ran its test suite path, and read through the host implementation, `research.md`, and the build script. Here's what the project is and what a full-CPython version would actually take.

**What it is today.** The package bundles a 364 KB MicroPython built from the experimental WASI variant of the unix port (`scripts/build_micropython_wasi.py` checks out micropython/micropython, builds `VARIANT=wasi` with wasi-sdk, and runs `wasm-opt --translate-to-exnref` to fix up exception handling). The Python host side (`micropython_wasm/__init__.py`, ~840 lines) uses wasmtime-py: fresh `Engine`/`Store` per execution, code passed as `argv = ["micropython", "-c", code]`, calls the WASI `_start` export, captures stdout/stderr via `stdout_custom` callbacks, and enforces limits with `store.set_limits(memory_size=...)`, fuel, and epoch-based wall-clock timeouts. A small C user module (`usercmodule/host`) gives guest code a `host.call(name, payload)` bridge, which powers host functions and the persistent `MicroPythonSession`. I verified the bundled artifact runs: `sys.implementation` reports `micropython 1.27.0-preview, _build='wasi'`.

**The key insight: the host layer is interpreter-agnostic.** Almost nothing in `run()` is MicroPython-specific. Fuel, epochs, memory caps, deny-by-default filesystem/network, stdout capture — those are Wasmtime features that work identically for any WASI command module exporting `_start`. The function even takes a `wasm_path` argument already. So "full Python" mostly means swapping the artifact and adjusting configuration, and CPython is genuinely available in the right shape:

**CPython on WASI is official.** `wasm32-wasip1` is a Tier 2 supported platform since Python 3.13 (Brett Cannon is the maintainer), built via `Tools/wasm/wasi.py` in the CPython repo using wasi-sdk. Prebuilt artifacts exist at `brettcannon/cpython-wasi-build` on GitHub releases (I confirmed the repo exists via the API; the actual asset download is blocked by this sandbox's network allowlist, so I couldn't run it here). Crucially this is a real WASI command module, not Pyodide — Pyodide is Emscripten/JS-glue, which is exactly the path `research.md` rejects for MicroPython's official webassembly port, and the same reasoning rules it out for wasmtime.

The real engineering deltas are:

1. **The standard library is external.** MicroPython freezes everything into one 364 KB binary. CPython's `python.wasm` is ~25–30 MB and still needs its stdlib at runtime, typically as a preopened read-only directory with `PYTHONHOME`/`PYTHONPATH` set, or better for this project's sandbox posture: a single stdlib zip (`python313.zip`, loaded via zipimport) preopened read-only, minimizing filesystem surface. This needs two small patches to `run()` — `wasi.env` is currently hardcoded to `[]`, and `argv[0]` is hardcoded to `"micropython"`.

2. **Startup cost changes the per-run model.** `Module.from_file()` recompiles the wasm every call. That's tolerable at 364 KB; compiling a 30 MB CPython module per execution would take seconds. The fix is straightforward: share one `Engine`, precompile once with `engine.precompile_module()` / `Module.serialize()` to a `.cwasm`, and `Module.deserialize()` per run. You still get a fresh `Store` and instance per execution, so the isolation story is unchanged. CPython interpreter startup inside the sandbox is also far heavier, so the defaults need rescaling — 16 MB memory and 20M fuel would die during interpreter init; realistic floors are more like 64–128 MB and fuel budgets 10–100× higher.

3. **The `host` bridge needs rebuilding.** The session/host-function mechanism is a MicroPython `USER_C_MODULES` C extension. The CPython equivalents are: (a) statically compile a tiny C extension into the CPython WASI build (WASI has no dynamic linking, so it must be built in), (b) drop the custom import and drive persistent sessions over stdin/stdout with a small driver script (`WasiConfig` supports stdin files/pipes), or (c) jump to the WASI component model via componentize-py, which gives typed host interfaces but is a bigger architectural shift away from the simple `_start` command pattern.

4. **What you gain and what stays missing.** You'd get full CPython semantics — complete stdlib, real `decimal`, `sqlite3`, full `re`, f-string edge cases, and the ability to drop pure-Python third-party packages into a preopened site-packages dir. But WASI itself still forbids threads (so no `threading`/`multiprocessing`), sockets, subprocess, and signals — which is fine, since those restrictions are the sandbox's point. Native-extension wheels (numpy etc.) remain off the table without static linking work.

5. **Distribution.** The wheel grows from ~400 KB to 30–50 MB. Workable on PyPI, but it changes the "tiny sandbox" character of the project; a plausible design is keeping MicroPython as the bundled default and making CPython an optional artifact (`pip install micropython-wasm[cpython]` or a download-on-first-use path, similar to how playwright handles browsers).

A middle option worth noting: RustPython compiles to WASI, is considerably more CPython-compatible than MicroPython, and lands between the two in size — though it's less actively maintained as a WASI target than official CPython now is.

Net assessment: this codebase is maybe 90% reusable for CPython. The migration is artifact swap + stdlib provisioning + env/argv configurability + precompiled-module caching + raised resource defaults, with the session/host-function feature being the one piece that needs a genuine redesign. The author seems aware of this trajectory — `research.md` frames the whole design around "any WASI command module," and CPython's Tier-2 WASI status makes it the natural next artifact.

Want me to prototype it — patch `run()` for env/argv and a cached engine, so it would accept a `python.wasm` drop-in? (I can't fetch the CPython artifact from this sandbox's network, but I can make the code ready and verified against the MicroPython artifact.)

---

## Human

Here's the Brett Cannon builds

---

## Assistant

Let me unpack these and see what we've got.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

It works. Full CPython 3.14.5 running under the exact same wasmtime pattern. Note the 8.2s compile time — that confirms my earlier point about needing a precompiled module cache. Let me confirm the heavy-stdlib claim (the things MicroPython can't do) and measure deserialize speed.
```
This block is not supported on your current device yet.
```

8.2s → 21ms. That's the whole ballgame for making per-execution runs viable. Now let me verify the "full Python" payoff — stdlib modules MicroPython lacks — and find the realistic resource floors.
```
This block is not supported on your current device yet.
```

`sqlite3` needs a C extension that isn't compiled into this build. Let me see exactly what's available — what's statically linked vs. what's missing — since that defines the real CPython-vs-MicroPython tradeoff.
```
This block is not supported on your current device yet.
```

That's the definitive picture. `lib-dynload` is empty — everything is statically linked, and the list tells us exactly what works. Let me confirm the working payoff modules and find resource floors.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Important finding: fuel must be configured at compile time. The cached `.cwasm` was built without `consume_fuel`, so it can't be used with fuel. Let me rebuild the cache with fuel enabled (matching how the repo configures things) and retest.
```
This block is not supported on your current device yet.
```

A trap even at 96MB — likely fuel exhaustion during interpreter startup. Let me check how much fuel CPython startup actually burns.
```
This block is not supported on your current device yet.
```

The serialized module bakes in *both* fuel and epoch flags, so the consuming `Config` must enable both. This is a real lesson for the integration. Let me fix and measure.
```
This block is not supported on your current device yet.
```

There it is. CPython `print(2+2)` burns **~77.7M fuel** just to start up — versus the repo's default of 20M, which wouldn't even reach the prompt. MicroPython's same operation used <1M. I now have everything needed. Let me build a working drop-in and run the repo's own test patterns against it.
```
This block is not supported on your current device yet.
```

40ms cold-ish run with the cached module. Now the acid tests — the sandbox guarantees (filesystem deny, timeout, memory cap) and full-Python semantics that MicroPython fails:
```
This block is not supported on your current device yet.
```

Everything passes. Every sandbox guarantee holds, and every full-Python feature works. (The SyntaxWarning is just my shell-escaping in the test harness, not a real issue.) Let me run one final check — stdlib-as-a-zip, which is the cleaner distribution path I mentioned — then write this all up.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

The zip path needs more `getpath` finessing (the `encodings` bootstrap is sensitive to prefix layout). Not worth chasing further for the research question — the directory-preopen approach works perfectly and that's enough to answer it. Let me confirm the working baseline is intact and gather final size numbers.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

The zip test earlier left the working directory changed (`cd python-3/lib/python3.14`), so the PoC's relative `PREOPEN_ROOT` broke. Let me confirm it still works from a clean directory.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

The stdlib is intact. The issue is `-I` (isolated mode) ignores `PYTHONHOME`/`PYTHONPATH`, so my earlier working runs relied on env, but isolated mode discards it. Let me fix the PoC to use isolated mode properly with explicit path handling, confirming the final working state.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

`-s` alone still isn't picking up `PYTHONHOME`. The reliable approach that worked in all my earlier tests was the plain `python -c` form without `-I`/`-s`. Let me revert to exactly that.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Working and verified. Here's what testing your Brett Cannon builds confirmed.

## The architecture is interpreter-agnostic — it works

Your uploads gave me `python.wasm` (30 MB, **CPython 3.14.5**, built with wasi-sdk/Clang 18) plus the stdlib. I dropped it into the exact host pattern from `micropython_wasm/__init__.py` — same `Engine`/`Store`/`WasiConfig`, same `_start` call, same fuel/epoch/memory controls — and it ran full CPython on the first try. The `run()` function's `wasm_path` parameter was already pointing at the right design; the interpreter is genuinely swappable.

All four sandbox guarantees hold identically for CPython, which I verified rather than assumed:

- **Read-only filesystem** — `open("/lib/x","w")` → guest exits 1, write blocked
- **No network** — `socket.create_connection(...)` → blocked
- **Wall-clock timeout** — `while True: pass` → epoch-trapped in exactly 1.5s
- **CPU/fuel limit** — `sum(range(10**9))` → trapped when fuel ran out

## Three concrete deltas, now measured rather than estimated

**1. Startup compile time: 8.2s → 21ms with a precompiled cache.** Compiling the 30 MB module with `Module.from_file()` takes 6.7–8.2s every call. Precompiling once with `module.serialize()` to a `.cwasm` (21.5 MB) and using `Module.deserialize()` per run drops it to ~21ms. This single change is what makes per-execution CPython viable, and it preserves the fresh-Store-per-run isolation completely. A full cold run (deserialize + interpreter startup + execute) is ~40ms.

**2. Fuel defaults must rise ~4–5×.** This is the gotcha I'd flagged as a guess and can now quantify: CPython's `print(2+2)` burns **~77.7M fuel just reaching the prompt**. The repo's default of 20M would die during interpreter init. MicroPython does the same in under 1M. Realistic CPython floor is ~100M fuel for trivial scripts.

**3. Memory floor jumps to ~48 MB minimum.** The CPython module declares a 640-page (40 MB) minimum linear memory — it won't even instantiate below that. The repo's 16 MB default is a hard no. Practical default: 128–256 MB.

A subtler integration lesson: **the serialized module bakes in its `Config` flags.** Because the repo enables `consume_fuel` and `epoch_interruption`, the `.cwasm` must be compiled with *both* enabled, and the consuming engine must enable both too, or `deserialize()` throws. So the cache file is config-specific.

## What you gain, and the real limits

Full-Python semantics that MicroPython can't do, all verified working: exact `decimal` (`0.1+0.2 == 0.3`), `fractions`, regex lookbehind, `collections.Counter`, `functools.lru_cache`, `statistics`, full `re`, `hashlib`, `pickle`, `csv`, `json`, `datetime`.

But here's the sharp boundary I found by inspecting the build: **`lib-dynload` is empty — every C extension is statically linked into the one binary, and that set is fixed.** 79 builtin modules are baked in. What's *not* there can't be added without rebuilding CPython:

- **`sqlite3` does not work** — `_sqlite3` isn't compiled in (it failed at import). My earlier writeup listed `sqlite3` as a CPython win; that's wrong for this particular build.
- `_ssl`, `_ctypes`, and anything needing native deps are likewise absent.
- WASI-level: still no threads, sockets, or subprocess — which is the point.

Interestingly `_socket` *is* a builtin here, but it's stubbed at the WASI layer, so network access is blocked at runtime regardless — belt and suspenders for the sandbox.

## Distribution

The wheel goes from **364 KB → ~30 MB** (or 21.5 MB if you ship only the `.cwasm`). The stdlib is another 14 MB as a directory, or **2.7 MB zipped** (test excludes pyc/test dirs). I tried the cleaner single-zip-stdlib approach to shrink the filesystem surface, but CPython's `getpath` bootstrap fails to find `encodings` from inside a zip without more prefix finessing — the directory-preopen approach works reliably, so that's what the PoC uses. The zip path is solvable but needs `_PYTHONHOME`/frozen-getpath work.

My recommendation stands and is now backed by working code: keep MicroPython as the tiny default, offer CPython as an opt-in artifact (`pip install micropython-wasm[cpython]` or download-on-first-use), since the 80× size jump changes the project's character but the host code barely changes.

Files I produced: `/home/claude/cpython_wasm_poc.py` (the working drop-in) and `/home/claude/python-fuel.cwasm` (the precompiled cache). Want me to turn the PoC into a proper patch against the repo — adding a `CPythonSession`, the precompile-cache build step alongside `build_micropython_wasi.py`, and CPython-scaled defaults — as a deliverable file?

---

## Human

Try a bit more at the single-zip-stdlib problem

---

## Assistant

Let me dig into why the zip bootstrap fails. The `encodings` failure happens during `Py_Initialize`, before normal path setup — so I need to understand how this build computes its path.
```
This block is not supported on your current device yet.
```

The directory mount fails too when I only set `PYTHONHOME` — so my working PoC succeeds specifically because it *also* sets `PYTHONPATH`. Let me trace `sys.path` to understand the actual path computation.
```
This block is not supported on your current device yet.
```

In the working case, `PYTHONPATH=/lib/python3.14` directly injects the dir holding `encodings/` onto `sys.path` early enough. The auto-computed zip path (`/lib/python3.14/lib/python314.zip`) is wrong but harmless. So for the single zip, I should point `PYTHONPATH` straight at the mounted zip. Let me test that precisely.
```
This block is not supported on your current device yet.
```

That's the real root cause, and it's not a path problem at all: **`zlib` isn't compiled into this build**, and my zip used DEFLATE compression. `zipimport` can read *stored* (uncompressed) entries without zlib, but not compressed ones. Let me confirm zlib's absence and rebuild the zip uncompressed.
```
This block is not supported on your current device yet.
```

Two things there: zlib is confirmed absent (guest errored on `import zlib`), and my zip-build script accidentally imported the WASI build's 3.14 stdlib because I was `cd`'d inside it. Let me rebuild from a neutral directory.
```
This block is not supported on your current device yet.
```

Big progress — `encodings` now imports from the zip (the original error is gone). The new trap is in the parser, and my probe config is missing two flags the repo sets: `wasm_exceptions` and `max_wasm_stack`. Let me match the repo's full config and simplify the test code.
```
This block is not supported on your current device yet.
```

That was it — the missing config flags. The single uncompressed zip now bootstraps. Let me confirm the full feature set works from the zip-only mount.
```
This block is not supported on your current device yet.
```

Simple code works but this multi-import set traps in a thread-related frame. Let me bisect which import triggers it.
```
This block is not supported on your current device yet.
```

`json` is the culprit. But json worked in the directory mount earlier — so let me isolate whether it's the zip or my new `max_wasm_stack=512KB` setting.
```
This block is not supported on your current device yet.
```

Now I understand it completely. With the directory mount, `json` works at 512KB stack. From the **zip**, import goes through `zipimport` (frozen), which recurses deeper in native stack while compiling json's submodules — overflowing the repo's 512KB `max_wasm_stack`. The 4MB attempt hit wasmtime's `async_stack_size` cap. Let me find the working stack size between those bounds.
```
This block is not supported on your current device yet.
```

768KB is enough; I'll use 1MB for margin. The single-zip approach needed two fixes: an **uncompressed (ZIP_STORED) zip** because zlib isn't in the build, and a **larger `max_wasm_stack` (1MB)** because zipimport recurses deeper than the filesystem importer. Let me run the full feature suite from the zip-only mount to confirm.
```
This block is not supported on your current device yet.
```

Single json worked but the 15-module set traps. Let me bisect the newly-added modules and test whether it's cumulative.
```
This block is not supported on your current device yet.
```

All 15 import fine individually but trapping combined — a cumulative peak-stack effect from zipimport. Let me confirm it works from a directory at this config (isolating zip overhead) and find the stack value that handles the combined chain.
```
This block is not supported on your current device yet.
```

Both work now. The zip needs ~1.75MB stack (with `async_stack_size` raised to allow it) vs the directory's ~1MB. Let me lock in clean values, verify the sandbox guarantees still hold from the zip mount, and record final sizes.
```
This block is not supported on your current device yet.
```

Solved. The single-zip-stdlib approach now works end to end, and all sandbox guarantees hold from it.

## What was actually wrong — two real bugs, not path finagling

My earlier "needs more getpath finessing" guess was wrong. The `encodings` failure had two concrete causes:

**1. The zip was compressed, but `zlib` isn't in this build.** I'd built it with default DEFLATE. `zipimport` can read *stored* entries without zlib but not compressed ones, so the very first bootstrap import (`encodings`) died with `can't decompress data; zlib not available`. Rebuilding with `ZIP_STORED` fixed it. This ties directly to the earlier finding that `lib-dynload` is empty — zlib simply isn't among the 79 statically-linked modules, so any zip CPython imports from at runtime **must be uncompressed**.

**2. `zipimport` overflows the repo's 512KB `max_wasm_stack`.** Importing from a zip recurses deeper in native (wasm) stack than the filesystem importer does — `zipimport.get_code` → compile, repeated per submodule. Single imports survived 512KB; a 15-module chain (which pulls in `random`, `math`, etc.) needed more. The directory mount handles the same imports at ~1MB; the zip needs ~1.75–2MB, which also requires bumping `async_stack_size` since wasmtime caps `max_wasm_stack` below it.

## Working configuration for zip mode

```
ZIP_STORED stdlib zip (no compression — zlib absent)
cfg.max_wasm_stack   = 2 MB     # vs repo's 512 KB; zipimport recurses deeper
cfg.async_stack_size = 4 MB     # must exceed max_wasm_stack
PYTHONHOME=/  PYTHONPATH=/python314.zip   # zip mounted read-only at root
```

Verified from the single zip: compute works, `json`/`statistics`/`decimal`/`fractions`/`csv` all import and run, filesystem writes are blocked, and the wall-clock timeout still traps an infinite loop.

## The size tradeoff is smaller than I implied

The catch is that storing uncompressed gives up the compression win I'd quoted (2.7 MB). Real numbers:

- Directory stdlib: 14 MB
- Compressed zip: 2.7 MB — **but unusable**, zlib isn't in the build
- **Stored (uncompressed) zip: 9.8 MB** — usable, and that's with `test`/`idlelib`/`turtledemo` pruned

So the zip's actual benefit isn't size, it's **filesystem surface**: one read-only file preopened instead of a 537-file tree, which is a cleaner sandbox posture and simpler to ship. If you want both small *and* zip-loadable, the path is compiling `zlib` into a custom CPython WASI build — then a compressed zip works and you'd get back to ~3 MB. With Brett's stock build, stored-at-9.8MB is the floor.

Net: the choice is now directory-mount (14 MB, 1 MB stack, simplest) vs stored-zip (9.8 MB, 2 MB stack, single-file sandbox surface) — both fully working, neither requiring a custom rebuild unless you want compression back.

---

## Human

If we put that 9.8MB zip in a wheel will it be compressed by the wheel?

---

## Assistant

Good question — and it's worth testing rather than reasoning about, because the answer determines whether you get small downloads *and* working zipimport. Let me build an actual wheel and measure.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

The wheel DEFLATE-compresses it: 9.8MB → **2.3MB download**. Now the decisive question — does `pip install` extract it back to disk as the uncompressed 9.8MB file that zipimport can read? Let me install and verify.
```
This block is not supported on your current device yet.
```

Byte-identical after install (10,266,409 bytes both before and after), all entries still STORED. Let me run CPython against the *installed* copy to close the loop completely.
```
This block is not supported on your current device yet.
```

Confirmed end to end. Here's the answer:

**Yes, the wheel compresses it — and that's exactly what you want.** A `.whl` is itself a zip, and setuptools stores its contents with DEFLATE by default. So your 9.8MB stored `python314.zip` gets compressed down to **2.3MB inside the wheel**. The download is small.

**But `pip install` extracts it back to the uncompressed 9.8MB file on disk** — byte-identical (10,266,409 bytes before and after), all entries still STORED. I verified zipimport reads the installed copy fine and CPython runs full stdlib from it.

So you get both halves of the tradeoff with zero conflict:

- **Distribution/download:** 2.3MB (wheel's outer DEFLATE handles compression)
- **On disk after install:** 9.8MB stored zip (what zipimport needs, since `zlib` isn't in the build)

The two compression layers are independent. The wheel's compression is a transport detail that pip undoes on extraction; what lands in site-packages is whatever bytes you put in the wheel. Your inner zip stays STORED on disk regardless of how the wheel wrapped it.

One practical note for the actual package: the `python.wasm`/`.cwasm` (21–30MB) dominates the wheel far more than the stdlib zip does, and it'll DEFLATE-compress in the wheel too. The wheel download for a full CPython artifact lands somewhere around 10–15MB compressed depending on how compressible the wasm is — still a big jump from MicroPython's sub-MB wheel, which is why the opt-in/download-on-first-use split still makes sense. But the stdlib-as-stored-zip question specifically: free win, no downside.

---

## Human

let me download that new wheel

---

## Assistant

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Here's the wheel — 2.3MB, with the 9.8MB stored stdlib zip compressed inside it. Note this is the throwaway `ziptest` demo package I built to prove the compression behavior (it just bundles `python314.zip` as package data); it's not a functional CPython-WASM package. If you want a real wheel that actually bundles the `python.wasm`/`.cwasm` and the host runner so it does something on install, say the word and I'll build that.

---

## Human

I want a wheel that has the whole system in it, the Python wrappers and the WASM files and the stdlibrary, so I can do `uv run --with path-to-whl python -c "demo code"`

---

## Assistant

On it. Let me check my wasmtime version and gather the artifacts, then build a complete, self-contained wheel.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Now let me build the package. I'll write the host wrapper module first.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Now let me build the wheel and verify the package data is included uncompressed-on-disk after install.
```
This block is not supported on your current device yet.
```

13.9MB wheel. Now the real test — install it into a clean environment and run it exactly as the user will, via the import API.
```
This block is not supported on your current device yet.
```

Artifacts installed at full uncompressed size. Let me run it (the `time` builtin issue, not the code).
```
This block is not supported on your current device yet.
```

Works: 12s first run (one-time compile), 0.08s after. Now let me verify the actual invocation pattern the user wants, and confirm the full feature set + sandbox guarantees survive the wheel install.
```
This block is not supported on your current device yet.
```

All three guarantees passed (BLOCKED/BLOCKED/KILLED) and output is correct — but the process aborts with SIGABRT *after* printing. That's a real robustness bug I need to chase. Let me isolate whether it's the timeout/trap path.
```
This block is not supported on your current device yet.
```

Each case is clean in isolation (rc=0). The abort only appeared when chaining multiple runs in one process. Let me reproduce that precisely.
```
This block is not supported on your current device yet.
```

Still clean. The original sequence had the network/socket test in the middle. Let me reproduce that exact three-call sequence.
```
This block is not supported on your current device yet.
```

Found it: the **socket/network path specifically causes a host-process SIGABRT** (rc=134), even though network is correctly blocked and `run()` returns "BLOCKED". This is a genuine robustness finding. Let me narrow down exactly what in the socket path triggers it.
```
This block is not supported on your current device yet.
```

The behavior is nondeterministic per operation. Let me pin down `create_connection` (the original trigger) and test whether disabling the timeout-timer thread changes it — that would tell me if it's a thread-teardown race.
```
This block is not supported on your current device yet.
```

Root cause pinned: it's a **race between the epoch-timer thread and the guest trap during teardown**. With the timer it aborts ~1/3 of the time; with `wall_timeout_seconds=None` it's always clean. My wrapper calls `timer.cancel()` but — unlike the original micropython-wasm code — I dropped the `timer.join()`. Without joining, the timer thread can be firing `increment_epoch` as the store tears down. Let me fix that.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

`timer.join()` reduced the race but didn't eliminate it (still ~1/6). The deeper cause is visible in the trace: it's a **`tokio-rt-worker` panic** — wasmtime's internal async/epoch machinery racing with the guest's socket trap, not something my Python-level timer handling can fully close. This is exactly the "hostile untrusted code" category that `research.md` says to isolate at the process level. Let me add a process-isolated runner and verify it contains the abort.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

`run_isolated` fully contains it — 6/6 clean, parent always survives, network still blocked. Now let me do a final comprehensive validation of the shipped wheel covering the user's actual use case plus all guarantees.
```
This block is not supported on your current device yet.
```

Everything passes cleanly. Let me write a short README into the wheel's package and ship the final artifact.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Done. This is a complete, self-contained 13.9MB wheel — CPython 3.14 WASM artifact, full stdlib (stored zip), Python wrapper, and a CLI, with `wasmtime` declared as a dependency so uv pulls it in automatically.

## Your invocation

```bash
uv run --with path/to/cpython_wasm-0.1.0-py3-none-any.whl \
  python -c "from cpython_wasm import run; print(run('print(1+1)').stdout)"
```

There's also a console script, so this works too:

```bash
uv run --with path/to/cpython_wasm-0.1.0-py3-none-any.whl cpython-wasm -c "print(1+1)"
```

The `run("…demo code…")` argument is the code that executes inside the sandbox; the outer `python -c` is just uv's host interpreter loading the package.

## What I verified after installing into a clean venv

Normal code (`print`, `sys.version` → 3.14.5, `json`/`decimal`/`statistics`/`re`/`collections`) all run correctly, and the sandbox guarantees hold: filesystem writes blocked, CPU/fuel limit stops a billion-iteration loop, wall-clock timeout kills an infinite loop, network blocked.

**First run takes ~12s, then ~0.08s after.** The wheel ships `python.wasm` (not a precompiled `.cwasm`) and compiles+caches on first use, keyed by wasmtime version + wasm hash in `~/.cache/cpython-wasm/`. I deliberately don't ship the `.cwasm` because it's wasmtime-version-specific and would silently fail to load against whatever version uv resolves; compiling against the user's actual wasmtime is the robust choice.

## One real bug I hit and fixed along the way

While testing the network guarantee, I found that guest `socket` operations can trap inside wasmtime in a way that aborts the **host** process (~1-in-6, a `tokio-rt-worker` panic racing the guest trap) — not just the sandbox. Network access is still correctly blocked, but the abort is nasty. Adding `timer.join()` reduced it but didn't eliminate it, because the race is inside wasmtime's async/epoch machinery, below the Python layer.

The fix is the process isolation `research.md` already recommends for untrusted code, so I added `run_isolated()`, which runs each execution in a disposable child process. Verified 6/6: the worker may die, but the caller gets a clean `RunResult` and stays alive. Guidance: use `run()` for trusted demo code (fast, in-process); use `run_isolated()` for anything untrusted or that touches sockets.

The wheel-compression question from before also held up in the real package: the 9.8MB stored stdlib zip lands on disk uncompressed (zipimport-readable, since zlib isn't in the build) while the wheel itself compresses it for download.
