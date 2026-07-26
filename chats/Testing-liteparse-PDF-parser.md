# Testing liteparse PDF parser

- Source: https://claude.ai/share/44a5ed86-e5b5-4e14-90be-1eba1e0acd13
- Author: Simon
- Created: 2026-04-23
- Messages: 10

---

## Human

Clone https://github.com/run-llama/liteparse and try it against this file

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

Cloned, built, and ran it against your PDF. Summary:

**Setup**
- `git clone` → `npm install` (319 pkgs) → `npm run build` (tsc + vendor copy). Clean build, no errors.

**Parse run** (30 pages, ~15 MB, `--no-ocr`):
- Text mode: **~5s**, 42 KB output, 959 lines
- JSON mode: **~5s**, 484 KB output — `{pages: [{page, width, height, text, textItems[], boundingBoxes[]}]}`, totaling 1,080 text items with per-item font info (`fontName`, `fontSize`, `x/y/width/height`, `confidence`)
- Screenshot of 2 pages at 100 DPI: ~3s, clean PNGs

**Quality observations**

Prose pages extract very cleanly — the author list, reviewer list, introduction, and the timeline on page 12 all came through with proper reading order. The timeline preserved date headers, event titles, and bullet indentation.

The one gap: the **risk register on pages 17–20** is embedded as a rasterized image in the PDF (not live text), so the no-OCR pass extracted only the surrounding prose and section headers — the table cells are empty in the text output. You can see this clearly in the page-17 screenshot I rendered. To get that table content, you'd need to re-run with OCR enabled (drop `--no-ocr`, Tesseract.js is bundled), at the cost of significantly more time and an internet fetch for the English traineddata on first run.

Two-column layouts (e.g. executive summary) are handled correctly — it reads left column then right column as separate paragraphs rather than interleaving lines.

Both outputs are attached above.

---

## Human

Run with OCR enabled

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

Excellent — the OCR now captures the rasterized risk register table content (with some expected minor OCR artifacts like "Al" instead of "AI" since Tesseract reads the capital "I"). Now the full document:
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

Done. OCR pass completed on all 30 pages in ~100s after a bit of sandbox plumbing.

**One speed bump worth noting**: Tesseract.js by default pulls its language model from `tessdata.projectnaptha.com`, which isn't in this sandbox's domain allowlist — the first attempt hung silently. I grabbed the `eng.traineddata` via the `@tesseract.js-data/eng` npm package (npm registry is allowed) and pointed `TESSDATA_PREFIX` at it, and things worked.

**What OCR recovered**

The extraction jumped from 1,080 text items / 42 KB to **3,493 items / 69 KB** — a 3× gain entirely from content that was baked into the PDF as raster images:

| Page | Items before | After | Content |
|---|---|---|---|
| 17–23 | 2–16 each | 105–378 each | Risk register & priority-action tables |
| 28–30 | 2–4 each | 91–210 each | Framework legend tables (appendix B) |
| 9, 27 | — | +16, +13 | The "From Vulnerability to Exploitation" chart labels |

Pages 1–8, 10–16, 24–26 were unchanged — those were already native text and OCR added nothing.

**Quality**: the table structure comes through in reasonable reading order, though with a few Tesseract-typical artifacts — mainly "AI" reading as "Al" (capital-I looks like lowercase-L in the source font), occasional dropped periods, and column boundaries rendered as whitespace rather than real delimiters. Good enough for search and downstream LLM ingestion; not clean enough for a structured-table extraction pipeline without post-processing.

Both outputs attached.

---

## Human

How does the no ocr mode work?

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

I now have a concrete picture from the source. Here's how no-OCR mode actually works:

**The pipeline** (see `src/core/parser.ts` line 160 onward):

```
loadDocument → extractAllPages → [skip OCR] → projectPagesToGrid → buildBoundingBoxes → format
```

