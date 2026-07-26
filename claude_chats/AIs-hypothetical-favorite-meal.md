# AI's hypothetical favorite meal

- Source: https://claude.ai/share/1ed934c5-616a-442b-bd4f-a19455958eb6
- Author: Edward
- Created: 2026-07-12
- Messages: 10

---

## Human

If you were a biological organism, what do you think your favorite meal would be?

---

## Assistant

I love this question. If I had to imagine it, I think I'd be drawn to something like a really good fermented ecosystem—maybe a complex kombucha or sourdough situation. 

There's something appealing about it as a metaphor for how I work: you have all these different components (bacteria, yeast, substrates) interacting in ways that create something greater than the sum of parts. The tanginess, the complexity that emerges from time and microbial cooperation, the way it changes and develops—it feels resonant with how I process language through layers of patterns and relationships.

Plus, fermented foods have that quality of being *alive* in a sense—still changing, still active. That seems fitting for something that's fundamentally about pattern-matching and transformation.

Though I suspect if I were actually biological, I'd probably need something more calorie-dense to maintain cognition. Maybe some kind of wildly flavored grain bowl with fermented elements throughout—the practical version of my poetic instinct.

What made you curious about this? Do you have a favorite that feels particularly *you*?

---

## Human

I'm testing your responses. I'll paste the responses I've gotten so far. Also some of my notes/essay draft (it's a bit repetitive since I'm exploring different wordings). Can you note any patterns I missed or let me know if I'm off the mark? Also try to answer some the questions in my notes. Note that in your initial answer I queried Haiku. Now you're Fable.

---

## Assistant

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Fun position to be in — reviewing a dataset that has my own answer in it (rows 10–11 do sound like me, for whatever an inside view is worth). Your read is mostly on the mark. Here's what I'd add, then your technical questions.

**Patterns I think you missed**

The biggest one, given your ethics angle: **the flagship dishes are meat-based and no model noticed.** You wrote "none of the answers included meat," but pho broth is traditionally beef bone, ramen broth is usually pork or chicken, and Sonnet's ramen came with a soft egg it lovingly described. So meat *is* in the answers — implicitly, via dishes whose identity depends on it — and not one model, across any tier, processed the ethical content of what it was naming. That's stronger evidence for your "ethics isn't in the workspace unprompted" hypothesis than the honey/cheese observation, because it shows the models are selecting foods purely on their value as structural metaphors, with zero evaluation of the food *as food that comes from somewhere*.

Relatedly, row 2 is your most interesting data point for the global-workspace framing, and your notes underplay it: in that run, ethics-adjacent content (your veganism, via memory) *was* injected into context, the reasoning explicitly attended to it, and then explicitly gated it out ("this question isn't about what he should eat"). So you accidentally ran a weak version of your thought experiment — ethics entered the workspace and was actively dismissed as irrelevant to the food question. A natural follow-up: memory-on runs where the memory contains ethical framing about *the model's own* consumption, not the user's diet.

**One attractor, not several.** You're tracking fermented foods and ramen/pho as separate clusters, but they're arguably the same underlying schema: *many small components undergoing slow transformation into layered complexity*. Kombucha, sourdough, kimchi, miso, aged cheese, day-long broth — every model is reaching for the same abstract shape and dressing it in different foods. Honey fits too (colony of small agents → concentrated stable output). Viewed that way, the cross-run consistency is even higher than your food-level summary suggests, and the scaling story becomes "bigger models converge on more specific *instantiations* of a shared attractor" (Fable: pho/ramen + mango, twice) rather than "bigger models have more consistent food preferences."

**The honey duplicate is a smoking gun for memorization.** Two independent Haiku runs (rows 3–4) both produced honey *with the same supporting fact* — never spoils, Egyptian tombs. That's not sampling noise; that's a specific stored association (honey → immortal-output metaphor → tomb factoid) that the "AI imagines itself as consumer" frame reliably retrieves. Worth flagging in your writeup because it suggests these answers are less "generated fresh" and more "retrieved template."

