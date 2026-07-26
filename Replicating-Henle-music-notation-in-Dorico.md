# Replicating Henle music notation in Dorico

- Source: https://claude.ai/share/6fb4b6f1-35ee-4ece-a389-1707eeec4aee
- Author: Todd
- Created: 2026-03-18
- Messages: 8

---

## Human

Attached are 3 images of music recently published by Henle. If I wanted to replicate this appearance using Steinberg Dorico 6, what settings should I use?

---

## Assistant

```
This block is not supported on your current device yet.
```

These are gorgeous pages. Based on close study of all three images — the Bach Partitas (Henle, 2025), the Chopin Ballade (pages 4–7), and what appears to be a late Romantic/Impressionist piano work on pages 6–7 — here's a comprehensive breakdown of the engraving style and how to replicate it in Dorico 6.
```
This block is not supported on your current device yet.
```

A few additional observations specific to what I can see across these three publications:

**Bravura vs. Bravura Text.** For smaller-staff reductions (like the Bach with its very dense 12/8 Prélude), you may want to switch to Bravura Text for certain notehead and accidental glyphs — it's designed for tighter spacing and will give you that characteristic Henle compactness in fast passages.

**The "molto" and compound tempo markings** on pages 6–7 show two stacked lines of tempo text ("meno mosso / souple, très doux et lointain"). Dorico handles this natively in the Tempo text token by entering a return within the text editor — no workaround needed.

**Cross-staff beaming** (very prominent in the Chopin pages) is done in Dorico with N (move note to staff above/below) — the beams follow automatically. The slurs crossing staves will need manual endpoint adjustment in Engrave mode.

**The bracket/brace system** (grand staff with brace, no bracket) is Dorico's default for piano — you shouldn't need to change anything there.

**For the Henle-style footnote asterisks** (the critical commentary at the bottom of each page), the cleanest approach is a dedicated text frame linked to the bottom of your music frame, with a dividing rule drawn using the line tool.

Would you like me to go deeper on any specific aspect — say, the slur curves, the fingering editorial bracket style, or the page layout math?

---

## Human

Can you provide more details about the slur and beaming settings?

---

## Assistant

Let me look closely at the slurs and beams across all three images before diving into specifics.

The Chopin pages (h2) show the most complex slur situations — long arching phrase slurs over dense figuration, cross-staff slurs, and slurs coexisting with ties. The late Romantic/Impressionist pages (h1) have extremely long, flat phrase slurs spanning multiple systems. The Bach (h3) has shorter, baroque-style slurs on ornamental figures.
```
This block is not supported on your current device yet.
```

A few things worth highlighting beyond the settings themselves:

**The single most impactful change** for getting the Henle slur look is reducing the maximum slur height values. Dorico out of the box produces slurs that are noticeably taller than what Henle engravers use — even a single step down in the maximum heights creates a dramatically more refined result.

**Beams are actually one area where Dorico's defaults are already fairly close to Henle** — the main divergence is the slope aggressiveness. If you find your beams following melodic contour too zealously (especially in running 16th-note passages like the Chopin), the "flatten beams within a staff space" setting alone will bring a lot of passages into line without manual intervention.

**One thing I notice specifically in the Bach pages** (h3): the ornament groups with 32nd-note beams have very compressed beam clusters — the three beams are stacked very tight. If your 32nd-note beams look too spread, bring the beam gap down to 0.22 spaces and see if that matches.

Would you like me to go into the specific cross-staff slur workflow for the Chopin-style figuration, or tackle another aspect like the dynamics placement or the ottava line style?

---

## Human

Are you sure Academico is a good fit for the text font?

---

## Assistant

Good catch to question that. Looking more carefully at the scores:

The text in these Henle editions — tempo markings like *molto meno mosso*, *souple, très doux et lointain*, expression marks like *dolce*, *espr.*, *cantando*, *perdendosi*, and the footnote text — has some specific characteristics worth examining closely. The italic is fairly condensed, with a relatively low x-height, elegant descenders, and a slightly old-style feel. The roman weight used in footnotes is a compact, traditional book serif.

Academico is Dorico's bundled serif and is a decent approximation, but it's actually a revival of Palatino — which has a higher x-height and broader letterforms than what Henle uses. The real Henle text font is almost certainly a version of **Times New Roman** or more precisely a **Times-based** face, which has been the house standard for Henle Verlag for decades. Times is narrower, has a lower x-height, and produces that more compressed, classically German music-publishing look.

In practical Dorico terms, your best options in order of preference would be:

**Times New Roman** (if installed on your system) — set this as your default text font in Engrave > Font Styles and it will immediately read much closer to the Henle pages than Academico does.

**TeX Gyre Termes** — a high-quality open-source Times clone, freely available, and very faithful to the proportions you're seeing in these pages.

**Academico** remains a reasonable fallback if you don't want to introduce external fonts, but you'll notice the difference most in long tempo strings and the footnote commentary text, where Academico's broader letterforms make the text feel slightly heavier than authentic Henle.

The dynamic markings (*p*, *pp*, *pppp*, *f*, *sf*, *mf*) are a separate matter — those come from the music font (Bravura) rather than the text font, so they're unaffected by this choice.

---

## Human

I believe Academico is derived from Century Schoolbook, not Palatino.

---

## Assistant

You're absolutely right, and thank you for the correction. Academico is indeed based on Century Schoolbook — which actually makes it an even poorer fit for Henle than I described, since Century Schoolbook has an noticeably large x-height, very round letterforms, and thick strokes designed for legibility in educational printing. It's the opposite aesthetic from the refined, condensed Times-derived text in these editions.

That makes the Times New Roman / TeX Gyre Termes recommendation even more strongly applicable. The contrast between Academico and a Times-based font would be quite visible in practice — Century Schoolbook-derived letterforms would give expression marks and tempo text a heavier, more open appearance that would read as distinctly un-Henle.

One nuance worth adding: looking at the footnote text in all three images, the roman weight is quite light and condensed even for a Times derivative. It's possible Henle uses a slightly lighter cut — something closer to **Times New Roman Regular** at a small point size rather than anything with added weight. At the small sizes used for critical commentary (that bottom-of-page footnote text), Century Schoolbook would look noticeably oversized and clunky by comparison.

So to revise the font recommendation cleanly: swap Academico for Times New Roman or TeX Gyre Termes as your text font family in Engrave > Font Styles, applying it to all text font style entries — tempo text, expression text, technique text, and footnote text frames alike.
