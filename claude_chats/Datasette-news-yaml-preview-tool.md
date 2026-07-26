# Datasette news.yaml preview tool

- Source: https://claude.ai/share/c96129b9-bcb0-4eba-aee9-4a7ad236dfb7
- Author: Simon
- Created: 2026-04-16
- Messages: 6

---

## Human

Clone https://github.com/simonw/datasette.io and look at the news.yaml file and how it is rendered on the homepage. Build an artifact I can paste that YAML into which previews what it will look like, and highlights any markdown errors or YAML errors

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


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Now let me read the frontend design skill for best practices.
```
This block is not supported on your current device yet.
```

Now I have a solid understanding of the YAML structure and rendering. Each entry has `date` (YYYY-MM-DD) and `body` (markdown with links, bold, code, lists). The homepage groups by date with a formatted heading like "29th January 2026" and renders the body as markdown. Let me build the preview tool.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Here's your preview tool. It has a split-pane layout with a YAML editor on the left and a live preview on the right that matches datasette.io's homepage rendering style. As you type/paste, it:

**Validates YAML** — parse errors with line numbers, checks for the expected array-of-objects structure, verifies `date` is YYYY-MM-DD format, flags unexpected keys, and warns if entries aren't in reverse chronological order.

**Lints markdown** — catches mismatched `**` bold markers, unmatched square brackets (broken links), unclosed link parentheses, unmatched backticks, empty link text `[](url)`, and empty link URLs `[text]()`. Affected entries get a yellow highlight in the preview with inline warnings.

**Renders the preview** — dates are formatted the same way the site does ("29th January 2026"), entries are grouped under date headings with the `#` permalink, and markdown is rendered with the same link color / code / typography styling as datasette.io.

---

## Human

> Entry #1: `date` should be YYYY-MM-DD format, got `Wed Jan 28 2026 16:00:00 GMT-0800 (Pacific Standard Time)`
That is wrong, I pasted in:

```
- date: 2026-01-29
  body: |-
    [Datasette 1.0a24](https://docs.datasette.io/en/latest/changelog.html#a24-2026-01-29) introduces a new `await request.form(files=True)` method for accepting file uploads, plus various other changes.

```

---

## Assistant

The problem is that js-yaml's default YAML 1.1 schema automatically converts `2026-01-29` into a JavaScript `Date` object. I need to tell it to keep dates as strings.
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

The fix was one option added to the `jsyaml.load` call: `{ schema: jsyaml.JSON_SCHEMA }`. This tells js-yaml to only resolve JSON-compatible types (strings, numbers, booleans, null) instead of applying YAML 1.1's implicit conversions that turn `2026-01-29` into a `Date` object. Block scalar syntax like `|-` and `>-` still works fine since that's handled by the parser, not the schema.

---

## Human

use colors from the datasette.io site (look in the CSS you git cloned earlier)

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

The colors are mostly right already since I pulled from that CSS, but a few are off. Let me align the remaining ones.
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

Updated to use the datasette.io palette throughout: `#0e0c82` dark blue for the divider and header bar, `#8484f4` purple for the OK badge (matching the site's button color), `blue` for links, `#999` for muted text, `#EEE` for light borders, white backgrounds, and default black body text — all pulled from `site.css`. Kept red for error states since those are functional UI colors the site doesn't need.