**1. Load (`pdfjs.ts:666`)**  
If given a path, reads the file into a `Uint8Array`; if given bytes, skips disk entirely. Hands it to a vendored Mozilla PDF.js build (the 16 MB under `src/vendor/pdfjs`). PDF.js parses the PDF object graph, fonts, and CMaps.

**2. Extract glyphs per page (`pdfjs.ts:721–810`)**  
The key call is `page.getTextContent()` — this returns every text-showing operation the PDF has already laid out, with font info and a 2×3 transform matrix per item. **Critically, PDF.js is not doing OCR here.** PDFs store text as actual character codes tied to a font's ToUnicode map, plus positioning operators that say "draw this glyph at matrix M". LiteParse reads those directly.

For each item it then:
- Multiplies the viewport transform by the item transform (`multiplyMatrices`) to convert PDF's bottom-left-origin coordinate space to screen-style top-left coordinates.
- Derives a tight bounding box from the lower-left and upper-right corners.
- Pulls rotation out of the matrix via `atan2(transform[1], transform[0])`.
- Pulls font size via `sqrt(a² + b²)` on the transform.
- Drops items with zero size or off-page coords.
- Runs Unicode cleanup: decodes "buggy font" markers (their patched PDF.js emits `:->|>_glyphId_charCode@glyphName@<|<-:` for fonts whose ToUnicode maps to Private Use Area or control chars), maps those glyph names through an Adobe Glyph List subset, decomposes ligatures (fi, fl), strips Windows-1252 C1 junk.
- If the text still looks garbled (Private Use Area, random script mixing, box-drawing characters in prose), the item is dropped and its bbox is saved to `garbledTextRegions` — that's the hook OCR would normally fill. With OCR off, garbled regions just stay blank. (This is why pages 17–23 in your document came out mostly empty in the no-OCR pass — those aren't text at all, they're raster images, so PDF.js has nothing to decode.)

At the end of this step you have a flat list of `TextItem { str, x, y, width, height, rotation, fontName, fontSize, confidence: 1.0 }`.

**3. Layout reconstruction — `projectPagesToGrid` (`processing/gridProjection.ts`, ~1650 lines, the hard part)**  
The flat list is just disconnected glyphs in space — no notion of "words", "lines", or "columns". This stage reconstructs reading order:
1. Group items by rotation so rotated blocks stay together.
2. `bboxToLine` — sort into lines by Y with a tolerance that scales with median glyph height (handles subscripts/superscripts).
3. `extractAnchorsPointsFromLines` — find recurring left-edges, right-edges, and centers across all lines, rounded to the nearest ¼ unit. These become column anchors.
4. For each line, classify each item as snapping left, right, center, or floating to one of those anchors. This is how it knows "these two bits of text are actually two columns, not one sentence."
5. `projectToGrid` — lay the items onto a character grid with `COLUMN_SPACES = 4` between columns and `FLOATING_SPACES = 2` between floating items, turning the 2D layout back into ordered text.
6. A margin-line-number detector catches short numbers in the gutter of two-column layouts so they don't get glued onto prose.

This is the step that gave you correctly-ordered two-column extraction on pages like the executive summary.

**4. Bounding boxes (`processing/bbox.ts:316`)**  
If `--no-precise-bbox` isn't set, one `{x1,y1,x2,y2}` box is emitted per remaining text item for the JSON output.

**5. Format**  
Either concatenate `page.text` joined by blank lines (text mode), or wrap the per-page `{width, height, text, textItems, boundingBoxes}` into JSON.

**The practical takeaway**: no-OCR mode is fast (~5s for your 30-page document) because it's essentially "read what's already spelled out in the PDF, then solve a geometry problem to put it in reading order." It extracts zero characters from anything rasterized — images, scans, or, as in your document, tables that were exported as pictures. That's exactly the gap the OCR stage fills, using the `garbledTextRegions` and image bboxes as targets so OCR results don't overwrite good PDF text.

