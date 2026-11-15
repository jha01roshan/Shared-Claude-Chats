# Project Log

Append-only session log. **Read this before starting new work** – other IDEs/sessions may have changed the project.

| Field | Format |
|---|---|
| Model / Date | who did it, when |
| Ask | what the user wanted |
| Approach | how it was tackled |
| Accomplished | outputs, files changed |
| Notes / Next | caveats, follow-ups |

---

## Session – Claude Sonnet 5.5 | 2026-11-15

**Ask:** Tejas (child) struggles with decimals ↔ fractions (e.g. 0.45 = 45/100) in a decimals workbook (ex. 10–16: place the decimal point, fill placeholders, divide, fraction→decimal). Wanted (A) a one-page colourful teaching sheet with a memorable trick and (B) 20 practice questions on the *underlying fundamentals* (not copies of the workbook questions), as a printable PDF: page 1 colour, other pages B/W but ink-efficient.

**Approach:** Built a "SEE · SWAP · SOLVE" method (count digits after the point → write as fraction over 10/100/1000 → solve with fractions / "hop rule"), plus ÷10/100/1000 hops, fraction→decimal by fixing the bottom, and "find the ?" by opposite operation. Generated with reportlab (`tejas_decimals/make_pdf.py`), rendered pages to PNG and visually checked layout.

**Accomplished:**
- `tejas_decimals/Tejas_Decimals_Fractions.pdf` – p1 colour lesson; p2–3 B/W practice (20 Qs in 5 sections A–E); p4 B/W answer key + parent tip.
- `tejas_decimals/make_pdf.py` – generator (edit & re-run to change content).

**Notes / Next:** From the photo, several of Tejas's written answers in Ex.12/14 look like decimal-place (hop count) slips, e.g. 0.2×0.3 written 0.6 (should be 0.06), 15×0.06 → 0.9, 20×0.05 → 1, 0.009×50 → 0.45, 0.001×0.1 → 0.0001, 11/8 → 1.375 – worth re-checking against the sheet's Hop Rule. Suggest re-doing those after Q6–10.

---

## Session – Claude Sonnet 5.5 | 2026-11-15 (#2)

**Ask:** "Another two-sheeter just like the previous" – 2-page PDF (p1 colour lesson, p2 B/W practice), no answer sheet – plus a print command.

**Approach:** Picked the next workbook skill (Ex.13 dividing decimals; Tejas's 11/8 slip is also a division). Method "SHIFT · DIVIDE · PLACE" (division = fraction, ×10 top & bottom = shift both points), with long-division picture for fraction→decimal, trap alert (÷ by <1 gets bigger), zeros-are-free, find the ?. Reused helpers from `make_pdf.py`.

**Accomplished:** `tejas_decimals/Tejas_Dividing_Decimals.pdf` (2 pages, A4) and generator `tejas_decimals/make_pdf2.py`. Checked layout via rendered PNGs; fixed overflowing tick-boxes and cluttered long-division sketch.

**Notes / Next:** Answers (for the parent) were given in chat, not in the PDF. Cloud session can't reach a printer – print commands were provided for the user's own machine.

---

## Session – Claude Sonnet 5.5 | 2026-11-15 (#3)

**Ask:** Correction to #2 – wanted a practice-only 2-page B/W PDF "like last time" (same skills as sheet 1: decimal↔fraction, multiplying, hops, fraction→decimal, find the ?) with different numbers; no lesson/explanation page; keep the small hint line above each question. (Sheet #2 "Dividing Decimals" was a misread – kept in repo but not what was wanted.)

**Approach:** Reused the practice layout from `make_pdf.py`, overrode the 20 questions with new numbers in `make_pdf3.py`.

**Accomplished:** `tejas_decimals/Tejas_Decimals_Practice_2.pdf` (2 pages, A4, B/W) + `make_pdf3.py`. No answer key in PDF.

**Notes / Next:** Answers: 1) 8/10 2) 53/100 3) 407/1000 4) 0.17 5) 1,2,3 6) 21/100=0.21 7) 30/100=0.3 8) 72→0.72 9) 28→0.028 10) 0.48 11) 617 12) 0.095 13) 40 14) 38/100=0.38 15) 8/10=0.8 16) 45/100=0.45 17) 375/1000=0.375 18) 6 19) 58 20) 0.3