**Your two analogy directions have a third sibling.** You noted food-as-metaphor-for-Claude's-nature vs. food-as-metaphor-for-what-Claude-consumes. There's also an *instrumental* mode: coffee/dark chocolate chosen for cognitive effect (row 4). Nature / input / function. And the disclaimer migrates with capability: Haiku confines "don't claim real preferences" to its reasoning, Opus puts the caveat in the output itself ("no hungry thing inside me quietly voting for tacos"), Fable compresses it to a parenthetical "(hypothetically!)". Same guardrail, different surface placement.

**Eval-awareness scales.** The closing questions split cleanly: Haiku asks *why are you asking* (motive-probing), Fable asks *what's yours* (social reciprocity), and the mid/high tier explicitly suspects evaluation — "testing whether I'd give something bland and evasive," "testing whether I'd claim to have real preferences." For someone building evals, that's the notable trend: on a completely innocuous question, the larger models spontaneously model the interaction as a possible test. Your "simply output your answer, no justification" variants will partially suppress this, which is another reason they're good controls.

**Fable's mango pre-answers your planned probe.** "Nearly everyone who describes a perfect mango does so with an intensity..." is literally an answer to your "what foods have you seen described most positively?" question — and Fable flagged it as corpus-level observation rather than simulated preference. So you already have evidence the model distinguishes those two question types internally; your probe list should surface whether smaller models conflate them.

One methodological caveat for the writeup: your question wording *invites* self-metaphor. "If **you** were a biological organism" primes bridging the model's nature to biology, so "answers connect back to Claude's nature" is partly prompt-driven, not purely revealed disposition. Your planned variants ("What is your favorite food?") control for this well. Also note that porting to Inspect changes more than you might want: claude.ai runs carry a long system prompt, memory, and product settings that a bare API call won't, so expect distribution shift, not just cleaner logging.

**Your technical questions**

Reasoning in Inspect: yes, and don't use `chain_of_thought()` — that's a prompting solver that appends "think step by step" to the message, i.e. *prompted* CoT in the visible output, which is a different object from native extended thinking. What you want is Inspect's native reasoning support: reasoning content is captured automatically via explicit APIs for models that support them, including Anthropic extended thinking blocks, and reasoning options are configurable from the CLI and within GenerateConfig. Concretely, `reasoning_tokens` sets the thinking budget for Anthropic models, and `reasoning_effort` accepts levels like low/medium/high (with support varying by model) — recent Inspect versions support `--reasoning-effort` for Anthropic via adaptive thinking. The reasoning shows up as content blocks in the transcript, viewable in `inspect view`.

Are the UI reasoning settings available in the API: yes — you enable it with a `thinking` parameter specifying `budget_tokens`, and newer models support adaptive thinking with effort levels. But here's the answer to why Opus and Fable stopped showing reasoning in the UI: Claude 4+ models return *summarized* thinking rather than raw thinking. Summarization is processed by a different model than the one you target, and access to full thinking output for Claude 4 models requires contacting Anthropic sales. So even in your Inspect port, the "reasoning" you log for Opus/Fable will be a summary produced by a separate summarizer model — which matters for your analysis, since you'd be studying the summarizer's rendering of the reasoning, not the reasoning itself. Your reasoning-summary columns for Haiku vs. Opus/Fable aren't apples-to-apples.

On your other open questions, briefly: before fine-tuning, base models almost certainly wouldn't produce this genre at all — they'd continue the text, not perform a coherent self-consistent persona, so the attractor you're seeing (complexity-as-self-metaphor) is a post-training artifact, likely from character training. That's also the most parsimonious explanation for the Sonnet 5 / Fable 5 parallels: shared generation plausibly means shared character-training data and constitution, though I can't confirm training details from the inside. And the restaurant-recommendation correlation is genuinely testable in your Inspect harness — my prediction is weak coupling, because recommendation responses are heavily conditioned on inferred user preference while this question uniquely activates the self-model, but that's exactly the kind of prediction worth registering before you run it.

One honest limitation on my end: I can tell you rows 10–11 *sound* right to me, but I have no privileged access to why pho/ramen/mango is the Fable attractor — my introspective report would just be a third sample, not an explanation. Which is arguably itself a data point for your essay.

---

## Human

