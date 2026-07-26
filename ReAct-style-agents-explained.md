# ReAct-style agents explained

- Source: https://claude.ai/share/b8f8d556-277e-44a7-8815-be8e91f199c8
- Author: Yves
- Created: 2026-06-08
- Messages: 6

---

## Human

What is a ReAct-style agent ?

---

## Assistant

A ReAct-style agent is an LLM agent that interleaves **reasoning** and **acting** in a loop—the name comes from "**Rea**soning + **Act**ing." It was introduced in a 2022 paper by Yao et al., and it became one of the foundational patterns for building tool-using agents.

The core idea is that instead of having the model either just think (chain-of-thought) or just call tools blindly, you let it alternate between the two in a structured cycle:

**Thought** → the model reasons about the current state and what to do next
**Action** → the model issues a tool call (search, API request, code execution, etc.)
**Observation** → the result of that action gets fed back in
…and then it loops back to **Thought**, using the new observation to inform its next step, until it decides it has enough to produce a final answer.

A toy trace looks like this:

```
Question: What's the population of the capital of France?

Thought: I need to find the capital of France first.
Action: search("capital of France")
Observation: Paris is the capital of France.

Thought: Now I need Paris's population.
Action: search("population of Paris")
Observation: Approximately 2.1 million.

Thought: I have what I need.
Answer: The population of Paris is about 2.1 million.
```

**Why it works well.** The reasoning steps keep the model grounded—it plans before acting and adapts when an observation contradicts its expectation. The action steps keep it factual, since it pulls real data from tools rather than hallucinating. The interleaving is the key: reasoning informs which action to take, and observations correct the reasoning. Pure chain-of-thought can reason its way confidently into a wrong answer; pure action-taking can't plan or recover from surprises.

In practice today, the "Thought/Action/Observation" text format from the original paper has largely been absorbed into native tool-calling APIs (function calling), where the model emits structured tool calls and the runtime feeds back results. But the underlying loop is still ReAct—it's the conceptual backbone behind frameworks like LangChain agents, LlamaIndex agents, and most custom agent loops you'd build yourself.

Given your RAG and agentic work, the main thing worth flagging is the trade-offs: ReAct loops can be token-hungry and occasionally get stuck in repetitive cycles (re-issuing similar actions), which is why people layer on things like step limits, reflection (e.g., Reflexion), or more structured planning (Plan-and-Execute) on top. Want me to sketch out how a ReAct loop differs from those alternatives, or what a minimal implementation looks like in a TS/Node setup?

---

## Human

link to the paper

---

## Assistant

```
This block is not supported on your current device yet.
```

Here's the paper: **ReAct: Synergizing Reasoning and Acting in Language Models** by Yao et al. (2022).

- arXiv abstract page: https://arxiv.org/abs/2210.03629
- PDF: https://arxiv.org/pdf/2210.03629

There's also a readable write-up from the authors on the Google Research blog if you want the lighter version: https://research.google/blog/react-synergizing-reasoning-and-acting-in-language-models/

One small correction to flag from what I said earlier: the work came out of Google Research's Brain Team, with Shunyu Yao (then a student researcher) as lead author. And it's worth noting the headline result for your purposes—on HotpotQA and Fever, ReAct addresses the hallucination and error-propagation problems that show up in pure chain-of-thought by interacting with a simple Wikipedia API, which is the grounding benefit I mentioned.

---

## Human

Elaborate on your last paragraph. No implementation.

---

## Assistant

ReAct's core contribution is best understood as a fix for the failure mode of pure chain-of-thought (CoT). When a model reasons via CoT, it isn't grounded in the external world and works only from its own internal representations, which limits its ability to reactively explore, reason, and update what it knows. The consequence is the familiar pathology: a model reasons fluently and confidently down a chain that's built on a wrong or stale premise, and because nothing external ever contradicts it, the error compounds at every subsequent step. That's the "hallucination and error propagation" problem.

ReAct breaks that closed loop by letting actions interrupt the reasoning. On HotpotQA and Fever, ReAct overcomes the hallucination and error-propagation issues prevalent in chain-of-thought by interacting with a simple Wikipedia API, and it produces human-like task-solving trajectories that are more interpretable than baselines lacking reasoning traces. The key word is *synergy*—it's bidirectional. Reasoning traces help the model induce, track, and update action plans and handle exceptions, while actions let it interface with external sources to gather additional information. So reasoning decides what to look up, the lookup injects a real fact, and that fact constrains the next round of reasoning—the model can't drift far from reality because it keeps getting pulled back to ground truth.

Two things from the paper are worth underlining for how you think about agent design:

First, the gains weren't marginal on the interactive tasks. On ALFWorld and WebShop—two interactive decision-making benchmarks—ReAct outperformed imitation- and reinforcement-learning methods by absolute success-rate margins of 34% and 10% respectively, while being prompted with only one or two in-context examples. That few-shot efficiency was a big part of why the pattern caught on: you got RL-beating behavior from a couple of prompt examples, no training loop required.

Second, ReAct alone wasn't strictly dominant on the QA tasks—the real winner was the hybrid. On HotpotQA and Fever, the best overall approach was a combination of ReAct and CoT that lets the model use both its internal knowledge and externally obtained information during reasoning. The takeaway is that grounding via tools and reasoning from internal knowledge aren't competitors; the strongest setup lets the model lean on its own priors when they're reliable and reach for external sources when they aren't. That tension—when to trust the model's internal knowledge versus when to force a retrieval—is exactly the design knob you're tuning in RAG and agentic pipelines.

The interpretability point is also more than a footnote. Because every step is an explicit thought or a named action with an observation, the trajectory is human-readable, which makes the system far easier to diagnose and steer when it goes wrong—a meaningful operational advantage over an opaque policy that just emits actions.
