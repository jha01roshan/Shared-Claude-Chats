# Text indentation and formatting tool

- Source: https://claude.ai/share/cf369134-45de-4516-9b4b-42e07ee26aef
- Author: Simon
- Created: 2025-10-15
- Messages: 2

---

## Human

```
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Text Indentation Tool</title>
<style>
* {
  box-sizing: border-box;
}

body {
  font-family: Helvetica, Arial, sans-serif;
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
  background: #f5f5f5;
}

h1 {
  margin-top: 0;
  color: #333;
}

.container {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

textarea {
  width: 100%;
  min-height: 300px;
  padding: 12px;
  font-size: 16px;
  font-family: 'Courier New', monospace;
  border: 1px solid #ddd;
  border-radius: 4px;
  resize: vertical;
  margin-bottom: 15px;
}

.buttons {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  font-family: Helvetica, Arial, sans-serif;
  background: #007aff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background 0.2s;
}

button:hover {
  background: #0051d5;
}

button:active {
  transform: translateY(1px);
}

button.remove {
  background: #ff3b30;
}

button.remove:hover {
  background: #d62d20;
}
</style>
</head>
<body>
<div class="container">
  <h1>Text indentation tool</h1>
  <textarea id="textInput" placeholder="Paste your text here..."></textarea>
  <div class="buttons">
    <button id="indent2">Indent 2</button>
    <button id="indent4">Indent 4</button>
    <button id="remove2" class="remove">Remove 2 spaces</button>
    <button id="remove4" class="remove">Remove 4 spaces</button>
    <button id="removeIndent" class="remove">Remove all indentation</button>
  </div>
</div>

<script type="module">
const textInput = document.getElementById('textInput');
const removeIndentBtn = document.getElementById('removeIndent');
const indent2Btn = document.getElementById('indent2');
const indent4Btn = document.getElementById('indent4');
const remove2Btn = document.getElementById('remove2');
const remove4Btn = document.getElementById('remove4');

removeIndentBtn.addEventListener('click', () => {
  const text = textInput.value;
  const lines = text.split('\n');
  const processed = lines.map(line => line.replace(/^\s+/, '')).join('\n');
  textInput.value = processed;
});

indent2Btn.addEventListener('click', () => {
  const text = textInput.value;
  const lines = text.split('\n');
  const processed = lines.map(line => '  ' + line).join('\n');
  textInput.value = processed;
});

indent4Btn.addEventListener('click', () => {
  const text = textInput.value;
  const lines = text.split('\n');
  const processed = lines.map(line => '    ' + line).join('\n');
  textInput.value = processed;
});

remove2Btn.addEventListener('click', () => {
  const text = textInput.value;
  const lines = text.split('\n');
  const processed = lines.map(line => {
    if (line.startsWith('  ')) {
      return line.slice(2);
    }
    return line;
  }).join('\n');
  textInput.value = processed;
});

remove4Btn.addEventListener('click', () => {
  const text = textInput.value;
  const lines = text.split('\n');
  const processed = lines.map(line => {
    if (line.startsWith('    ')) {
      return line.slice(4);
    }
    return line;
  }).join('\n');
  textInput.value = processed;
});
</script>
</body>
</html>

```

Add a "Quote" button that adds `> ` to the beginning of every line. If the system detects that every line in the textarea has that show a "Unquote" button to undo it. Both buttons can be clicked multiple times to create multiple levels of quote.

---

## Assistant

I'll add a "Quote" button that adds `> ` to each line, and an "Unquote" button that appears when all lines are quoted. Here's the updated code:

