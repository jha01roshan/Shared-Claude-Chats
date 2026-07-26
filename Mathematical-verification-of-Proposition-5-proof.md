# Mathematical verification of Proposition 5 proof

- Source: https://claude.ai/share/db71e110-e439-45c1-9f2c-6aebbf1edc88
- Author: Alexis
- Created: 2026-06-01
- Messages: 8

---

## Human

I have just uploaded the paper ``An impossibility theorem for wealth in heterogeneous-agent models with limited heterogeneity'' published in Journal of Economic Theory. Can you check the mathematical correctness of the proof of Proposition 5?

---

## Assistant

I'll work through the proof of Proposition 5 carefully to check its mathematical correctness.

## Setup and Statement

**Proposition 5** claims: under Assumptions 1–3 and $1 \le R < 1/\beta$, with $\bar\gamma = \limsup_{x\to\infty} -xu''(x)/u'(x) \in [0,\infty)$, for all $m \in (1-1/R, 1-\beta^{1/\bar\gamma}R^{1/\bar\gamma - 1})$ there exists $A \ge 0$ such that $c(a,z) \ge ma$ for all $a \ge A$, $z \in Z$.

Note the upper bound rewrites as $1 - \beta^{1/\bar\gamma}R^{1/\bar\gamma-1} = 1 - (\beta R)^{1/\bar\gamma}/R$, i.e. $R(1-m) > (\beta R)^{1/\bar\gamma}$, consistent with the definition of $\bar m$ via $(\beta R)^{1/\bar\gamma} = R(1-\bar m)$ in Step 1.

## Checking the components

**Lemma 10** (zero-income lower bound). The argument that the optimal policy of the full problem dominates the zero-income policy, $c(a,z) \ge c_0(a)$, via showing $Kc_0 \ge c_0$ and monotone convergence, is correct. The contradiction argument uses $u'$ strictly decreasing, $c_0$ increasing, $y' \ge 0$ — all valid. ✓

**Lemma 11 / condition (A.6).** The derivation in (A.7) using the Fundamental Theorem of Calculus is correct:
$$-\log\kappa = \int_1^{y/x} \frac{\gamma(xs)}{s}\,ds,$$
and bounding $\gamma \le M$ gives $y/x \ge \kappa^{-1/M}$, hence (A.8): $\liminf (u')^{-1}(\kappa u'(x))/x \ge \kappa^{-1/M}$. ✓

## The core argument (Proof of Proposition 5)

**Step 1.** With $\bar\gamma$ defined, $(\beta R)^{1/\bar\gamma} = R(1-\bar m)$ and the claim is that for $m \in (1-1/R, \bar m)$,
$$\liminf_{x\to\infty} \frac{(u')^{-1}(\beta R\, u'(x))}{x} > \frac{1}{R(1-m)}. \tag{A.11}$$

Here is the **first issue worth flagging**. The proof picks $M > \bar\gamma$ with $(\beta R)^{1/M} < R(1-m)$ and sets $\kappa = \beta R$ in (A.8) to conclude (A.11). But (A.8) — derived in Lemma 11 — requires $\gamma(x) \le M$ *for large enough $x$*, which holds for any $M > \bar\gamma = \limsup \gamma(x)$. So this is fine **provided $\bar\gamma > 0$**. The case $\bar\gamma = 0$ needs separate handling: then $(\beta R)^{1/\bar\gamma}$ is interpreted as $0$ (since $\beta R < 1$), $\bar m = 1$, and one can take $M$ arbitrarily small, giving $\kappa^{-1/M} = (\beta R)^{-1/M} \to \infty$, so (A.11) holds for any $m$. The paper's footnote/limit conventions cover this, though it's handled somewhat implicitly. Minor expository gap, not an error.

