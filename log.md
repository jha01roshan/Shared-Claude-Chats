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
