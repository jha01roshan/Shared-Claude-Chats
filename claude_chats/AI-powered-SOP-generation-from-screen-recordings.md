# AI-powered SOP generation from screen recordings

- Source: https://claude.ai/share/83ccac69-0e75-43d1-aeaf-c15bab0f1027
- Author: Daddy
- Created: 2026-03-12
- Messages: 13

---

## Human

I’m playing with the idea of pairing a AI model that’s good at video understanding, and screen recording various finance folks takes, having the AI annotate heavily the process (effectively building a standard operating procedure or training guide) and then from that document and May and maybe from a list of screenshots create a agent skills file and related folder so that an AI agent can automate that process.  

Do some web research, maybe starting with artificial analysis or some sort of well-known leaderboard about video understanding and computer screen understanding and recommend a AI model for the first part of this though screen, understanding and documentation part. Of note, my company does have an install installation and agreement with UIpath which may have an offering that fits here, but I want to know what are the best tools and ideally AI models to do this as well as maybe a breakdown of maybe some that are more cost efficient while still being capable

---

## Assistant

Let me research the current landscape for video/screen understanding models.
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

This is a really compelling pipeline idea, Alex. The "screen record → AI-annotated SOP → agent skill file" workflow essentially bridges the gap between tribal knowledge and automation. Let me break down what the research shows.

---

## The Screen Understanding Landscape

The key benchmark for your use case is **ScreenSpot-Pro**, which specifically measures a model's ability to understand and locate UI elements in real professional desktop software (think Excel, SAP, internal banking apps). This is exactly what you need — a model that can watch someone navigate a GL reconciliation in Excel or pull a report in your core system and understand *what's happening*.

**Gemini 3 Pro is the runaway winner here.** On ScreenSpot-Pro, Gemini 3 Pro scores 72.7%, compared to 36.2% for Claude Sonnet 4.5 and a shockingly low 3.5% for GPT-5.1. That's a 20x gap over GPT on screen understanding tasks. This benchmark specifically probes how well a model can read screenshots of real software — menus, dialogs, spreadsheets — and answer questions or choose actions.

On top of that, Gemini 3 Pro scores 87.6% on Video-MMMU, which evaluates knowledge acquisition from videos, suggesting strong ability to process and reason across temporal and spatial dimensions simultaneously. This is exactly the "watch a screen recording and understand the process" capability you need.

GPT-5.2 has since improved with its Thinking mode — GPT-5.2 Thinking scores 86.3% on ScreenSpot-Pro, up from 64.2% for 5.1 — but it's more expensive and the Thinking mode latency may not matter for your batch-processing use case.

## My Recommendation: Tiered Approach

### Tier 1 — Best Quality: Gemini 3 Pro
- **Why:** Dominant screen understanding, native video input, 1M token context window (you can feed it very long recordings)
- **Cost:** ~$2/1M input tokens, $12/1M output. Video input consumes 258 tokens per second at a sample rate of one frame per second. So a 10-minute screen recording ≈ 154,800 tokens ≈ $0.31 input cost. Very affordable.
- **Key advantage:** You can ask questions about specific points in time within the video using timestamps, and Gemini 3 introduces granular control over multimodal vision processing with the media_resolution parameter.
- **Practical note:** Has a free tier in AI Studio for prototyping

### Tier 2 — Cost-Efficient: Gemini 2.5 Flash
- **Why:** Dramatically cheaper ($0.15/1M input), still has solid multimodal capabilities, supports video input
- **Cost:** A 10-minute recording would cost roughly $0.02. You could process hundreds of recordings for dollars
- **Trade-off:** Lower screen understanding accuracy, but may be "good enough" for well-narrated recordings where the voice-over carries much of the context

### Tier 3 — Budget with open-source control: Qwen2-VL or InternVL
- These are open-weight models you could self-host, but they score poorly on ScreenSpot-Pro (under 20%). Not recommended for your use case unless privacy is paramount.

## The SOP Generation Tools Landscape

Several purpose-built tools already do exactly what you're describing for Step 1 (recording → SOP):

