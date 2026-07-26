# Proof of Integral Kernel Inequality

- Source: https://grok.com/share/c2hhcmQtNA_885159eb-bd8b-4fa6-b602-c673afb8825c
- Created: 2025-12-09
- Model: grok-4-heavy
- Messages: 2

---

## Human

Give rigorous mathematical step by step proof of this lemma. 

\noindent\textbf{LEMMA 2.1.}
Let $\Omega$ be any measure space and let $K(x,y)$ be a nonnegative
symmetric integral kernel defined on $\Omega\times\Omega$.
\newr{Suppose $\kappa$ is defined by.
\[
\kappa = \sup_{x}\int_{\Omega} K(x,y)^{\frac{p}{p-1}}\,dy.
\]}
Let $p$ be an integer greater than $1$. \newr{Then
\[
\int_{\Omega^{p}}
\prod_{i\neq j}K^{\frac{2}{p-1}}(x_{i},x_{j})
\prod_{s=1}^{p} F_{s}(x_{s})\,dx_{1}\cdots dx_{p}
\;\le\;
\kappa^{\,p-1}\,
\prod_{s=1}^{p}\|F_{s}\|_{p}.
\]}

---

## Assistant

\int_{\Omega^{p}}
\prod_{1 \leq i < j \leq p} K(x_{i},x_{j})^{\frac{2}{p-1}}
\prod_{s=1}^{p} F_{s}(x_{s})\,dx_{1}\cdots dx_{p}
\;\le\;
\kappa^{\,p-1}\,
\prod_{s=1}^{p}\|F_{s}\|_{p}.

**Note:** The product in the integrand is interpreted over unordered pairs $1 \leq i < j \leq p$ (as the version over all ordered pairs $i \neq j$ leads to a false inequality, per counterexample). Equivalently, this is $\prod_{i \neq j} K(x_i, x_j)^{\frac{1}{p-1}}$.

### Proof

Since $K$ is symmetric and nonnegative, we rewrite the product in the integrand as
\[
\prod_{1 \leq i < j \leq p} K(x_i, x_j)^{\frac{2}{p-1}} = \prod_{k=1}^p \left( \prod_{j \neq k} K(x_k, x_j) \right)^{\frac{1}{p-1}}.
\]

Thus, the left-hand side is
\[
\int_{\Omega^p} \prod_{k=1}^p \left[ F_k(x_k) \left( \prod_{j \neq k} K(x_k, x_j) \right)^{\frac{1}{p-1}} \right] \, dx_1 \cdots dx_p.
\]

Define functions $h_k: \Omega^p \to \mathbb{R}$ for $k=1, \dots, p$ by
\[
h_k(x_1, \dots, x_p) = F_k(x_k) \left( \prod_{j \neq k} K(x_k, x_j) \right)^{\frac{1}{p-1}}.
\]

The integrand is $\prod_{k=1}^p h_k(\mathbf{x})$, so the integral is $\int_{\Omega^p} \prod_{k=1}^p h_k(\mathbf{x}) \, d\mathbf{x}$.

By the generalized Hölder's inequality on the space $L^p(\Omega^p)$ (with each exponent equal to $p$, since $\sum_{k=1}^p \frac{1}{p} = 1$),
\[
\left| \int_{\Omega^p} \prod_{k=1}^p h_k(\mathbf{x}) \, d\mathbf{x} \right| \leq \prod_{k=1}^p \| h_k \|_{L^p(\Omega^p)}.
\]

Without loss of generality, compute $\| h_1 \|_p$ (the others follow by symmetry, relabeling the $F_k$).
\[
\| h_1 \|_p^p = \int_{\Omega^p} \left[ F_1(x_1) \left( \prod_{j=2}^p K(x_1, x_j) \right)^{\frac{1}{p-1}} \right]^p \, dx_1 \cdots dx_p
= \int_{\Omega} F_1(x_1)^p \, dx_1 \cdot \prod_{j=2}^p \int_{\Omega} K(x_1, x_j)^{\frac{p}{p-1}} \, dx_j,
\]
since the integrals separate. Each inner integral is $\int_\Omega K(x_1, y)^{\frac{p}{p-1}} \, dy \leq \kappa$, so
\[
\prod_{j=2}^p \int K(x_1, x_j)^{\frac{p}{p-1}} \, dx_j = \left( \int_\Omega K(x_1, y)^{\frac{p}{p-1}} \, dy \right)^{p-1} \leq \kappa^{p-1}.
\]

Thus,
\[
\| h_1 \|_p^p \leq \kappa^{p-1} \int_\Omega F_1(x_1)^p \, dx_1 = \kappa^{p-1} \| F_1 \|_p^p,
\]
so $\| h_1 \|_p \leq \kappa^{\frac{p-1}{p}} \| F_1 \|_p$.

Similarly for each $k$, $\| h_k \|_p \leq \kappa^{\frac{p-1}{p}} \| F_k \|_p$.

Therefore,
\[
\int_{\Omega^p} \prod_{k=1}^p h_k(\mathbf{x}) \, d\mathbf{x} \leq \prod_{k=1}^p \left( \kappa^{\frac{p-1}{p}} \| F_k \|_p \right) = \kappa^{p-1} \prod_{k=1}^p \| F_k \|_p.
\]

This completes the proof.
