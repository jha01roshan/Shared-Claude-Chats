# Claude queries per gallon of gasoline

- Source: https://claude.ai/share/44fdc891-0fe5-40f3-a5b5-b203bbb6ab02
- Author: Casey
- Created: 2026-06-08
- Messages: 2

---

## Human

How many Claude queries can I make for the equivalent energy in 1 gal of gas?

---

## Assistant

A gallon of gasoline contains about 33.7 kWh (120 megajoules) of energy.

A single text query to Claude uses roughly 0.1 to 0.3 watt-hours, based on published estimates for typical LLM inference. Using ~0.2 Wh as a midpoint:

33,700 Wh ÷ 0.2 Wh ≈ **170,000 queries**

So very roughly on the order of 100,000–300,000 queries, depending on which per-query estimate you use (a range of about 110,000 at 0.3 Wh to 340,000 at 0.1 Wh).

Big caveats: per-query energy figures vary widely by model size, query length, and methodology, and most published numbers don't capture full lifecycle/cooling/training-amortization energy. Treat this as an order-of-magnitude answer, not a precise one.