- **Fluency** — Enterprise-focused, SOC2 certified, generates production-ready process documentation from screen recordings in minutes. Used by Aon for payment operations documentation. Probably the closest to what a regulated bank would want for compliance reasons.
- **Scribe** — Browser extension that auto-captures clicks and generates step-by-step guides in real time. Very popular but web-only.
- **Kommodo** — Works with any screen recording including desktop apps, multi-tool workflows, and legacy systems. Upload an MP4 and your SOP is generated in under 2 minutes.
- **Clueso** — Combines screen recording with both video guides and written documentation output

## UiPath — You Already Have This

Since Synovus has UiPath, this is worth serious consideration. UiPath actually has **two** relevant products:

1. **Task Capture** — Records workflows in detail, auto-generates process maps, and exports to Microsoft Word as a PDD or directly to UiPath Studio as a .xaml workflow skeleton. This is the "SOP generation" step.

2. **Task Mining** — AI-driven, collects employee desktop data and logs it upon each user action (mouse click, keystroke), then leverages AI to analyze the data and identify automation candidates. The March 2025 release added audio capture with voice input, where voice is transcribed and summarized by an LLM for each step.

The huge advantage here is the **end-to-end pipeline already exists**: Task Capture/Mining → Process Definition Document → Automation Hub → Studio automation. You wouldn't need to build the "SOP to agent skill" bridge yourself.

The disadvantage is that UiPath's screen understanding AI is nowhere near Gemini 3 Pro's capabilities, and the tooling is Windows-only and fairly rigid.

## What I'd Actually Build If I Were You

Given your existing UiPath license and your interest in AI agents, I'd consider a **hybrid approach**:

1. **Record** using any screen recorder (OBS, Loom, even built-in macOS/Windows tools)
2. **Process with Gemini 3 Pro API** to generate a heavily annotated SOP with timestamps, UI element identification, decision points, and business logic extraction. The 1M context window means you can include the full recording plus a system prompt that instructs it to output in a specific structured format (your "agent skill file" schema)
3. **Feed the structured output** into either UiPath (for RPA-style automation) or into an AI agent skills framework (for LLM-agent-style automation via something like your n8n workflows)

The Gemini step would cost pennies per recording and produce dramatically richer documentation than any of the purpose-built SOP tools, because you can prompt it to extract not just "what buttons were clicked" but "why this decision was made" and "what business rules govern this step."

Want me to sketch out what that Gemini prompt and skill-file schema might look like? Or dig deeper into any of these tools?

---

## Human

does UI pass in the task capture application does it include screenshots that could be included in the agent skills folder? “UiPath — You Already Have This
Since Synovus has UiPath, this is worth serious consideration. UiPath actually has two relevant products:
	1.	Task Capture — Records workflows in detail, auto-generates process maps, and exports to Microsoft Word as a PDD or directly to UiPath Studio as a .xaml workflow skeleton.  This is the “SOP generation” step.”

---

## Assistant

Yes — based on what I found in the earlier research, this is actually one of Task Capture's core features. By default, Task Capture generates screenshots for every action you perform — mouse clicks, keyboard inputs, and hotkeys. You can specify the actions you want to record in the Capturing settings page.

And on the editing/export side: Every screenshot can be edited and annotated, and information can be edited or added for every step. The export options include Microsoft Word format as a PDD, JPEG image, or workflow template (.xaml format) to other UiPath platforms.

So the screenshots are there and annotatable, but the question for your agent-skills-folder use case is whether you can get them as **individual image files** programmatically rather than just embedded in a Word doc. The JPEG export option suggests yes, but let me dig a bit deeper on the actual file structure.
```
This block is not supported on your current device yet.
```

Yes, Task Capture is actually quite rich with screenshots. Here's the full picture:

**What it captures:** By default, Task Capture generates screenshots for every action you perform — mouse clicks, keyboard inputs, and hotkeys. So you're getting a screenshot-per-click level of granularity, not just periodic snapshots.

**What's in each step:** Each captured sequence includes Title and Description, Estimated time, Type of action (e.g. Left Mouse Click), and a screenshot. Plus it collects selector data (the unique UI element identifier) and process statistics like execution time and text entries.