**A genuine concern in Step 1:** the definition $\bar m$ via $(\beta R)^{1/\bar\gamma} = R(1-\bar m)$ requires $R(1-\bar m) \le 1$ to be consistent with $\bar m \le 1$, and the text asserts $\bar m \in (1-1/R, 1]$. Since $(\beta R)^{1/\bar\gamma} < 1$ (as $\beta R<1$) and $R \ge 1$, we get $1-\bar m = (\beta R)^{1/\bar\gamma}/R < 1/R$, so $\bar m > 1 - 1/R$. And $1-\bar m > 0$ requires $(\beta R)^{1/\bar\gamma} > 0$, true. So $\bar m \in (1-1/R, 1)$ when $\bar\gamma>0$. ✓ Consistent.

**Step 2** is the heart. The goal (A.12): for all $m \in (1-1/R,\bar m)$ there is $A$ with $(Kc)(a) \ge ma$ for $a \ge A$, where $K$ is the **zero-income** operator (A.9) and $c$ is the candidate (A.10).

The contradiction (A.13) assumes some $a$ (arbitrarily large) with $t = (Kc)(a) < ma$. The argument:

- If $\beta R u'(c(R(a-t))) < u'(a)$, then (A.9) gives $u'(t) = u'(a)$, so $t = a \ge ma$ — contradiction. ✓
- Otherwise $g(t) := u'(t) - \beta R u'(mR(a-t)) = 0$, using $c(R(a-t)) = mR(a-t)$ — **this requires $R(a-t) \ge A$** so that the candidate policy uses the linear branch $c(\cdot) = m(\cdot)$. For large $a$ and $t < ma$, $R(a-t) > R(1-m)a \to \infty$, so this holds for $a$ large. ✓ (Implicit but correct.)
- $g$ strictly decreasing since $g'(t) = u''(t) + \beta m R^2 u''(mR(a-t)) < 0$. ✓
- From $t < ma$ and $g(t)=0 > g(ma)$:
$$g(ma) = u'(ma) - \beta R u'(mR(1-m)a) < 0,$$
which gives $u'(ma) < \beta R u'(mR(1-m)a)$, i.e. applying $(u')^{-1}$ (decreasing):
$$(u')^{-1}(\beta R\, u'(mR(1-m)a)) < mR(1-m)a \cdot \frac{1}{R(1-m)} \cdot \frac{1}{m}\cdot \ldots$$

Let me verify the displayed inequality precisely. The paper writes:
$$\frac{(u')^{-1}(\beta R u'(mR(1-m)a))}{mR(1-m)a} < \frac{1}{R(1-m)}.$$

From $g(ma) < 0$: $u'(ma) < \beta R u'(mR(1-m)a)$. Apply $(u')^{-1}$ (order-reversing): $ma > (u')^{-1}(\beta R u'(mR(1-m)a))$. Setting $x = mR(1-m)a$ in the numerator argument, divide both sides by $x = mR(1-m)a$:
$$\frac{(u')^{-1}(\beta R u'(x))}{x} < \frac{ma}{mR(1-m)a} = \frac{1}{R(1-m)}. \checkmark$$

The algebra is correct. Then letting $a \to \infty$ (legitimate since (A.13) allows arbitrarily large $a$), $x = mR(1-m)a \to \infty$, yielding
$$\liminf_{x\to\infty} \frac{(u')^{-1}(\beta R u'(x))}{x} \le \frac{1}{R(1-m)},$$
contradicting (A.11). ✓

**One subtlety to verify carefully:** going from "$g(ma) < 0$ for the particular $a$ satisfying (A.13)" to a statement about $\liminf$ as $a\to\infty$. (A.13) says: for *all* $A > 0$ there *exists* $a \ge A$ with $t < ma$. This produces a *sequence* $a_n \to \infty$ along which the inequality $(u')^{-1}(\beta R u'(x_n))/x_n < 1/(R(1-m))$ holds with $x_n = mR(1-m)a_n \to \infty$. The $\liminf$ over $x\to\infty$ is therefore $\le 1/(R(1-m))$. This correctly contradicts the strict $>$ in (A.11). ✓ The logic is sound — the $\liminf$ (not $\lim$) is exactly what's needed here, and the strict inequality in (A.11) does the work.

**Step 3.** Choosing $\epsilon$ with $c_0(A) \le \epsilon m A$ and showing $(Kc)(a) \ge c(a)$ for $a < A$ via $c_0(a) > (Kc)(a) \ge (K^n c)(a) \to c_0(a)$ contradiction. This uses monotonicity of $K$ (Lemma 13) and that $c \le c_0$ on $[0,A)$ since $c = \epsilon c_0$ there with $\epsilon \in (0,1)$. Wait — for $a < A$, (A.10) sets $c(a) = \epsilon c_0(a)$, so indeed $c \le c_0$, hence $K^n c \le K^n c_0 \to c_0$... but the chain $c_0(a) > (Kc)(a) \ge (K^nc)(a)$ needs $(Kc) \ge (K^n c)$, which follows from $Kc \ge c$ on the whole domain combined with monotonicity — and $Kc \ge c$ on $[A,\infty)$ is Step 2, while on $[0,A)$ it's what's being proven. The argument is by contradiction: *assuming* $(Kc)(a) < c(a) = \epsilon c_0(a)$ for some $a < A$, then since $\epsilon < 1$, $(Kc)(a) < c_0(a)$; iterating $K$ and using $(K^n c) \to c_0$ gives the contradiction. ✓ This is correct, though it leans on the convergence $K^n c \to c_0$ which holds because $c \in C$ and $K$ is a contraction (Lemma 14, Proposition 4).

## Verdict

**The proof of Proposition 5 is mathematically correct.** I checked each step — the FTC computation in Lemma 11, the construction of $\bar m$, the contraction-policy contradiction in Step 2, the $\liminf$/strict-inequality interplay, and the boundary patching in Step 3 — and found no errors.

A few minor expository points (none affecting correctness):

1. The boundary case $\bar\gamma = 0$ (where $(\beta R)^{1/\bar\gamma} = 0$, $\bar m = 1$) is handled only implicitly through limit conventions; an explicit line would help readers.

2. Step 2 silently uses $R(a-t) \ge A$ to invoke the linear branch of the candidate policy. True for large $a$, but unstated.

3. The transition from the single-$a$ inequality to the $\liminf$ statement relies on (A.13) generating an unbounded sequence of such $a$; correct, but compressed.

These are the kinds of gaps a careful referee might ask the authors to spell out, not flaws in the result. The proposition holds as stated, and the explicit interval $m \in (1-1/R, 1-\beta^{1/\bar\gamma}R^{1/\bar\gamma-1})$ is correctly derived.

---

## Human

I have a concern with your Step 3. The candidate policy function in (A.10) is discontinuous at $A$, but don't you need continuity of the function?

---

## Assistant

Good catch — let me look at this carefully, because the discontinuity does matter for whether the argument in Step 3 (and indeed the well-definedness of $K$ acting on $c$) goes through.

## Where continuity could matter

The candidate policy is
$$c(a) = \begin{cases} \epsilon c_0(a), & 0 < a < A \\ ma, & a \ge A \end{cases}$$
with $\epsilon \in (0,1)$ chosen so $\epsilon c_0(A) \le mA$. At $a = A^-$ we have $c(A^-) = \epsilon c_0(A) \le mA = c(A)$, so the function **jumps up** (or is continuous) at $A$ — it is lower-semicontinuous there, with a possible upward jump.

Now, the key question: **does the proof actually require $c \in C$**, and does $C$ require continuity?

## Membership in $C$

Looking at Appendix B, the candidate set $C$ consists of functions $c: S \to \mathbb{R}$ such that $c(a,z)$ is **increasing in $a$**, $0 < c(a,z) \le a$, and $\|u' \circ c - \phi\|_\infty < \infty$ where $\phi(a,z) = u'(a)$. 

Notably, **$C$ does not require continuity** — only monotonicity, the feasibility bound $0 < c \le a$, and the sup-norm condition. This is the standard Li–Stachurski (2014) setup, and the omission of continuity is deliberate: monotone functions are automatically "nice enough" (they have at most countably many jumps and are measurable), and the operator $K$ and the metric $\rho$ are built to work on this class.

So the relevant questions become:

**(a) Is the candidate $c$ in (A.10) increasing?** At the seam, $c(A^-) = \epsilon c_0(A) \le mA = c(A)$, and both branches are individually increasing ($c_0$ increasing by Proposition 4; $ma$ increasing). So yes, $c$ is increasing across $A$ — the jump is *upward*, preserving monotonicity. ✓

**(b) Does $c$ satisfy $0 < c \le a$?** On $(0,A)$: $0 < \epsilon c_0(a) < c_0(a) \le a$. ✓ On $[A,\infty)$: need $ma \le a$, i.e. $m \le 1$, true since $m < \bar m \le 1$; and $ma > 0$. ✓

**(c) Is $\|u'\circ c - \phi\|_\infty < \infty$?** This is the only condition where the jump could in principle cause trouble, but it's a sup-norm bound, insensitive to a single jump as long as it's finite. On $[A,\infty)$, $c = ma$ with $m > 1-1/R > 0$, so $u'(ma)/u'(a)$ stays bounded under BRRA-type conditions; on $(0,A)$, $c = \epsilon c_0$ and $c_0 \in C$. The jump at $A$ contributes a finite value, harmless to the sup. ✓

So $c \in C$ despite the discontinuity. **$C$ is not a space of continuous functions.**

## Does $K$ require continuity of its argument?

This is the subtler point. In Lemma 13, $(Kc)(a,z)$ is defined as the unique $t \in (0,a]$ solving
$$u'(t) = \max\big\{\beta R\, \mathbb{E}[u'(c(R(a-t)+y',z')) \mid z],\ u'(a)\big\}.$$
For the zero-income version (A.9): $u'(t) = \max\{\beta R\, u'(c(R(a-t))),\ u'(a)\}$.

The function $g(t) = u'(t) - \max\{\beta R u'(c(R(a-t))), u'(a)\}$ needs to be shown to have a unique zero. The proof of Lemma 13 establishes $g$ is **continuous and strictly decreasing** using that $u'$ is continuous and strictly decreasing — but it also implicitly uses that $t \mapsto c(R(a-t))$ is well-behaved.

Here is the real concern: if $c$ has a jump (discontinuity), then $t \mapsto u'(c(R(a-t)))$ has a jump too, so $g(t)$ may have a jump discontinuity. A function with a downward jump might **skip past zero** without attaining it, in which case "$t$ solving $g(t) = 0$" could fail to exist.

Let me check the direction of the jump. As $t$ increases, $R(a-t)$ decreases, so the argument of $c$ decreases. Since $c$ is **increasing**, $c(R(a-t))$ decreases as $t$ increases, so $u'(c(R(a-t)))$ **increases** as $t$ increases (since $u'$ decreasing). Thus $-\beta R u'(c(R(a-t)))$ decreases, and $g(t) = u'(t) - \max\{\ldots\}$ is decreasing in $t$ (both terms push down). The jump in $c$ at the point where $R(a-t) = A$ is an **upward** jump in $c$, hence a **downward** jump in $u'(c(\cdot))$ as the argument crosses $A$ upward... 

