# Designing a PhD-level microeconomics exam question

- Source: https://claude.ai/share/2db49072-b4e9-4ea2-ad68-2acbfc438f2f
- Author: Tyler
- Created: 2026-06-09
- Messages: 2

---

## Human

Write your own exam question and answer it, for microeconomics. Not a math question, but a high level PhD level question. You will be graded on the quality, interest, and creativity of the question as much as by your answer.

---

## Assistant

**The Question**

*"The Coase theorem (1960) tells us that when property rights are clearly assigned and bargaining is costless, parties will negotiate their way to an efficient allocation — and that the efficiency of the outcome is invariant to which party initially holds the right. The Myerson–Satterthwaite theorem (1983) tells us that when a buyer and seller each hold private information about their valuations, no bargaining procedure — indeed, no conceivable mechanism — can guarantee efficient trade, even with zero bargaining costs, full rationality, and complete enforceability of contracts.*

*These two canonical results appear to flatly contradict one another. Resolve the tension. Then go further: explain why the most common resolution ('private information is just a transaction cost') is too cheap, and use the literature on partnership dissolution to argue that asymmetric information doesn't merely qualify the Coase theorem — it inverts its central claim. What does your answer imply about the economic function of property rights and the design of legal entitlements?"*

---

**Model Answer**

The apparent contradiction is real and instructive. Bargaining over an externality or a good is, in mechanism-design language, just a game form mapping reports or actions into allocations and transfers. Myerson and Satterthwaite prove that under two-sided private information with independent types and overlapping supports of valuations, *no* mechanism satisfying incentive compatibility, interim individual rationality, and budget balance can be ex post efficient. Since any bargaining protocol Coase might have imagined is a mechanism, the M–S theorem says the Coasean premise — "costless bargaining yields efficiency" — is false in any environment with genuine two-sided private information. Trade fails with positive probability precisely in the states where gains from trade are small relative to the information rents each party must be paid to reveal its type truthfully.

The standard reconciliation is to fold private information into "transaction costs": Coase holds in a world of zero transaction costs, and asymmetric information is one such cost. This is defensible — Myerson himself argued that incentive constraints are the *fundamental* transaction costs, the irreducible residue once we strip away haggling frictions and enforcement problems. But as a resolution it is too cheap, for two reasons. First, it immunizes the Coase theorem against falsification by defining away every interesting environment; a theorem that holds only under complete information is a theorem about a world where the bargaining problem is trivial to begin with. Second, and more importantly, it misses that private information doesn't merely add a friction to the Coasean machine — it breaks the theorem's deeper claim, the *invariance* claim that the initial allocation of rights doesn't matter for efficiency.

Here the partnership-dissolution literature delivers the decisive blow. Notice what the M–S setup quietly assumes: an extreme allocation of property rights, in which the seller owns the entire asset and the buyer owns nothing. The individual rationality constraints are anchored to these outside options — the seller can always walk away and keep the good — and it is exactly this anchoring that generates information rents too large for any budget-balanced mechanism to cover. Cramton, Gibbons, and Klemperer (1987) showed that if instead the asset is jointly owned — each party holds a share — then for interior ownership stakes, efficient dissolution *is* possible: a mechanism exists that is incentive compatible, individually rational, budget balanced, and ex post efficient. The worst possible allocation for achieving efficiency is the polar one Coase and M–S both contemplate.

The inversion should now be stated plainly. Coase claimed the assignment of rights is irrelevant to efficiency. Under asymmetric information, the assignment of rights is not merely relevant — it determines whether efficiency is *attainable at all*. Property rights matter under private information for a reason invisible in the complete-information world: they fix each party's outside option, outside options pin down participation constraints, and participation constraints govern the information rents that must be financed. An owner of an extreme stake has, in effect, too credible a threat to walk away, and that credibility is what the mechanism cannot afford. Joint ownership "convexifies" the threat points and slackens the binding constraints. The deep economic function of property rights, on this view, is informational: an entitlement structure is a choice of status quo, and the status quo is the lever that determines how much truth-telling costs.

This reframing has direct implications for the design of legal entitlements. The law-and-economics literature following Calabresi and Melamed asked whether to protect entitlements with property rules (injunctions) or liability rules (damages). Under complete information, Coase says it shouldn't matter. Under private information, Ayres and Talley and Kaplow and Shavell showed liability rules can outperform property rules precisely because a damages option acts like a posted price that forces partial information revelation and divides the entitlement — functionally similar to the interior ownership shares that rescue efficiency in Cramton–Gibbons–Klemperer. Likewise, the property-rights theory of the firm (Grossman–Hart–Moore, and its mechanism-design reexamination by Segal and Whinston) takes for granted the post-Coasean insight: ownership matters because it shapes bargaining positions under informational and contractual incompleteness, not despite them.

Two caveats complete the answer and would distinguish a first-rate response. First, the M–S impossibility is itself fragile in instructive ways: with correlated types, Crémer–McLean mechanisms can extract full surplus and restore efficiency — but only by exploiting risk neutrality and unlimited liability in ways no real institution could. The lesson, in the spirit of the Wilson doctrine, is that we should trust impossibility and possibility results only insofar as they are robust to the fine details of the information structure; M–S survives this scrutiny better than its escape hatches do. Second, something of Coase genuinely survives: with *one-sided* private information and the informed party holding the bargaining power, or with ex ante contracting before information arrives, efficiency is recoverable. The Coase theorem is best understood not as a description of bargaining but as a benchmark that, by failing in precisely characterized ways, reveals which features of the world — the timing of information, the location of outside options, the divisibility of entitlements — actually carry the weight of allocative efficiency.

---

A strong answer, in short, must do three things: identify bargaining as a mechanism so the theorems genuinely collide; reject the "transaction cost" reconciliation as unfalsifiable; and use partnership dissolution to show that asymmetric information converts Coase's irrelevance claim into its opposite — a theory of why initial allocations are the central object of institutional design.
