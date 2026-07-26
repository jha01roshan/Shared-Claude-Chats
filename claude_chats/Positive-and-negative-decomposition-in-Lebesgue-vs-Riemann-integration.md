# Positive and negative decomposition in Lebesgue vs Riemann integration

- Source: https://claude.ai/share/46cbe64d-035a-4c5c-83e7-941745545378
- Author: Terry
- Created: 2026-03-25
- Messages: 2

---

## Human

In Lebesgue integration theory (specifically the part concerning absolutely integrable integrals), analysts decompose a function f into its positive and negative parts. However, such an approach is not taken when studying the Riemann integral. Is it because this decomposition aligns with ideas in harmonic analysis or other fields of analysis?

---

## Assistant

This is a great question that touches on some deep foundational reasons. The decomposition $f = f^+ - f^-$, where $f^+ = \max(f,0)$ and $f^- = \max(-f, 0)$, is not primarily motivated by harmonic analysis. Rather, it is forced upon us by the **measure-theoretic and order-theoretic foundations** of Lebesgue integration itself. Let me explain carefully.

---

## Why the Riemann integral doesn't need it

The Riemann integral is defined via **uniform approximation by step functions** on intervals. The whole construction is essentially geometric and finitary: you partition a bounded interval, pick sample points, and take a limit. Because you're always working with bounded functions on bounded domains, the integral $\int_a^b f$ is automatically finite whenever $f$ is Riemann integrable. There is no risk of an "infinite minus infinite" catastrophe, so no decomposition is needed to keep things well-defined. The sign of $f$ is simply handled automatically by the signed areas in the Riemann sums.

---

## Why Lebesgue integration *must* use it

The issue is entirely about **how to extend the integral to unbounded functions and infinite measure spaces** while preserving a coherent notion of "absolute integrability." Several interlocking reasons force the decomposition:

### 1. Defining the integral of a non-negative function first
The Lebesgue integral is built in stages. One first defines $\int \varphi \, d\mu$ for **simple functions** $\varphi \geq 0$, then extends to all **measurable $f \geq 0$** via the monotone convergence theorem (taking a supremum over simple functions $\leq f$). This extension uses the lattice structure of $[0, \infty]$ crucially: you can take suprema freely because $+\infty$ is an allowed value and there is no subtraction ambiguity. The whole edifice of the monotone convergence theorem, Fatou's lemma, and the dominated convergence theorem rests on this non-negative foundation.

### 2. Avoiding the indeterminate form $\infty - \infty$
Once you have the integral for non-negative functions, you *must* split a general $f$ into $f^+$ and $f^-$ to define $\int f \, d\mu := \int f^+ \, d\mu - \int f^- \, d\mu$. If both $\int f^+ = \infty$ and $\int f^- = \infty$, the expression is undefined ($\infty - \infty$). The condition of **absolute integrability**, $\int |f| \, d\mu = \int f^+ \, d\mu + \int f^- \, d\mu < \infty$, is precisely the condition that rules this out. The Riemann integral has no analogous danger because everything is automatically finite.

### 3. Compatibility with the $L^1$ norm and the Banach space structure
The space $L^1(\mu)$ is defined to be the space of functions with $\int |f| \, d\mu < \infty$. This is a **norm**, and the resulting space is a **Banach space** — a complete normed vector space. The $f^+/f^-$ decomposition reflects the fact that $L^1$ is an **ordered Banach lattice**: it has both a vector space structure and a lattice order ($f \mapsto f^+$, $f \mapsto f^-$, $f \mapsto |f|$ are all natural operations). This Banach lattice structure is fundamental and has no real Riemann counterpart.

### 4. The Hahn decomposition / signed measures
The decomposition $f = f^+ - f^-$ at the level of functions corresponds exactly to the **Hahn decomposition theorem** for signed measures: any signed measure $\nu$ decomposes as $\nu = \nu^+ - \nu^-$ into two mutually singular positive measures (the Jordan decomposition). The condition $\int |f|\, d\mu < \infty$ corresponds to $\nu$ having **finite total variation** $|\nu| = \nu^+ + \nu^-$. So the decomposition is not an analytic trick but a fundamental fact about the structure of signed measures.

---

## Is harmonic analysis involved?

Only tangentially, and at a later stage. In harmonic analysis, one certainly uses $L^1$ and $L^p$ spaces constantly, and the Lebesgue integral is the indispensable foundation. But the decomposition $f = f^+ - f^-$ is not a harmonic-analysis idea; it pre-exists harmonic analysis logically. 

Where something more sophisticated occurs in harmonic analysis is in the distinction between **absolutely convergent** and **conditionally convergent** integrals. For example, the **improper Riemann integral** $\int_0^\infty \frac{\sin x}{x}\, dx$ converges conditionally (as a limit) but not absolutely (i.e., $\int_0^\infty \frac{|\sin x|}{x}\, dx = \infty$). This function is *not* in $L^1(\mathbb{R})$, so it has no Lebesgue integral in the standard sense — yet the improper Riemann integral exists. This contrast is important in harmonic analysis (e.g., the analysis of the Dirichlet kernel and issues with pointwise convergence of Fourier series), but it is a *consequence* of the absolute integrability requirement, not a motivation for the $f^+/f^-$ decomposition itself.

---

## Summary

The decomposition is forced by **measure theory and functional analysis**, not harmonic analysis:

- The Lebesgue construction requires building the integral for non-negative functions first (to use monotone limits freely in $[0,\infty]$).
- Handling general $f$ then requires splitting to avoid $\infty - \infty$.
- The absolute integrability condition $\int |f| < \infty$ is what makes $L^1$ a Banach space and signed measures have finite total variation.
- The Riemann setting is simply too constrained (bounded functions, bounded intervals) for any of these dangers to arise, so no decomposition is necessary.
