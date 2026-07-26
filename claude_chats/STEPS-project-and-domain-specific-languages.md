# STEPS project and domain-specific languages

- Source: https://claude.ai/share/a50c5e0f-4834-48d6-9e6f-abe7f332a2e7
- Author: Carlos
- Created: 2026-06-17
- Messages: 4

---

## Human

Tell me about the Alan Kay project devoted to creating a series of domain specific languages, culminating in the ability to write a very short program that fully specified the graphical, uh, aspects of an operating system.

---

## Assistant

The project is **STEPS** — "Steps Toward Expressive Programming Systems" — run at Alan Kay's Viewpoints Research Institute (VPRI) on NSF funding from roughly 2006 to 2012. The headline bet was that you could rebuild the functionality of a complete personal computing system — operating system, GUI, document editor, network stack, the works — in about 20,000 lines of code, against the tens of millions of lines such systems normally take. A factor of a thousand.

The mechanism was the thing you're pointing at: don't write the system, write *problem-oriented languages* and then write the system as a near-direct statement of what it is. The leverage came from cheap language creation. Two meta-tools made new DSLs almost disposable — Ian Piumarta's **Maru** (a tiny self-describing Lisp-like kernel that could redefine itself, part of his "COLA" work) and Alessandro Warth's **OMeta** (a pattern-matching language for writing parsers and compilers in a page or two). With those underneath, a new language for a given domain cost you an afternoon rather than a career, so each subsystem could get a notation fitted exactly to its problem.

The graphics case is the cleanest demonstration and almost certainly the one you're remembering: **Nile**, a declarative dataflow language by Dan Amelang, and the **Gezira** renderer built in it. The entire 2D vector graphics pipeline — rasterization, anti-aliasing, alpha compositing, gradients, strokes — was expressed in a few hundred lines of Nile (the figure cited was around 400), versus the ~44,000 lines of C in something like Cairo doing the same job. The code reads as the *mathematics* of rendering: compositions of pure functions over streams of pixels, not an implementation grinding toward that math. The companion party trick was the network stack — a working TCP/IP done in ~160 lines by writing a DSL whose programs looked like the packet-layout diagrams in the RFCs themselves.

The deep claim, which is what makes it more than a code-golf stunt: most of the bulk in real systems is accidental — the distance between what a thing *means* and how a fixed general-purpose language forces you to *say* it. If you can mint a notation that closes that gap, the program collapses to roughly the size of the specification, because it *is* the specification. The primary sources are the annual VPRI progress reports (findable as the "STEPS … Progress Report" RN documents), which are worth reading directly if you want the actual code samples rather than my approximate line counts.

---

## Human

Provide some useful links, especially to YouTube videos on the subject.

---

## Assistant

I'll search for current, working links rather than reconstructing URLs from memory.
```
This block is not supported on your current device yet.
```

Now let me find the YouTube videos, which is the part the user especially wants.
```
This block is not supported on your current device yet.
```

Here are the worthwhile ones, sorted by type.

**YouTube**

- **"Programming and Scaling"** — Alan Kay, 2011 (~1 hr): https://www.youtube.com/watch?v=y9xLi0iJg1g. The canonical talk laying out the thesis (Maxwell's-equations-for-software, the 20KLOC bet, why bulk is accidental). Best to watch the whole thing.
- **"How Complex is Personal Computing?"** — https://www.youtube.com/watch?v=HAT4iewOHDs. The most useful one for your interest: Kay does intro/overview, then Dan Amelang demos the 2D rendering (Gezira & Nile) starting around 17:05, then a segment on the DSLs (OMeta etc.). This is where you actually see the graphics-from-a-few-hundred-lines claim demonstrated.
- **Kay talk with Amelang Q&A** — https://www.youtube.com/watch?v=ubaX1Smg6pY. Covers the same concepts in a more entertaining register; Dan Amelang answers questions at the end.

**Primary papers (VPRI progress reports)**

- **2012 Final NSF Report** (the capstone — start here): https://tinlizzie.org/VPRIPapers/tr2012001_steps.pdf
- 2011: http://archive.rickardlindberg.me/writing/alan-kay-notes/tr2011004_steps11.pdf
- 2010 (introduces "Frank," the assembled system): https://tinlizzie.org/VPRIPapers/tr2010004_steps10.pdf
- 2007 First-Year Report: https://worrydream.com/refs/Kay_2007_-_STEPS_2007_Progress_Report.pdf
- Alex Warth's publications page indexes the full run plus the OMeta/Worlds papers: http://alexwarth.github.io/scholarly.html

**Worth knowing for the skeptical read**

Two recent posts puncture the line-count romance usefully. Daniel Taylor's Gezira retrospective notes that the Nile C runtime is ~2,000 lines and Maru is ~10K of C plus ~10K of Lisp — i.e., the few-hundred-line figure is the Nile-expressed spec sitting atop substantial infrastructure, and Kay himself said the early demos "tempted me away from the original goal" toward giving talks. https://djtaylor.me/post/2025-10-11-gezira. The chreke.com "little languages" essay is the better sympathetic framing: https://chreke.com/posts/little-languages.html.

One honest caveat on the videos: a few aggregator pages conflate the two Kay talks, so the exact runtime and date on the first two may be slightly off — the video IDs themselves are correct.
