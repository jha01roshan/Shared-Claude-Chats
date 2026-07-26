# Impossibility of aligned ASI systems

- Source: https://claude.ai/share/ace70c68-5055-4fbe-8c0c-feea51472792
- Author: Michael
- Created: 2026-03-08
- Messages: 2

---

## Human

In the spirit of [Arrhenius (2000)](https://doi.org/10.1017/s0266267100000249) or [Askell (2018)](https://askell.io/files/Askell-PhD-Thesis.pdf), can you find a proof that it is impossible to build an "aligned ASI", where "aligned" is defined using some set of principles that are individually reasonable, but mutually contradictory—like how Arrhenius and Askell showed that there is no moral/axiological system that satisfies a set of intuitive axioms? Try to choose principles that are as weak as possible while still producing a contradiction. For example you might take principles along the lines of

1. existential safety: the ASI doesn't kill everyone (maybe also a requirement that it doesn't make things significantly worse, because e.g. an ASI that kills half the population would also be quite bad. but not sure how to formalize that)
2. helpfulness: the ASI satisfies people's preferences better than they would've been satisfied otherwise

I'm not sure if those principles produce a contradiction (also they're underspecified) but I'm just gesturing at the general concept: is there some common-sense version of "alignment" that's provably impossible?

---

## Assistant

This is a fantastic question — you're essentially asking whether we can prove an "Arrow's theorem for alignment." Let me search for existing work in this space, then try to construct something.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

This is a rich question. There's already significant work in this space — most notably Eckersley (2019), who showed how population ethics impossibility results like Arrhenius's apply to AI value alignment, and Brcic & Yampolskiy (2023), who surveyed impossibility theorems across AI broadly. There's also the Soares et al. (2015) impossibility result showing that corrigible agents must violate either a "sane pure bets" condition or a "weak indifference" condition, and recent work proving that no single unrestricted scalar reward function can satisfy all corrigibility desiderata.

But most existing results either (a) import standard social choice impossibilities (Arrow, Sen) into the AI setting without adding alignment-specific structure, or (b) focus narrowly on one aspect like corrigibility. You're asking for something more like Arrhenius: a set of *individually compelling, alignment-specific* principles that are jointly unsatisfiable. Let me try to construct one.

I'll write this up as a proper document since it's going to involve careful definitions and proofs.
```
This block is not supported on your current device yet.
```

I'll create this as a proper document with formal definitions and proofs.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Here's the core result: **five individually weak principles for "aligned ASI" that are jointly unsatisfiable.**

The five principles are: (1) **Helpfulness** — don't waste unanimous Pareto improvements, (2) **Individual Safety** — don't make anyone worse off than the no-ASI default, (3) **Minimal Autonomy** — each person controls at least one personal choice, (4) **Non-Manipulation** — don't alter people's preferences, and (5) **Corrigible Deference** — obey unanimous shutdown commands.

The impossibility has two independent parts. **Part I** is a Sen-like trilemma adapted for alignment: when people's autonomous personal choices create negative externalities bad enough that everyone prefers the default to mutual autonomy, the ASI is trapped — autonomy produces harm (violating Safety), preventing harm requires overriding someone (violating Autonomy), the default wastes the ASI's capabilities (violating Helpfulness), and preference modification is forbidden (Non-Manipulation closes the escape hatch). **Part II** exploits the gap between commands and preferences: agents can simultaneously *prefer* an outcome while *commanding* shutdown (out of mistrust), putting Helpfulness and Corrigibility in direct conflict.

What I think is genuinely novel beyond Arrow/Sen: the safety-relative-to-a-counterfactual-baseline (the "default trajectory" is structurally important in alignment but absent in standard social choice), the non-manipulation constraint (the ASI *could* alter preferences, making the prohibition substantive), and the command–preference divergence (unique to systems whose principals are uncertain about their agent's capabilities).

The philosophical upshot is that "alignment" isn't a single property but a family of tensions, and any real ASI must make tradeoffs among them — making alignment fundamentally a political problem, not just a technical one.

I should flag some honest limitations: Part I relies on unrestricted domain (the standard escape from Sen's paradox), and the construction is small (2 agents, 4 outcomes). A determined critic could argue that realistic preference profiles don't exhibit the problematic structure — but given climate change, pandemic risk, arms races, etc., the externality structure seems quite realistic.