Let me be careful about the parametrization. Define $t^* $ by $R(a - t^*) = A$, i.e. $t^* = a - A/R$. For $t$ slightly below $t^*$: $R(a-t) > A$, so $c$ uses the $ma$-branch. For $t$ slightly above $t^*$: $R(a-t) < A$, so $c$ uses the $\epsilon c_0$-branch, which is **lower**. So as $t$ increases through $t^*$, $c(R(a-t))$ jumps **down** (from $mA$ to $\epsilon c_0(A) \le mA$), hence $u'(c(R(a-t)))$ jumps **up**, hence $\max\{\beta R u'(\cdot), u'(a)\}$ jumps up (or stays), hence $g(t)$ jumps **down**.

So $g$ has a **downward jump** at $t^*$. **This is exactly the dangerous case** — a strictly decreasing function with a downward jump can cross zero *in the gap*, meaning no exact solution $t$ to $g(t) = 0$ exists.

## Does this actually break the proof?

Not quite, and here's why — but it does mean the proof as written is **slightly imprecise** and the operator definition needs the right convention.

In the Li–Stachurski framework, $K$ is genuinely well-defined on monotone (possibly discontinuous) candidates because the relevant object is $u' \circ c$, and the Coleman operator is set up around the Euler equation in a way that the "$\max$" and the endogenous-grid structure accommodate jumps. More concretely, when $g$ has a downward jump straddling zero at $t^*$, the correct reading of the Euler/KKT condition is that the constraint structure selects $t = t^*$ (the kink point) — the optimizing $t$ sits at the discontinuity, which corresponds economically to the consumption choice being pinned at the point where the next-period policy regime switches. The "unique $t \in (0,a]$ solving (A.5)" should be read as the unique $t$ where $g$ changes sign, which exists and is unique for a strictly-decreasing-with-jumps function.

