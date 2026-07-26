# Opening SWE-bench in Chrome with Claude

- Source: https://claude.ai/share/81a0c519-c727-4caa-b0d4-0d866375d0da
- Author: Simon
- Created: 2026-02-19
- Messages: 10

---

## Human

Use claude in chrome to open https://www.swebench.com/

---

## Assistant

I'll open that website for you. Let me first check the browser context.
```
This block is not supported on your current device yet.
```

It looks like the Chrome extension isn't currently connected. Let me try to establish a connection.
```
This block is not supported on your current device yet.
```

It seems the Claude in Chrome extension isn't connected right now. To use it, you'd need to have Chrome open with the Claude extension installed and connected.

However, I can open that website using the built-in Playwright browser instead. Want me to go ahead with that?

---

## Human

how about now? I opened chrome

---

## Assistant

Let me check again!
```
This block is not supported on your current device yet.
```

Still not connecting. Let me try broadcasting a connection request — you should see a "Connect" button appear in the Claude extension in your Chrome browser. Click it when you see it.
```
This block is not supported on your current device yet.
```

Unfortunately it's still not detecting the extension. Here are a few things to check:

1. Make sure the **Claude in Chrome** extension is installed in your Chrome browser
2. Ensure the extension is **enabled** (check `chrome://extensions`)
3. Try clicking the extension icon in Chrome's toolbar to open it, then look for a "Connect" option

Alternatively, I can open the website using the built-in Playwright browser right now — would you like me to do that instead?

---

## Human

sure try that

---

## Assistant

```
This block is not supported on your current device yet.
```

The SWE-bench website is now open! It's showing the **Official Leaderboards** page, currently on the "Bash Only" tab. Here's what's on the leaderboard (top entries, all dated 2026-02-17):

| Model | % Resolved | Avg. Cost |
|---|---|---|
| Claude 4.5 Opus (high reasoning) | 76.80% | $0.75 |
| Gemini 3 Flash (high reasoning) | 75.80% | $0.36 |
| MiniMax M2.5 (high reasoning) | 75.80% | $0.07 |
| Claude Opus 4.6 | 75.60% | $0.55 |
| GLM-5 (high reasoning) | 72.80% | $0.53 |
| GPT-5-2 (high reasoning) | 72.80% | $0.47 |
| Claude 4.5 Sonnet (high reasoning) | 71.40% | $0.66 |
| Kimi K2.5 (high reasoning) | 70.80% | $0.15 |
| DeepSeek V3.2 (high reasoning) | 70.00% | $0.45 |
| Claude 4.5 Haiku (high reasoning) | 66.60% | $0.33 |
| GPT-5 Mini | 56.20% | $0.05 |

The page also has tabs for Verified, Lite, Full, and Multimodal benchmarks, plus a news section and links to related tools like SWE-agent and SWE-smith. Would you like me to explore any specific section?

---

## Human

Click on "Compare results" and then select "Select top 10"

---

## Assistant

```
This block is not supported on your current device yet.
```

The "Compare models" dialog is open. Now let me click "Select top 10".
```
This block is not supported on your current device yet.
```

Done! The top 10 models are now selected (all checkboxes checked), and a **"Compare results"** dialog has appeared with a bar chart. It's currently showing the "Resolved (bar chart)" view. Let me take a screenshot so you can see the chart:
```
This block is not supported on your current device yet.
```

Here's the comparison chart! It shows a bar chart of the **% Resolved** for the top 10 models on SWE-bench Bash Only. The models are quite competitive, ranging from about 66.6% (Claude 4.5 Haiku) to 76.8% (Claude 4.5 Opus with high reasoning) at the top.

You can also switch the visualization using the dropdown — options include "Resolved by repository", "Resolved vs cost (scatter plot)", "Cumulative cost distribution", and more. There are also buttons to export as PNG, JSON, or copy a link. Would you like to explore any of those?

---

## Human

See those bar charts? I want them to display the percentage on each bar so I can take a better screenshot, modify the page like that

---

## Assistant

Let me inspect the chart to understand what library it's using, then add the labels.
```
This block is not supported on your current device yet.
```

It's using Chart.js. Let me add percentage labels on top of each bar.
```
This block is not supported on your current device yet.
```

Let me try a different approach — drawing directly on the canvas after the chart renders.
```
This block is not supported on your current device yet.
```

Let me try drawing directly on the canvas without modifying the chart object.
```
This block is not supported on your current device yet.
```

Let me take a screenshot to verify the labels are showing.
```
This block is not supported on your current device yet.
```

The labels appeared but the bars disappeared due to the earlier plugin error corrupting the chart. Let me reload the page and do this cleanly.
```
This block is not supported on your current device yet.
```

Page reloaded. Now let me click "Compare results", then "Select top 10", and this time inject the labels cleanly.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Good, the chart is back. Now let me carefully add the labels using an inline plugin on the chart instance to avoid the recursion issue.
```
This block is not supported on your current device yet.
```

Let me take a screenshot to check the result.
```
This block is not supported on your current device yet.
```

The bars are there but the labels didn't render. Let me try a different approach — using `requestAnimationFrame` to draw labels on top of the canvas after Chart.js finishes.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

The percentage labels are now displaying on top of each bar. You can see all the values clearly: 76.8%, 75.8%, 75.8%, 75.6%, 72.8%, 72.8%, 71.4%, 70.8%, 70.0%, and 66.6%. 

Let me clean up the interval now that the labels are visible.
```
This block is not supported on your current device yet.
```

The chart now has percentage labels on every bar — ready for your screenshot! You can also use the **PNG** button in the dialog to download the chart directly as an image. Would you like me to do anything else with it?
