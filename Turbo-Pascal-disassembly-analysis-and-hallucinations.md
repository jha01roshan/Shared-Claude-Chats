# Turbo Pascal disassembly analysis and hallucinations

- Source: https://claude.ai/share/a64c94eb-c623-4fd4-b101-e3e7d66c77ca
- Author: Simon
- Created: 2026-03-24
- Messages: 2

---

## Human

Fetch and unzip https://static.simonwillison.net/static/2026/turbo-pascal-analysis.zip Clone simonw/tools in order to view turbo-pascal-deconstructed.html
Investigate the complaint in this comment t someone posted:
For the code generator, it produced this annotated disassembly:

```
    2100 push ax            ;--- EmitByte: write one byte to code output ---
    2101 mov di, [code_ptr] ;DI → current position in output buffer
    2104 stosb              ;Write AL to output, advance DI
    2105 mov [code_ptr], di ;Update code pointer
    2108 pop ax             ;Restore AX
    2109 ret                ;Every compiled instruction flows through this 6-instruction emitter
    2110 mov al, 0E8h       ;--- EmitCall: generate CALL instruction ---
    2112 call EmitByte      ;Emit opcode byte E8h (near CALL)
    2115 sub bx, [code_ptr] ;Calculate relative offset
    2118 sub bx, 2          ;Adjust for instruction length
    211A xchg ax, bx        ;AX = relative offset
    211B call EmitWord      ;Emit 16-bit relative displacement
    211E ret                ;Generated: E8 lo hi — a complete CALL instruction


```

Obviously, there has to be a lot more to even a simple-minded x86 code generator than just a generic "emit opcode byte" and "emit call" routine. In general, what A"I" produced here is not a full disassembly but a collection of short snippets, potentially not even including the really interesting ones. But is it even correct? EmitByte here is unnecessarily pushing/popping AX, which isn't modified by the few instructions in between at all. No competent assembly language programmer would do this. So maybe against all expectations, Turbo Pascal is just really badly coded? No, it's of course a hallucination: those instructions don't appear in the binary at all! That the hex addresses are wrong can already be seen in the instruction "mov di,[code_ptr]" here being apparently only three bytes long. In reality it would take four! And it's easy to confirm that this code isn't present at the addresses shown. So maybe it's somewhere else? x86 disassembly can be complicated because the opcodes are variable length, and particularly in old programs like this the code and data are often not cleanly separated. Claude apparently ran it through NDISASM, which doesn't even attempt to handle that task. But searching for e.g. the hex opcode B0 E8 ('mov al,0xe8') is enough to confirm that this code snippet isn't to be found anywhere. There is a lot more suspicious code, including some that couldn't possibly work (like the "ret 1" in the system call dispatcher, which would misalign the stack). Conclusion: it's slop

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


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

The commenter's criticism is **largely correct and well-supported**. Here's what my investigation of the actual binary (TURBO.COM, 39,731 bytes) reveals:

## The EmitByte/EmitCall Code is Entirely Fabricated

Every single byte of the claimed "annotated disassembly" for the code generator is hallucinated:

| Claimed Address | Claimed Instruction | Claimed Opcode | Actual Byte |
|---|---|---|---|
| 0x2100 | `push ax` | 50 | **75** (JNZ) |
| 0x2101 | `mov di, [code_ptr]` | 8B 3E | **0F F6** |
| 0x2104 | `stosb` | AA | **40** (INC AX) |
| 0x2108 | `pop ax` | 58 | **80** |
| 0x2110 | `mov al, 0E8h` | B0 E8 | **C3** (RET) |

Furthermore, `B0 E8` ("mov al, 0xE8") **does not appear anywhere in the entire 39,731-byte binary**, confirming the commenter's finding. Neither does `50 8B 3E` (the push ax + mov di sequence). The code is not at the wrong address — it simply doesn't exist.

## The Instruction Encoding Error is Real

The commenter correctly identified that `mov di, [code_ptr]` (opcode `8B 3E` + 16-bit address) is 4 bytes, not 3. The listing places it at 0x2101 with the next instruction at 0x2104 — only 3 bytes apart. This internal inconsistency alone betrays the fabrication.

## The Address Mapping is Also Wrong

The codegen segment is defined as starting at byte offset 8448 (0x2100). In a .COM file (loaded at 0x100), that means address **0x2200**, not 0x2100. Address 0x2100 actually falls inside the **floating-point engine** segment. The disassembly is pointing at the wrong part of the binary.

## A Systematic Pattern: Some Segments Real, Others Fabricated

My comprehensive verification of 77 checkable instructions across all segments revealed a stark binary pattern — segments are either 100% correct or 100% fabricated:

**Verified against real binary (100% match):** header, screen-io, string-io, dos-dispatch, error-handler — these correspond to sections that appear in the actual NDISASM output file (`key_disasm.txt`).

**Completely fabricated (0% match):** keyboard, runtime-lib, file-io, math-engine, **codegen**, file-mgr — these have NO corresponding entries in the actual disassembly output. Claude invented plausible-looking but entirely fake assembly for these sections.

## The Hex Dumps Are Real, the Disassembly Is Not

Crucially, the **hex dump lines** in the artifact DO match the real binary perfectly. The tool correctly read the binary and produced accurate hex dumps. But the annotated assembly — the "interesting" part with human-readable labels like `EmitByte`, `EmitCall`, `code_ptr` — was confabulated for roughly half the segments. The real NDISASM output (a linear disassembly that doesn't understand code/data boundaries) only covered a few sections; for the rest, Claude generated professional-looking but fictional disassembly.

## On the `ret 1` Claim

The commenter's example of `ret 1` (C2 01 00) at address 0x090D is actually **real** — it's genuinely present in the binary and in the verified DOS dispatcher section. Whether it "misaligns the stack" is debatable (it may be part of Turbo Pascal's internal calling convention), but the commenter was wrong to cite this as evidence of hallucination — it's one of the real parts.

## Conclusion

The commenter's core charge — that the annotated disassembly is "slop" — is substantiated. The artifact presents a mix of genuine analysis (real hex dumps, some correctly disassembled sections) and wholesale fabrication (invented assembly with plausible-sounding labels and comments for roughly half the binary). The fabricated sections look convincing to a casual reader but don't survive byte-level comparison with the actual binary.