```html
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Text Indentation Tool</title>
<style>
* {
  box-sizing: border-box;
}

body {
  font-family: Helvetica, Arial, sans-serif;
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
  background: #f5f5f5;
}

h1 {
  margin-top: 0;
  color: #333;
}

.container {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

textarea {
  width: 100%;
  min-height: 300px;
  padding: 12px;
  font-size: 16px;
  font-family: 'Courier New', monospace;
  border: 1px solid #ddd;
  border-radius: 4px;
  resize: vertical;
  margin-bottom: 15px;
}

.buttons {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  font-family: Helvetica, Arial, sans-serif;
  background: #007aff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background 0.2s;
}

button:hover {
  background: #0051d5;
}

button:active {
  transform: translateY(1px);
}

button.remove {
  background: #ff3b30;
}

button.remove:hover {
  background: #d62d20;
}

button.quote {
  background: #34c759;
}

button.quote:hover {
  background: #28a745;
}

button.hidden {
  display: none;
}
</style>
</head>
<body>
<div class="container">
  <h1>Text indentation tool</h1>
  <textarea id="textInput" placeholder="Paste your text here..."></textarea>
  <div class="buttons">
    <button id="indent2">Indent 2</button>
    <button id="indent4">Indent 4</button>
    <button id="remove2" class="remove">Remove 2 spaces</button>
    <button id="remove4" class="remove">Remove 4 spaces</button>
    <button id="removeIndent" class="remove">Remove all indentation</button>
    <button id="quote" class="quote">Quote</button>
    <button id="unquote" class="remove hidden">Unquote</button>
  </div>
</div>

<script type="module">
const textInput = document.getElementById('textInput');
const removeIndentBtn = document.getElementById('removeIndent');
const indent2Btn = document.getElementById('indent2');
const indent4Btn = document.getElementById('indent4');
const remove2Btn = document.getElementById('remove2');
const remove4Btn = document.getElementById('remove4');
const quoteBtn = document.getElementById('quote');
const unquoteBtn = document.getElementById('unquote');

function updateQuoteButtons() {
  const text = textInput.value;
  if (!text.trim()) {
    unquoteBtn.classList.add('hidden');
    return;
  }
  
  const lines = text.split('\n');
  const nonEmptyLines = lines.filter(line => line.trim().length > 0);
  const allQuoted = nonEmptyLines.length > 0 && nonEmptyLines.every(line => line.startsWith('> '));
  
  if (allQuoted) {
    unquoteBtn.classList.remove('hidden');
  } else {
    unquoteBtn.classList.add('hidden');
  }
}

textInput.addEventListener('input', updateQuoteButtons);

removeIndentBtn.addEventListener('click', () => {
  const text = textInput.value;
  const lines = text.split('\n');
  const processed = lines.map(line => line.replace(/^\s+/, '')).join('\n');
  textInput.value = processed;
  updateQuoteButtons();
});

indent2Btn.addEventListener('click', () => {
  const text = textInput.value;
  const lines = text.split('\n');
  const processed = lines.map(line => '  ' + line).join('\n');
  textInput.value = processed;
  updateQuoteButtons();
});

indent4Btn.addEventListener('click', () => {
  const text = textInput.value;
  const lines = text.split('\n');
  const processed = lines.map(line => '    ' + line).join('\n');
  textInput.value = processed;
  updateQuoteButtons();
});

remove2Btn.addEventListener('click', () => {
  const text = textInput.value;
  const lines = text.split('\n');
  const processed = lines.map(line => {
    if (line.startsWith('  ')) {
      return line.slice(2);
    }
    return line;
  }).join('\n');
  textInput.value = processed;
  updateQuoteButtons();
});

remove4Btn.addEventListener('click', () => {
  const text = textInput.value;
  const lines = text.split('\n');
  const processed = lines.map(line => {
    if (line.startsWith('    ')) {
      return line.slice(4);
    }
    return line;
  }).join('\n');
  textInput.value = processed;
  updateQuoteButtons();
});

quoteBtn.addEventListener('click', () => {
  const text = textInput.value;
  const lines = text.split('\n');
  const processed = lines.map(line => '> ' + line).join('\n');
  textInput.value = processed;
  updateQuoteButtons();
});

unquoteBtn.addEventListener('click', () => {
  const text = textInput.value;
  const lines = text.split('\n');
  const processed = lines.map(line => {
    if (line.startsWith('> ')) {
      return line.slice(2);
    }
    return line;
  }).join('\n');
  textInput.value = processed;
  updateQuoteButtons();
});

// Initial check
updateQuoteButtons();
</script>
</body>
</html>
```

**Key changes:**

1. **Added Quote button** (green) - Adds `> ` to the beginning of every line
2. **Added Unquote button** (red, initially hidden) - Removes one level of `> ` from each line
3. **Smart visibility** - The Unquote button only appears when all non-empty lines start with `> `
4. **Multiple levels** - Both buttons can be clicked multiple times to create nested quotes like:
   ```
   > > > This is a triple-quoted line
   ```
5. **Updates on changes** - The button visibility updates whenever you type or click any button

Try pasting some text and clicking Quote multiple times to see the nesting effect!