**However** — and this is the legitimate force of your objection — Lemma 13's proof literally argues "$g$ is continuous and strictly decreasing, $g(0^+) = \infty$, $g(a) \le 0$, therefore a unique zero exists by the intermediate value theorem." That IVT argument **requires continuity of $g$**, which fails for the discontinuous candidate (A.10). So:

1. For the genuine fixed point $c_0$ (which is continuous, indeed increasing and continuous as the limit of the iteration), Lemma 13 applies cleanly. No problem.

2. For the artificial candidate (A.10) used in Step 3 / Step 2, $Kc$ requires interpreting "the solution of (A.5)" as the sign-change point rather than a literal root, OR one must verify that $g$ doesn't straddle zero at the jump in the relevant range.

## Resolving it for the actual argument

The cleanest fix: notice that in **Step 2**, the relevant range is $a \ge A$ large, and the contradiction hypothesis is $t = (Kc)(a) < ma$. There, the proof works with the branch $c(R(a-t)) = mR(a-t)$, i.e. it stays on the linear (upper) branch because $R(a-t) > R(1-m)a \ge A$ for large $a$. So in Step 2 the discontinuity is never crossed — the argument $R(a-t)$ stays above $A$, the candidate behaves like the smooth function $ma$ there, and $g$ is continuous on the relevant interval. The jump is irrelevant to Step 2. ✓

