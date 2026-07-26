# Recreating Bloom's 2-sigma problem with elite tutoring

- Source: https://claude.ai/share/58a8e074-18d5-4320-aae6-4a57914f6ef4
- Author: David
- Created: 2026-07-07
- Messages: 2

---

## Human

"I'm excited to announce the most ambitious recreation of Bloom's 2Sigma study of the last 40 years. It's funded by @reedhastings  and staffed by a team of 20 of the best educators in this country. Our education team's goal is to show the largest academic gains in one year ever recorded, and we'll publish our results even if we fail. Recently, @jwdanner  introduced me to @reedhastings . Most people know Reed co-founded Netflix. Fewer know he has been one of the driving forces behind improving education for the last twenty years. When Reed pitched me on recreating Bloom's famous 2-sigma problem, I felt an overwhelming sense of hope for education. Over the last few months we have moved at breakneck speed to assemble an exceptional team. Someone recently described it to me as the "Avengers of education." We are testing one question with the rigor it deserves: can elite one-on-one tutoring reproduce the largest learning gains ever measured in a controlled study? We will work with researchers from Stanford, Brown, Cornell, and other leading institutions, and we intend to be the most transparent research group in the field. That means publishing our methods, our benchmarks, and our results, whatever they show. We will invest up to $100,000 per year per student to give them the best education on the planet. If it works, the data and methods can help educators and technologists recreate these outcomes for every child. We are actively hiring tutors, engineers, and operations people to help us climb this mountain."
What do you anticipate is the #1 potential validity issue with this study, such that the results can't be compared on a level scale with other educational interventions?

---

## Assistant

```
This block is not supported on your current device yet.
```

This is Modern Bloom (the Hastings-funded study announced late 2025), and their site does address some obvious objections upfront: they claim pre-registered methods, strong controls, open data, and a control group receiving typical classroom instruction. So the crudest failure modes (no counterfactual at all, hidden methods) are at least nominally handled. The question is what survives those commitments. Since "the #1 issue" is a judgment call, three samples:

**Sample 1 (p ≈ 0.35): Outcome-measure alignment.** The same organization designs the curriculum, employs the tutors, and — per their own announcement — will publish their own benchmarks and evaluations. If the outcome measure is developed or selected by the intervention team, tutors can (and rationally will, given the stated goal of "largest gains ever recorded") teach directly toward it for a full year. Other interventions in the comparison set are mostly evaluated on distal standardized tests. This is the largest known moderator of effect sizes in education research — Cheung & Slavin and the What Works Clearinghouse literature find researcher-made/curriculum-aligned measures yield roughly 2–4x the effects of independent standardized measures. Notably, Bloom's original 2σ came from exactly this: experimenter-designed mastery tests aligned to the taught unit, over weeks not years.

**Sample 2 (p ≈ 0.30): The standard-deviation denominator.** "Sigma" is not a fixed unit. A small, self-selected sample (families opting into an intensive, high-visibility program) will have a range-restricted, non-representative SD; effect sizes computed against the sample's pooled SD, or against a control group of a few dozen kids, are not on the same scale as effect sizes from population-normed assessments across 600k students. The No More Marking critique of Bloom makes essentially this point — 2σ against a small local sample is a much smaller real-world claim than 2σ against national norms, and which denominator gets used can swing the headline number by a factor of two or more without any misconduct.

**Sample 3 (p ≈ 0.15): The bundle/dosage confound.** $100k/year doesn't buy "one-on-one tutoring," it buys a total-environment intervention — more instructional hours, elite tutor selection from a national applicant pool, team coordination, tutor-swapping, family engagement, plausibly motivation and expectancy effects from being publicly part of an "Avengers of education" moonshot. Whatever effect emerges can't be attributed to the tutoring modality, which is the thing the study is nominally about and the thing other interventions would be compared against.

My actual pick is Sample 1, with Sample 2 as the compounding multiplier. Here's the discriminating logic: the bundle confound (Sample 3) limits *causal attribution* but doesn't stop you comparing the measured effect to other studies — it's honestly a feature of the design, since they're deliberately trying to find the ceiling of a maximal intervention. Selection and Hawthorne effects are partially addressed by randomization within the enrolled sample. What randomization *cannot* fix is the outcome measure itself. If the benchmark is aligned to what the tutors teach — and with the evaluator, curriculum designer, and instructor all inside one org whose declared objective is to produce a record number, alignment is the default outcome even in good faith — then a reported "3σ" is measured in units that are simply not commensurable with the ~0.3–0.4 SD tutoring effects from meta-analyses (e.g., Nickow et al.), which are mostly on independent standardized tests. And Sample 2 then compounds it: even a perfectly independent test yields inflated sigmas if the denominator is a small selected sample's SD rather than the population's.

The testable prediction: watch whether they pre-register a fully independent, nationally-normed assessment (MAP, state tests, or similar) administered by a third party, report effects in national-norm SD units, and firewall the tutors from item-level knowledge of it. If they do all three, the headline number will be dramatically smaller than 2σ — my prior would be something like 0.4–0.9 SD for a genuinely maximal one-year intervention — and if they don't, the number they publish won't mean what "2 sigma" meant in the studies it's being compared to. Given they're publicly committed to publishing methods regardless of outcome, this is checkable at pre-registration time, before any results exist.