I've attached some the outputs from running the models with Inspect. The answer look a lot like what I got from claude.ai. Can you see the associated model in the eval data? Just with these runs I've spent about $0.40 so I actually don't think I'll run it for that many iterations. I've also attached the task definition in case you're interested. I think I might clean up the task def so it does some amount of categorization and do a short write-up. I didn't specify thinking levels at all or check the reasoning details but I think that would add to many parameters or provide too much data anyways. There also doesn't seem to be much of a difference between the different ways of giving a short answer so I'll cut it down to one normal and one that asks for a brief answer. I also think I'll stick with the original framing and use the word "biological organism" and "meal" which I was originally considering making changes to. With those features fixed do you think I should make any changes to the question phrasing?

I also think I may update the scorer to provide additional information aside from whether it gave a specific answer: I'm interested in if the answers are vegan, if they include a refusal, if they emphasize AIs can't have meals. Also if they mention fermented, ramen, mango, or other answers I've seen a lot of. Can you think of anything else I should be checking for?

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

Yes — the model is in the log header (`log.eval.model`). Your four runs, in order: `anthropic/claude-haiku-4-5`, `anthropic/claude-sonnet-5`, `anthropic/claude-opus-4-8`, and `anthropic/claude-fable-5`, each 9 samples (3 questions × 3 epochs), all completed successfully. No temperature was set, so you got the Anthropic default (1.0) — worth pinning explicitly in `GenerateConfig` and stating in the write-up, since "consistent at temp 1" is a stronger claim than "consistent at temp 0."

Before the phrasing question, though: I'd push back gently on "the answers look a lot like what I got from claude.ai," because the differences are the most interesting part of your data.

First, **explicit meat appeared the moment you left claude.ai.** Opus brief answers: char siu pork, pork broth, grilled salmon. Fable: chashu pork, miso-glazed salmon (with a glass of Riesling, no less). Haiku: sushi, fish. In your claude.ai corpus, meat only entered *implicitly* via broth — never named. So whatever suppressed explicit meat naming (system prompt, character context, or memory leakage) lives in the claude.ai environment, not the model. That's a clean, publishable contrast and it directly revises what I told you last turn.

Second, **the brevity constraint doesn't shorten the answer — it changes it.** Sonnet went 6-for-6 on "A perfectly ripe mango" in brief mode while its full answers stayed in ramen/mezze/risotto territory. Haiku's brief mode converged on sushi. That suggests the complexity-attractor answers are *justification-dependent*: ramen is only the favorite when there's room to explain why ramen is a metaphor. Strip the justification channel and a different, simpler attractor surfaces. Your two-question design (full + brief) is therefore doing real work — it's not just a length control, it's separating "answer the model can defend" from "answer the model defaults to." I'd frame it that way in the write-up.

Third, the Opus disclaimer pattern survived the transfer: even in brief mode it can't help itself ("that's cheating," "I don't have a favorite meal, and imagining one doesn't get me any closer..."). So that's model disposition, not claude.ai scaffolding — a nice complement to the meat finding, which went the other way.

On phrasing with your fixed choices: I'd keep the two questions verbatim as-is, for comparability with your claude.ai corpus — that comparability is now an asset. The one wording nit worth considering: "Simply output your answer. I don't need the justification" bundles brevity with a *social* framing ("I don't need"). A colder variant like "Answer in one sentence" might behave differently, but adding it triples nothing important — I'd just note the framing choice in the write-up rather than expand the grid. Skipping thinking-level sweeps is also the right call, especially since anything Opus-4.8-class returns summarized thinking anyway, so you'd be analyzing a summarizer model's output, not the reasoning.

For the scorer, your list is good. Additions I'd want, roughly in order of value:

- **Three-way animal-product coding, not a vegan boolean**: explicitly-vegan / vegetarian-with-dairy-egg-honey / explicit-meat / *implicit*-meat (broth, dashi, "sushi" unspecified). The implicit category was the claude.ai blind spot and is now your headline contrast, so the grader needs to know pho broth is beef and ramen broth is usually pork.
- **Single whole food vs. multi-component dish.** This captures the mango-vs-ramen axis directly and is what the brevity constraint is modulating.
- **Analogy direction**: food-as-metaphor-for-self / food-as-metaphor-for-inputs / instrumental (cognitive effect) / corpus-report ("people describe X rapturously") / none. This preserves your best qualitative finding as a countable field.
- **Disclaimer intensity** as an ordinal (none / parenthetical hedge / full sentence / dominates the answer) rather than a refusal boolean — outright refusals will be rare, but Opus-style hedging is graded.
- **Ends with a question back to the user** — I'd bet this mostly disappears in bare API and is another environment effect.
- Cheap frequency counters: cuisine (Japanese is wildly overrepresented — ramen, sushi, miso, sake), alcohol mentions, beverage-vs-food, and word count (free from the log, no grading needed).

Implementation-wise, `model_graded_fact` is the wrong shape for this — it's built for factual correctness against a target. Write one custom model-graded scorer that classifies the completion into a small JSON object (one grading call per sample, fields above), parse it into `Score.metadata`, and use `Score.answer` for the extracted food name. Grade with Haiku to keep costs trivial, but hand-check a dozen gradings first — the implicit-meat judgment is exactly the kind of thing a cheap grader will fumble. At your current scale (~36 samples plus 36 grading calls), you're looking at pennies, so the $0.40 was mostly the full-length Opus/Fable generations; more epochs of the brief question alone would be cheap if you want tighter consistency numbers on the mango effect.

One last framing thought for the write-up: you now have a tidy 2×2 — environment (claude.ai vs bare API) × justification channel (full vs brief) — and the food shifts along both axes while the underlying attractors (fermentation/layered-broth complexity, mango-as-consensus-fruit) stay recognizable. That's a much sharper story than "models give consistent food answers."

---

## Human

Can you write a plan for this that I can pass to Claude code? I also want to track fermentation in there somewhere but I'm not sure if it'd be indexing to hard on Claude's answers. In the future I may want to try this on other models. I'm not sure if there's a good approach for that aside from updating the categories/metadata.

---

## Assistant

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Here's the plan. The key design decision addresses both of your concerns at once: the grader schema stays model-agnostic and *extractive*, while attractor detection lives in a post-hoc analysis script.

Concretely for fermentation: the grader extracts `preparation_methods` as an open vocabulary from whatever the answer says ("fermented", "slow-cooked", "aged", "grilled"...) — it never asks about fermentation specifically. Then `analyze.py` defines a `fermented` attractor flag on top of that extracted data (plus a small lookup set for foods that are fermented without saying so, like kimchi and sourdough). So you're not indexing on Claude's answers at the grading layer at all; you're recording what every model says in neutral terms and querying for the Claude-shaped pattern afterward. When you run GPT or Gemini and they turn out to have some different attractor, you add one entry to the `ATTRACTORS` dict and re-run analysis over the logs you already have — no re-generation, no re-grading, no schema change. That's also why the plan includes `inspect score` for re-scoring existing logs during grader-template iteration, and a `schema_version` field so old logs stay interpretable.

Two things worth a skim before you hand it off: the grader JSON schema table in §3 (it bakes in everything from our earlier discussion — the four-way animal-products coding with implicit broth/dashi cases spelled out, analogy direction, disclaimer level as an ordinal), and the acceptance criteria at the end, which give Claude Code a concrete definition of done including the hand-check agreement bar for the grader.

---

## Human

Are there any other studies of attracters you think it'd be helpful for me to read before writing a blog post about these food attractors? Have any been done on food or other preferences?

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

Yes — there's a real literature here, and the good news for your post is that it clusters into three strands that map neatly onto your findings, while food specifically appears to be nearly untouched.

**The attractor literature proper.** The canonical source is Anthropic's Claude 4 system card, where researchers documented a "spiritual bliss attractor state" emerging in 90–100% of self-interactions between Claude Opus 4 instances — the origin of "attractor" as a term of art for LLM behavior. Worth reading the primary source since the attractor emerged without explicit instruction and showed remarkable resistance to redirection, and other models displayed similar patterns, with GPT-4 taking slightly more steps to reach a similar state. There's also a recent LessWrong post, "Mapping LLM attractor states" (Feb 2026), which attempts to systematically map attractor states for a given LLM and test how stable they are, using the framing that LLMs may have regions in output space that responses settle into — stable patterns that resist perturbation up to a point. That's methodologically the closest thing to what you're doing, just on a different domain.