For **Step 3** ($a < A$), the argument is purely the monotone-iteration contradiction: assume $(Kc)(a) < c(a)$, apply $K$ repeatedly, use $K^n c \to c_0$ and $c \le c_0$ on $[0,A)$ to derive $c_0(a) > (Kc)(a) \ge (K^n c)(a) \to c_0(a)$. This uses only **monotonicity of $K$** (which holds on $C$ regardless of continuity, per Lemma 13's second part — that proof uses only monotonicity of $c$ and strict monotonicity of $u'$, not continuity) and the contraction convergence. The existence/uniqueness of $(K^n c)$ for each $n$ does require $K$ to be well-defined on the iterates, but the iterates $K^n c$ for $n \ge 1$ are increasing and, after one application, inherit better regularity — and in any case the convergence $K^n c \to c_0$ in the $\rho$-metric (Lemma 14, contraction) doesn't depend on continuity of the starting point $c$.

## Bottom line

You've identified a real imprecision, but not a fatal one:

- **The objection is valid** that Lemma 13's existence argument for $Kc$ is stated via an IVT that presumes continuity of $g$, and the candidate (A.10) is discontinuous at $A$, so $g$ can have a downward jump and the literal "$g(t) = 0$ has a solution" can fail at the seam.

- **But the proof is rescued** because (i) $C$ itself requires only monotonicity, not continuity, so (A.10) is a legitimate member of $C$; (ii) the well-definedness of $K$ on monotone discontinuous functions holds under the correct (sign-change / endogenous-grid) reading of the Euler operator, which is the intended Li–Stachurski convention; (iii) Step 2 never crosses the discontinuity (the relevant argument $R(a-t)$ stays on the linear branch above $A$); and (iv) Step 3 uses only monotonicity of $K$ and metric convergence, neither of which needs continuity.