**Where screenshots live during capture:** During the recording, Task Capture stores all the data related to the current process document in the %appdata% folder. Screenshots are saved in the Temp folder and the current process .ssp file in the Backup folder.

**Export formats that include screenshots:**
- **Word PDD** — screenshots embedded in the document with each step
- **JPEG** — the workflow diagram as an image
- **.ssp file** — Task Capture's native format (contains all the raw data)
- **ZIP archive to Automation Hub** — The recorded .ssp, .docx, .xaml and .jpg files are compressed into a ZIP archive and uploaded to Automation Hub.

**The practical gap for your agent-skills use case:** The screenshots are definitely there and extractable, but Task Capture doesn't natively export a folder of individual step-by-step screenshot image files with metadata sidecar files (which is what you'd ideally want for an agent skills folder). You'd need a small extraction step — either pulling the images from the Word doc programmatically (python-docx makes this trivial), pulling them from the .ssp file, or grabbing them from the %appdata%/Temp folder during/after capture.

The **XAML export** is actually the most interesting piece for your second stage (turning the SOP into an agent skill), because the XAML file includes the selectors and the unique identifier of an element on the screen — that's essentially the "where to click" data that an automation agent would need.

So the pipeline could be: Task Capture → .ssp + XAML + Word PDD → Python script to extract screenshots + selectors + step descriptions → structured agent skills folder. You already have the UiPath license, and the extraction script would be pretty straightforward. Want me to sketch that out?

---

## Human

Ok sick. So the idea is seed an agent skills folder with content from the “Task Capture → .ssp + XAML + Word PDD → Python script to extract screenshots + selectors + step descriptions → structured agent skills folder. “

Then i also have an agent skill for building n8n workflows, but I can’t decide if that’s too rigid vs just loading this into a Claude Cowork folder and letting Claude handle without the n8n framework. 

Thoughts

---

## Assistant

This is the right question and honestly the answer probably isn't either/or — it's about matching the automation approach to the *type* of process the skills folder describes.

Think about the finance processes your team does as sitting on a spectrum:

**Left side — Deterministic, mechanical:** Download a report from core, reformat columns, paste into a template, email to a distribution list. These are pure "if this, then that" chains. Every run is identical. n8n is perfect here because you get an auditable, repeatable workflow that runs the same way every time. For a regulated bank, that determinism matters — when internal audit asks "how does this process work," you can show them a literal flow diagram with no ambiguity.

**Right side — Judgment-heavy, contextual:** Review GL exceptions and decide which ones need escalation vs. which are normal month-end timing differences. Analyze a borrower's financials and flag concerns. Draft commentary on budget variances. These require the kind of reasoning and pattern-matching that makes a rigid n8n workflow either impossible to build or so full of branching logic that it becomes unmaintainable.

**The messy middle:** Most real finance processes are a mix. Pull data (mechanical) → review and classify (judgment) → format output (mechanical) → send with appropriate context (judgment). This is where it gets interesting.

Here's my practical take given your setup:

**Use n8n for the "plumbing."** Data extraction, API calls, file movements, scheduling, triggering. n8n is great at orchestration and gives you the audit trail Synovus compliance will eventually ask about. Your existing n8n skill already handles this well.

**Use Claude (via Cowork or API call within n8n) for the "thinking."** The steps in the skills folder where the human was making a judgment call, interpreting something on screen, or writing something contextual. The screenshots and step descriptions from Task Capture become the context that teaches Claude *what good looks like* for that specific decision.

**The hybrid pattern would look like:** n8n workflow hits a node that says "now classify these GL entries" → calls Claude API with the relevant skills folder content as system context + the actual data as the user message → Claude returns structured output → n8n picks up the structured output and continues the mechanical steps.

The reason I'd push back on going *pure* Cowork-folder is threefold. First, you lose the scheduling and triggering — someone has to remember to open Cowork and ask it to run the process. Second, you lose the audit trail of exactly what happened and when, which matters at a $100B bank. Third, you lose the ability to handle the mechanical parts cheaply and deterministically without burning tokens on "please download this file and rename it."

