# Conflicting Markdown extensions

- Source: https://claude.ai/share/2cded2e5-3940-4d92-bfc3-e9d2ab78617e
- Author: Brendan
- Created: 2026-07-19
- Messages: 2

---

## Human

Are there any common Markdown extensions that make conflicting assumptions and can't both be rendered correctly by a parser which doesn't know which extensions are in use? I'm just looking for a brief list of examples so I can share it in a blog post.

---

## Assistant

Yes, several. The clearest cases are where an extension claims a character sequence that base CommonMark—or another extension—reads differently:

- **Inline math `$...$`** (Pandoc, KaTeX/MathJax renderers) vs. literal dollar signs. In a math-aware parser, "I paid $5 for lunch and $7 for coffee" turns everything between the first and second `$` into a math span; a plain parser leaves it as text. Currency-heavy prose is the usual casualty.

- **Subscript/superscript `~x~` and `^x^`** (Pandoc) vs. strikethrough `~~x~~` (GFM). `CO~2~` is "CO₂" under Pandoc but literal `CO~2~` under GFM, and a parser that only knows GFM strikethrough can't tell a lone `~` from a malformed `~~`.

- **Footnotes `[^1]`** (Pandoc, PHP Markdown Extra, GFM's footnote extension) vs. shortcut reference links (CommonMark). `[^1]` is a footnote marker in one world; in plain CommonMark it's a reference link whose label is literally `^1`, and `[^1]: text` reads as a link reference definition.

- **Wikilinks `[[Page]]`** (Obsidian, MediaWiki-style) vs. reference links (CommonMark). CommonMark parses `[[Page]]` as nested brackets around a shortcut reference link `[Page]`, not as a link to a page named "Page."

- **Attribute blocks `{#id .class}`** (Pandoc, kramdown, markdown-it-attrs) vs. literal braces (CommonMark). `## Heading {#anchor}` sets the heading's id in an attribute-aware parser but prints the braces verbatim otherwise—and this even conflicts *between* extensions, since kramdown spells it `{: #anchor}`.

If you want a sixth that's more "extension vs. nothing" than a true two-way collision, **highlight `==text==`** (markdown-it-mark, Obsidian) renders as `<mark>` in some parsers and literal `==` in others.

The root cause worth stating in the post: Markdown has no formal in-document way to declare its dialect, so a parser has to guess, and these overloaded sigils (`~`, `$`, `^`, `[`, `{`, `=`) are exactly where the guesses diverge.

Palabra del día: ambigüedad (ahm-bee-gweh-DAHD) - ambiguity. "La ambigüedad de la sintaxis confunde al analizador." - "The ambiguity of the syntax confuses the parser."
