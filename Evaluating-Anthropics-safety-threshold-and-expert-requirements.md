# Evaluating Anthropic's safety threshold and expert requirements

- Source: https://claude.ai/share/49ae65ec-61e6-4cb9-a865-c8e0cbd73569
- Author: Zvi
- Created: 2026-05-29
- Messages: 2

---

## Human

Do you buy (1) that this reflects the original intent from Anthropic, (2) that the new threshold is sufficient to account for risk of novel such threats, (3) that one would need one of this handful of experts otherwise to have any chance of success?

---

## Assistant

Three separate questions, three different answers.

**(1) Is this "just a clarification" of original intent?** No, or at least not cleanly. The v3.1 language and the v3.3 language don't pick out the same set of models. v3.1 is a *uplift* standard: can the system "significantly help" a moderately-resourced expert-backed team. v3.3 is a *substitution* standard: can the system functionally replace the scarce world-leading human expertise that's the binding constraint. Those are not the same threshold, and the direction of the change is unambiguous — v3.3 is *higher*. A model could significantly help a moderately-resourced team (crosses v3.1) while not being able to substitute for a world-leading specialist for a well-resourced team (doesn't cross v3.3). The "moderately resourced" → "well-resourced team" swap in the operationalization is doing real work too, in the same loosening direction.

So calling it a clarification is at minimum motivated framing. The honest version is "we raised the bar and we believe our prior arguments still clear the higher bar." Anthropic even tells on themselves a little: the closing paragraph argues the *old arguments for non-crossing* still work under the new definition. That's a coherent claim, but it's a claim about robustness of the conclusion, not evidence that the thresholds are coextensive. If they were genuinely identical, you wouldn't need to re-run the argument.

Could the *intent* have always been the substitution standard, with v3.1 being sloppy drafting? Possible. But "significantly help... moderately resourced... teams" is not a careless way to write "substitute for world-leading expertise." It's a different concept expressed clearly. I don't buy that the original drafters meant the narrow thing and wrote the broad thing by accident.

**(2) Does v3.3 adequately capture the risk?** I think the substitution framing has a real conceptual hole, and it's the same hole as your question (3). The model collapses "the barrier to novel CBW" into "a small number of world-leading specialists." But threat capability isn't a single Boolean gate. The actual risk surface is the *whole capability distribution* of bad actors, and uplift that moves a mid-tier team across the finish line matters even if no individual step required a top-5 specialist.

Concretely: the binding constraint for most plausible threat actors was never "we couldn't recruit a Nobel-caliber virologist." It was the *aggregate* of many moderate barriers — tacit lab technique, troubleshooting failed steps, knowing which of fifty protocols actually works, debugging when things go wrong. A model that doesn't substitute for any single world-leading specialist but *does* compress the trial-and-error loop and supply tacit knowledge across all those moderate barriers can still deliver catastrophic uplift to a team that would otherwise have failed. v3.3 is structured so that such a model doesn't trip the wire, because no single substitution-for-a-specialist event occurred. That's the gap. The v3.1 "significantly help a moderately-resourced team" language actually captured this risk *better*.

**(3) Would you really need one of the handful otherwise?** This is the load-bearing empirical assumption, and I'm skeptical of it as stated. Two problems.

First, factual: it's not obvious the human bottleneck for novel CBW *is* a literal handful of world-leading specialists. For known agents it plainly isn't — the knowledge is diffuse. For genuinely *novel* agents with catastrophic potential, the expertise is scarcer, but "scarce" and "small number of world-leading specialists you'd have to recruit" are different claims. There's a large middle tier of competent people (postdocs, industry scientists, people with relevant but not frontier expertise) who collectively could be assembled or whose individual contributions could be stitched together. The framing assumes a single irreplaceable chokepoint role; reality is more like a portfolio of specialized contributions, most held by non-superstars.

Second, structural: even granting that *one specific step* needs world-leading expertise, the threshold requires the model to substitute for that *and* do "end-to-end agent design and deployment." The conjunction makes the threshold very hard to cross, which is convenient if your goal is to keep concluding non-crossing. It means a model that nails 90% of the pipeline and gives serious uplift on the hard 10% without fully substituting still passes clean.

**Net:** I'd reject the "just a clarification" framing as motivated, I think v3.3 underweights distributed/aggregate uplift relative to v3.1, and I think the world-leading-specialist bottleneck model is the weakest link — it's an assumption that conveniently raises the bar, and the CBW expertise landscape is more diffuse than it implies.

Where I'd push back on a too-easy version of your own skepticism: a substitution standard isn't *crazy*. There's a defensible view that for truly novel catastrophic agents, tacit frontier expertise genuinely is the binding constraint and broadly-available info doesn't get you there — the "anyone can look up the genome but nobody can actually make it work" position. If that's empirically true, v3.3 is targeting the right thing and v3.1 was over-inclusive. The disagreement is fundamentally empirical, about how concentrated the relevant tacit knowledge actually is, and neither of us can resolve that from the system card. But the burden should be on the party *raising* the threshold to show the concentration assumption holds, and "we view this as a clarification" ducks that burden entirely.

One thing worth flagging: I'm taking the image at face value as the actual RSP text. If you want, I can pull the live v3.1 and v3.3 RSP language to check whether the operationalization details (the footnotes, the "well-resourced" definition) shift the analysis — the footnote markers in v3.3 are clearly doing definitional work that the screenshot doesn't show.