---

## Human

How does that change when you use OCR mode?

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

Here's how the pipeline changes when OCR is on — concrete, source-grounded:

**What's added upfront**

In `parser.ts` the `extractAllPages` call now passes `extractImages: true` (line 166), so the PDF.js engine additionally asks PDFium to enumerate every embedded image on each page via `extractImageBounds` (lines 812–843 of `pdfjs.ts`). Each image gets a bounding box attached to the page. This doesn't happen in no-OCR mode — it's skipped for speed.

After text extraction, before the grid-projection stage, `runOCR(doc, pages)` runs (`parser.ts:170`). It uses `pLimit(numWorkers)` to OCR pages concurrently, though with Tesseract the effective concurrency is limited by the worker pool.

**Per-page triage — OCR is not unconditional**

In `processPageOcr` (line 356) each page is classified:
- `textLength = sum of str.length across all PDF text items`
- `hasGarbledRegions = len(garbledTextRegions) > 0` (the Private-Use-Area / Arabic-Latin-mix / box-drawing bboxes that the text-extraction stage dropped)
- `needsFullOcr = textLength < 100 || page.images.length > 0`

If neither is true, the page is **skipped entirely** — no rasterization, no OCR. This explains what you saw in your document: pages 10–16 and 24–26 had `+0` items added because they had plenty of native text and no suspicious images. Pages 17–23, 28–30 hit `textLength < 100` and got rasterized. Pages 9 and 27 got `+16` and `+13` because a chart/diagram image triggered `images.length > 0`, so OCR ran but only produced a handful of results.

**The rasterize step**

When a page is flagged, `pdfEngine.renderPageImage(doc, pageNum, dpi)` runs. This delegates to `PdfiumRenderer.renderPageToBuffer` (not PDF.js — separate engine, explicitly because PDFium renders better for OCR; see `pdfium-renderer.ts:84`). Key detail: `scale = dpi / 72`. At the default 150 DPI each page is rasterized at ~2× PDF coordinate resolution. PDFium renders to raw RGBA, then Sharp wraps it as PNG and returns a `Buffer`. No temp file.

**Tesseract does the OCR**

`ocrEngine.recognize(imageBuffer, { language, correctRotation: true })` (line 388). Inside `tesseract.ts`:
- A `Scheduler` holds a pool of up to `numWorkers` workers, each loaded with `eng.traineddata` (the 23 MB file I pulled from npm earlier).
- `correctRotation: true` enables Tesseract's `rotateAuto` for upside-down/sideways content.
- `blocks: true` makes Tesseract emit the full hierarchy: blocks → paragraphs → lines → words. Only word-level results are collected, each carrying `{ text, bbox: [x0,y0,x1,y1], confidence/100 }`.
- First confidence filter happens here: `results.filter(r => r.confidence > 0.3)` (line 149, the 30% cutoff from the README).

**Coordinate remapping and deduplication**

OCR bboxes are in image pixels, but the rest of the pipeline works in PDF points. In `parser.ts:397`:

```
scaleFactor = 72 / config.dpi   // e.g. 72/150 = 0.48
```

Every OCR bbox is multiplied by this to land in the same coordinate space as the PDF text items. Then three filters run, in order (lines 446–476):

1. `confidence > 0.1` — a second, looser cutoff (30% was already applied in Tesseract, so this is belt-and-suspenders for HTTP OCR backends that may not pre-filter).
2. **Targeted mode**: if the page has `garbledTextRegions` but *not* `needsFullOcr`, only keep OCR results whose bbox overlaps a garbled region (±5 PDF points). This is the "selective OCR replacement" case from the PDF engine README — corrupted-font text gets repaired without rasterizing around it.
3. **Spatial dedup against existing PDF text**: drop any OCR result that overlaps any existing text item (±2 PDF points). Prevents Tesseract's read of native text from double-counting. On full-OCR pages this matters because the page body was mostly blank (rasterized tables) but it may still have native page numbers, footers, and titles.

