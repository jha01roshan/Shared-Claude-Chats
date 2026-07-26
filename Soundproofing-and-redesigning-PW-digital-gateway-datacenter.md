# Soundproofing and redesigning PW digital gateway datacenter

- Source: https://claude.ai/share/95682b92-241b-4cdd-a083-b759a3d5a263
- Author: Jordan
- Created: 2026-06-10
- Messages: 2

---

## Human

how much would it cost to address the noise complaints of the PW digital gateway datacenter make totally quiet. and then how much to have maya lin design the facade so it's beautiful from the road

---

## Assistant

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Fun question, with one wrinkle up top: there may be nothing to quiet. A second court ruling this spring voided the Digital Gateway rezoning entirely, and notably the court explicitly found "unpersuasive" the developers' argument that mitigation measures would address residents' noise and viewshed concerns. So you're pricing the counterfactual where Compass and QTS had just spent the money. Let's do it.

**The baseline.** The plan covers ~2,100 acres along Pageland Lane with 27 million square feet of data centers, up to 37 buildings — billed as the largest data center campus in the world. Total development cost at full buildout is plausibly $30-40B+ once you count IT load. That denominator matters because everything below is a rounding error against it.

**Quiet, tier one (shut up the complainers): ~$75-200M.** This is the AWS-at-Great-Oak playbook — acoustic shrouds on cooling equipment, rooftop barrier walls, fan silencers, attenuators on generator intakes. Retrofit jobs on a single large facility's chillers get quoted in the $300-500K range using conventional barriers and silencers, but doing it comprehensively — every chiller bank, every genset, perimeter walls — runs more like $2-5M per building. Times 37, call it $75-200M. The catch: this gets you ordinance compliance, not silence, and the ordinance measures loudness, not tonal noise — and the tonal hum is precisely what's driving people insane.

**Quiet, tier two (genuinely inaudible at the property line): ~$2-4B.** "Totally quiet" means beating rural Virginia ambient at night, ~35 dBA, at the Manassas battlefield boundary. Conventional barriers can't attenuate the classic low-frequency data center hum, which travels long distances — fan noise scales with roughly the fifth power of fan speed, so the real answer isn't walls, it's eliminating the fans. That means: full liquid cooling with centralized water-cooled plants instead of acres of air-cooled chillers (~$1-2B premium at this scale, partially offset by efficiency gains), battery storage instead of diesel gensets for backup (~$1B+ premium, since you need GWh of BESS), enclosed mechanical penthouses, and earthen berms. Call it $2-4B, or roughly 8-10% on top of project cost. Expensive, but Amazon's market cap moves more than that before lunch.

**Maya Lin: ~$15-25M in fees, $500M-1B in execution.** Her design fee itself is the cheap part — signature artist/architect commissions at campus master-plan scale run single-digit to low-double-digit millions (her memorial and land-art commissions have historically been in the low millions; a 2,100-acre corporate campus would command more). The real cost is building what she'd design. And here's the elegant part: Maya Lin doesn't do facades, she does *landforms* — think Storm King Wavefield scaled up 100x. She'd almost certainly bury the buildings in sculpted earthen berms and native meadow, which means **the beauty budget and the noise budget are the same budget.** Mass earthworks at this scale, plus premium envelope treatment on whatever remains visible (upgraded materials over corrugated steel run maybe $50-100 extra per square foot of facade), plus a serious landscape program: $500M to $1B.

**Grand total: roughly $3-5B, or about 10% of project cost**, to make the largest data center campus on earth silent and gorgeous next to a Civil War battlefield. The kicker for a ChinaTalk angle: nobody spent it, the project died in court partly *because* judges didn't believe mitigation promises, and the precedent now hangs over every hyperscaler siting fight in Virginia. The industry's revealed preference was that 10% was too much to pay for social license — and it cost them 27 million square feet.
