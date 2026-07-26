# Model weight interventions for Fable 5 classifiers

- Source: https://claude.ai/share/78d57944-e7d3-4b2c-ba9f-8febd163fbb3
- Author: Nathan
- Created: 2026-06-09
- Messages: 2

---

## Human

Do the model weight / peft style interventions apple to Fable 5 if the classifiers fail?

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


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Short answer: no — they're a separate, narrowly scoped safeguard, not a backstop for the cyber/bio classifiers, and they're detection-gated themselves.

The system card draws the distinction in Section 1.5. The cybersecurity, bio/chem, and distillation safeguards are fallback classifiers — in client apps, triggered requests automatically fall back to Claude Opus 4.8 with the user notified; in the Messages API the request is blocked by default with a structured refusal category, with optional server-side fallback. The PEFT-style stuff is a different track entirely: interventions that limit Claude's effectiveness for requests targeting frontier LLM development (pretraining pipelines, distributed training infrastructure, ML accelerator design), implemented through prompt modification, steering vectors, or parameter-efficient fine-tuning, which unlike the cyber/bio/distillation interventions are not visible to the user and don't trigger fallback.

So two implications for your question:

1. **If the cyber/bio classifiers miss, there's no weight-level net underneath.** Fable 5 has the same underlying model weights as Mythos 5, and the executive summary is explicit that Fable 5's scores are broadly comparable to Mythos 5 in areas where its safety classifiers do not trigger, and similar to Opus 4.8 where they do. A classifier miss means you're talking to full Mythos-grade capability on that turn.

2. **The PEFT/steering interventions are themselves conditional on detection.** The card says "when these interventions are active" and that Anthropic will continue improving the precision of its detection methods post-launch — implying they're applied selectively when a request is flagged as frontier-LLM-dev (estimated ~0.03% of traffic), not baked permanently into the served weights. If that detection fails, presumably the intervention doesn't fire either.

So the architecture is detection-dependent at every layer — the difference between the tracks is what happens *after* detection (fallback/block vs. silent capability degradation), not which one is more robust to classifier failure. Worth noting the card doesn't explicitly state what the failure mode of the frontier-dev detection looks like, so point 2 is inference from the "when active" framing rather than a stated guarantee.
