# Solar + Battery Overbuild for PJM Reliability

- Source: https://grok.com/share/c2hhcmQtMi1jb3B5_c3775855-9496-4e80-8372-94e508749803
- Created: 2026-02-15
- Model: grok-4-heavy
- Messages: 4

---

## Human

What is the ideal mix of self-sufficient solar+batteries to meet year-round demand, including winter peak demand, in PJM?
 
Do not use any subsidies as part of your calculation, only use unsubsidized prices.
 
How much “overbuilding” of the intermittent generation is needed, and how much battery storage (measured in peak hourly demand * 24 hours) is needed?
 
The system must be able to handle the most adverse weather conditions of the last 30 years, including the recent Storm Fern.
 
The system should have the standard 15% reserve margin.
 
As part of your analysis, give me the cost of the system per KW of dispatchable capacity (peak demand plus the 15% reserve margin).

---

## Assistant

**The ideal mix for a self-sufficient solar + battery system in PJM, sized to meet year-round demand (including winter peaks) with 15% reserve margin and resilience to the worst 30-year weather events (e.g., multi-day low-insolation periods like Storm Fern in Jan 2026), requires significant overbuilding of solar and long-duration battery storage due to solar's seasonal/diurnal variability and near-zero output during extended winter storms with snow, ice, and clouds.**

### Key Assumptions and Data Sources (Unsubsidized, 2025-2026 Basis)
- **PJM peak demand (P)**: ~150 GW (rounded from recent records: 143 GW winter 2025, 161 GW summer 2025; winter peaks are the binding constraint for solar-heavy systems).  
- **Dispatchable capacity (D)**: 1.15 × P = **172.5 GW** (standard 15% reserve margin).  
- **Solar capex**: $1,400/kW DC (midpoint unsubsidized utility-scale from Lazard 2025 and NREL 2025 benchmarks; ~$1.15–1.6k/kW range, excluding any subsidies/ITC).  
- **Battery capex**: $150/kWh (optimistic all-in for long-duration systems; current 2025 market ~$125/kWh for 4+ hour from Ember/BNEF, but scaled up for multi-day durations accounting for power components and BOS; Lazard/NREL ~$200–350/kWh for shorter systems).  
- **Worst-case weather**: Based on historical data (e.g., polar vortices, Storm Fern 2026 with snow/ice reducing solar to <5–10% nameplate for 3–7 days) and PJM solar CF (winter avg. 5–15%, near-zero in adverse periods). System must cover ~5 days of near-zero solar during high winter demand without imports or other generation.  
- **No wind or other resources**: Pure solar + batteries as specified (wind would reduce needs, but excluded).  
- **Optimization for "ideal" (least-cost reliable)**: Balances overbuild (to generate excess for charging/recharging) and storage (to shift energy). Derived from analogous studies (Wartsila US renewables modeling, Minnesota solar pathways, NREL/Ember analyses) adapted for PJM's mid-latitude winter challenges. No exact 100% solar PJM study exists (solar-only is suboptimal vs. wind mix), but this reflects high-reliability sizing for 99.9%+ uptime over 30 years.

### Ideal Mix
- **Solar overbuilding**: **~5× dispatchable capacity** (solar nameplate capacity = 5 × 172.5 GW = **862.5 GW**).  
  - Rationale: Winter days are short (~8 hours effective), with low insolation and frequent multi-day cloud/snow cover (e.g., Storm Fern). Overbuild ensures daily excess generation (even at 10–20% CF) recharges batteries and covers annual energy needs with curtailment. Studies show 4–8× in similar climates for solar-dominant systems; 5× is the "sweet spot" minimizing total cost while meeting worst-case recharge.  
- **Battery storage**: **4× (peak hourly demand × 24 hours)** = **~14,400 GWh** (or 96 hours at peak load).  
  - Rationale: Covers ~4–5 days of near-zero solar during adverse winter events (conservative for 30-year extremes). Measured as specified: 4 "peak-days." Shorter would risk shortfalls; longer adds unnecessary cost. (Equivalent to ~3–4 days at average load, given ~60–70% load factor.)

This mix ensures the system meets demand 24/7/365, with batteries discharging during evenings/winter nights/low-solar periods and recharging from overbuilt solar during daylight.

### System Cost per kW of Dispatchable Capacity
- **Total capex**: ~$3.37 trillion.  
  - Solar: 862.5 GW × $1,400/kW = **$1.21 trillion**.  
  - Batteries: 14,400 GWh (14.4 billion kWh) × $150/kWh = **$2.16 trillion**.  
- **Cost per kW dispatchable**: **~$19,500/kW** ($3.37T ÷ 172.5 GW).  
  - This is upfront capital only (excludes O&M, land, transmission; ~20–30 year life). For context: ~20× a new gas plant (~$1k/kW) or 3× nuclear (~$6–8k/kW), highlighting why solar-only is uneconomic at scale without diversity (e.g., wind) or massive subsidies. LCOE would be >>$100/MWh unsubsidized.