4. `cleanOcrTableArtifacts` runs on each surviving result — my guess is pipe/dash/border-stroke misreads; quick check:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Confirmed — the cleaner strips `| [ ] ( ) { }` characters at the start or end of numeric-looking cells, because vertical table borders read as those characters.

**Merging and what happens downstream**

Surviving OCR results are converted into the same `TextItem` shape the PDF-extraction stage produced (`parser.ts:463–474`), but with two tells: `fontName: "OCR"` and `confidence` populated with the real Tesseract score (rounded to 3 decimals) rather than the `1.0` native text gets. They're then just `push`-ed onto `page.textItems` — the list becomes a mixed bag of native items and OCR items that `projectPagesToGrid` doesn't need to know apart.

From here, everything that happens in no-OCR mode happens identically. The grid-projection algorithm (anchors, snap detection, line grouping, column spacing) sees every item as just `{str, x, y, w, h, rotation, fontName, fontSize, confidence}` and sorts them into reading order. That's how the risk register table came back with mostly-intact row structure — the OCR gave it a dense field of items with sensible bboxes, and the grid projector did the same two-column / multi-column reconstruction it would have done on native text.

**Why the whole thing took ~100 seconds for your document**

Not the number of pages, but the number of flagged pages × rasterization time × OCR time. 12 of 30 pages needed OCR. At 150 DPI an 8.5×11 page is ~1275×1650 pixels; PDFium renders that in a few hundred milliseconds, and then Tesseract typically spends 3–8 seconds on a page of that size at default settings. Sequential by default (`concurrency: 1` in the log) because I didn't bump `--num-workers`. You could get ~3-4x speedup by setting `--num-workers 4`, at the cost of 4× peak RAM — each Tesseract worker holds its own copy of the trained model.

**The one subtle design choice worth flagging**

The `needsFullOcr = textLength < 100 || images.length > 0` heuristic will miss a page that has, say, 200 characters of native caption text *plus* a large rasterized chart with no separate image bbox detected by PDFium — it'll look "text-rich enough" and OCR won't fire. Conversely, a pure text page with a tiny decorative icon that PDFium registers as an image will trigger a full-page OCR it didn't need. In your document, page 9 is an example of the second case: the timeline chart triggered OCR even though the page already had plenty of native prose. The `overlapsExistingText` filter catches most of the wasted work, but the rasterization itself still happened.

---

## Human

Does this library run in a browser? Could it?

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

Short answer: **no, not as-is. Yes, with targeted changes** — and the core text-extraction path is closer to browser-ready than it looks.

**What blocks it today**

From `package.json`: `"engines": { "node": ">=18.0.0" }`, Node-style `bin` entries, ESM. Grepping the source for Node built-ins, the Node-coupled files are:

| File | Node dep | Purpose |
|---|---|---|
| `engines/pdf/pdfjs.ts` | `node:fs/promises` | Reading PDF from a path |
| `engines/pdf/pdfium-renderer.ts` | `fs`, `sharp` | Page rasterization for OCR |
| `engines/ocr/http-simple.ts` | `fs` (file upload) | HTTP OCR client |
| `conversion/convertToPdf.ts` | `fs`, `path`, `os`, `child_process` | LibreOffice/ImageMagick conversion |
| `processing/gridDebugLogger.ts` | `fs`, `path` | Debug tracing (optional) |
| `processing/gridVisualizer.ts` | `fs`, `sharp` | Debug image output (optional) |
| `engines/ocr/tesseract.ts` | `process.env.TESSDATA_PREFIX` | Offline tessdata lookup |
| `cli/parse.ts` | `commander`, `fs` | CLI — irrelevant for library use |

And from `dependencies`: `sharp` is a native Node addon (libvips bindings), `file-type` v21 is Node-only, `p-limit`'s package manifest declares `browser: false` (though in practice it's pure ESM and does work).

