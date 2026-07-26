# Chat compaction and context reduction

- Source: https://claude.ai/share/9e24f1d6-cec9-4ae2-9710-f7bbc1c80e30
- Author: Sean
- Created: 2026-02-28
- Messages: 16

---

## Human

In a long running chat I noticed that you compacted the chat before answering. Is that using a summary of the chat to reduce the size of the context?

---

## Assistant

Yes, exactly. When a conversation gets very long, Claude compacts the earlier portions of the chat history by summarizing them — condensing what was discussed into a shorter representation — so that the full context fits within the model's context window. The recent messages stay intact, but older parts get replaced with a summary. This lets the conversation continue without hitting the context limit while preserving the most important information from earlier in the chat.

---

## Human

That is a nice contrast to ChatGPT, where long chats will completely stall and I need to open I new chat just to answer a new, but related question.

---

## Assistant

Yeah, that's a real quality of life difference. ChatGPT hitting a hard wall where it just stops working mid-conversation is pretty frustrating, especially when you've built up a lot of context and now have to either start fresh or manually re-explain everything. The compaction approach is much more graceful — the conversation just keeps going, and while some early detail might get smoothed over in the summary, the thread of the conversation stays intact.

---

## Human

Does that happen automatically with API calls, or does that need to be implemented. If so, how?

---

## Assistant

For API calls, it does **not** happen automatically — that's a Claude.ai product feature. When you're using the API directly, you're responsible for managing the context window yourself.

For your own implementation, the main approaches are:

**Manual truncation** — just drop the oldest messages from your conversation history array when it gets too long. Simple but lossy.

**Summarization** — when the conversation gets long, make a separate API call asking Claude to summarize the earlier portion of the conversation, then replace those messages with a single message containing that summary. This is essentially what Claude.ai is doing.

**Prompt caching** — for cases where you have a long, stable system prompt or reference material, you can use Anthropic's prompt caching feature to cache that content so it doesn't count against your processing costs on every call, though it still counts against the context window.

Given your Python background and the API work you've been doing, the summarization approach is pretty straightforward to implement — you'd track token count using something like `anthropic`'s token counting endpoint, and when you get close to your limit, trigger a summarization pass on the oldest N messages before continuing. Anthropic's Python SDK makes this reasonably clean to set up.

---

## Human

How do you know when the context is long enough to need summarization, and how do you decide how much to replace with a summary?

---

## Assistant

Good questions. For detecting when to summarize, you have a couple of options:

**Token counting** — the Anthropic Python SDK has a `count_tokens` method (or you can use the `beta.messages.count_tokens` endpoint) that lets you check the token count of your message list before sending. You'd set a threshold, say 75-80% of the model's context window, and trigger summarization when you cross it. This is the most precise approach.

**Message count heuristic** — simpler but less accurate, just summarize after every N messages. Works fine for predictable conversation patterns but can miss cases where individual messages are very long.

For deciding how much to replace with a summary, the typical strategy is to summarize everything except the most recent few exchanges — maybe keep the last 4-6 messages intact. The reasoning is that the most recent context is almost always the most relevant to what's happening right now, so you want that verbatim. The older stuff gets collapsed into a summary that captures key decisions, facts established, and important context.

You could also be more sophisticated and keep the system prompt plus a rolling summary message plus the recent raw messages as your three-part context structure. Each time you need to compact, you re-summarize by feeding the existing summary plus the next oldest chunk into a summarization call, producing an updated summary. That way the summary grows incrementally rather than you doing one big summarization pass when things get critical. It's a bit more complex to implement but produces better results in very long-running conversations.

---

## Human

What os the context window for current Claude models?

---

## Assistant

Let me check the current documentation for accurate numbers.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Here's the current picture:

**Standard context window:** 200,000 tokens by default across Claude models, which works out to roughly 150,000 words or over 500 pages of material.

**Extended 1M token context window:** Claude Opus 4.6 and Sonnet 4.6 support a 1M token context window when using the `context-1m-2025-08-07` beta header, with long context pricing applying to requests exceeding 200K tokens.