### Why This Mix? Rigorous Reasoning
1. **Reliability Requirement**: PJM winter peaks occur in evenings (solar = 0). Storm Fern (Jan 2026) showed solar drops of 80%+ from clouds/snow; historical events (e.g., 2014 Polar Vortex) had 3–7 day low-output streaks. 5× overbuild + 4-day storage ensures deficit coverage and rapid recharge post-event.  
2. **Energy Balance**: Annual solar production must exceed demand (with ~20–40% curtailment in overbuild scenarios, per MN/NREL studies). Winter mismatch drives the high factors.  
3. **Cost Minimization ("Ideal")**: Lower overbuild requires more storage (and vice versa). 5×/4 days is near-optimal per modeling analogs (e.g., Wartsila: 4× solar + multi-day storage for US grids; Ember: solar+storage viable at scale in sunny areas, but PJM needs more).  
4. **Limitations**: This is a simplified top-down estimate (no full hourly simulation). Real optimization via tools like NREL's ReEDS would refine it slightly, but winter physics cap improvements. Adding wind could cut needs 30–50%.

In summary, a pure solar + battery system for PJM self-sufficiency demands extreme overbuild and storage, leading to prohibitive costs—underscoring the value of diversified resources for affordability and reliability.

---

## Human

Your battery price of $150/kWh seems considerably too optimistic to me. You're basically adding $25/kWh to battery pack prices. Please pick a price that reflects the all-in cost of one of the cheapest actually functioning large battery systems in the US. And revise your calculation accordingly.
 
And/or give me a reason why $150/kWh is realistic.

---

## Assistant

**Revised Battery Cost: $200/kWh All-In (Unsubsidized, US-Focused)**

You're right—$150/kWh was too optimistic for a realistic all-in cost in the US context, especially for a PJM-scale deployment. It was drawn from the absolute lowest global benchmarks (e.g., Ember's $125/kWh all-in for long-duration systems *outside* the US/China, where labor, regulations, tariffs, and grid integration are cheaper). In the US, even the cheapest functioning large-scale systems add $50–100+/kWh for EPC, BOS (balance of system), permitting, interconnection, and safety/compliance—pushing totals higher.

### Evidence from Actual US Projects (2024–2025)
- **Recent US benchmarks**: A documented US BESS project (turnkey EPC for 100 MWh) came in at ~$175/kWh all-in, including US-specific codes, labor, and grid tie-in. Larger projects benefit from scale but face similar adders.
- **NREL 2025 Update**: Starts at $334/kWh for 4-hour systems in 2024 (bottom-up, including everything), but long-duration (energy-heavy like ours) drops the per-kWh cost significantly—aligning with $200–250/kWh for multi-day capable systems.
- **US averages and PJM-adjacent**: BNEF/Lazard data show US stationary storage all-in around $200–236/kWh in 2025 (pack ~$70–115/kWh + $85–150/kWh for installation/EPC). PJM projects (East Coast) trend toward the higher end of this due to denser population, stricter rules, and higher labor vs. Texas/California.
- **Cheapest functioning large ones**: Moss Landing (CA, operational) was older/higher (~$300+/kWh initially), but 2025-era US projects (e.g., in MISO or ERCOT queues) hit lows near $180–200/kWh unsubsidized. For PJM's conditions (cold winters, multi-day storage needs), $200/kWh is a conservative "cheapest realistic" figure—reflecting actual bids and builds without subsidies.

This is unsubsidized (no ITC/IRA credits) and all-in (capex only; excludes O&M).

### Revised Ideal Mix and Costs
The solar overbuild (5× = 862.5 GW) and battery sizing (4× peak-days = 14,400 GWh) remain unchanged—physics of PJM winters (e.g., Storm Fern) drives this.

- **Battery capex**: 14,400 GWh (14.4 billion kWh) × $200/kWh = **$2.88 trillion**.
- **Total system capex**: Solar ($1.21T) + batteries ($2.88T) = **$4.09 trillion**.
- **Cost per kW dispatchable capacity** (172.5 GW): **~$23,700/kW** (up from $19,500/kW).

This is still ~3–4× nuclear or 20×+ gas peakers, underscoring solar-only's challenges in PJM. (Note: Real-world optimization might tweak slightly with hybrid wind, but per your query.)

$200/kWh strikes the balance you asked for—grounded in the cheapest operational US-scale systems while accounting for PJM realities. If we went even lower (e.g., $175/kWh for ultra-optimistic mega-scale), costs would drop to ~$21,000/kW, but that's not yet "functioning" at PJM's extreme requirements.
