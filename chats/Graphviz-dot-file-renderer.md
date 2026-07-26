# Graphviz dot file renderer

- Source: https://claude.ai/share/2b78a93e-cdc3-4b1d-9b02-457eb62140a5
- Author: Simon
- Created: 2025-10-10
- Messages: 4

---

## Human

Build a .dot renderer - I can paste a .dot file content into a textarea and it shows rendered below using the most appropriate library

---

## Assistant

I'll create a .dot file renderer using Viz.js, which is the standard library for rendering Graphviz DOT files in the browser.
```
This block is not supported on your current device yet.
```

[View your DOT renderer](computer:///mnt/user-data/outputs/dot-renderer.html)

I've created a .dot file renderer using Viz.js (the standard library for rendering Graphviz DOT files). Features include:

- **Textarea input** for pasting .dot content
- **Render button** to generate the graph visualization
- **Example loader** to see a sample graph
- **Keyboard shortcut** (Ctrl/Cmd + Enter) to quickly render
- **Error handling** with helpful messages

The renderer displays graphs as interactive SVG below the input area.

---

## Human

No need to have a render button, it should render any time text is changed or added to that textarea

Also have it update the fragment URL with the text from the textarea - and on page load it should render that if it's present and populate the textarea too

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

[View your updated DOT renderer](computer:///mnt/user-data/outputs/dot-renderer.html)

Perfect! I've updated the renderer with:

- **Auto-rendering** as you type (with 500ms debounce to avoid excessive renders)
- **URL fragment sync** - the textarea content is saved to the URL hash
- **Page load** - if there's a hash in the URL, it populates the textarea and renders automatically
- **Browser navigation** - back/forward buttons work with the graph history

Now you can share DOT graphs just by sharing the URL!
