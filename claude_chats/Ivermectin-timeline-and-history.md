# Ivermectin timeline and history

- Source: https://claude.ai/share/24e3a51f-fcdc-4e7f-abe9-daadd65baf11
- Author: Henry
- Created: 2026-06-10
- Messages: 6

---

## Human

please make a timeline for Ivermectin which includes: discovery, patent?, use in various animals and humans, WHO recommendation. Vertical, probably starting each entry with the year

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

Here's a vertical timeline of ivermectin's history. The color bands group the entries by phase: discovery and development, deployment in animals and humans, and recognition and WHO position.
```
This block is not supported on your current device yet.
```

A few notes on the compressed entries, with sources:

- The source microbe was isolated from a Japanese soil sample (collected near a golf course in Ito); the avermectin-producing organism was discovered by Ōmura in 1973, with Campbell's Merck team then showing the fermentation products were potently antiparasitic. The generic name "ivermectin" came from chemically modifying avermectin B1 into a safer, more effective derivative.

- Patent: Merck filed/held patents on the avermectins and ivermectin from the late 1970s–early 1980s. Ivermectin is now an old, cheap, off-patent drug — the original composition patents have long since expired, which is why it's a low-cost generic today. (I couldn't pin a single authoritative expiry year, so I've left the timeline at "derived and patented, 1979" rather than asserting an expiry date.)

- 1981: Merck began commercializing ivermectin as a broad-spectrum veterinary antiparasitic in 1981. The same year, Merck worked with WHO to run the first human river-blindness trials in Senegal under Mohammed Aziz.

- 1987: two things at once. Ivermectin was approved for human use in 1987 under the name Mectizan (launching the Mectizan Donation Program for onchocerciasis), and that same year it was marketed as Heartgard for canine heartworm prevention.

- "WHO recommendation" is ambiguous, so I included both WHO positions. The dated one: on 31 March 2021, WHO advised that ivermectin only be used to treat COVID-19 within clinical trials, applying to any disease severity. Separately and on an ongoing basis, ivermectin is included on the WHO essential medicines list for several parasitic diseases — onchocerciasis, strongyloidiasis, soil-transmitted helminthiasis, and scabies.

Want me to add the 1996 introduction of human scabies/strongyloidiasis approval (Stromectol), or output this as a standalone SVG file for a wiki page?

---

## Human

Can you update the excellent SGV which includes the 1996 information?

---

## Assistant

```
This block is not supported on your current device yet.
```

Verified — added it. Stromectol (ivermectin) tablets, NDA 050742, was initially approved by the FDA on November 22, 1996, for strongyloidiasis of the intestinal tract and onchocerciasis. It slots into the human-use band between the 1987 Mectizan launch and the 1998 donation-program expansion.
```
This block is not supported on your current device yet.
```

One nuance worth flagging: 1996 is specifically the *US FDA* approval, which came nearly a decade after the 1987 Mectizan approval used in the African/Latin American mass-distribution programs. So the timeline now distinguishes the global humanitarian approval (1987) from the US regulatory approval (1996) — they're often conflated in popular accounts.

Want this as a downloadable standalone `.svg` file for a VitaminDWiki page?

---

## Human

yes, please

---

## Assistant

I'll create a self-contained `.svg` file with all styling inlined (so it doesn't depend on the chat environment), plus a dark-mode variant so it adapts to whatever theme the wiki page uses.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Done. A few notes for embedding it on VitaminDWiki:

The file is fully self-contained — all styling is inlined, fonts fall back to a system sans-serif stack, and there are no external dependencies. It includes a `prefers-color-scheme: dark` block, so card fills and text flip automatically on dark wiki themes while the year/dot colors stay constant for contrast in both.

The canvas is a fixed 680 × 908. If you drop it inline as `<img src="...">` it renders at that size; if you want it fluid, set `width:100%; height:auto` on the element since the `viewBox` is present. The `<title>`/`<desc>` are there for screen readers and as alt-style metadata. The Ōmura "Ō" is encoded as a numeric entity (`&#x14C;`) so it survives any encoding mangling on upload.
