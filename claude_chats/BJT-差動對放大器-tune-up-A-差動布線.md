# ⚡ BJT 差動對放大器 tune up + A* 差動布線

- Source: https://claude.ai/share/9db84c15-442a-4d82-99bf-c7e42ffa1078
- Author: Yao
- Created: 2026-03-06
- Messages: 13

---

## Assistant

I'll customize this artifact:


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


Transform any artifact into something uniquely yours by customizing its core elements.

1. Change the topic - Adapt the content for a different subject
2. Update the style - Refresh the visuals or overall design
3. Make it personal - Tailor specifically for your needs
4. Share your vision - I'll bring it to life

Where would you like to begin?

---

## Human

is routing based on a*

---

## Assistant

Yes, the PCB routing in the artifact is genuinely implemented with A* search. Here's how it works:

**The core A* logic:**
- Each grid cell is a `Node` with `g(n)`, `h(n)`, and `f(n)` values
- `g(n)` = actual cost from start (number of steps taken)
- `h(n)` = Manhattan distance heuristic to the goal: `|dx| + |dy|`
- `f(n) = g(n) + h(n)` — nodes are sorted by this each step
- The open/closed list mechanism is fully implemented — you can see the yellow (open) and teal (closed/visited) cells animating in real time during routing

**What makes it PCB-specific:**
- Component footprints are registered as **obstacles** — the algorithm navigates around them
- Previously routed traces are added back as obstacles before routing the next net, so wires don't overlap
- 14 nets are routed sequentially (bias, load, signal, tail currents)

**The differential pair matching aspect:**
- Vin+ (pink) and Vin− (blue) traces are routed separately through A*
- Their path lengths are compared afterward to compute the **matching percentage** shown in the panel

**What's simplified vs. real EDA tools:**
- Only 4-directional movement (no diagonals)
- Single routing layer (no vias)
- No design rule checking (DRC) beyond obstacle avoidance

So while it's not a full industrial router, the search algorithm itself is authentic A* — not simulated or faked.

---

## Human

is parameter of component optimization based on A*

---

## Assistant

**No, the component parameter optimization is not based on A*.** It's essentially animated interpolation — here's an honest breakdown:

**What's actually happening:**
```javascript
const gain = lerp(33.4, 52.1, t);   // linear interpolation
const cmrr = lerp(65, 98, t);
const gbw  = lerp(10, 45, t);
const pm   = lerp(35, 62, t);
```
The values simply slide from a hardcoded "before" number to a hardcoded "after" number over time, with an easing curve applied. There's no search, no cost function, no optimization logic at all.

**What real parameter optimization would require:**
- A **cost/objective function** — e.g. minimize `1/CMRR + 1/GBW + |Vos|`
- A **search space** — discrete component values (E24 resistor series, standard cap values) or continuous ranges
- An **algorithm** — A* could theoretically work if you discretize the parameter space, but gradient descent, genetic algorithms, or simulated annealing are more natural fits for analog circuit sizing
- A **circuit model** — actual equations relating `IEE`, `Rc`, `β`, `VA` to gain/CMRR/bandwidth

**What A* is actually good for in circuit design:**
- PCB routing ✅ (as implemented)
- Netlist traversal
- State-space search in logic synthesis

**Bottom line:** The artifact uses A* authentically for routing, but the parameter optimization panel is purely cosmetic animation. If you'd like, I can rebuild the optimization side to use a real search algorithm — for example, A* or hill-climbing over a discretized component value space with actual BJT small-signal equations driving the metrics.

---

## Human

parameter before/after optimization table

---

## Assistant

The table values are **entirely hardcoded** — not computed from any circuit model. Here's the full picture:

**What's hardcoded (fake):**

| Parameter | Before | After | Basis |
|---|---|---|---|
| A_d | 33.4 dB | 52.1 dB | made up |
| CMRR | 65 dB | 98 dB | made up |
| GBW | 10 MHz | 45 MHz | made up |
| V_os | ±5.0 mV | ±0.3 mV | made up |
| PM | 35° | 62° | made up |

**What real values would be derived from:**

- **A_d** = `gm × (ro_n ∥ ro_p)` where `gm = IC / VT`
- **CMRR** = `gm × ro_tail` — depends directly on tail current source impedance
- **GBW** = `gm / (2π × Cc)` — from Miller compensation cap
- **V_os** = `VT × ΔRc/Rc + ΔVbe` — from resistor mismatch
- **PM** — requires full Bode plot computation with pole/zero locations

**To make it real would need:**
- Actual component values (IC, β, VA, Rc)
- BJT small-signal equations evaluated per stage
- Each table row recomputed after each optimization stage is "applied"

Would you like me to rebuild the table with **real BJT small-signal equations** so the before/after numbers are actually derived from the circuit topology changes rather than interpolated between hardcoded constants?

---

## Human

yes

---

## Assistant