One interesting side note relevant to our earlier conversation — Anthropic also offers server-side compaction in beta for Claude Opus 4.6, which provides automatic summarization that condenses earlier parts of a conversation, enabling long-running conversations beyond context limits with minimal integration work. So the manual summarization approach we discussed is something Anthropic is now offering as a managed API feature, at least in beta.

Also worth noting practically: even with a huge context window, performance can degrade as you approach the limit. Research shows that performance degrades substantially as models approach their limits — the "free" context space isn't wasted, it's where reasoning happens. So for agentic work, triggering compaction well before hitting the ceiling (say, at 75-80%) is better than waiting until you're nearly full.

---

## Human

Can you give me a comparison of context windows across major  AI models. formatted as a Markdown table?

---

## Assistant

```
This block is not supported on your current device yet.
```

Here's a current comparison table of context windows across major models:

| Model | Provider | Context Window | Notes |
|---|---|---|---|
| **Llama 4 Scout** | Meta | 10M tokens | Open source; largest available |
| **Grok 4.1** | xAI | 2M tokens | |
| **Gemini 2.5 Pro** | Google | 1M tokens | Standard; no beta header required |
| **Gemini 2.5 Flash** | Google | 1M tokens | Faster/cheaper Gemini option |
| **GPT-4.1** | OpenAI | 1M tokens | Full family (mini, standard) |
| **GPT-5** | OpenAI | 400K tokens | 128K output window |
| **Claude Opus 4.6** | Anthropic | 200K (1M beta) | 1M requires `context-1m-2025-08-07` header + tier 4 |
| **Claude Sonnet 4.6** | Anthropic | 200K (1M beta) | Same beta conditions as Opus |
| **GPT-4o** | OpenAI | 128K tokens | Older flagship |
| **Llama 4 Maverick** | Meta | 1M tokens | Open source enterprise variant |
| **Llama 3.1** | Meta | 128K tokens | Older Llama generation |
| **DeepSeek R1/V3** | DeepSeek | 128K tokens | Strong reasoning, very low cost |
| **Mistral Large** | Mistral | 128K tokens | |
| **Qwen3-Next** | Alibaba | 256K (1M ext.) | Extendable via additional config |

A few caveats worth keeping in mind: advertised context windows and real-world effective context windows differ meaningfully — the "lost in the middle" problem means information buried in the center of a huge context gets recalled less reliably than content at the edges. For practical purposes, staying well under the ceiling tends to produce better results than filling the window to capacity.

---

## Human

Can you give me the table formatted as markdown text instead of rendering it?

---

## Assistant

```
| Model | Provider | Context Window | Notes |
|---|---|---|---|
| **Llama 4 Scout** | Meta | 10M tokens | Open source; largest available |
| **Grok 4.1** | xAI | 2M tokens | |
| **Gemini 2.5 Pro** | Google | 1M tokens | Standard; no beta header required |
| **Gemini 2.5 Flash** | Google | 1M tokens | Faster/cheaper Gemini option |
| **GPT-4.1** | OpenAI | 1M tokens | Full family (mini, standard) |
| **GPT-5** | OpenAI | 400K tokens | 128K output window |
| **Claude Opus 4.6** | Anthropic | 200K (1M beta) | 1M requires `context-1m-2025-08-07` header + tier 4 |
| **Claude Sonnet 4.6** | Anthropic | 200K (1M beta) | Same beta conditions as Opus |
| **GPT-4o** | OpenAI | 128K tokens | Older flagship |
| **Llama 4 Maverick** | Meta | 1M tokens | Open source enterprise variant |
| **Llama 3.1** | Meta | 128K tokens | Older Llama generation |
| **DeepSeek R1/V3** | DeepSeek | 128K tokens | Strong reasoning, very low cost |
| **Mistral Large** | Mistral | 128K tokens | |
| **Qwen3-Next** | Alibaba | 256K (1M ext.) | Extendable via additional config |
```

---

## Human

Perfect. Test's another area ChatGPT struggles with  where you shine. ChatGPT will often drop into rendering the Markdown, even when I tell it not to.

---

## Assistant

That's a common frustration. The instruction-following gap is real — getting ChatGPT to consistently output raw markdown without rendering it often requires repeated nudging, and even then it sometimes slips back. It's one of those things that sounds like a small quality-of-life issue but gets genuinely annoying in practice when you're trying to copy content for use elsewhere.
