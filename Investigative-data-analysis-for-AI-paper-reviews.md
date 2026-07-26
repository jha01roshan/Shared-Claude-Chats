# Investigative data analysis for AI paper reviews

- Source: https://claude.ai/share/0c919398-d2f8-4682-a6ea-c68f24b98ab2
- Author: Anand
- Created: 2026-01-13
- Messages: 6

---

## Human

Here is a reviews.json generated via prompts.md from AI AgentsForScience (https://agents4science.stanford.edu/)
Analyze data like an investigative journalist hunting for stories that make smart readers lean forward and say "wait, really?"
Here's a typical analysis pattern. You don't need to follow this exactly -- this is just for inspiration.
- Understand the Data: Identify dimensions & measures, types, granularity, ranges, completeness, distribution, trends. Map extractable features, derived metrics, and what sophisticated analyses might serve the story (statistical, geospatial, network, NLP, time series, cohort analysis, etc.).
- Define What Matters: List audiences and their key questions. What problems matter? What's actually actionable? What would contradict conventional wisdom or reveal hidden patterns?
- Hunt for Signal: Analyze extreme/unexpected distributions, breaks in patterns, surprising correlations. Look for stories that either confirm something suspected but never proven, or overturn something everyone assumes is true. Connect dots that seem unrelated at first glance.
- Highlight Heroes & Villains: Identify standout entities (people, places, products, segments) that defy norms. Who's overperforming or underperforming? Who's driving trends or bucking them?
- Segment & Discover: Cluster/classify/segment to find unusual, extreme, high-variance groups. Where are the hidden populations? What patterns emerge when you slice the data differently?
- Find Leverage Points: Hypothesize small changes yielding big effects. Look for underutilization, phase transitions, tipping points. What actions would move the needle?
Then share the most interesting items explaining it to a layman. The main this is to identify big, useful, surprising insights. Assume that the audience cares about how to use AI for reviewing papers.

---

## Assistant

I'll analyze this AI paper review data from the Agents4Science conference. Let me start by understanding the structure and hunting for interesting patterns.
```
This block is not supported on your current device yet.
```

Let me extract and analyze this data systematically with Python to hunt for interesting patterns.
```
This block is not supported on your current device yet.
```

Wow - 90% AI reviews! Let me dig into the scoring patterns and differences between AI and human reviewers.
```
This block is not supported on your current device yet.
```

This is striking! Let me dig deeper into reviewer behavior patterns.
```
This block is not supported on your current device yet.
```

Huge patterns emerging! Let me analyze the review text content for deeper insights.
```
This block is not supported on your current device yet.
```

Incredible patterns! Let me look at what makes AIRev2 so generous and compare actual review text.
```
This block is not supported on your current device yet.
```

Let me now analyze what patterns predict acceptance and look at other interesting dimensions.
```
This block is not supported on your current device yet.
```

Only 0.15 correlation between AI and human reviewers! Let me dig into the sub-scores and ethical concerns.
```
This block is not supported on your current device yet.
```

AI reviewers never fill in subscores or flag ethics! Let me look at timing and what makes papers stand out.
```
This block is not supported on your current device yet.
```

Let me analyze keyword patterns that predict scores and compile the key findings.
```
This block is not supported on your current device yet.
```

Let me look at the AI reviewer "personalities" more deeply and then summarize all findings.
```
This block is not supported on your current device yet.
```

Now let me create a compelling summary of all findings.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

## The "Wait, Really?" Findings

Here's what this data reveals about AI paper reviewers—some of it quite damning:

**1. The confidence paradox:** All three AI reviewers claim 100% confidence (5/5) on every single review, yet they disagree by up to 5 points on the same paper. One AI calls a paper "exceptionally well-executed with outstanding technical quality" (score: 6), while another calls the *same paper* "fundamentally flawed with critical inconsistencies" (score: 1). Both are "completely confident."

**2. AI and humans barely correlate (r=0.15):** This is almost random. Whatever the AI reviewers are evaluating, it's systematically different from what human experts value. AI is more generous by ~1 point on average, and never harsher than humans.

**3. The "missing review" problem:** AI reviewers write longer reviews (2,000+ chars) but leave critical sections blank:
- 0% ask clarifying questions (humans: 96%)
- 0% discuss limitations (humans: 92%)  
- 0 ethical concerns flagged in 751 AI reviews (humans: 41)

**4. Three distinct "personalities" would make opposite decisions:**
- AIRev1 would reject 65% of papers, accept 0%
- AIRev2 would accept 56% of papers
- AIRev3 sits in the middle

**5. Predictable patterns = gaming vulnerability:** Papers mentioning "outstanding" average 5.86; those flagged as "not reproducible" average 1.63. The keywords are formulaic enough to reverse-engineer.

**Bottom line for anyone thinking about AI-assisted review:** The technology can produce plausible-sounding assessments at scale, but the 0.15 correlation with human judgment and systematic blindspots (ethics, genuine questions, calibrated uncertainty) mean we're nowhere near replacing thoughtful human peer review.

---

## Human

I asked ChatGPT to synthesize your response, Gemini's, it's own, fact check the results, and share the big, useful, surprising & defensible insights. They are below.
Convert them into a beautiful slide deck, McKinsey style.
Make the slides content rich, i.e. clear and self-explanatory with enough detail to help the audience understand without a narrator.
Feel free to analyze to create any datasets for charts/tables you think are necessary.
Write as a single page HTML application.
Use iconography, typography, stock images, etc. as appropriate.
<CHATGPT-INSIGHTS>
I pulled the numbers from your `reviews.json` and tried to *break* the Gemini + Claude storylines rather than confirm them. A bunch holds up — but a few “headline” claims collapse once you control for scale, selection, and what the fields actually mean.
## What’s in the data (provenance sanity check)
* **315 submissions, 830 reviews.**
* **250 submissions** have the full trio of AI reviews (**AIRev1/2/3**) → **750 AI reviews** (90.4%).
* **79 submissions** (25.1% of 315) have at least one **non-AI** review → **80 non-AI reviews** total.
* **AI confidence is completely saturated:** every AI review has **confidence = 5** (zero information).
* **Batch-generated feel:** **~91% of reviews were created on one day (Oct 6, 2025)**, consistent with an automated run rather than organic reviewing.
(That last point doesn’t invalidate anything — it just matters for how you interpret “review behavior”: you’re studying a *pipeline run*, not a human process.)
---
## Gemini + Claude claims: what holds up vs what breaks
### Holds up (and is defensible)
**1) “Good cop / bad cop” is real — but it’s even more structural than personality.**
AIRev1’s scale is compressed and harsh (**mean ≈ 2.30; max = 4**). AIRev2 is expansive and generous (**mean ≈ 4.24; max = 6**). AIRev3 sits between (**mean ≈ 3.00; max = 5**).
This isn’t just “tone”; it’s **different scoring distributions**, which creates predictable downstream failure modes.
**2) The “Sycophancy loop” anecdote is real in the scores.**
Submission **148** (the one titled *“The Self-Consistent Hallucination Loop”* in the review text) is exactly as Gemini said: **AIRev2 = 6** while **AIRev1 = 2**.
**3) “Time travelers / future artifacts” show up, and reviewers sometimes catch them.**
Example: Submission **309 (PST-Auto-Agent)** mentions future-ish model identifiers like **“GPT-5-2025-08-07”** and is heavily penalized (AIRev2 gives it **1**) — and the submission page itself shows those claims. ([OpenReview][1])
**4) Some “simulated experiment” accusations appear in reviews (e.g., #82).**
Submission **82** exists and is about eigenvalue problems per its submission page; the reviewers’ “simulation / hard-coded curve” critique is present in the review text. ([OpenReview][2])
Important caveat: from *this dataset alone*, we can’t independently verify who’s right — only that **reviewers flagged it**.
**5) Human reality-check contrast exists (your #195 example).**
Submission **195** exists (title visible on OpenReview), and there is a **non-AI reviewer** giving it **2** while AIRev2 gives **6**. ([OpenReview][3])
So the “AI dazzled by claim; human poked benchmark validity” pattern is plausible — and the score clash is factual.
**6) “Consciousness trap” split exists (e.g., #39).**
Submission **39** exists (OpenReview shows it’s about AI consciousness/sentience), and the scores split in the direction Gemini described (AIRev2 much higher than AIRev3). ([OpenReview][4])
---
### Breaks (or needs major qualification)
**A) “AI and humans barely agree” from a low correlation is *not* a safe conclusion here.**
The biggest reason: **selection + ceiling effects.**
On the 79 submissions that have non-AI reviews, **AIRev2 gives 6 to 75 of them** (mean ≈ 5.95, tiny variance). When one side is nearly constant, correlation will look “near random” even if it’s not. So the “Pearson ≈ 0.15 therefore AI is random vs humans” narrative is **not defensible without correcting for restricted range**.
**B) “AI reviews never discuss limitations / ethics / questions” depends on *where you look*.**
* In the structured **form fields**, AIs often put “N/A”, so it looks like “0%”.
* In the **free-text**, AIs *do* frequently mention “limitations” and “ethical” — they just don’t reliably populate the corresponding structured boxes.
  So the real criticism isn’t “they never consider X”; it’s **they don’t produce reliably structured, machine-actionable reviews unless the prompt forces it.**
