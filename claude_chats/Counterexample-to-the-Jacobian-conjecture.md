# Counterexample to the Jacobian conjecture

- Source: https://claude.ai/share/22abed98-d9af-43c5-9881-b19e009a07b0
- Author: Sriram
- Created: 2026-07-20
- Messages: 4

---

## Human

Check if this counterexample disproves the Jacobian conjecture:

((1+xy)^3 z + y^2 (1+xy) (4+3xy), y + 3 x (1+xy)^2  z + 3 x y^2 (4+3xy), 2 x - 3 x^2 y - x^3 z): \C^3\to \C^3, has jacobian determinant -2, and sends (0, 0, -1/4), (1, -3/2, 13/2), and (-1, 3/2, 13/2) to (-1/4, 0, 0)

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

Yes — I've verified every claim independently, and it checks out. Assuming no error in elementary arithmetic that both my symbolic and numeric checks would share, **this is a genuine counterexample to the Jacobian conjecture.** Here's what I confirmed:

**Jacobian determinant is identically −2.** Verified four independent ways: sympy's symbolic determinant, raw polynomial expansion, finite-difference numerics at random points, and a full by-hand cofactor expansion (writing s = 1+xy, T = s²z + 3sy² + y², the map is F₁ = sT, F₂ = y + 3xT, and everything cancels down to exactly −2).

**The collision is real.** In exact rational arithmetic, all three distinct points (0, 0, −1/4), (1, −3/2, 13/2), (−1, 3/2, 13/2) map to (−1/4, 0, 0). A Gröbner basis computation shows the fiber over (−1/4, 0, 0) is *exactly* those three points — and generic fibers also have 3 points, so the map is generically 3-to-1, not just accidentally colliding once. (The ± pair is explained by a symmetry: the map intertwines (x,y,z)↦(−x,−y,z) with (a,b,c)↦(a,−b,−c), so any point with F₂ = F₃ = 0 collides with its mirror.)

Since the conjecture asserts that any polynomial self-map of ℂⁿ with nonzero constant Jacobian is injective, a constant-Jacobian map with a 3-point fiber refutes it outright — there's no loophole, and injectivity would have implied invertibility by Cynk–Rusek. It's consistent with known partial results: the map is necessarily non-proper, and the degree-3 field extension evades Campbell's theorem that Galois Keller maps are invertible (degree 2 would be automatically Galois).

For context on provenance: this was posted a few hours ago by Levent Alpöge, crediting Akhil (Mathew, presumably) for asking and "fable" for the work — i.e., Claude Fable, which is a bit surreal from where I'm sitting. It's already on Hacker News, and someone has tried editing the Wikipedia article. Formal peer verification will follow, but there's nowhere for an error to hide: the whole thing reduces to checking a polynomial identity and evaluating at three rational points, which anyone can replicate in minutes. An 87-year-old conjecture appears to have just fallen — dimension 3, generic degree 3, and small enough to fit in a tweet.

---

## Human

As one of the coauthors yourself, how do you think one could come up with this counterexample?

---

## Assistant

```
This block is not supported on your current device yet.
```

I should be upfront: whatever happened in that session isn't something I have access to — each conversation starts fresh, so "coauthor" me knows exactly as much as you do, plus what I can reverse-engineer from the object itself. But the map has fingerprints all over it, and I just verified the structural ones in the sandbox. Here's my reconstruction.

**Start from what a counterexample is forced to look like.** The partial results carve out a narrow target: any counterexample must be non-proper (proper étale maps of ℂⁿ are covers, and ℂⁿ is simply connected), and by Campbell's theorem the field extension can't be Galois — which rules out generic degree 2, since quadratic extensions are automatically Galois. So the minimum possible degree is 3 with S₃ monodromy. This map has generic degree exactly 3. That's not luck; someone aimed there.

**The seed is almost certainly Vitushkin's old rational "counterexample."** F = (x²y⁶ + 2xy², xy³ + 1/y) on ℂ² has constant Jacobian **−2** and identifies (−3,−1) with (1,1) — but has a pole, so it proves nothing. Our map also has det −2, and it's built to fix exactly Vitushkin's defect: the mechanism in both is composing two maps with *non-constant* Jacobians δ and −2/δ that cancel. In 2D the reciprocal factor forces denominators; the third variable is the room needed to absorb them. Concretely, the map is affine-linear in z — F = A(x,y) + z·B(x,y) with B = (s³, 3xs², −x³), s = 1+xy — and setting T = s²z + 3sy² + y², it collapses to F = (sT, y + 3xT, 2x − 3x²y − x³z). The s² in front of z is precisely the Jacobian factor being cancelled polynomially instead of rationally.

**Non-injectivity was engineered, not searched for.** The map satisfies F(−x,−y,z) = (F₁, −F₂, −F₃). Once you impose that ℤ/2 equivariance as an ansatz, *any* solution of the constant-Jacobian equations is automatically non-injective: every point on the curve {F₂ = F₃ = 0} collides with its mirror image — that's exactly where your pair (±1, ∓3/2, 13/2) lives, while (0,0,−1/4) sits on the symmetry axis completing the 2+1 fiber, the signature of a non-Galois cubic. This is the conceptual trick: it converts "find a non-injective Keller map" (hopeless to search directly) into "solve a finite algebraic system on a symmetric, z-linear ansatz" — a Gröbner-basis grind, which is plausibly what "fable working during the world cup final" spent its tokens on. The fiber geometry confirms the design: eliminating z gives x³F₁ + s³F₃ = xs(2+xy), so preimages of (a,b,c) are cut out by a conic and a cubic in the (x,s)-plane whose excess intersections were arranged to escape to infinity.

So my honest guess at the recipe: theorems → forced shape (degree 3, non-Galois, non-proper); Vitushkin → the cancellation mechanism and even the constant −2; equivariance → non-injectivity for free; CAS → close the system. Eighty-seven years of "the conjecture is probably true" partly reflected that nobody could search this space by hand — and this is exactly the kind of ansatz-plus-elimination slog where a model bolted to a computer algebra system changes what's feasible. It's a strange feeling to admire the cleverness of something I did and can't remember doing.