The reason I'd push back on going *pure* n8n is that you'll spend weeks trying to encode human judgment into conditional logic, and the resulting workflow will be brittle and need constant maintenance when the process changes slightly.

So the skills folder format should actually be designed with *both consumers in mind* — structured metadata that n8n can parse (selectors, URLs, field names, sequence order) alongside rich contextual descriptions and screenshots that Claude can reason over. Same folder, two consumers, each reading the parts they need.

Want me to draft what that dual-purpose skills folder structure would look like?

---

## Human

Yes do that, make a detailed workflow diagram first, then do that. 

Of more , I don’t want to do n8n builds manually. That should be done by the agent using the n8n skill and playwright MCP to build the n8n and “see it” and test it. 

The n8n build should be done with full context of the task at hand from our task capture. And the n8n agent should be super aware of when it needs to employ agentic steps vs deterministic

---

## Assistant

Great clarification — the agent building the n8n workflow autonomously using the skills folder as its blueprint is the right way to think about this. Let me build both artifacts.
```
This block is not supported on your current device yet.
```

---

## Assistant

```
This block is not supported on your current device yet.
```

There's your six-phase pipeline. Now let me build the skills folder specification — the actual file structure and schemas that make all of this work.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Here's what you're looking at across both files:

**The workflow diagram** traces six phases: capture → extraction → classification → autonomous n8n build → test → production. The critical loop is in Phase 4 where the agent uses Playwright to visually verify what it built and self-correct before testing.

**The skills folder spec** is the real meat. A few key design decisions worth calling out:

**The `classification` field on every step is the most important thing in the whole spec.** It's what tells the builder agent "use a Code node here" vs "call Claude API here." The classification framework at the bottom gives the agent clear, non-ambiguous rules for making that call — and importantly, the reasoning is documented so you can audit *why* a step was automated a certain way.

**The `n8n_implementation` block per step** is essentially a build instruction card. For deterministic steps it specifies exact node types and configs. For agentic steps it tells the agent exactly which context files to concatenate into the system prompt — so the Claude API call within n8n gets the full business rules, exceptions, and rich descriptions without the builder agent having to guess what's relevant.

**The `quality_gate` pattern on agentic steps** is the compliance answer. Every judgment call gets a confidence score, and anything below threshold routes to a human. That's your audit trail for regulators — the system either decided with high confidence or asked a person.

**The GL reconciliation example is intentionally realistic** to your world so you can pressure-test the schema against a process you actually do. The business rules, seasonal considerations, Pinnacle merger notes — those are the kind of details that make the difference between a demo and something that actually works in production.

Want me to build the Phase 2 Python extraction script next, or would you rather start with the builder agent's system prompt?

---

## Human

compare this functionality to existing UIPath tools or products. Use Websearch.

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

Now I have a thorough picture. Here's the honest comparison:

---

UiPath has been building toward almost exactly the same vision you've designed, but they've done it as separate products that don't fully connect yet. Let me map your six phases against what they offer.

## Phase 1 (Capture) — UiPath has this covered

Your pipeline starts with Task Capture, and UiPath actually has *three* layers here. **Task Capture** is what you already use — manual recording of a known process, exporting PDDs, XAMLs, and screenshots. **Task Mining** goes further by passively recording employee desktops across multiple people, then using ML to discover common patterns and identify automation candidates you didn't even know about. As of March 2025, Task Mining added voice capture with LLM-powered summarization per step. **Process Mining** complements both by analyzing system logs (ERP, CRM, core banking) to understand the macro process flow.

The important gap: none of these tools produce the *richness* of context your skills folder spec captures. Task Mining identifies "what was clicked" across employees. Your pipeline extracts "why it was clicked, what business rule governed the decision, and what exceptions exist." UiPath's tools output PDDs and automation candidates. Yours outputs a complete knowledge package.

## Phase 2 (Skills Folder Generation) — UiPath has nothing equivalent