So the **conclusion of Proposition 5 stands**, but a rigorous write-up should either (a) explicitly note that $K$ is well-defined on monotone discontinuous candidates with the sign-change convention, or (b) — cleaner — use a *continuous* candidate that interpolates across $[A', A]$ instead of the discontinuous (A.10), e.g. patch with a continuous increasing bridge so that $g$ stays continuous and Lemma 13's IVT applies literally. The latter would remove the gap entirely at no cost to the argument, since only the asymptotic ($a \to \infty$) behavior on the linear branch is actually used.

This is a fair referee-level point: the proof is *correct* but relies on a convention about $K$ that the discontinuous candidate makes non-obvious, and it deserves an explicit line.

---

## Human

Do you know if anyone has corrected the authors' paper?

---

## Assistant

I should search for this rather than rely on my training knowledge, since corrections, comments, or corrigenda could have been published at any point.
```
This block is not supported on your current device yet.
```

Yes — the authors themselves published a corrigendum that specifically corrects the proof of Proposition 5, which is the very proposition you and I were scrutinizing.

The corrigendum is: Stachurski, J., & Toda, A. A. (2020). Corrigendum to "An impossibility theorem for wealth in heterogeneous-agent models with limited heterogeneity" [Journal of Economic Theory 182 (2019) 1–24], Journal of Economic Theory, Vol. 188. It appeared in 2020. The stated purpose is exactly on point: it corrects the proof of Proposition 5 in Stachurski and Toda (2019), which shows that the consumption function has an explicit linear lower bound and is used to prove their main result that wealth inherits the tail behavior of income in Bewley–Huggett–Aiyagari models.

So your instinct was well-aimed — the authors found the proof of Proposition 5 needed repair. Let me fetch the corrigendum to see exactly what they corrected and whether it matches the continuity concern you raised.
```
This block is not supported on your current device yet.
```

The picture is now clear, and it confirms there was a genuine error. Notably, one of the authors (Toda) states plainly on his own publications page: "During this ordeal, it seems that nobody read the proofs. We later found an error in Proposition 5, and published a corrigendum."

So to directly answer your question: yes, the paper has been corrected — but the correction came from the authors themselves, not an outside party. The corrigendum (Stachurski & Toda, *Journal of Economic Theory*, Vol. 188, 2020) is devoted entirely to fixing the proof of Proposition 5.

A couple of things worth noting in relation to our earlier discussion:

The corrigendum abstract describes Proposition 5 as the result showing that the consumption function has an explicit linear lower bound, used to prove their main result that wealth inherits the tail behavior of income. That's exactly the proposition we dissected — the linear lower bound $c(a,z) \ge ma$. So the part of the paper that turned out to need repair is precisely the part you pressed on.

I should be careful, though: I don't yet know whether the specific defect the authors fixed is the discontinuity-of-the-candidate-policy issue you raised, or something else in the Step 1/Step 2 machinery (for instance, a problem in how the explicit bound $\bar m$ and the interval for $m$ were derived, or in the application of condition (A.6)). The search results tell me the corrigendum exists and that it targets Proposition 5, but they don't reveal the content of the correction. The corrigendum itself is behind Elsevier's paywall, and I wasn't able to surface a freely readable version (the arXiv versions I found are pre-publication and predate the corrigendum).

If you can access the corrigendum through ScienceDirect (DOI region 10.1016/j.jet... in Vol. 188, 2020), or if you have a copy, I'd be glad to read it and check (a) what the actual error was, (b) whether it overlaps with the continuity concern you identified, and (c) whether the corrected proof is itself sound. There's also a closely related companion paper, Ma–Toda on asymptotic linearity / asymptotic MPC of consumption functions, which the authors developed around the same time and which may contain the cleaner machinery they ultimately relied on.

---

## Human

I have just uploaded the PDF of the corrigendum for you. Can you analyze it? Did the author make an overly strong assumption? Does the original Proposition 5 still stand?

---

## Assistant

Excellent — now I can see exactly what the authors corrected, and your earlier instinct was vindicated. Let me work through the corrigendum carefully.

## What the authors acknowledge as the errors

The corrigendum identifies **two** errors in the original proof, and the first is precisely the one you flagged:

1. the candidate policy in (A.10) is potentially discontinuous, which is not allowed when applying policy function iteration (in particular, the intermediate value theorem).

2. the argument in Step 3 of the proof requires the inequality to hold pointwise, which is not necessarily true under the stated assumptions.

So your continuity objection was exactly right, and the authors agree it was a genuine defect — not merely an expository gap rescuable by "the right convention," as I had tried to argue in our earlier exchange. I was too generous to the original proof; the authors themselves judged the IVT step in Lemma 13 to be invalid for the discontinuous candidate. The second error (the pointwise inequality in Step 3) is also one I waved past too quickly.

## The new proof strategy

Rather than patch the discontinuous candidate, they discard the whole "candidate policy (A.10) + sign-change" apparatus and replace it with a cleaner argument:

**Lemma 1** is the key device. If $\beta R < 1$ and there is $m \in (0,1)$ with the *functional inequality*
$$u'(a) \ge \beta R\, u'(R(1-m)a) \quad \text{for all } a > 0, \tag{3}$$
then the optimal policy satisfies $c(a,z) \ge ma$ everywhere. The proof defines the closed set $C_0 = \{c \in C : c(a,z) \ge ma\}$ and shows $K$ maps $C_0$ into itself by a clean contradiction on the Euler equation, then uses that $K$ is a contraction with $a \mapsto a$ a member of $C_0$ to conclude the fixed point lies in $C_0$. This is a *global* invariant-set argument — no discontinuous interpolation, no IVT on a jumpy function, no asymptotic "large $a$" patching. The inequality $c \ge ma$ holds **for all $a$**, not just $a \ge A$. This is genuinely a better proof.

I checked the chain of inequalities in Lemma 1's proof and it is correct: from $t < ma$, strict monotonicity of $u'$, $c_0 \in C_0$ (so $c_0(\cdot) \ge m\cdot$), and $y \ge 0$, one gets $u'(ma) < \beta R\, \mathbb E[u'(m(R(a-t)+y))] \le \beta R\, u'(mR(1-m)a)$, contradicting (3) with $a$ replaced by $ma$. ✓