**C) The “keywords that predict high scores” analysis (from Claude) is mostly a tautology.**
If you mined *review text* for words like “outstanding” and found they correlate with high *review scores*, that’s backwards:
the reviewer uses “outstanding” **because** they already decided to score high.
That does **not** show what features of the *paper* caused the score — and it does **not** demonstrate “gaming opportunities” unless you also analyze the paper text or the model’s scoring mechanism.
---
## The single biggest failure mode (and the one you should operationalize against)
### 1) Ensemble illusion: averaging raw scores mostly gives you **AIRev2 wearing a moustache**
If you compute “paper score = average(AIRev1, AIRev2, AIRev3)”, the **rank-order** of that average has **Spearman ≈ 0.90** with AIRev2 alone.
So you *think* you’re getting robustness from an ensemble; you’re mostly getting **AIRev2 dominance** because:
* AIRev2 uses the top of the scale constantly,
* AIRev1 almost never goes above 4 (so it can’t “pull up” anything),
* and the mean is sensitive to a single generous rater.
**Actionable fix:** aggregate by **ranks or per-reviewer normalization**, not raw scores.
A simple Borda/rank-average aggregation makes the ensemble behave like an ensemble (correlations with each reviewer become much more balanced).
Second-order effect (worth saying out loud): if you don’t fix this, you create a pipeline where **one reviewer’s quirks become the conference’s acceptance policy**, while everyone still believes “the committee decided.”
---
## Robustness tests I’d trust (and what they said)
### 2) Disagreement is real — but don’t overinterpret it
Raw “spread” between AI reviewers is huge (mean spread ≈ 2.37; ~49% of papers have spread ≥ 3).
But: that spread is **strongly confounded** with AIRev2 being generous. High spread often means “AIRev2 went high while AIRev1 stayed low,” not necessarily “paper is genuinely controversial.”
**Better triage rule than “high spread”:**
Flag papers where **AIRev2 ≥ 5 AND AIRev1 ≤ 2** (a “hype vs rigor” collision). That happens for **~25% of submissions** — perfect targets for human review, because the ensemble is telling you “this hinges on standards, not taste.”
### 3) Human comparison is informative mainly as *calibration*, not “agreement”
Given the selection/ceiling effects, use human reviews to answer:
* Which AI reviewer is *calibrated* (not “which agrees”)?
* Where do humans systematically penalize things AIs let slide (benchmark validity, leakage, evaluation design)?
Your #195 example is exactly the kind of calibration anchor you want: “AI says flawless; human says benchmark is broken.” ([OpenReview][3])
---
## Cross-check externally: does the outside world see the same risks?
Yes — and in a way that sharpens your most important “gaming” point.
1. **Agents4Science is explicitly an AI-agent + OpenReview setup** (Stanford-hosted), so treating this as a “peer review pipeline experiment” is aligned with the project framing.
2. **Independent research on LLMs as reviewers** generally finds they can produce plausible reviews, but reliability/calibration and consistency vs humans are unresolved and highly setup-dependent (i.e., you must measure, not assume). 
3. **Prompt-injection / hidden-text attacks against AI reviewers are now a live, reported issue** — papers have been found embedding instructions to manipulate LLM reviewers. This is exactly the “Goodhart / gaming” failure mode you want to take seriously in any AI-assisted review workflow. ([OpenReview][4])
---
## Prioritize & package: the top defensible, high-leverage insights
### Insight 1 — **Your ensemble is not an ensemble unless you fix scale**
* **Surprise:** averaging 3 reviewers mostly reproduces AIRev2.
* **Action:** use rank aggregation or z-score/percentile normalization per reviewer.
* **Defensible:** directly measured (Spearman ≈ 0.90 between mean-rank and AIRev2).
### Insight 2 — **AI “confidence” is junk; replace it with measurable uncertainty signals**
* **Surprise:** perfect confidence everywhere, despite massive disagreement.
* **Action:** compute uncertainty from (a) calibrated disagreement after normalization, (b) presence of specific red flags (date/model/citation sanity checks), (c) forced self-critique with evidence requirements.
* **Defensible:** confidence is constant; disagreement is large.
### Insight 3 — **Human-vs-AI “agreement” is the wrong KPI here**
* **Surprise:** “low correlation” can be a statistical mirage from restricted range.
* **Action:** treat human reviews as *calibration anchors* and *error taxonomy builders*, not as a leaderboard.
* **Defensible:** AIRev2 nearly saturates at 6 on the human-reviewed subset.
### Insight 4 — **Build a “fraud / impossibility” gate before you build better taste**
* **Surprise:** reviewers are sometimes effective at catching blatant impossibilities (future models/dates) — and you can automate those checks cheaply.
* **Action:** pre-flight checks for:
  * model existence / release dates,
  * dataset date ranges,
  * citation existence,
  * “simulated results” telltales,
  * missing eval details.