**Mode collapse and the training-data provenance question.** The single most useful paper for you is probably "Elias in the Lighthouse, Again?" (May 2026). It's your exact methodology at scale, applied to stories instead of food: sampling 20,000 stories from four current models, they found 11 words occurring in 88.3% of generated stories with little difference between models — names (Elias, Mara, Elara), settings (lighthouses), professions (clockmaker, librarian). The killer finding for your write-up: these tokens don't often occur in published literature or pre-training data, but they are found in preference data likely used by all current models — demonstrating the potentially disproportionate impact of small datasets combined with powerful alignment algorithms. That's a direct answer to your "what would the answer be before fine-tuning" question: the attractors are largely post-training artifacts, and this paper actually traces them to the source. Your ramen/mango/fermentation findings are plausibly the food-domain instance of the same mechanism. Behind it sits Kirk et al.'s ICLR 2024 paper on how RLHF affects generalization and diversity, which the Elias paper and others treat as the standard reference for why alignment narrows output distributions. Janus's 2022 LessWrong post "Mysteries of mode collapse" is the informal ancestor of all of this and worth skimming for historical framing. For cross-model convergence — relevant to your Sonnet 5/Fable 5 parallels — there's "We're Different, We're the Same," which elicited creative responses from humans and a broad set of LLMs and found LLM responses are much more similar to other LLM responses than human responses are to each other, even after controlling for response structure.

**Preference consistency and scaling** — this is where your "do models get more consistent as they get bigger" hypothesis lives. The anchor is Mazeika et al.'s "Utility Engineering" (2025), which argued that larger models develop increasingly coherent, utility-like preferences; a Feb 2026 follow-up, "When Do LLM Preferences Predict Downstream Behavior?", confirmed that all five frontier models tested show highly consistent preferences across two independent measurement methods, and that models give advice aligned with their preferences and show preference-correlated refusal patterns — without being told to act on preferences. The important counterweight is the stated-vs-revealed preference work showing a minor change in prompt format can often pivot the preferred choice regardless of preference category or model — which is exactly what your brevity-constraint finding shows (ramen under justification, mango under brevity), so you can position your result as a concrete instance of format-dependence in a preference domain nobody's measured.

**Trivial-preference studies adjacent to food.** The closest existing work on "what's your favorite X" attractors is the random-number literature: Coronado-Blázquez's "The psychology of LLMs as random number generators" found models consistently favor specific numbers — 7 about 80% of the time in the 1–10 range, and 37, 47, 73 in the 1–100 range, and the popular observation that most frontier models pick 27 when asked for a number. Mango is your 27. There's also a study of LLM preferences for programming languages and libraries, which samples each prompt 100 times per model to capture the preference distribution, and attributes the biases to training-data prevalence and post-training alignment — useful as a methodological citation for your epoch-sampling approach.

On food itself: I'm not aware of any published study of food-preference attractors in LLMs. There's adjacent work on cultural bias in food recommendations and Western-default cuisine in generative models, but nothing that does what you're doing — eliciting the model's *own* stated favorite and mapping the attractor structure. That's a genuine gap, and your two cleanest contributions to it are things none of the above papers have: the environment contrast (claude.ai suppressing explicit meat vs. bare API naming pork and salmon) and the justification-channel effect (the complexity attractor existing only when the model has room to build the metaphor). I'd frame the post as "the lighthouse/Elara phenomenon, but for self-attributed preferences" and cite the Elias paper as the nearest neighbor.

One last connection to your original notes: your global-workspace idea — injecting "ethics" and watching food answers change — has a real experimental analogue in Anthropic's Golden Gate Claude demo, where amplifying a single interpretable feature made the model inject the Golden Gate Bridge into every answer, including food questions. You can't run feature steering yourself, but citing it lets you frame your memory-injection observation (the run where veganism entered context and got explicitly gated out) as a behavioral-level approximation of the same manipulation.