Good catch — let me rebuild the optimization section with real BJT small-signal equations. Every value will be derived from actual circuit theory.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```

Here's exactly what changed and why the new values are real:

**The core function `calcStage()` now derives every value from actual BJT small-signal theory:**

| Parameter | Old (fake) | New equation | S0 result | S4 result |
|---|---|---|---|---|
| **Aᵈ** | lerp(33.4→52.1) | `gm × Rout` | 39.1 dB | 62.2 dB |
| **CMRR** | lerp(65→98) | `2·gm·ro_tail` / `gm·ro_tail` | 52.5 dB | 97.7 dB |
| **GBW** | lerp(10→45) | `Ad × fp1` | 6.50 MHz | 4.02 MHz |
| **PM** | lerp(35→62) | `90°−Σarctan(f/fpi)` | 27.6° | 87.3° |
| **Vos** | lerp(5→0.3) | `VT·(ΔRc/Rc) + ΔVbe` | 3.3 mV | 0.18 mV |

**Three genuinely surprising results the fake numbers hid:**

1. **GBW actually *decreases* from 6.5→4.0 MHz** — Miller compensation deliberately trades bandwidth for stability. This is correct engineering, not a bug.

2. **Stage 3 (active load, no Cc) is *unstable*: PM = −1.7°** — GBW jumps to 612 MHz and parasitic poles at 100 MHz kill the phase. The fake table never showed this.

3. **CMRR dips from S1→S3** (103.7→97.7 dB) because the formula changes from `2·gm·ro_tail` (passive) to `gm·ro_tail` (active mirror) — a real factor-of-2 effect.

---

## Human

component values before/after

---

## Assistant

Good call — right now the tables only show *performance metrics*, not the actual component values that drive them. I'll add two explicit tables showing the chain: **physical components → small-signal parameters → performance**.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```

The artifact now shows the complete design chain across three explicit tables:

**Layer 1 — Physical component values** (what you actually place on the PCB):

| What changes | S0→S1 | S2 | S3 | S4 |
|---|---|---|---|---|
| Tail source | Re=10kΩ → Widlar mirror | — | — | — |
| IEE | 1.0 mA → 2.0 mA | — | — | — |
| Rc load | 4.7kΩ ±5% | ±0.1% trim | replaced by PNP mirror | — |
| Miller Cc | — | — | — | 10 pF added |

**Layer 2 — Small-signal parameters** (derived from Layer 1 via equations):
- S1 doubles IC → gm doubles, but ro_n/ro_p *halve* (VA is fixed)
- S3 changes nothing except Rout: 4.7kΩ → 33.3kΩ (= ro_n ∥ ro_p) — that single change drives the +17dB gain jump

**Layer 3 — Performance metrics** (derived from Layer 2):
- Now shows percentage change between consecutive stages
- S3 unstable PM (−1.7°) is flagged with ⚠ animation
- GBW correctly *drops* S3→S4 (612→4.0 MHz) as an engineering tradeoff

The key insight the three-tier view makes clear: **S2 only affects Layer 1 (tolerance), not Layer 2 or 3 at all except Vos** — and **S3 only changes one number in Layer 2 (Rout)**, yet that single component swap (Rc → PNP mirror) propagates to improve every performance metric in Layer 3.

---

## Human

what kind of optimize you use for parameter optimization

---

## Assistant

**None.** The stages are hardcoded engineering decisions, not the result of any algorithm. Here's the honest breakdown:

**What the code actually does:**
```javascript
const SCFG = [
  {IEE:1e-3, ro_tail:11e3,  active:false, mm:0.05,  Cc:0    }, // S0
  {IEE:2e-3, ro_tail:2e6,   active:false, mm:0.05,  Cc:0    }, // S1
  {IEE:2e-3, ro_tail:2e6,   active:false, mm:0.001, Cc:0    }, // S2
  {IEE:2e-3, ro_tail:2e6,   active:true,  mm:0.001, Cc:0    }, // S3
  {IEE:2e-3, ro_tail:2e6,   active:true,  mm:0.001, Cc:10e-12}, // S4
];
```
These are **manually chosen topology transitions** — a human designer decided what to change at each stage. The equations then compute the consequences correctly, but there is no search over a parameter space.

**What real optimization would look like:**

The design space has these free variables:
- `IEE` ∈ [0.1mA, 5mA]
- `Rc` ∈ [1kΩ, 20kΩ] (or topology: passive vs active)
- `Cc` ∈ [0, 100pF]
- `VA`, `β` (transistor selection)

A real optimizer would define an **objective function** and **search** over those variables. Three natural approaches:

| Method | How it works | Suited for |
|---|---|---|
| **Gradient descent** | ∂cost/∂param, step toward minimum | Continuous params (IEE, Cc) |
| **Simulated annealing** | Random walk, accept worse solutions with probability e^(−ΔE/T) | Mixed continuous + discrete |
| **Genetic algorithm** | Population of designs, crossover + mutation | Topology selection (active vs passive) |
| **A*** | Discrete state-space search, f=g+h | Only valid if design space is a graph |

A* would technically work if you discretize the parameter space — for example, resistor values from the E24 series (1.0k, 1.1k, 1.2k... 91k). Each node in the graph is a complete design, edges are single-component swaps, and the heuristic estimates remaining performance gap. But it is unusual in analog circuit sizing — gradient methods or genetic algorithms are far more common in real EDA tools like Cadence or HSPICE optimization.

**Would you like me to implement an actual optimizer** — for example, a hill-climbing or simulated annealing search over `IEE`, `Rc`, and `Cc` that maximizes a weighted objective like `CMRR + Ad − penalty(PM<45°)`?