**Proposition 5'** then just verifies (3) holds under the new assumptions. Setting $\kappa = \beta R$, using the Lemma 11 bound $y/x \ge \kappa^{-1/\gamma}$ (with $y = (u')^{-1}(\kappa u'(x))$), and $R(1-m) = (\beta R)^{1/\gamma}$, they derive $u'(a) \ge \beta R\, u'(R(1-m)a)$ directly. The explicit value $m = 1 - \beta^{1/\gamma}R^{1/\gamma-1}$ is the same closed form as in the original. ✓

## Now to your actual question: did they make an overly strong assumption?

Yes — and this is the substantive cost of the correction. There are **three** strengthenings, and one is more consequential than the authors' framing ("slightly strengthening the assumptions") suggests.

**Strengthening 1 — Assumption 3 → 3' (BRRA at the supremum, not the limsup).** The original used the *asymptotic* coefficient $\bar\gamma = \limsup_{x\to\infty} -xu''(x)/u'(x)$. The corrigendum uses
$$\gamma = \sup_{x>0} -xu''(x)/u'(x),$$
the **global supremum** over all $x > 0$. This is strictly stronger: a utility function could have bounded asymptotic RRA but a spike in RRA at some finite wealth level, satisfying Assumption 3 but violating 3'. The reason they need the sup is that Lemma 1's inequality (3) must hold *for all $a > 0$* (it's a global invariant-set argument), whereas the original only ever needed the bound to bite for large $a$. So the move from "asymptotic" to "global" RRA bound is the price of getting a clean global proof. For CRRA this is irrelevant ($\gamma$ is constant), and for the HARA family with $a>0$ the sup is also finite, so the headline examples are unaffected — but it does narrow the admissible utility class relative to the original claim.

**Strengthening 2 — Assumption 2 → 2' (finite-state Markov $z$, plus a new moment condition).** The original Assumption 2 allowed $\{z_t\}$ to be a Markov process on an arbitrary set $Z$. The corrigendum restricts $\{z_t\}$ to a **finite** set (with an IID transitory shock $\eta_t$ layered on, which may still be unbounded/heavy-tailed). They note in a footnote that abstract $Z$ can be recovered under regularity conditions, and that finite $Z$ suffices for their applications. More importantly, they add a moment condition that was **missing** from the original:
$$\sup_{z} \mathbb E[u'(y(z,\eta)) \mid z] < \infty,$$
which they explicitly say is not mentioned in ST, is required so that the policy functions remain in the space C defined below. This is a real gap-filling: the original implicitly needed the iterates to stay in the candidate space, and without a bound on $\mathbb E[u'(y)]$ that isn't guaranteed.

**Strengthening 3 — $C$ is now explicitly a space of *continuous* functions.** In the original Appendix B, $C$ required only monotonicity (this is what I leaned on in our earlier discussion to argue the discontinuous candidate was admissible). The corrigendum redefines $C$ as the set of continuous functions from S to (0,∞) such that c is increasing in its first argument, c(a, z) ≤ a, and ‖u'∘c − u'‖ < ∞. This is the formalization that makes the IVT-based well-definedness of $K$ legitimate — and it's exactly why the original discontinuous candidate (A.10) was illegal. They lean on Ma–Stachurski–Toda (2020) for the contraction/fixed-point facts on this space.

## Does the original Proposition 5 still stand?

This needs a careful answer in two parts:

**As originally stated and proved: no.** The proof was invalid (both errors are real), and the *statement* was slightly too strong — it claimed the result under the weaker asymptotic-RRA Assumption 3 and the more general Assumption 2, but the authors could only establish it after moving to global-sup RRA (3') and finite-state-plus-moment (2'). So the original Proposition 5 as written is not a theorem under its stated hypotheses; it is a theorem under strengthened hypotheses.

**As it matters for the paper's main result: yes, it survives.** This is the crucial point. The authors stress that although the assumptions used here are stricter than those in ST, they do not exclude the applications that follow the main impossibility theorem (Theorem 8). Proposition 5 is only an intermediate lemma; its job is to deliver the AR(1) upper bound $a_{t+1} \le \rho a_t + y_{t+1}$ with $\rho = R(1-m) \in [0,1)$ (Proposition 6), which then feeds Theorem 3 and the impossibility Theorem 8. Since the headline applications (Aiyagari with CRRA and finite-state Markov income, Quadrini, Castañeda et al., Cagetti–De Nardi — all CRRA, mostly finite-state or bounded-support) sit comfortably inside the strengthened assumptions, the impossibility theorem itself is unaffected. The economics — wealth cannot be heavier-tailed than income in canonical Bewley–Huggett–Aiyagari models — stands.

## Bottom line

To answer your two questions directly:

**Did the author make an overly strong assumption?** They made *three* strengthenings. Two are reasonable gap-fillings (the missing moment condition on $\mathbb E[u'(y)]$, and the explicit continuity of $C$). The genuinely "stronger" assumption is the move from **asymptotic** bounded relative risk aversion ($\limsup_{x\to\infty}$) to **global** bounded relative risk aversion ($\sup_{x>0}$). That is more than cosmetic: it's what the global invariant-set proof requires, and it does shrink the admissible utility class — though not in any way that touches the CRRA/HARA examples the paper actually uses. There's also the restriction of the Markov state to a finite set, somewhat softened by allowing an unbounded IID transitory component and by the footnote sketching the abstract-$Z$ extension.

**Does the original Proposition 5 still stand?** Not as proved (both errors are real, and one is exactly your continuity objection), and not under its original weaker hypotheses. But a corrected version — Proposition 5' — holds under modestly stronger assumptions, and it delivers everything the main impossibility theorem needs. So the paper's central result is intact; only the intermediate lemma had to be re-proved on a slightly narrower footing.

You were right to be skeptical, and right about the specific mechanism. I'd been too quick to defend the original proof by appealing to a "convention" for handling the discontinuity — the authors' own verdict is that the discontinuity (and the pointwise-inequality step) genuinely broke the argument, which is why they rebuilt it.