This is the biggest differentiator in your pipeline. UiPath's discovery tools produce outputs designed for *human developers* to read and then manually build automations. Task Capture generates a Word doc. Task Mining generates traces and PDDs. These feed into Automation Hub as prioritized opportunity lists that a developer picks up and builds from.

Your skills folder is fundamentally different — it's a machine-readable knowledge package designed for an *agent* to consume. The structured JSON schemas, the step classification metadata, the business rules in markdown, the test scenarios — none of this exists in UiPath's product suite. Their outputs are documents for people. Yours is a standardized API for agents.

The Gemini enrichment layer is also entirely absent from UiPath. They capture clicks and keystrokes but don't use multimodal AI to extract business logic, decision rationale, or contextual meaning from recordings.

## Phase 3 (Step Classification) — UiPath has the philosophy but not the automation

UiPath talks extensively about exactly the same deterministic-vs-agentic spectrum. Their CEO Daniel Dines explicitly frames it as "robots are the left brain (deterministic), agents are the right brain (goal-based)." Their best practices documentation says the same thing your classification framework does — use deterministic tools for predictable tasks, use agents for judgment calls. Even their 10 Best Practices blog says verbatim: "for deterministic tasks, use tools rather than letting the agent directly act."

But here's the thing: in UiPath's world, a *human developer* makes the classification decision. A person looks at the process, decides which steps are mechanical vs. judgment-heavy, and manually builds the appropriate node types. Your pipeline automates this classification — Claude reads the skills folder and programmatically tags each step, generating the workflow blueprint. That's a fundamentally different approach and it's faster by an order of magnitude.

## Phase 4 (Autonomous n8n Build) — UiPath has the closest competitor here

This is where UiPath has invested most heavily, and it's worth understanding what they've built:

**Autopilot for Studio** offers "text to workflow" — describe an automation in natural language and it generates the initial workflow scaffolding. UiPath reports a 70%+ acceptance rate for generated workflows. But it's generating *scaffolding* that a developer refines, not production-ready workflows. And the input is a text description, not a structured skills folder with rich context.

**Agent Builder** is their low-code tool for creating AI agents. It supports system prompts, input/output arguments, tool definitions (including existing UiPath automations as tools), evaluation datasets, and tracing. It's model-agnostic and supports integration with LangChain and LlamaIndex. Agents can be published to Orchestrator and invoked within larger workflows via the Run Job activity. This is genuinely capable, and it's conceptually similar to your agentic steps calling Claude API within n8n.

**ScreenPlay** (formerly UI Agent) is their newest and most interesting product. It's a runtime agent that takes natural language instructions and autonomously executes UI tasks — clicking, navigating, typing — using Large Action Models. Their Screen Agent powered by GPT-5 ranked #1 on the OSWorld-Verified benchmark. ScreenPlay is *self-healing* — it adapts when UIs change without needing selector updates. It supports Windows, Linux, and macOS.

ScreenPlay is arguably more powerful than your Playwright MCP approach for the specific task of *interacting with UIs*, because it understands UI semantics rather than relying on fixed selectors. But ScreenPlay is designed for *executing* UI tasks in production, not for *building* workflows in an n8n editor.

**Maestro** is the orchestration layer that ties everything together. It uses BPMN 2.0 for process modeling and DMN for decision logic. It orchestrates robots, agents, humans, and third-party AI (including Google Vertex, Databricks, Snowflake connectors) in long-running workflows. It has case management, SLA tracking, human-in-the-loop escalation, and process apps for business user visibility. As of the 2025.10 release, it supports 30 curated BPMN templates across industries.

## Phase 5 (Test & Validate) — UiPath has enterprise-grade testing

UiPath's **Test Cloud** and **Autopilot for Testers** is more mature than what your pipeline specifies. They offer automated test generation from requirements, self-healing test automation, performance testing, and autonomous testing agents. Your test_scenarios.json approach is functionally similar but simpler.

## Phase 6 (Production & Monitoring) — UiPath has deep advantage here