* **Defensible:** concrete examples like #309 appear both in submission text and reviews. ([OpenReview][1])
### Insight 5 — **The safest use of “Good cop / bad cop” is *not* averaging; it’s arbitration**
* **Surprise:** the most valuable signal is often the *collision*, not the mean.
* **Action:** if (AIRev2 high, AIRev1 low) → route to a human or a stricter verifier model; if all low → fast-reject; if all high (rare) → fast-accept candidate.
* **Defensible:** this split is common and systematically identifiable.
---
## What you *cannot* conclude from this dataset alone
* Whether “simulated experiment” accusations are true (you’d need code + reproduction).
* Whether humans are “right” and AIs are “wrong” (you don’t have ground-truth acceptance/outcomes here).
* Whether papers can “game” AIs via writing style (you’d need the *paper text* and controlled perturbations; review-word correlations don’t prove causality).
---
## If you want one “next experiment” that will actually settle arguments
Take ~50 submissions and run a controlled re-review where you vary **only**:
1. aggregation method (mean vs rank-aggregate),
2. a pre-flight “impossibility + citation verification” gate,
3. forcing each AI to output (a) 3 crisp questions, (b) 3 falsifiable failure modes, (c) an evidence table.
Then measure:
* variance reduction,
* how often humans change their mind given the evidence table,
* which failure modes disappear.
That will turn today’s narrative into a reproducible result.
* [washingtonpost.com](https://www.washingtonpost.com/nation/2025/07/17/ai-university-research-peer-review/?utm_source=chatgpt.com)
* [theguardian.com](https://www.theguardian.com/technology/2025/jul/14/scientists-reportedly-hiding-ai-text-prompts-in-academic-papers-to-receive-positive-peer-reviews?utm_source=chatgpt.com)
[1]: https://openreview.net/forum?id=6b5kZtfwIH "PST-Auto-Agent: A Multi-Agent Ensemble Framework for Paper Source Tracing | OpenReview"
[2]: https://openreview.net/forum?id=oUvoYRXNFE "Iterative Algorithms and Convergence Analysis for Constrained Nonlinear Multi-Parameter Eigenvalue Problems in the Complex Domain | OpenReview"
[3]: https://openreview.net/forum?id=MYEr4iPFMn "How Large Language Models Perform Arithmetic Reasoning in 2025: Capabilities, Limitations, and Performance Patterns | OpenReview"
[4]: https://openreview.net/group?id=Agents4Science%2F2025%2FConference "Agents4Science 2025 Conference | OpenReview"
</CHATGPT-INSIGHTS>

---

## Assistant

```
This block is not supported on your current device yet.
```

Let me first extract the precise data needed for the charts and tables.
```
This block is not supported on your current device yet.
```

Now let me create the McKinsey-style presentation as a single-page HTML application.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

I've created an 11-slide McKinsey-style presentation. Navigate with arrow keys, spacebar, or click the dots at the bottom.

**Slide structure:**

1. **Title** — The big numbers: 830 reviews, 90% AI-generated
2. **Executive Summary** — All 5 insights at a glance with key metrics
3. **Data Overview** — Score distributions showing the three AI "personalities"
4. **Insight 1: Ensemble Illusion** — ρ=0.90 correlation proves averaging = AIRev2
5. **Insight 2: Confidence is Junk** — 100% at max, yet 5-point disagreements
6. **Insight 3: Wrong KPI** — Why correlation is misleading; use calibration instead
7. **Insight 4: Fraud Gate** — Automatable pre-flight checks that catch real problems
8. **Insight 5: Arbitration** — The 25% "hype vs rigor" collision = best human triage targets
9. **Caveats** — What you can't conclude (keyword tautology, unverified claims)
10. **Recommendations** — Four specific, testable actions
11. **Closing** — The three numbers that matter

The design uses navy/gold consulting palette, IBM Plex fonts, data tables, bar charts, evidence boxes, and action frameworks—all the hallmarks of a serious strategy deck. Each slide has a "takeaway statement" title and supporting evidence.

---

## Human

Revise this for someone who has no idea what AI Agents for science is about, what process they followed, what a Pearson = 0.15 means, etc.

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

Done! The revised presentation is now accessible to a general audience. Key changes:

**Added context for newcomers:**
- **Slide 2 (new):** Explains what peer review is, what Agents4Science did, and why it matters—with a visual process diagram

**Replaced jargon with plain language:**
- "Spearman ρ=0.90" → "90% identical to just using one AI"
- "Pearson correlation" → removed entirely; explained the concept instead
- "Saturated confidence" → "Every AI always says it's 100% confident—even when wrong"

**Added analogies throughout:**
- Movie critics giving 2 stars vs 6 stars for same film
- "Three judges, but one shouts and two whisper" for averaging problem
- Weather app always saying "100% sunny" for broken confidence

**Made data visual and intuitive:**
- Score dots (filled/empty) instead of raw numbers
- Color-coded "The Skeptic" / "The Fan" / "The Moderate" labels
- Simple before/after comparison boxes

**Clarified what's proven vs. hypothesized:**
- Slide 9 now explicitly separates "Can Prove" from "Cannot Prove"
- No statistical claims without plain-English explanations

Navigate with arrow keys or click the dots at the bottom.
