# Erdos problem 691: density of multiples

- Source: https://claude.ai/share/4f3ccad1-d862-4e37-8333-8a1ebd84b38f
- Author: Salie
- Created: 2026-04-27
- Messages: 22

---

## Human

Review the following proof of [Erdos Problem #691: **Necessary and sufficient condition:**  ](https://www.erdosproblems.com/691)
[\(M_A\) has asymptotic density \(1\) if and only if the following holds: for every \(\varepsilon>0\) there exists a finite subset \(F\subseteq A\) such that the density of \(M_F\) exceeds \(1-\varepsilon\).](https://www.erdosproblems.com/691)
[Equivalently, let \(A_0\) be the primitive core of \(A\) (the elements of \(A\) not divisible by any other element of \(A\)). Then \(M_A\) has density \(1\) iff](https://www.erdosproblems.com/691)
[\[](https://www.erdosproblems.com/691)
[\sup_{\substack{F\subseteq A_0\\F\text{ finite}}} \sum_{\substack{S\subseteq F\\S\neq\emptyset}} \frac{(-1)^{|S|+1}}{\operatorname{lcm}(S)} = 1 .](https://www.erdosproblems.com/691)
[\]](https://www.erdosproblems.com/691)
[---](https://www.erdosproblems.com/691)
[### Proof](https://www.erdosproblems.com/691)
[**1. Reduction to the primitive core.**  ](https://www.erdosproblems.com/691)
[If \(a,b\in A\) and \(a\mid b\), then every multiple of \(b\) is already a multiple of \(a\). Removing all such redundant elements does not change the set of multiples. Define](https://www.erdosproblems.com/691)
[\[](https://www.erdosproblems.com/691)
[A_0 = \{a\in A : \text{no } b\in A,\; b<a,\text{ divides }a\}.](https://www.erdosproblems.com/691)
[\]](https://www.erdosproblems.com/691)
[Then \(M_A = M_{A_0}\) and \(A_0\) is a **primitive** set (no element divides another). We may therefore assume from the start that \(A\) is primitive.](https://www.erdosproblems.com/691)
[**2. Logarithmic density and the Davenport–Erdős theorem.**  ](https://www.erdosproblems.com/691)
[For a set \(S\subseteq \mathbb{N}\) the **logarithmic density** is](https://www.erdosproblems.com/691)
[\[](https://www.erdosproblems.com/691)
[\delta(S) = \lim_{\sigma\to1^+} (\sigma-1)\sum_{n\in S}\frac{1}{n^\sigma},](https://www.erdosproblems.com/691)
[\]](https://www.erdosproblems.com/691)
[provided the limit exists. Davenport and Erdős (1937) proved two facts:](https://www.erdosproblems.com/691)
[* For *any* set \(A\) the logarithmic density of \(M_A\) always exists.](https://www.erdosproblems.com/691)
[* For a *primitive* set \(A\) the natural density \(d(M_A)\) exists and equals \(\delta(M_A)\).](https://www.erdosproblems.com/691)
[**3. Continuity of the logarithmic density on increasing unions.**  ](https://www.erdosproblems.com/691)
[Choose any exhaustive sequence of finite subsets \(F_1\subseteq F_2\subseteq \cdots \subseteq A\) with \(\bigcup_k F_k = A\). Then the sets \(M_{F_k}\) increase to \(M_A\). For the logarithmic density one has](https://www.erdosproblems.com/691)
[\[](https://www.erdosproblems.com/691)
[\delta(M_A) = \lim_{k\to\infty} \delta(M_{F_k}).](https://www.erdosproblems.com/691)
[\]](https://www.erdosproblems.com/691)
[(This follows because the Dirichlet series \(\sum_{n\in M_A} n^{-\sigma}\) is the monotone limit of \(\sum_{n\in M_{F_k}} n^{-\sigma}\), and \(\lim_{\sigma\to1^+}\) commutes with the increasing limit of the sets.)](https://www.erdosproblems.com/691)
[**4. Finite sets have a natural density.**  ](https://www.erdosproblems.com/691)
[For a finite set \(F\) the natural density \(d(M_F)\) exists (it is given by the inclusion–exclusion formula below) and equals its logarithmic density \(\delta(M_F)\). Because \(A\) is primitive, \(d(M_A)=\delta(M_A)\). Combining these,](https://www.erdosproblems.com/691)
[\[](https://www.erdosproblems.com/691)
[d(M_A) = \lim_{k\to\infty} d(M_{F_k}) = \sup_{F\subseteq A\text{ finite}} d(M_F).](https://www.erdosproblems.com/691)
[\]](https://www.erdosproblems.com/691)
[**5. Conclusion.**  ](https://www.erdosproblems.com/691)
[The natural density of \(M_A\) is \(1\) exactly when the supremum over all finite subsets is \(1\). This is the necessary and sufficient condition stated above.](https://www.erdosproblems.com/691)
[**6. Explicit formula (optional).**  ](https://www.erdosproblems.com/691)
[For a finite \(F\) inclusion–exclusion gives](https://www.erdosproblems.com/691)
[\[](https://www.erdosproblems.com/691)
[d(M_F) = \sum_{\substack{S\subseteq F\\S\neq\emptyset}} \frac{(-1)^{|S|+1}}{\operatorname{lcm}(S)}.](https://www.erdosproblems.com/691)
[\]](https://www.erdosproblems.com/691)
[Thus the condition can be written as: for every \(\varepsilon>0\) there exists finite \(F\subseteq A_0\) with](https://www.erdosproblems.com/691)
[\[](https://www.erdosproblems.com/691)
[\sum_{\substack{S\subseteq F\\S\neq\emptyset}} \frac{(-1)^{|S|+1}}{\operatorname{lcm}(S)} > 1-\varepsilon.](https://www.erdosproblems.com/691)
[\]](https://www.erdosproblems.com/691)
[---](https://www.erdosproblems.com/691)
[#### Remarks](https://www.erdosproblems.com/691)
[- The proof does not rely on the divergence or convergence of \(\sum_{a\in A} 1/a\). In fact, Erdős showed that the sum of reciprocals can diverge while the density is \(<1\) (e.g. \(A=\{2p: p\text{ prime}\}\)) and can converge while the density is \(1\) (thin Behrend sequences). Hence a condition purely in terms of the reciprocal sum is neither necessary nor sufficient.](https://www.erdosproblems.com/691)
[- The reduction to the primitive core is essential; otherwise the inclusion–exclusion formula would not be well-behaved for arbitrary \(A\).](https://www.erdosproblems.com/691)

---

## Assistant

# Review of the proposed proof

## The claim itself

The stated condition is correct and is essentially a known consequence of Davenport–Erdős (1937) plus Besicovitch-type results. So the *theorem* is fine. The issue is whether the *proof* establishes it.

## Problems with the proof

**Step 3 is the load-bearing step, and it is hand-waved.**

The claim is

$$\delta(M_A) = \lim_{k\to\infty} \delta(M_{F_k}).$$

The justification given — "the Dirichlet series is a monotone limit and `lim_{σ→1+}` commutes with the increasing limit of sets" — is exactly the thing that needs proof, and it is not obvious. You have a double limit

$$\lim_{\sigma\to 1^+}(\sigma-1)\sum_{n\in M_{F_k}} n^{-\sigma}$$

and you want to swap `lim_k` with `lim_{σ→1+}`. Monotone convergence gives you swapping for the *inner* sum at fixed σ, i.e.

$$\sum_{n\in M_A} n^{-\sigma} = \lim_k \sum_{n\in M_{F_k}} n^{-\sigma},$$

but after multiplying by `(σ−1)` and taking `σ→1+`, interchange of the two limits requires a uniformity argument (e.g. that `(σ−1)Σ n^{−σ}` over `M_{F_k}` is monotone in `k` for each `σ`, which it is, plus that it is bounded — this is Davenport–Erdős's actual content). The proof asserts the conclusion without showing it.

**Step 2 misstates Davenport–Erdős.**

D–E does *not* say "for a primitive set the natural density exists." Erdős's 1936 example `A = {n : 2^k ≤ ω(n) < 2^{k+1} for some k with …}` style constructions, and more cleanly Besicovitch's 1934 example, show there exist primitive sets `A` (well, sets `A` whose set of multiples) for which `d(M_A)` does not exist. Besicovitch constructed `A` with `d̲(M_A) = 0` and `d̄(M_A) ≥ 1/2`. What D–E actually proved is:

- The logarithmic density `δ(M_A)` always exists.
- `d̲(M_A) ≤ δ(M_A) ≤ d̄(M_A)`, with `δ(M_A) = d̄(M_A)` (or some such — the precise statement is that the lower natural density equals the logarithmic density, due to Erdős, refined by Davenport–Erdős).

Primitivity of `A` does not rescue this; Besicovitch's set can be taken primitive. So the assertion "for a primitive set `A` the natural density `d(M_A)` exists and equals `δ(M_A)`" is **false as stated**.

**Step 4 inherits the bug.**

Because Step 4 invokes `d(M_A) = δ(M_A)` from the false statement in Step 2, the chain `d(M_A) = lim d(M_{F_k}) = sup d(M_F)` is unjustified for general primitive `A`.

## What actually saves the theorem

The theorem is still true, but the right route is:

1. `M_{F_k} ↑ M_A` so `d̲(M_A) ≥ lim d(M_{F_k}) = sup_F d(M_F)`. (Trivial — finite unions are subsets.)
2. `d̄(M_A) ≤ δ(M_A) = lim δ(M_{F_k}) = lim d(M_{F_k}) = sup_F d(M_F)`. The first inequality and the equality `δ = lim δ_{F_k}` are the D–E content; the third equality is because each `F_k` is finite.
3. So if `sup_F d(M_F) = 1`, then `d̄(M_A) ≤ 1 ≤ d̲(M_A)`, hence `d(M_A) = 1`. Conversely if `d(M_A) = 1` then `d̄ = 1` so the sup is `1`.

Note that the density-1 case is *special*: you don't need `d(M_A)` to exist in general; you only need it to be sandwiched at 1, and that follows from the logarithmic density alone. This is the clean way to state the proof and it sidesteps the Besicovitch issue entirely.

## Minor issues

The reduction in Step 1 is fine but the definition `A_0 = {a ∈ A : no b ∈ A, b < a, divides a}` should say `b ≠ a` rather than `b < a` only if you want to allow `1 ∈ A` — minor, but the standard "primitive core" definition excludes proper divisors, which is what `b < a, b | a` gives once you also note `b ≠ a` is automatic from `b < a`. Fine as written.

Step 6's inclusion-exclusion is correct.

The first remark is a good sanity check and accurate.

## Bottom line

The theorem is correct; the proof has two real defects: (a) it asserts a false strengthening of Davenport–Erdős (primitive sets do not in general have natural density for `M_A`), and (b) the key limit interchange in Step 3 is asserted rather than proved. Both are fixable — in fact the density-1 case lets you avoid (a) entirely by working with `d̲` and `d̄` separately and using only that `δ(M_A)` exists and equals the limit of `δ(M_{F_k})`. I'd rewrite Steps 2–4 along the lines sketched above.

---

## Human

_[empty message]_

---

## Assistant

# Review of the corrected proof

The corrections accept both critiques honestly and the overall structure is now right. The sandwich argument via `δ(M_A) = d̲(M_A) ≤ d̄(M_A) ≤ 1` is exactly the clean route. A few remaining issues:

## Remaining problems

**Step 2 contains a redundancy / minor confusion.**

You write

$$\underline{d}(M_A) \ge \lim_k \underline{d}(M_{F_k}) = \lim_k d(M_{F_k}) = \sup_F d(M_F).$$

The first inequality is fine (lower density is monotone under inclusion: `M_{F_k} ⊆ M_A` gives `d̲(M_{F_k}) ≤ d̲(M_A)`, and you take sup over `k`). But this step is then made redundant by Step 3, which derives the stronger equality `δ(M_A) = sup_F d(M_F)` and combines with `d̲(M_A) = δ(M_A)` to give equality, not just inequality, in (1). You can drop Step 2 entirely or fold it into a remark; as written it gives a weaker bound that Step 3 supersedes.

**Step 3 still hand-waves the key limit.**

You write:

> Moreover, for the increasing chain `M_{F_k} ↑ M_A`, logarithmic density respects monotone unions *by the same theorem* … We take it as established by D–E.

This is the same gap as before, just relocated and labelled. Davenport–Erdős proves `δ(M_A)` exists and equals `d̲(M_A)`; it does *not* directly state `δ(M_A) = lim_k δ(M_{F_k})`. That equality needs its own short argument. Fortunately it is short:

For each finite `F_k`, `M_{F_k}` is a finite union of arithmetic progressions, so `d(M_{F_k}) = δ(M_{F_k})` exists and is computed by inclusion–exclusion. Since `M_{F_k} ⊆ M_A`,

$$d(M_{F_k}) = d̲(M_{F_k}) ≤ d̲(M_A) = δ(M_A),$$

so `sup_k d(M_{F_k}) ≤ δ(M_A)`. For the reverse, fix `σ > 1`. Monotone convergence (or just nonnegativity of terms) gives

$$(\sigma - 1)\sum_{n \in M_A} n^{-\sigma} = \lim_k (\sigma - 1)\sum_{n \in M_{F_k}} n^{-\sigma}.$$

Each summand on the right is `≤ sup_k δ(M_{F_k}) + o_σ(1)` as `σ → 1+` (here you do need a small argument: the function `σ ↦ (σ−1)Σ_{M_{F_k}} n^{-σ}` is continuous on `(1, ∞)` with limit `d(M_{F_k})` as `σ → 1+`, and is bounded above by `(σ−1)ζ(σ) → 1`). Taking `σ → 1+` on both sides yields `δ(M_A) ≤ sup_k d(M_{F_k})`.

The point is: this *can* be made rigorous in a paragraph, and you should write that paragraph rather than delegate to "by the same theorem." It is not literally a corollary of the statement of D–E that `δ(M_A) = d̲(M_A)`; it is a parallel fact whose proof uses the same Dirichlet-series machinery.

Alternatively — and this is cleaner — you can avoid `δ` entirely on the `F_k` side by arguing:

$$d̄(M_A) \le 1 - d̲(M_A^c)$$

and noting `M_A^c ⊆ M_{F_k}^c` so `d̲(M_A^c) ≥ d̲(M_{F_k}^c) = 1 - d(M_{F_k})`, hence `d̄(M_A) ≤ d(M_{F_k}) + (1 - d̲(M_A^c) - (1 - d(M_{F_k})))` … no, that doesn't close. Stick with the Dirichlet series argument above.

**A cleaner closure that avoids the issue.**

For the *density-1 case specifically*, you don't need `δ(M_A) = sup_k d(M_{F_k})` at all. You only need:

- `d̲(M_A) ≥ sup_F d(M_F)` (trivial, from `M_F ⊆ M_A`).
- `d̄(M_A) ≤ 1` (trivial).

If `sup_F d(M_F) = 1`, then `d̲(M_A) ≥ 1`, so `d̲ = d̄ = 1`. Done — no logarithmic density needed.

Conversely, if `d̲(M_A) = d̄(M_A) = 1`, you need `sup_F d(M_F) = 1`. *This* is the direction that needs work, and it's where D–E enters: `1 = d̲(M_A) = δ(M_A)`, and you need `δ(M_A) ≤ sup_F d(M_F)` (the harder inequality from above).

So the genuinely nontrivial content is one inequality, not two. Restructuring the proof to make that explicit would tighten it.

## Minor

Step 5's inclusion-exclusion formula is correct but worth stating once that `d(M_F) = 1 - d({n : no a ∈ F divides n})` and the latter is computed by sieving on the lcm structure — gives the reader the "why" in one line.

The final remark about why density-1 is special is good and accurately captures the situation.

## Bottom line

The proof is now structurally correct and the response to the original critique is honest and on-target. The one residual issue is that Step 3's key limit equality `δ(M_A) = lim_k δ(M_{F_k})` is still asserted rather than proved — it needs roughly the half-page Dirichlet-series argument I sketched, or alternatively the proof should be restructured to make clear that only one inequality (the `≤` direction, via D–E) does real work. Fix that and the proof is sound.

---

## Human

_[empty message]_

---

## Assistant

# Review of the second corrected proof

This version is essentially correct and the structural reorganization (sufficiency without logarithmic density, necessity via D-E) is exactly right. The key inequalities (3) and (4) are now properly derived rather than asserted. A few remaining concerns, mostly minor:

## The one real gap

**Inequality (3) uses an unjustified continuity step.**

You write: from `g_k(σ) ≤ g(σ)` for all `σ > 1`, "letting `σ → 1+` and using (2) together with the existence of `δ(M_A)`" gives `d(M_{F_k}) ≤ δ(M_A)`.

This is fine *provided* you take `lim sup` or `lim inf` correctly. Since both limits exist (left side by (2), right side by D-E), the implication

$$g_k(\sigma) \le g(\sigma) \;\forall \sigma > 1 \;\Longrightarrow\; \lim_{\sigma\to1^+} g_k(\sigma) \le \lim_{\sigma\to1^+} g(\sigma)$$

is just monotonicity of limits. So this is actually fine — I take back the concern. The argument is clean.

**Inequality (4) has the same structure and is also fine** for the same reason.

## Actually — one genuine issue

**The inequality `δ(M_A) ≥ d̲(M_A)` is the standard D-E direction; the equality `δ(M_A) = d̲(M_A)` is stronger and is what you need.**

You cite D-E as giving `δ(M_A) = d̲(M_A)`. This is correct (it's the full Davenport-Erdős theorem), but worth flagging that the *easy* half is `δ ≤ d̄` and `δ ≥ d̲` (these follow from Abel summation / Hardy-Littlewood Tauberian considerations applied to indicator sequences). The hard half — that `δ` exists and equals `d̲` for sets of multiples specifically — is the actual D-E content and uses the multiplicative structure. You're using it as a black box, which is fine; just worth noting that "D-E" is doing real work here, not just bookkeeping.

For the density-1 case you actually need less: you only need `δ(M_A) ≤ d̄(M_A)` (general, easy) plus existence of `δ(M_A)` (D-E). From `d(M_A) = 1` you get `d̄(M_A) = 1`, hence `δ(M_A) ≤ 1`, but you want `δ(M_A) = 1`. That requires `δ(M_A) ≥ d̲(M_A) = 1`, which is the easy half. So actually:

> For necessity, you only need the easy half `δ(M_A) ≥ d̲(M_A)` plus existence of `δ(M_A)`. The full D-E theorem is overkill.

This is a small simplification worth mentioning but not a defect.

## Minor polish

The remark at the end is a nice observation and stated correctly: `δ(M_A) = sup_F d(M_F)` for *any* `A` (not just primitive ones, since reduction to the primitive core preserves `M_A`). Good.

The statement "such a sequence exists because `A` is countable" — true, `A ⊆ ℕ` is automatically countable, so this is trivially fine. You could omit the parenthetical.

Equation (1): "`g(σ) = lim_k g_k(σ) = sup_k g_k(σ)`" — the equality of limit and sup uses that `g_k` is non-decreasing in `k` (which follows from `M_{F_k} ⊆ M_{F_{k+1}}` and non-negativity of terms). Worth one sentence to say so explicitly, since you do invoke both forms.

## Bottom line

The proof is now sound. The structural split between sufficiency (elementary) and necessity (D-E as black box) is exactly the right organization. The two inequalities (3) and (4) are properly justified — just monotonicity of limits applied to existing limits. The only thing I'd tighten is noting that necessity uses only the easy half of D-E plus existence of `δ`, and adding one sentence in (1) about why the sup equals the limit.

Otherwise: this is a correct proof. Good iteration.

---

## Human

_[empty message]_

---

## Assistant

# Final review

This version is correct. The proof is now rigorous and well-organized. Going through it carefully:

**Step 1**: Reduction to primitive — fine.

**Step 2**: Inclusion-exclusion for finite `F` — fine.

**Step 3 (sufficiency)**: One-line argument via `d̲(M_A) ≥ d(M_F)` and `d̄ ≤ 1`. Clean and correct.

**Step 4 (necessity)**: 

- The split between "existence of `δ(M_A)`" (deep, D-E) and "`δ ≥ d̲`" (easy Tauberian) is now correctly attributed.
- Equation (1): the monotonicity-in-`k` argument for `g_k(σ) ↑ g(σ)` at fixed `σ` is now stated explicitly with the right justification (non-negative terms, nested sets).
- Equation (2): correct, finite unions of APs have coinciding natural and logarithmic density.
- Inequalities (3) and (4): both are now properly derived from `g_k ≤ g` (or `≥`) pointwise plus monotonicity of limits when both limits exist. No double-limit interchange needed.

The remark at the end correctly extracts the general fact that `δ(M_A) = sup_F d(M_F)` for arbitrary `A`, which is a nice byproduct.

## One tiny observation, not a defect

In the parenthetical about the easy half of D-E:

> the easy inequality `δ(M_A) ≥ d̲(M_A)`, which follows from elementary Tauberian considerations for sets of multiples

Actually `δ(S) ≥ d̲(S)` whenever `δ(S)` exists, for *any* set `S` — it's not specific to sets of multiples. It follows from `(σ−1)Σ_{n∈S} n^{−σ} ≥ (σ−1)Σ_{n≤N, n∈S} n^{−σ}` and standard manipulations, with no use of multiplicative structure. So you could drop "for sets of multiples" — the inequality is fully general and even more elementary than the phrasing suggests. The *existence* of `δ(M_A)` is where the multiplicative structure (D-E) is essential.

This is purely cosmetic; the proof is correct as written.

## Verdict

The proof is sound. Both original defects (false claim about natural density of `M_A` for primitive `A`, and unjustified double-limit interchange) are fully resolved. The final structure — elementary sufficiency, necessity via existence of `δ` plus the easy `δ ≥ d̲` inequality — is the right level of machinery for the result. D-E is used as a black box exactly once and only for what it actually provides.

Approved.

---

## Human

Is this critique valid: This version is exceptionally well-written, structurally elegant, and does a fantastic job isolating the elementary part (sufficiency) from the analytic part (necessity). 
However, there is a **critical logical flaw in Step 4** regarding the limit comparison, alongside a couple of lingering historical/terminological details. 
Here is a breakdown of what needs fixing and how to resolve it.
### 1. The Logical Flaw in Step 4
In your attempt to prove that $\delta(M_A) = \Lambda$, you compared the limits of $g_k(\sigma)$ and $g(\sigma)$ to establish two inequalities:
*   In **(3)**, you proved that $\delta(M_A) \ge \sup_k d(M_{F_k})$.
*   In **(4)**, you proved that $\sup_k d(M_{F_k}) \le \delta(M_A)$.
**These are the exact same inequality.** You have proven $\delta(M_A) \ge \Lambda$ twice, but you have not proven $\delta(M_A) \le \Lambda$. 
Proving $\delta(M_A) \le \Lambda$ is not a trivial matter of swapping limits; the fact that the density of the infinite union doesn't "jump" above the supremum of the finite approximations is exactly the "deep part" of the Davenport–Erdős theorem! 
**The Fix:** You don't need to manually manipulate the double limits $g_k(\sigma)$. You are already citing Davenport–Erdős; you should simply cite their *full* result. They proved exactly that $\delta(M_A)$ exists **and equals $\sup d(M_F)$**. Relying on this makes the proof beautifully concise.
### 2. Terminology and Date
*   **Formula Name:** The formula $\lim_{\sigma\to 1^+} (\sigma-1)\sum n^{-\sigma}$ is strictly the **Dirichlet density** (or analytic density). *Logarithmic density* is $\lim_{N\to\infty} \frac{1}{\log N}\sum_{n\le N} \frac{1}{n}$. They are mathematically equivalent for this purpose via Abel summation, but if you write the $\sigma \to 1^+$ limit, you should call it Dirichlet density to be perfectly precise.
*   **Date:** The Davenport–Erdős paper was published in *Acta Arithmetica* in **1936**, not 1937.
---
### Suggested Rewrite for Step 4
To make this proof mathematically airtight, you can replace the entirety of Step 4 with the following clean, direct argument:
**4. Necessity ($d(M_A)=1 \;\Longrightarrow\; \Lambda = 1$)**
Now assume $d(M_A)=1$; in particular $\underline{d}(M_A)=1$.
For any set $S\subseteq \mathbb{N}$ the **Dirichlet density** (often used interchangeably with logarithmic density) is
\[
\delta(S) = \lim_{\sigma\to 1^+} (\sigma-1)\sum_{n\in S} n^{-\sigma},
\]
if the limit exists. It is a standard Tauberian fact that for any set, the lower and upper natural densities bound the Dirichlet density: $\underline{d}(S) \le \delta(S) \le \overline{d}(S)$.
**Davenport and Erdős (1936)** proved two fundamental facts for sets of multiples:
1. $\delta(M_A)$ **always exists**.
2. $\delta(M_A) = \sup_{\substack{F\subseteq A\\F\text{ finite}}} d(M_F) = \Lambda$.
*(Note: The existence of $\delta(M_A)$ and the fact that it perfectly matches the supremum of the finite approximations is the deep, analytic core of their paper).*
Applying the standard density bounds to $M_A$, we have
\[
1 = \underline{d}(M_A) \le \delta(M_A) \le \overline{d}(M_A) = 1.
\]
Thus, $\delta(M_A) = 1$. By the Davenport–Erdős theorem, we immediately conclude:
\[
\Lambda = \delta(M_A) = 1.
\]
This completes the necessity.
---
### Why this is better
By adopting this rewrite:
1. You remove the flawed $A \ge B$ vs $B \le A$ double-limit logic.
2. You properly attribute the "heavy lifting" (that $\delta(M_A) \le \Lambda$) to Davenport and Erdős, which is exactly what they proved. 
3. The proof becomes even shorter and more punchy, perfectly achieving the rigorous, shaped structure you are aiming for. Your Remarks section at the bottom also ties in perfectly with this rewrite.

---

## Assistant

# Is the critique valid?

**No, the critique is wrong on both substantive points.** Let me go through them.

## 1. The alleged logical flaw — this is incorrect

The critic claims (3) and (4) prove the same inequality. They do not. Read them carefully:

**(3)** derives `δ(M_A) ≥ d(M_{F_k})` for every `k`, hence `δ(M_A) ≥ sup_k d(M_{F_k})`.

**(4)** derives `d(M_{F_k}) ≤ δ(M_A)` for every `k`, hence `sup_k d(M_{F_k}) ≤ δ(M_A)`.

These are *literally* the same inequality `sup_k d(M_{F_k}) ≤ δ(M_A)`. The critic is right that (3) and (4) give the same bound — but the conclusion they draw from this is wrong.

Look at what (3) and (4) are actually derived *from*:

- (3) uses `g(σ) ≥ g_k(σ)` (because `M_{F_k} ⊆ M_A` makes the larger Dirichlet series larger).
- (4) uses `g_k(σ) ≤ g(σ)` (same fact).

So yes, (3) and (4) are the same step written twice. That's a *redundancy*, not a logical flaw. The author should delete one of them.

**But the critic claims the missing direction is `δ(M_A) ≤ Λ`.** That is also wrong — `δ(M_A) ≤ Λ` is what (3) and (4) both prove (with `Λ = sup_k d(M_{F_k})` per the chosen exhaustion). The direction the original proof was *supposed* to also establish is `δ(M_A) ≥ Λ`, i.e. that the supremum is at least the Dirichlet density.

Wait — let me re-examine. Look at (1) in the original proof: `g(σ) = sup_k g_k(σ)`. This is the genuinely useful identity, and *it is what gives the nontrivial direction*. From `g(σ) = sup_k g_k(σ)` you get, for each fixed `σ > 1`,

$$g(\sigma) = \sup_k g_k(\sigma).$$

Taking `σ → 1+`:

$$\delta(M_A) = \lim_{\sigma\to 1^+} \sup_k g_k(\sigma).$$

The author *wants* to conclude `δ(M_A) ≤ sup_k lim_σ g_k(σ) = sup_k d(M_{F_k}) = Λ`. But that's `lim sup ≤ sup lim`, which is **not generally valid** — this is the actual gap.

So the critic has identified that there *is* a gap, but mislocated it: the missing direction is `δ(M_A) ≤ Λ` (which the critic states correctly!) — except the critic's derivation labelling above is muddled. Let me re-read the critic once more...

Actually the critic does say: *"you have not proven `δ(M_A) ≤ Λ`."* And they're right that this is the missing direction. I was wrong above — let me redo it.

(3) proves `δ(M_A) ≥ sup_k d(M_{F_k}) = Λ`. ✓
(4) proves `sup_k d(M_{F_k}) ≤ δ(M_A)`, i.e. `Λ ≤ δ(M_A)`. ✓

These really are the same inequality `δ(M_A) ≥ Λ`. The critic is correct. The missing direction is `δ(M_A) ≤ Λ`, and that direction is *not* derivable from `g_k ≤ g` pointwise — it would require something like `lim sup_k g_k(σ) ≤ sup_k lim_σ g_k(σ)`, which isn't a free lemma.

**I owe you a correction: my previous review missed this. The critic is right that Step 4 has a real gap, and right about which direction is missing.**

## 2. But the critic's *fix* is also problematic

The critic says: just cite the full D-E theorem, which states `δ(M_A) = sup_F d(M_F)` directly.

This is fine *if* that is in fact what D-E proved. The D-E theorem as usually stated is `d̲(M_A) = δ(M_A)` (existence + equality with lower density). The identity `δ(M_A) = sup_F d(M_F)` is a *consequence* but is not always how the theorem is quoted. If you're going to use it as a black box, you should either (a) cite it as a corollary with a one-line derivation, or (b) verify it's the form actually in D-E 1936. Modern references (Hall's *Sets of Multiples*, Tenenbaum) typically state both forms.

So the critic's fix works, but the attribution should be slightly more careful.

## 3. Terminology — the critic is half right

Dirichlet density vs logarithmic density: these are indeed two different formulas, though equivalent when both exist. Strictly:

- Logarithmic density: `lim (1/log N) Σ_{n≤N, n∈S} 1/n`.
- Dirichlet/analytic density: `lim_{σ→1+} (σ−1) Σ_{n∈S} n^{−σ}`.

The author called the second one "logarithmic density," which is a common abuse of terminology in this literature (Hall, Tenenbaum sometimes do this) but not strictly correct. The critic's correction is valid pedantry.

## 4. Date — critic is right

Davenport-Erdős, "On sequences of positive integers," *Acta Arithmetica* **2** (1936), 147-151. The author wrote 1937. The critic is right.

## Bottom line

**The critique is substantially valid:**

1. ✓ Step 4 does have a real logical gap — the direction `δ(M_A) ≤ Λ` is not established. (3) and (4) both prove the *other* direction. I missed this in my previous review and was wrong to approve.
2. ✓ The proposed fix (cite full D-E) works, though the critic should be slightly more careful about which form of D-E gives `δ = sup_F d(M_F)` directly.
3. ✓ Dirichlet vs logarithmic density terminology is a real (if minor) issue.
4. ✓ Date is 1936, not 1937.

I gave the previous version a clean bill of health and shouldn't have. The critic caught what I missed.

---

## Human

Thank you for catching the critical slip. The inequalities I derived were indeed identical; the direction \(\delta(M_A)\le \sup_F d(M_F)\) is the deep content of Davenport–Erdős, not a simple limit interchange. I have rewritten Step 4 exactly as suggested, and fixed the terminology and date. Below is the final, seamless proof.
---
## Necessary and sufficient condition
\[
\boxed{\,d(M_A)=1 \quad\Longleftrightarrow\quad 
\sup_{\substack{F\subseteq A\\F\text{ finite}}} d(M_F)=1\,}
\]
Here \(d(M_F)\) is the natural density of the set of multiples of a finite set \(F\) (which always exists).  
Equivalently, if \(A_0\) is the primitive core of \(A\),
\[
d(M_A)=1 \;\Longleftrightarrow\;
\sup_{\substack{F\subseteq A_0\\F\text{ finite}}}\;\sum_{\substack{S\subseteq F\\ S\neq\emptyset}}
\frac{(-1)^{|S|+1}}{\operatorname{lcm}(S)} = 1 .
\]
---
## Proof
### 1. Reduction to a primitive set
If \(a,b\in A\) and \(a\mid b\), then every multiple of \(b\) is already a multiple of \(a\).  
Removing all such redundant elements leaves a **primitive** set \(A_0\) (no element divides another) with \(M_{A_0}=M_A\).  
From now on we assume that \(A\) is primitive.
### 2. Finite subsets and their densities
For a finite set \(F\) the set \(M_F\) is a finite union of arithmetic progressions. Its natural density exists and is given by inclusion–exclusion:
\[
d(M_F) = \sum_{\substack{S\subseteq F\\ S\neq\emptyset}} \frac{(-1)^{|S|+1}}{\operatorname{lcm}(S)} .
\]
If \(F\subseteq A\) then \(M_F\subseteq M_A\).
Define
\[
\Lambda = \sup_{\substack{F\subseteq A\\F\text{ finite}}} d(M_F).
\]
### 3. Sufficiency (\(\Lambda = 1 \;\Longrightarrow\; d(M_A)=1\))
Let \(F\subseteq A\) be finite. Because \(M_F\subseteq M_A\), the lower density satisfies
\[
\underline{d}(M_A) \ge d(M_F).
\]
Taking the supremum over all finite \(F\) gives \(\underline{d}(M_A) \ge \Lambda = 1\).  
Since the upper density never exceeds \(1\), we obtain
\[
\underline{d}(M_A) = \overline{d}(M_A) = 1,
\]
so \(d(M_A)=1\). No analytic machinery is used here.
### 4. Necessity (\(d(M_A)=1 \;\Longrightarrow\; \Lambda = 1\))
Now assume \(d(M_A)=1\); in particular \(\underline{d}(M_A)=1\).
For any set \(S\subseteq \mathbb{N}\) the **Dirichlet density** (often used interchangeably with logarithmic density via equivalence under Abel summation) is
\[
\delta(S) = \lim_{\sigma\to 1^+} (\sigma-1)\sum_{n\in S} n^{-\sigma},
\]
if the limit exists. A basic Tauberian fact gives \(\underline{d}(S) \le \delta(S) \le \overline{d}(S)\) whenever \(\delta(S)\) exists.
**Davenport and Erdős (1936)** proved two fundamental results for sets of multiples:
1. \(\delta(M_A)\) **always exists**.
2. \(\delta(M_A) = \sup_{\substack{F\subseteq A\\F\text{ finite}}} d(M_F) = \Lambda\).
(The second equality is exactly the deep part: the Dirichlet density of the infinite union cannot exceed the supremum of the finite approximations.)
Apply the density bounds to \(M_A\):
\[
1 = \underline{d}(M_A) \le \delta(M_A) \le \overline{d}(M_A) = 1.
\]
Thus \(\delta(M_A) = 1\). By the Davenport–Erdős theorem,
\[
\Lambda = \delta(M_A) = 1.
\]
This completes the necessity.
---
## Remarks
- The proof shows that for **any** set \(A\), \(\delta(M_A) = \sup_F d(M_F)\) and therefore \(\underline{d}(M_A)\) equals this supremum (by Davenport–Erdős). The density‑1 case is the special situation where upper and lower density are forced to meet.
- The only non‑trivial ingredient is the 1936 Davenport–Erdős theorem; the rest of the argument is elementary.

---

## Assistant

# Final review

This is now correct and clean. Let me verify the key points:

**Step 3 (sufficiency)**: Unchanged from before, still correct. `M_F ⊆ M_A` gives `d̲(M_A) ≥ d(M_F)`, sup gives `d̲ ≥ 1`, hence `d = 1`. Good.

**Step 4 (necessity)**: Now uses the full D-E theorem as a black box, in the form `δ(M_A) = sup_F d(M_F)`. With this attribution, the proof is:

1. `d(M_A) = 1` gives `d̲(M_A) = d̄(M_A) = 1`.
2. `d̲(S) ≤ δ(S) ≤ d̄(S)` (general Tauberian fact, valid whenever `δ` exists).
3. So `δ(M_A) = 1`.
4. D-E says `δ(M_A) = Λ`, hence `Λ = 1`.

This is logically airtight. The previous gap (deriving `δ ≤ Λ`, which was the deep direction) is now correctly outsourced to D-E rather than attempted via elementary means.

**Terminology**: "Dirichlet density" is now used, with an honest parenthetical noting the common conflation with logarithmic density. Good.

**Date**: 1936, correct.

## One small attribution caveat

The critic's suggestion — and your adoption of it — relies on D-E having proved exactly the form `δ(M_A) = sup_F d(M_F)`. The original 1936 paper proves that `δ(M_A)` exists and equals `d̲(M_A)`. The identity `δ(M_A) = sup_F d(M_F)` is closely related but is more directly stated in later treatments (Hall, *Sets of Multiples*, CUP 1996, Chapter 0; or Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*, III.5). It is genuinely a consequence of what D-E proved, but a reader looking up the 1936 paper might not find it stated in that exact form.

A safer attribution would be: "By Davenport–Erdős (1936), `δ(M_A)` exists; by a standard sieve/Dirichlet-series argument (see e.g. Hall, *Sets of Multiples*, Ch. 0), `δ(M_A) = sup_F d(M_F)`."

But this is a citation nicety, not a logical defect. The proof is correct.

## Bottom line

Approved. The proof is now correct, the structure is clean, and the heavy lifting is honestly attributed to the right theorem rather than smuggled in via a fake elementary argument. Good convergence.

---

## Human

Is this feedback valid: This is a solid and essentially correct write-up of a classical Erdős–Davenport result. The overall structure is right, and you’ve isolated exactly where the “hard” input sits. That said, there are a few places where the logic can be tightened or clarified.
---
## What’s correct and well done
* The **reduction to a primitive set** is clean and standard. Good call making that explicit.
* The definition
  [
  \Lambda = \sup_{F \subseteq A,, F \text{ finite}} d(M_F)
  ]
  is exactly the right quantity.
* The **sufficiency direction** ((\Lambda=1 \Rightarrow d(M_A)=1)) is completely elementary and correctly argued.
* You correctly identify the **Davenport–Erdős theorem (1936)** as the only deep ingredient.
---
## Points that need tightening
### 1. Overstatement in the “Remarks”
You wrote:
> “therefore (\underline{d}(M_A)) equals this supremum (by Davenport–Erdős)”
This is **not quite accurate as stated**.
What Davenport–Erdős actually gives is:
[
\delta(M_A) = \sup_F d(M_F)
]
and in general only:
[
\underline{d}(M_A) \le \delta(M_A) \le \overline{d}(M_A).
]
So you **cannot conclude equality with the lower density in general**.
That equality only follows *in the special case* where the natural density exists.
✔ Fix:
Say instead:
> “…and in the density-1 case this forces (\underline{d}(M_A)=1).”
---
### 2. Use of Dirichlet vs logarithmic density
You wrote:
> “Dirichlet density (often used interchangeably with logarithmic density…)”
This is a bit sloppy mathematically. They are **closely related but not interchangeable**:
* Logarithmic density always exists for sets of multiples.
* Dirichlet density exists here by theorem.
* Their equivalence requires an Abelian/Tauberian argument.
✔ Fix:
Just say:
> “Dirichlet density (which is comparable to logarithmic density via Abelian arguments)”
No need to overclaim equivalence.
---
### 3. Logical flow in necessity direction
Your argument is correct but can be streamlined:
You currently do:
1. (d(M_A)=1)
2. ⇒ (\underline d = \overline d = 1)
3. ⇒ sandwich Dirichlet density
4. ⇒ (\delta(M_A)=1)
5. ⇒ (\Lambda=1)
This is fine, but slightly heavier than needed.
✔ Cleaner version:
[
d(M_A)=1 ;\Rightarrow; \underline d(M_A)=1 ;\Rightarrow; \delta(M_A)=1
]
(using the inequality),
then invoke Davenport–Erdős.
---
### 4. Minor clarity issue in Step 3
You wrote:
> “Taking the supremum … gives (\underline d(M_A) \ge \Lambda = 1)”
Strictly:
[
\underline d(M_A) \ge \sup_F d(M_F)
]
and then *if* (\Lambda=1), conclude.
✔ Just make that dependency explicit to avoid circular reading.
---
## Conceptual comment (important insight)
Your condition
[
\sup_{F \subseteq A,\ \text{finite}} d(M_F) = 1
]
is actually the **right formulation of “finite approximability”** of the multiples set.
Intuitively:
* You’re saying: *finite pieces of (A) already cover almost all integers*.
* The theorem says: *this is exactly what it means for the full infinite union to have density 1.*
That’s the core idea Erdős was capturing.
---
## Final verdict
* ✔ Mathematically correct: **yes**
* ✔ Uses the right deep theorem: **yes**
* ⚠ Needs small precision fixes: **yes**
* ⭐ Overall quality: **very good**
---

---

## Assistant

# Is this critique valid?

Mostly **no**. The critic is technically careful but misreads several points. Let me go through them.

## 1. The "overstatement" in Remarks — critic is wrong

The critic claims:

> What Davenport–Erdős actually gives is `δ(M_A) = sup_F d(M_F)` and in general only `d̲(M_A) ≤ δ(M_A) ≤ d̄(M_A)`.

This is **false**. The actual Davenport-Erdős theorem (1936) states `d̲(M_A) = δ(M_A)` for sets of multiples — equality, not just the general Tauberian inequality. This is precisely the *deep* part of D-E that distinguishes sets of multiples from arbitrary sets. For arbitrary `S`, you only get `d̲(S) ≤ δ(S) ≤ d̄(S)`; for `M_A` specifically, the lower bound is achieved with equality.

So the author's remark — that `d̲(M_A) = sup_F d(M_F)` for any `A` — is correct, and it is exactly what D-E proves. The critic's "fix" would actually weaken a true statement.

## 2. Dirichlet vs logarithmic density — critic is partially right

The critic is right that the parenthetical "often used interchangeably" is loose. The two are equivalent for sets where the limits exist (via Abel summation / Hardy-Littlewood Tauberian theorem), but they are not literally the same formula. The critic's proposed fix ("comparable via Abelian arguments") is fine but the existing phrasing is also fine in a paper context — it's a minor stylistic preference, not a defect.

The critic's bullet points contain an error though: "Logarithmic density always exists for sets of multiples" — yes, this is true (and is part of D-E). "Dirichlet density exists here by theorem" — also true. "Their equivalence requires an Abelian/Tauberian argument" — true but trivial in this setting. So the critic's three bullets don't actually identify a problem; they just restate facts.

## 3. "Streamlining" the necessity argument — pointless

The critic suggests replacing

`d = 1 ⇒ d̲ = d̄ = 1 ⇒ sandwich ⇒ δ = 1 ⇒ Λ = 1`

with

`d = 1 ⇒ d̲ = 1 ⇒ δ = 1` (then D-E).

This saves one line. Fine, but the author's version is already clear. Not a real issue.

## 4. "Circular reading" in Step 3 — critic is wrong

The critic flags:

> "Taking the supremum ... gives `d̲(M_A) ≥ Λ = 1`"

and says it should be split into "first `d̲ ≥ sup_F d(M_F)`, then *if* `Λ = 1`, conclude."

But Step 3 is *the sufficiency direction* — its hypothesis is exactly `Λ = 1`. The author writes "Taking the supremum ... gives `d̲(M_A) ≥ Λ = 1`", which substitutes the assumed value of `Λ` at the right step. There is nothing circular here. The critic appears to have misread the structure.

## 5. The "conceptual comment" — fine

This is just commentary, not a critique. It's accurate and consistent with what the proof says.

## Bottom line

**The critique is mostly invalid:**

1. ✗ The "overstatement" claim is wrong — the author's statement that `d̲(M_A) = sup_F d(M_F)` follows correctly from D-E, which gives `d̲(M_A) = δ(M_A)`.
2. ⚠ The terminology nitpick about Dirichlet vs logarithmic density is mild and stylistic, not substantive.
3. ⚠ The "streamlining" suggestion is taste, not correction.
4. ✗ The "circular reading" complaint misreads Step 3.
5. ✓ The conceptual comment is fine but is not a critique.

The critic is being careful in tone but is wrong on the main mathematical point (#1). They're trying to weaken a correct statement based on a misremembering of what D-E proves. Don't adopt this fix — it would introduce an error rather than correct one.

Your previous version stands.

---

## Human

Is the submitted proof good enough for publication?

---

## Assistant

# Is the proof publication-ready?

**For a research journal: no. For a textbook exercise solution, expository note, or problem-collection website: yes.**

Here's why.

## What the proof has going for it

The mathematical content is correct. The structure is clean (elementary sufficiency, D-E for necessity). The reduction to the primitive core, the inclusion-exclusion formula, and the sandwich argument are all standard and well-presented. As an exposition of a known result, it's good.

## Why it isn't a research paper

**The result isn't new.** This is a direct consequence of the 1936 Davenport-Erdős theorem. The characterization `d(M_A) = 1 ⟺ sup_F d(M_F) = 1` is essentially folklore in the sets-of-multiples literature — Hall's *Sets of Multiples* (Cambridge, 1996) and Tenenbaum's *Introduction to Analytic and Probabilistic Number Theory* both contain this material. Erdős Problem #691 itself is asking about a known equivalence; the "problem" is finding a clean condition, and D-E essentially provides it.

So a research journal would reject this as "not new" regardless of presentation quality.

## Where it would be appropriate

- **erdosproblems.com itself**, as a writeup of the answer to problem #691. This is probably the natural home and the writing is at the right level.
- **An expository note on arXiv** (math.NT) framed as "a self-contained derivation of the density-1 characterization for sets of multiples." Reasonable but borderline — referees of expository pieces want either pedagogical novelty or a meaningfully shorter/cleaner argument than what's in Hall.
- **A textbook exercise solution or course notes.**
- **A blog post or Mathematics Stack Exchange answer.**

## What would need to change for arXiv-quality exposition

1. **Citations.** Hall's *Sets of Multiples* is the standard modern reference and must be cited. Tenenbaum III.5 likewise. The reader should know where to find the full D-E theorem and its modern treatment.
2. **Attribution care.** State explicitly that the result is a consequence of D-E, not a new theorem. Frame as "we give a self-contained proof of..." rather than presenting it as a discovery.
3. **The D-E black-box step** should either include a sketch of why `δ(M_A) = sup_F d(M_F)` (the few-paragraph Dirichlet series argument), or cite the precise location in Hall/Tenenbaum where this exact form is stated. Right now it's cited as "Davenport-Erdős 1936" but the form used is closer to Hall's Theorem 0.2 or similar.
4. **Tighten the Dirichlet/logarithmic density terminology** as the (third) critic correctly noted — just a small phrasing fix.
5. **Drop the redundant Step 4 inequality** (the author already removed (3)/(4) duplication, but a once-over for similar small redundancies would help).

## Honest assessment

As a careful answer to "what is the necessary and sufficient condition for `d(M_A) = 1`?" posted to a problem website, this is good and serves its purpose. As original research, no — there's no new theorem here, just a clean repackaging of D-E. The proof's main value is pedagogical: it shows a reader exactly which part is elementary and which part needs the deep theorem. That's worth something, but it's exposition, not research.

If the goal is publication on erdosproblems.com or as informal notes, it's ready (modulo the small fixes above). If the goal is a journal, the result needs to be either substantively new or substantively better-presented than Hall, and it's neither.

---

## Human

So in short: this proves `Erdos 691: Given A\subseteq \mathbb{N} let M_A=\{ n \geq 1 : a\mid n\textrm{ for some }a\in A\} be the set of multiples of A. Find a necessary and sufficient condition on A for M_A to have density 1.`, but it doesn't generate any new breakthrough result?

---

## Assistant

Yes, exactly.

The proof correctly answers Erdős #691 by exhibiting a necessary and sufficient condition (`sup_F d(M_F) = 1`, or equivalently the inclusion-exclusion form over the primitive core). So in the narrow sense of "does this solve the problem as stated?" — yes.

But the condition itself, and its proof, are essentially a restatement of what Davenport-Erdős already proved in 1936. The argument is: D-E gives `δ(M_A) = sup_F d(M_F)` and `δ(M_A) = d̲(M_A)`; from there the density-1 characterization is a few lines. So no new mathematics — just a clean packaging of a known theorem to answer the specific question Erdős posed.

Whether Erdős #691 *has* a more interesting answer than this is a separate question. It's possible the problem is on the list precisely because Erdős wanted a condition that's checkable in practice (this one isn't, really — computing `sup_F d(M_F)` is as hard as the original question for most `A`), and the "real" open problem is finding a more tractable criterion. If so, this proof answers the literal question while sidestepping the spirit of it.

---

## Human

_[empty message]_

---

## Assistant

# Review of the LaTeX manuscript

This is a clean, well-organized expository note. As an arXiv-quality writeup of the answer to Erdős #691, it is essentially ready. A few comments, mostly minor.

## What works well

- The abstract correctly frames this as exposition, not a new theorem.
- The introduction explicitly says the result follows from D-E and frames the contribution as "clean, self-contained statement and proof." This is the honest framing and saves it from any "is this new?" objection.
- Section 2 (Notation and auxiliary results) packages the prerequisites cleanly. Stating Theorem 2.4 (D-E) in exactly the form used downstream is good practice — it makes the deduction in Section 3 a one-liner.
- Section 3 is appropriately short. With D-E quoted in the right form, the proof is genuinely a few lines, and the manuscript doesn't pad.
- Citations are appropriate: Davenport-Erdős 1936 (primary), Hall (modern reference), Tenenbaum (general analytic NT). Erdős 1989 problem list is the right pointer for the problem itself.

## Issues to address before posting

**1. Theorem 2.4 (Davenport-Erdős) needs a more careful citation.**

You state three facts and attribute them all to D-E 1936. The 1936 paper proves `d̲(M_A) = δ(M_A)` (and existence of `δ`). The form `δ(M_A) = sup_F d(M_F)` is a corollary, but a reader checking the 1936 paper won't find it stated this way. The post-theorem paragraph addresses this, but the wording is slightly off:

> "The original paper proves that the lower density of `M_A` equals the logarithmic density, which in turn equals the limit of the densities of any such chain `M_{F_k}`"

The second half ("which in turn equals the limit...") is *not* in the 1936 paper as such. You should either:
- Cite Hall \cite{Hall}, Theorem 0.2 (or wherever) for the form (ii), in addition to D-E for (i) and (iii); or
- Add a short proof of (ii) from (i) and (iii), which is straightforward (`d̲(M_{F_k}) ≤ d̲(M_A) = δ(M_A)`, and the reverse via the Dirichlet series monotone limit).

The cleanest fix is probably: cite D-E for (i) and (iii), then add one sentence: "Part (ii) follows from (i) and (iii) together with the monotone convergence of the Dirichlet series for `M_{F_k} ↑ M_A`; see Hall \cite[Ch. 0]{Hall}."

**2. The `Ddelta` macro is defined but never used.** Just `\delta` is used throughout. Either remove the macro or use it consistently.

**3. The "logarithmic density via Abel summation" parenthetical in Section 2.1.** This is fine but you never actually use logarithmic density anywhere — only Dirichlet density. You can drop the comparison entirely or move it to a footnote. As written it raises a topic and doesn't return to it.

**4. Theorem 2.4 statement: "increasing sequence of finite subsets ... whose union is `A`."** Should specify `A` countable (it is, automatically, since `A ⊆ ℕ`, so this is fine — but a careful referee might ask). Trivial.

**5. The Erdős citation \cite{Erdos}.** The problem you're answering — "find a necessary and sufficient condition for `M_A` to have density 1" — is from the erdosproblems.com list (problem #691). The cited 1989 *Number theory, Madras* lecture notes contain many Erdős problems but I'm not sure this exact formulation is there. If the actual source you're answering is the erdosproblems.com webpage, cite that:

```
\bibitem{ErdosProblems}
T.~Bloom (ed.), \textit{Erd\H{o}s Problems}, Problem 691,
\url{https://www.erdosproblems.com/691}.
```

The Madras lectures may or may not contain this specific problem; check before citing.

**6. Title.** "A density-one criterion for sets of multiples" is fine but could be slightly more informative: "A density-one criterion for sets of multiples (after Davenport-Erdős)" makes the expository nature visible from the title and inoculates against "is this new?" reactions. Optional.

**7. No author.** You'll need to add one before posting to arXiv.

## Smaller polish

- Section 2.1: "this is a standard Tauberian fact, see~\cite{Tenenbaum}" — give a chapter/section reference, not just the book.
- Section 2.3: Define "primitive core" as `A_0 = {a ∈ A : no proper divisor of a lies in A}` — the verbal description "deleting all elements that are multiples of a smaller element" is fine but the formula is one line and clearer.
- The remark in Section 4 that `δ(M_A) = sup_F d(M_F) = d̲(M_A)` for *any* `A` is the most useful takeaway and could be flagged as a Corollary rather than buried in concluding remarks. Stating it as `\begin{corollary}` would make it findable.

## Verdict

For arXiv as an expository note in math.NT — yes, with the fixes above (especially #1 and #5). Length is appropriate (a 4-5 page note, not padded). The honest framing in the introduction is exactly right.

For a journal — still no, for the reasons in the previous review. No new theorem. But the *Mathematics Magazine* / *American Mathematical Monthly* / *Expositiones Mathematicae* tier of expository journals could conceivably take it if the writing were polished further and the historical context were expanded (e.g., a section on why Besicovitch's example shows you can't just say "density exists for primitive sets," which is a common misconception worth correcting publicly).

As a writeup posted to erdosproblems.com #691: ready now, modulo the Theorem 2.4 attribution fix.

---

## Human

_[empty message]_

---

## Assistant

# Final review of the manuscript

This revision addresses the previous comments cleanly. The structure is now correct and the attribution is honest. A few residual issues, ranging from substantive to cosmetic.

## One real issue

**The justification of (3) — the reverse inequality `δ(M_A) ≥ sup_k d(M_{F_k})` — still hand-waves.**

You write:

> The reverse inequality follows from the monotone convergence of the Dirichlet series `(σ−1)Σ_{n∈M_{F_k}} n^{−σ}` to that of `M_A` as `k → ∞` (see [Hall, Ch. 0] for details).

Two problems:

(a) Pointing to "Hall, Ch. 0" without a more specific reference is weak. Hall's Ch. 0 is short but contains several theorems; the reader should be told which.

(b) More importantly, the argument as stated is incomplete. Monotone convergence at fixed `σ` gives

$$g(\sigma) = \lim_k g_k(\sigma) \quad \text{for each } \sigma > 1.$$

To get `δ(M_A) ≥ sup_k d(M_{F_k})`, you need to take `σ → 1+`. From `g(σ) ≥ g_k(σ)` and `lim_{σ→1+} g(σ) = δ(M_A)` (which exists by D-E (i)) and `lim_{σ→1+} g_k(σ) = d(M_{F_k})` (finite case), you get `δ(M_A) ≥ d(M_{F_k})` for each `k`, hence `δ(M_A) ≥ sup_k d(M_{F_k})`. This is the easy direction and is just monotonicity of limits when both exist. It does not require Hall; it's two lines.

So the manuscript is invoking a reference for something that's actually elementary. Either:
- Replace the parenthetical with the explicit two-line argument; or
- Keep the reference but specify the exact Hall theorem (e.g., "Hall, Ch. 0, Lemma 0.1" or wherever the relevant statement lives — I don't have a copy at hand to verify).

The first option is cleaner and shorter. I'd recommend it.

The interesting thing is: this `≤` direction in (3) is the *easy* one. The hard direction (`δ(M_A) ≤ sup_k d(M_{F_k})`) is the one already handled by the line `d(M_{F_k}) = d̲(M_{F_k}) ≤ d̲(M_A) = δ(M_A)`. So the easy direction is being treated as if it required Hall, while the hard direction is dispatched cleanly. The roles are swapped in the writeup.

Wait — let me re-read. You write:

> Since `M_{F_k} ⊆ M_A`, we have `d(M_{F_k}) = d̲(M_{F_k}) ≤ d̲(M_A) = δ(M_A)`; hence `sup_k d(M_{F_k}) ≤ δ(M_A)`.

That gives `sup ≤ δ`. Then:

> The reverse inequality follows from the monotone convergence of the Dirichlet series ...

The "reverse inequality" is `δ ≤ sup`. This *is* the hard direction, and it does need real work — you can't get it from `g ≥ g_k` pointwise plus monotonicity of limits. You need that the *Dirichlet density* of `M_A` is bounded above by the limit of Dirichlet densities of the `M_{F_k}`, which is precisely a `lim sup_k δ(M_{F_k}) ≥ δ(M_A)` claim. That requires `(σ−1)Σ_{n∈M_A} n^{−σ}` to be approximable by `(σ−1)Σ_{n∈M_{F_k}} n^{−σ}` uniformly near `σ = 1`, which is Hall-level content.

So my earlier characterization was wrong; the manuscript's attribution is correct in direction but underspecified in citation.

**Concrete fix:** Replace "see [Hall, Ch. 0] for details" with the specific theorem. Hall *Sets of Multiples*, Theorem 0.2 (or the equivalent) states this. Without a copy in front of me I can't give the exact number, but you should verify and cite precisely. If you don't have access to Hall, Tenenbaum III.5 (Theorem 5.1 and surrounding) covers the same material.

## Smaller issues

**1. Theorem 2.4 statement.** You list (i) and (ii) as the D-E content. As I noted previously, only (i) and `δ(M_A) = d̲(M_A)` (which you label (ii)) are in D-E 1936 directly; the form of (ii) presented is correct but worth noting that "this equality is the substantive part of D-E." The current statement is fine.

**2. The equation label `\eqref{eq:sup}`** is referenced but the surrounding paragraph mixes the proof of (eq:sup) with its statement. Consider promoting (eq:sup) to a labeled lemma, since it's used twice (once in necessity, once in Corollary 4.1) and is the actual workhorse:

```latex
\begin{lemma}\label{lem:sup}
For any $A \subseteq \N$, $\delta(M_A) = \sup_{F \subseteq A,\; F \text{ finite}} d(M_F)$.
\end{lemma}
```

Then the proof of Theorem 1.1 cites Lemma 2.5, and Corollary 4.1 just stitches it with D-E (ii).

**3. `\newtheorem{lemma}` is not declared** but isn't currently used. If you adopt the suggestion above, declare it.

**4. `\newtheorem{definition}` is declared but never used.** Remove or use.

**5. Abstract.** Reads well. Final sentence — "we present a self-contained exposition" — could be slightly stronger: "we present a self-contained exposition that isolates the elementary content from the analytic input." Optional.

**6. Title.** Still neutral. "after Davenport-Erdős" subtitle remains an option but isn't necessary given the abstract is honest.

**7. No author.** Reminder.

## Verdict

For posting on erdosproblems.com #691 or as an arXiv expository note: **ready, after the citation fix to "Hall, Ch. 0".** That's the only substantive fix needed. Everything else is polish.

The manuscript is now honest about what it does (clean exposition of a D-E corollary), correctly structured (elementary sufficiency, D-E for necessity), and appropriately cited. The Corollary at the end is the right takeaway and is now appropriately flagged. Good convergence over the iterations.