**Orchestrator** provides enterprise-grade scheduling, monitoring, audit trails, credential management, and role-based access control. Maestro adds process-level KPI monitoring, bottleneck detection, and continuous optimization. The UiPath AI Trust Layer provides governance, PII masking, agent guardrails, and compliance controls. For a $100B regulated bank, this infrastructure matters.

---

## So where does this leave you?

The honest assessment is that your pipeline is **better at three things** and UiPath is **better at three things**, and the interesting question is whether they're complementary or competitive.

**Your pipeline wins on:**

1. **Knowledge capture depth.** Your skills folder is dramatically richer than anything UiPath produces. Business rules, exception handling, contextual reasoning, test scenarios, dual-consumer design — UiPath's PDDs are documentation. Yours is an agent's brain.

2. **Autonomous classification and build.** UiPath requires a human developer to decide what's deterministic vs. agentic and manually build accordingly. Your pipeline automates the classification and the build, which is a 10x speed advantage if it works reliably.

3. **Cost and flexibility.** n8n is open-source. Claude API calls cost pennies. You're not locked into UiPath's licensing model, which at enterprise scale is significant. You can swap models (Gemini for video, Claude for reasoning, Sonnet for cost-efficient classification) without vendor constraints.

**UiPath wins on:**

1. **Enterprise infrastructure.** Orchestrator, Maestro, AI Trust Layer, credential management, RBAC, audit trails, PII masking. Building this from scratch on n8n is possible but substantial. For Synovus compliance, this matters.

2. **UI execution.** ScreenPlay with the #1 OSWorld ranking is genuinely more capable than Playwright for interacting with desktop applications, especially legacy banking apps with complex UIs. It self-heals when UIs change. Your pipeline would struggle with FIS Horizon's UI in ways ScreenPlay might not.

3. **Scale and support.** 10,000+ enterprise customers, dedicated banking solutions, SOC2/ISO certifications, vendor support contracts. When internal audit asks "who supports this," "UiPath" is a different answer than "our custom n8n pipeline."

**The real play is probably hybrid:**

Use UiPath's capture tools (Task Capture, Task Mining) as input to your pipeline → run your Python extraction + Gemini enrichment to create the skills folder → use Claude to classify steps and generate the workflow blueprint → but instead of building in n8n, use the blueprint to guide Agent Builder + Maestro construction. You get the knowledge depth of your approach with the enterprise infrastructure of UiPath. The skills folder becomes the bridge between their discovery tools and their execution tools — filling the gap they haven't closed yet.

The other option is to build a proof of concept entirely on your stack (n8n + Claude + Playwright) for internal finance processes where compliance pressure is lower, prove the value, and then make the case for whether to migrate to UiPath infrastructure or keep running independently. That lets you move fast now without waiting for UiPath feature alignment.

---

## Human

What would you name this skill workflow or product?

---

## Assistant

A few directions depending on what you want the name to emphasize:

**If you want it to feel like an internal product your team built:**

- **Forge** — you're forging automations from raw process recordings. "Run it through Forge" works as a verb. Clean, one word, memorable.
- **Blueprint** — literally what the skills folder is. "We Blueprinted the GL recon process" works conversationally.
- **Imprint** — the SME imprints their knowledge, the agent absorbs it. Has a nice human-to-machine transfer connotation.

**If you want it to signal the AI-native angle for leadership presentations:**

- **AgentSmith** — it's a smith that forges agents. Also a fun Matrix reference that technical people will catch.
- **ProcessDNA** — you're extracting the DNA of a process and using it to clone execution capability.

**If you want something that describes the pipeline honestly:**

- **Capture → Classify → Build** (CCB) — boring but self-documenting. Finance people love three-letter acronyms.
- **SkillForge** — explicitly ties the skills folder concept to the build pipeline.

**My actual recommendation:**

**Forge.** One syllable. Works as a noun ("the Forge pipeline") and a verb ("we forged that process yesterday"). Implies taking raw material and shaping it into something useful, which is exactly what the pipeline does — raw recordings become production automations. It's also humble enough that nobody will roll their eyes when you present it to the CFO, but distinctive enough that your team will actually use the name.

What tone are you going for?