The only *hard* blocker in that list is `sharp`. Everything else is either a straight swap or isolated to a feature you can disable.

**What's already browser-shaped**

The big pieces:
- **PDF.js** — the vendored `pdf.mjs` is the normal browser build. `pdfjsImporter.ts` installs stubs for `DOMMatrix`, `Path2D`, `ImageData` *because it's running in Node*; a browser has those natively, so the stubs would just get skipped. The worker file `pdf.worker.mjs` is already a standard ES module worker.
- **Tesseract.js** — originally designed for browsers. Runs via WASM + Web Workers. Accepts `ImageData`, `HTMLCanvasElement`, `Blob`, `File`, or `ArrayBuffer` directly.
- **@hyzyla/pdfium** — WASM-based, declares `"browser": true` in its manifest.
- **Everything in `src/processing/`** — grid projection, bbox building, text cleanup, coordinate math, the Adobe Glyph List tables. ~1,650 lines in `gridProjection.ts` alone, zero Node imports. This is the interesting 80% of the library and it would port without a single line change.
- **`src/core/parser.ts`** — zero Node built-ins. Just orchestrates the other pieces.

**The concrete changes you'd need**

1. **Replace `sharp`**. In `pdfium-renderer.ts` it's used to wrap PDFium's raw RGBA output as PNG. Browser swap: either use `OffscreenCanvas.convertToBlob()` / `canvas.toDataURL()`, or — cleaner — **skip PNG encoding entirely** and hand the raw RGBA to Tesseract.js as `ImageData`, which it accepts natively. That actually makes the browser version faster than the Node one, which currently encodes PNG only to have Tesseract decode it again.

2. **Gate the path-based `loadDocument` branch** (`pdfjs.ts:668`). The `Uint8Array` branch already works unchanged; you'd just throw a clear error if someone passes a string in a browser context. `File`/`Blob` → `Uint8Array` is one `arrayBuffer()` call at the call site.

3. **Drop or stub `conversion/convertToPdf.ts`**. It shells out to LibreOffice and ImageMagick. No browser equivalent short of shipping a WASM LibreOffice (it exists, but it's ~50 MB). Realistic approach: browser build supports PDF and images only, throws on `.docx`/`.pptx`/`.xlsx`.

4. **Guard `process.env` and `process.stderr.write`** behind `typeof process !== 'undefined'`. Two sites, five lines total.

5. **Bundler asset handling**. `pdf.worker.mjs`, the WASM blobs (`jbig2.wasm`, `openjpeg.wasm`, `qcms_bg.wasm`), the CMap tables, standard fonts, and Tesseract's `eng.traineddata` all need to be resolvable as URLs at runtime. Vite / webpack / esbuild all handle this with `import.meta.url` + an asset plugin. The existing `pdfjsImporter.ts` already uses `new URL(..., import.meta.url)` — that pattern works in browsers.

6. **Debug-only files** (`gridDebugLogger`, `gridVisualizer`) — tree-shake them out of the browser bundle or stub the write calls.

**How much work**

Rough sketch:
- Browser build producing correct text extraction (no OCR) on a `Uint8Array`-in-memory PDF: a day, maybe two. The changes are mechanical.
- Plus OCR: another half-day once the rasterizer is rewired to skip PNG encoding.
- Feature parity including Office conversion: not worth it; restrict the browser build to PDF + images.

**Why nobody has done it yet is probably intentional**

The library has a CLI-first shape — `lit parse document.pdf` is the headline usage — and LlamaIndex clearly positions this as local tooling paired with their cloud product (LlamaParse) for the harder cases. A browser build would overlap more directly with things like PDF.js-powered web viewers and compete with it for the same niche. But there's no technical reason it couldn't exist; the core algorithm is pure, dependency-free TypeScript, and the Node coupling is at the edges.
