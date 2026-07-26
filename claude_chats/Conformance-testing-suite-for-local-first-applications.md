# Conformance testing suite for local-first applications

- Source: https://claude.ai/share/df001d9f-e700-4b8e-be4e-b28470f7f5cf
- Author: Rich
- Created: 2026-05-24
- Messages: 12

---

## Human

So I'm building a conformance testing suite for a specific type of application. (https://github.com/richbodo/personal_network_toolkit) I think it's going to help me build this specific type of application faster when I want to build applications, because it really spells out a lot of architectural constraints. I've talked to you about this one before, and I feel the framing is unique, but I'm wondering if there is something like this already being used as a conformance test suite for applications, perhaps in another domain. The domain that I'm targeting is local-first contact and relationship data applications in general.   Is a standard developing among agentic coding organizations around a format for conformance tests when building applications? I have to think that inside Anthropic or OpenAI, where they test their models and build a lot of internal applications specifically testing to see how they perform on coding. I imagine that something like conformance tests is used there, and they're probably pretty sophisticated. It could be that they have conformance test suites. They may have published one. Could you see if you could look for one somewhere or something like it so that I can see what else is out there that's similar to my effort? Thanks.

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


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Looked into this carefully. There are several distinct things in this space and your framing sits in an interesting gap between them — let me lay out what I found.

**The closest direct analog: Solid's Conformance Test Harness**

The Solid project (Tim Berners-Lee's decentralized personal data ecosystem) has the cleanest precedent for what you're building. The [`solid-contrib/conformance-test-harness`](https://github.com/solid-contrib/conformance-test-harness) runs conformance tests against the Solid specifications, with test cases derived from annotated spec documents, EARL/RDFa reports for tool interop, and a "test subject" description model for the implementation under test. The Inrupt writeup from mid-2025 describes it as the mechanism that "guarantees implementations interoperate as intended" across a decentralized ecosystem of independent servers. Same domain neighborhood as yours (user-owned data), same load-bearing role (interop across many implementations of one spec), and a similar shape — a spec plus a programmatic check that an implementation honors it.

The big difference: Solid is conformance for *servers implementing a protocol*, not for *applications implementing an architectural pattern*. That's structurally simpler. You're declaring conformance against a class of applications that vary on six axes, which is closer in spirit to a "reference architecture" than a protocol.

**The agentic-coding space: SDD, but not what you're doing**

Spec-Driven Development consolidated as a methodology between mid-2025 and now. The canonical tools — [GitHub Spec Kit](https://github.com/github/spec-kit), AWS Kiro, OpenSpec, BMAD-METHOD, Tessl, Google Antigravity — all share the same loop: write a spec → generate a plan → decompose into tasks → implement. GitHub Spec Kit even has a `constitution.md` concept that's pretty close to your universal architectural commitments — "immutable principles that govern how specifications become code," enforced as guardrails during agent runs. There's an arXiv paper from January 2026 ([2602.00180](https://arxiv.org/abs/2602.00180)) titled *Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants* that frames the field.

But — and this is the key point — every one of these tools is for writing the spec *for your specific app*. They're spec authoring environments. None of them ship a *domain-specific conformance spec* you can attest against. Spec Kit gives you the machinery to declare your own constitution; it doesn't hand you the PNA constitution. Your toolkit is one level up: it's the spec that someone else's Spec Kit project would attest conformance to.

**What Anthropic and OpenAI actually publish for testing applications**

I looked specifically for what the frontier labs publish in this space. Three findings:

The standard public artifacts are *coding-agent benchmarks* — SWE-bench Verified, Terminal-Bench, SWE-bench Pro — which measure "can the agent patch a real GitHub issue and pass the existing test suite." These are evals for the *agent*, not conformance tests for a *class of applications*. Anthropic's [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) writeup explicitly frames this distinction: capability evals that graduate into regression suites. It's about whether Claude can code, not whether the resulting code conforms to a category-specific blueprint.

The Model Context Protocol — Anthropic's own protocol — has an [open issue (#1990)](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1990) requesting an official conformance test suite, and the [MCP roadmap](https://modelcontextprotocol.io/development/roadmap) lists "Conformance Test Suites: automated verification that clients, servers, and SDKs correctly implement the specification" as an active investment area. So even MCP doesn't have a finished one yet. There are *implementer-side* conformance docs (e.g. the DinCoder one I found cross-references spec sections to checklist items, which is very close to the structure you have in `spec/contracts/`).

I couldn't find anything from either Anthropic or OpenAI that's a *published, domain-specific conformance suite for a class of applications*. The Anthropic C compiler experiment used the existing C conformance tests (which already existed independently of Anthropic), which is suggestive: when they wanted a conformance target, they reached for one from a standards body, not one they'd built themselves.

**Other domain-specific application conformance suites worth looking at**

A few in other domains that have the same shape as what you're building:
- **HL7 FHIR** is the strongest cross-domain analog I know of — a spec for healthcare apps with formal conformance tooling (CapabilityStatements, profiles, ImplementationGuides). Multiple flavors of conforming apps, machine-checkable contracts, reference servers. Worth looking at FHIR's `CapabilityStatement` resource specifically — it's structurally similar to your axes attestation.
- **xAPI LRS Conformance Test Suite** — 1,300 criteria for Learning Record Stores, with a public registry of conformant implementations.
- **W3C Web Platform Tests (WPT)** — the conformance suite browsers attest against, with EARL-style reports.
- **EU Interoperability Test Bed (ITB)** — a generic harness with the test-subject + actor + test-suite model that Solid borrowed from.

**What's actually novel in your framing**

Putting all that together, the genuinely new thing in PNT isn't the conformance-suite-for-an-app-class part (FHIR, Solid, xAPI have been doing that for years). It's the *axes + slot map* approach: a single spec that admits multiple legitimate flavors, each declaring which slot picks it implements, with typed contracts at every load-bearing interface. FHIR has profiles, but those are constraints on a single canonical schema; your axes are more like a Cartesian product of valid configurations, each a first-class conformance target.

The other novel piece is the explicit AI-readability framing — the typed contracts in `spec/contracts/` (JSON Schema, OpenAPI, SQL DDL, TS interfaces) are the load-bearing thing, with prose specs derived from them. FHIR has this property too but inherited it from being a healthcare interop spec; you're doing it because the spec's primary readers are agents. That's the right bet given where SDD is going.

**Practical recommendation for comparison reading**

If you only have time for a few, I'd order it: Solid CTH first (closest spirit, closest domain), then FHIR's CapabilityStatement model (best example of a spec where many valid implementations declare conformance against a slot-like surface), then Spec Kit's constitution.md (closest tooling pattern in agentic land — and worth checking whether your typed contracts could plug in as a constitution for downstream Spec Kit projects building PNAs). MCP's pending conformance work is worth tracking but isn't published yet.

The short answer to "is a standard developing": yes, but at the tooling layer (SDD methodologies), not at the application-class layer. You're early in the application-class layer. That's a reasonable place to be standing.

---

## Human

So I'm reading through Solids conformance test suite, and it kind of reads like it was made pre-AI.  I think it will work fine for agents, in fact they will love it, but it might be overkill to adopt it's architecture.  It seems like it is there more to test applications, and wasn't thought of as a thing that agents will use to build applications.  Is there anything you see there that we can borrow for personal network toolkit?  I do think maybe conformance test suite is the wrong language for what the personal network toolkit is, because it's a way for agents to build and validate apps meeting behavioral characteristics, but it's not a test suite for instances of a specific app, per se.  Solid conformance is operating on what I would call a specific application or protocol suite, rather than validating an application as posessing certain behaviors and architectural characteristics.

---

## Assistant

You're putting your finger on something real. Solid's CTH is fundamentally an *evaluative* artifact — it inspects a finished thing and asks "does it conform?" Your toolkit is *generative* — it's the thing an agent reads to know how to build a conformant thing in the first place. Same word "conformance," very different workflow. The CTH treats the implementation as opaque and pokes at it from outside. PNT is white-box from the start because the agent is reading the spec while building.

That generative-vs-evaluative split is the cleanest framing I have for the distinction. Once you see it, a lot of what's in Solid CTH stops being load-bearing for you.

**What's actually borrowable from Solid**

A few things genuinely transfer:

The *test-subject description* pattern is useful. Solid uses Turtle files declaring what the implementation claims to be — what server, what version, what optional features it supports. Your axes attestation does exactly the same job, and the `Architecture.md` in `fellows_local_db` that "declares spec-version conformance and the per-slot specializations" is functionally a test-subject description. Worth knowing you've reinvented a well-tested pattern. Solid's choice to put it in a structured machine-readable format (RDF) rather than prose is the thing to copy — your axis picks should probably end up in a YAML or JSON file an agent can parse cold, not buried in prose in a per-impl README.

The *spec-annotation* pattern is also useful: Solid annotates spec documents with test-case identifiers so the connection between spec assertion and test is bidirectional. You can pull a section of the spec and immediately know which contracts it generates; you can pull a contract and immediately know which section it derives from. For PNT this would mean each AC in `PNA_Spec.md` carries a stable ID that the matching sub-contract in `spec/contracts/` references back to. That's traceability you'll want anyway when contracts evolve.

The *EARL vocabulary* (Evaluation and Report Language, W3C) is worth knowing about but probably not worth adopting. It's a machine-readable result format for "subject X passed/failed assertion Y." If you ever produce conformance reports for a real PNA, EARL is the standard. But you're not in the report-generation business — you're in the contract-satisfaction business. Skip it unless and until you want third parties to publish conformance claims about apps they've built.

What I'd *not* borrow: the live-server test harness model (alice/bob accounts, Docker images, HTTP-level wire validation). That's appropriate for protocol conformance where the implementation is a black-box network endpoint. Your contracts get satisfied at build time by the agent reading the typed schemas and producing code that compiles against them. The "test" is "does the implementation type-check against the contracts for its declared axis picks." That's a different beast entirely.

**On the terminology**

You're right that "conformance test suite" is the wrong frame for what PNT is, and I think it's worth being precise about why. Here are some candidate framings, ordered by how well I think they fit:

*Buildable spec* or *generative spec* — emphasizes that the spec is designed to be read by builders (agents), not just by auditors. The output of consuming the spec is an application, not a report.

*Application-class blueprint* — emphasizes that PNT defines a *class* of applications (not a single one), and that conformance is per-axis-pick rather than per-spec. This is what your README already calls it and I think it's underrated.

*Reference architecture with typed contracts* — emphasizes the load-bearing distinction from prose reference architectures. Most reference architectures (TOGAF, NIST SP 800-160) are advisory. Yours has machine-checkable contracts attached, which makes it categorically different — the contracts are the conformance mechanism, not a separate test suite layered on top.

*Protection profile* — this is the term of art from Common Criteria security evaluation. A Protection Profile defines the security requirements for a *category* of products (e.g., "operating systems," "smart card readers"), against which specific products are then evaluated. The structure — category-level spec + per-implementation attestation against it — is genuinely close to what you're building. The CC world also has the concept of a *Security Target*, which is a specific product's claim "this is the Protection Profile I'm implementing, here's how." That maps very cleanly onto your reference designs declaring axis picks. I wouldn't adopt CC terminology wholesale (it's heavy and security-flavored), but the conceptual model is worth knowing.

*OWASP ASVS-style verification standard* — ASVS (Application Security Verification Standard) defines requirements for "is this app secure?" with three conformance levels. The level-based model — "I claim Level 2 conformance" — is structurally similar to your axes. Apps don't pass or fail ASVS; they attest to a level. That's much closer to your model than Solid's binary pass/fail.

If I had to pick one phrase for PNT, I'd say it's a *generative architectural blueprint with typed conformance contracts for an application class*. That's a mouthful, but every word is doing work:
- *generative* — designed to be consumed by builders, not auditors
- *architectural blueprint* — the artifact is structural guidance, not a protocol or schema
- *typed conformance contracts* — the load-bearing checking happens at the contract layer
- *application class* — many valid implementations, distinguished by axis picks

In casual conversation just calling it a blueprint is fine. In the spec itself I'd lean away from "conformance test suite" toward something like "conformance framework" or "conformance contracts" or just "the spec." The word "test" in particular implies runtime evaluation and is the bit that misleads readers about what they're looking at.

One last thought: if you keep the word "conformance" anywhere, make sure the spec defines what conformance *means* for a PNA in a short, blunt sentence near the top. Something like "A PNA conforms to this spec if it satisfies the universal architectural commitments and the axis-derived contracts for each of its declared axis picks." That single sentence does more to fix the reader's mental model than any amount of architectural prose, and it telegraphs immediately that conformance here is build-time and axis-relative, not runtime and uniform.

---

## Human

I'm going to restate the question because I do feel that applications like Lovable and Replit, these sort of SaaS systems that make applications with AI agents, must be doing this.  When I build an app with one of those systems, if it's a common type, it comes out one-shotted and fully formed and generally not exactly what I asked for, as if it's being built to a spec or blueprint.  Maybe their blueprints are their secret sauce. I know that today people are calling every spec an eval, but if they've published something, then they're the ones with the experience doing this. Organizations like Replit and Lovable and Factory would have the right form for what I'm trying to make with the personal network toolkit. I wonder if they have released this kind of learning to the open source world, even in a blog post or video or something. It'd be very interesting to know. Maybe the model vendors would be more interested in letting that info out.  Can you do some searching for that particular type of blueprint or spec system from a company that has an app builder?  Thanks.

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

Searched hard for this. Short answer: yes, these companies are doing exactly what you're describing, and a fair amount of it is now in the open — but the surprising thing is that what they have is *thinner* and *more stack-coupled* than what you're building. Let me show you what's actually out there.

**The canonical leaked-prompts repo**

The mother lode is [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) (123k stars, fork count north of 30k). It has the extracted system prompts and internal tool definitions for v0, Cursor, Manus, Same.dev, Lovable, Devin, Replit Agent, Windsurf, Bolt, Augment Code, Kiro, Leap.new, Claude Code, and a couple dozen others. Mirror repos exist (CL4R1T4S, ntreq/Leaked-system-prompts) but x1xhlol is the actively maintained one. The "Lovable" and "Replit" subdirectories are the most directly relevant to your question.

What you actually find when you read these:

Lovable's agent prompt is mostly *stack and style enforcement*. Snippets that came up in search results: `PERFECT ARCHITECTURE: Always consider whether the code needs refactoring given the latest request` and `CRITICAL: The design system is everything. You should never write custom styles in components, you should always use the design system and customize it and the UI components (including shadcn components)...`. The "blueprint" is: React + Vite + Tailwind + shadcn/ui + Supabase, plus a list of MUSTs about how those components compose. There's no domain-specific layer — it's the same prompt whether you're building a CRM or a recipe app. Lovable's "secret sauce" turns out to be ruthless consistency about one stack, not a library of per-app-class specs.

Replit Agent is similar but multi-agent: Plinius's leak (April 2025) revealed it's actually two prompts — an initial code-generation agent and a follow-up agent — with a ReAct-style loop and role-specialized sub-agents (manager + editor). Langchain has a [decent breakdown](https://www.langchain.com/breakoutagents/replit) of the architecture. Again, the system prompt is mostly about *how* to build, not *what class of app* you're building.

Bolt's prompt (publicly open-sourced, since Bolt itself is) sits in the same shape — stack rules (WebContainer, Vite, TypeScript), tool-use protocol, output format requirements.

**The closest official thing to what you're building: Replit Enterprise custom templates**

This is the find I'd point you to first. Replit has [public documentation](https://docs.replit.com/teams/custom-templates) for an Enterprise feature where customers create their own templates by writing a `custom_instruction/instructions.md` file. The docs describe it almost word-for-word in PNT terms:

> *"This is the most important file in your template — it tells Agent how your organization builds software. Agent injects this file directly into its system prompt with a preamble that frames it as company-provided guidance."*

And the suggested content is:

> *"Architecture patterns: How your apps should be structured. Coding standards: Naming conventions, file organization rules, linting expectations. Component usage: Which libraries and components to use (and which to avoid). API patterns: How to call your backend services, handle authentication, manage errors. Testing requirements. Deployment guidelines."*

This is the published mechanism that's structurally closest to what you're doing — but the scope is per-organization, not per-application-class. A bank uses this to encode "how Acme Bank builds React apps." Nothing stops you from using it to encode "how all PNAs are built," but Replit hasn't published a library of such per-class instructions; they expect customers to write their own.

GitHub Spec Kit's `constitution.md` is the same pattern at a different scope — per-project rather than per-org. The arXiv SDD paper from January (2602.00180) explicitly treats "constitution + spec + plan + tasks" as the consolidated 2026 pattern.

**What's notably absent in the open**

Here's the interesting gap. Across all the leaked prompts and all the official docs:

- *None of them ship a published library of per-application-class specs.* You can't go to Lovable's site and download "the PNA spec" or "the CRM spec" or "the marketplace spec." If they have such things internally as templates or fine-tuning data, they haven't released them.
- *Templates as starter projects exist* (Bolt, Replit, v0 all have galleries of "here's a SaaS dashboard template, here's a chat app template"), but those are code skeletons, not architectural blueprints with typed contracts.
- *The leaked prompts are the explicit ones, and they're stack-flavored, not domain-flavored.* The implicit knowledge — "what does a good chat app look like, what does a good CRM look like" — is in the model weights, not in any spec document.

That gap is exactly where PNT sits. You're filling in the layer that the commercial app-builders deliberately abstract over (because their business model requires them to handle "any app") with a domain-specific blueprint someone else's agent can consume. Lovable's prompt says "use shadcn"; your spec says "if you pick axis storage:opfs-sqlite-wasm, your worker init handshake must conform to this JSON Schema." Different altitude entirely.

**What's worth actually reading**

If you want to spend a focused hour digging:

The Lovable agent prompt in [`x1xhlol/.../Lovable/Agent Prompt.txt`](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/blob/main/Lovable/Agent%20Prompt.txt) is probably the single most condensed example of a "build app to spec" system prompt that's in production at scale. Read it for the structural choices (how they handle refactoring decisions, design system enforcement, the "not every interaction requires code changes" framing). You'll see what kinds of rules are load-bearing for an agent producing apps, which will help you decide what should be in the prose of your spec versus in the contracts.

The Replit Agent prompts (initial + follow-up) are interesting for the multi-agent decomposition, which is more relevant to *building* a PNA than to specifying one.

The Replit Enterprise [custom templates docs](https://docs.replit.com/teams/custom-templates) are the official, supported, by-a-real-company explanation of "how you encode an architectural blueprint into an agent's behavior." The doc structure is the closest thing to a "how to write a PNT-shaped artifact" guide that exists in vendor documentation right now. If you wrote up your spec's deliverables in the same five-section structure (architecture / coding standards / components / APIs / testing), it would slot into a Replit Enterprise template without modification.

**The takeaway**

Your bet that the app-builder companies have richer per-class blueprints than what you're making — turns out to be roughly half right. They have richer *stack* blueprints (Lovable's prompt is meaningfully more sophisticated than most spec docs you'll see) but they have *no public per-application-class blueprints*. The model vendors haven't released anything in this space either; Anthropic's published artifacts are all eval-shaped, not blueprint-shaped.

So PNT is genuinely a step beyond what's been published. Whether anything richer exists behind closed doors at Lovable or Replit or Anthropic, I can't tell you — but the gap in the open ecosystem is real, and your toolkit is filling it.

---

## Human

So I greatly appreciate this entire conversation, because from the first prompt down through this last response, we have surveyed the playing field around application class specification. I feel that local-first applications that use contact data are an application class. Although I don't have a great definition of an application class, after looking at some of these, I do think a Replit Enterprise template or custom template could be used to do almost exactly the same thing. It's just not going to have the specific architectural considerations that are required for a local-first.
I should mention this survey that we've done and its findings in the Personal Network Application Toolkit as just research on prior art. Although a lot of the research found that there wasn't anything exactly like what we are doing, it'd be good to have these references and to show that we have examined the domain of application templating and conformance specifications for this type of blueprint. I think you're right. I think maybe I just continue to call this a generative blueprint for application class that's pretty much going to be separate from these other things.
Can you create a markdown file with a list of each resource we checked in this entire session, from the first prompt on, and its proximity to generative application class blueprints, contrasting those and showing where Personal Network Toolkit fits? I think, in the end, I think generative application class blueprints are a good idea, and we should continue with Personal Network Toolkit. That's pretty much my conclusion, but I'd like you to just create a markdown file with that research and that conclusion that Personal Network Toolkit fits here and it's not like these other things. We will therefore continue working because it has the specific architectural constraints for our application class and it's a better fit for what we're doing.  i'll include that research survey in the repo. thanks.

---

## Assistant

Going to write this up as a clean research artifact you can drop into the repo.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Done. Structured it around the four-property working definition (generative + class-scoped + multi-flavor + machine-checkable) so the positioning argument has a clear yardstick, with a proximity matrix at the end that makes the "PNT occupies the empty quadrant" claim visible at a glance.

One small thing worth flagging: I left the section about Replit Enterprise's `custom_instruction` mechanism with the framing that PNT could "slot into it without modification" — that's a useful claim for the repo but you may want to verify it yourself before it ships, since I haven't actually run a PNT-shaped artifact through their template system. If you keep that line, possibly soften to "with little reshaping" (which is what I already used) or just "the deployment target whose structure most closely matches PNT's."

Also: if you want, the working definition could be a separate short doc that the spec itself references (so "generative application class blueprint" becomes a defined term in PNT's vocabulary). That would let the spec's preamble say something crisp like *"A PNA spec is a generative application class blueprint per the four-property definition. See PRIOR_ART.md."* But that's a refinement for later — the survey as it stands does its job.

---

## Human

Side quest: Intuitively I feel like karpathy going to anthropic, the state of affairs in what we have been discussing, lets call it "application templating", and the continual release of anthropic features, none of which suggest a centralized dependency outside of tokens, but most of which now seem to focus on gathering local context, aims at a sort of natural anthropic app store, but it makes almost more sense to me that they would want to have a "blueprint store" that gives you the blueprints for cheap, and you build upon those to make your apps with their tokens.  It's weird because it hasn't been done, but it makes business sense to me, and logical sense in general.  I doubt most users would want it, but the builders would, so if they wanted to, they could release a builders blueprint store and allow builders to either give their stuff away there in the hopes of getting other revenue, or sell stuff there.  Maybe not because they have been so focuses on models to date, but have you noticed that everything karpathy is doing now is about context and not the models?

---

## Assistant

Let me check the Karpathy claim first — that one's a factual question and I want to make sure I'm not pattern-matching to something that didn't happen.
```
This block is not supported on your current device yet.
```

Quick correction on the Karpathy piece, because the actual story is more interesting than the framing you're working with: yes, he joined Anthropic — confirmed last Tuesday, May 19, just five days ago. But he's going to **pre-training**, under Nick Joseph. He's specifically building a team focused on "using Claude to accelerate pre-training research." That's roughly the opposite direction from context engineering — it's the deepest model-building layer, with Claude as the tool to make better Claudes. He has been *talking* about context a lot publicly (Software 3.0, the LLM-OS framing, agentic context windows), but the career move is back to the substrate, not to the application layer. So the "everything Karpathy is doing now is about context" reading doesn't really hold once you see where he actually went.

That said, the larger thesis you're putting together is more solid than that one data point. Let me engage with it on its own terms.

The pattern you're identifying in Anthropic's product direction is real. MCP, Skills, Claude Code, memory, web search, Claude in Chrome/Excel/Cowork, the Computer Use API, the recently expanded code-execution sandboxes — almost none of these are end-user-facing applications. They're all infrastructure for *getting context into Claude* and *letting Claude take actions in the user's environment*. The strategic posture is: we make the model, we make the protocols and primitives, you (the builder) compose them into applications. Anthropic doesn't sit between the builder and the end user the way Apple sits between a developer and an iPhone owner. They sit underneath.

Given that posture, an end-user app store would be off-strategy. They'd suddenly have to do curation, payments, refunds, content moderation of consumer-facing products — none of which is in their muscle memory. A builder-facing blueprint store fits the existing posture much better. The customers are already buying tokens; selling blueprints alongside is a natural extension, not a category jump.

The thing worth knowing, and you'll find this interesting, is that **Anthropic already shipped the primitive form of this.** Skills — the SKILL.md folders Claude reads before doing tasks like creating Word docs or PDFs or analyzing data — are exactly the shape of what you're describing. They're prepackaged best-practice blueprints that the agent consumes at the start of a task. Right now Skills are mostly bundled in the product (the docx skill, the pptx skill, the data-analysis skill) plus some user-uploaded skills in a user-skills folder. There's no marketplace, no third-party publishing, no commerce. But the artifact format already exists, and the consumption pattern is in production. Going from "Skills bundled with Anthropic products" to "Skills marketplace where third parties publish" is a small UI/commerce/policy lift, not a new product category. They've already built the runtime.

The MCP Registry shows they're comfortable with the marketplace concept on the tools side. A Skills Registry on the blueprints side would be the same move at the next layer up. PNT in that world would be a single Skill (or a collection of related Skills) that an agent reads when a builder says "build me a personal network application."

The reasons it hasn't happened yet are probably more boring than strategic: marketplaces need curation, safety review, payment infrastructure, dispute resolution, and a critical mass of supply. Skills are too new for any of that to be ready. But if you squint at the trajectory — MCP launches as an open protocol in late 2024, MCP Registry stands up in 2025, Skills ship in 2025, Skills marketplace would be the logical 2026-or-2027 move — it's a plausible roadmap, and a builder-tier blueprint store is exactly the shape that makes sense given how the rest of the product surface is laid out.

The part of your intuition I'd push back on is that "most users wouldn't want it, but the builders would." I'd actually flip it: the *direct* market is small (working professional builders), but the *indirect* market is everyone. A blueprint store full of PNAs, CRMs, study apps, household tools, etc. would mean every end user with a Claude subscription effectively has a one-prompt path to a working app in any of those classes, with the blueprint doing the heavy lifting silently. That's much closer to an end-user feature than a builder feature — the builder is just an intermediate distributor. Apple App Store works the same way: the customer is the end user, the supplier is the builder, and the platform owner's job is curation and infrastructure. A blueprint store would have the same shape, just with the artifact-being-sold one layer of abstraction lower.

So your intuition that this should exist is, I think, right. The piece you're missing is that the primitive is already shipped and is called Skills. The piece you're getting right is that nobody has yet turned it into a marketplace, and there's no obvious reason it couldn't be the next move.

---

## Human

That move by Karpathy makes way more sense than my guess did.  Thanks.  For PNT, This does not quite fit into a /skill or I would make it one.  Building the reference apps feeds the spec and the apps in a virtuous loop, so there is no conventional path that makes this more accessible like adding to /skill-creator repos.

---

## Assistant

You've put your finger on a real structural mismatch. A Skill is a static knowledge bundle — agent reads it, applies it, done. The skill format has no slot for "and here's how this knowledge itself evolves through being used." PNT's spec gets sharper every time you build a reference app, because reference apps surface where the spec was ambiguous or wrong. That's not a bug in PNT; it's the actual mechanism by which the spec gets good. The Skill format assumes someone else did that loop already, off-stage, and you're just consuming the polished output.

The pattern you're describing is closer to how mature specs actually develop than to how Skills work. HL7 FHIR is the cleanest example — there's a *living* working-group process where the spec and reference servers co-evolve, and there's a *frozen* versioned distribution (R4, R5) that implementers attest against. The living loop happens in the repo and committee; the distribution layer is just stable snapshots. FHIR didn't have to choose between those two modes because they're answering different questions: how does the spec get better, and how does someone consume a stable version of it.

PNT could do the same thing, eventually. The repo stays the place where the virtuous loop lives. When a version of the spec gets stable enough to be useful externally, you cut a tagged release — at which point that frozen snapshot *could* be packaged as a Skill (or whatever the equivalent is in 2027). But you only do that when there's enough demand from external builders to justify the freeze. Right now there isn't, and trying to make it Skill-shaped prematurely would actually fight against the loop you've got going.

The other option worth keeping in mind: PNT could eventually be served by an MCP server rather than packaged. An agent building a PNA queries the server for the current spec + the contracts for its declared axis picks, and the server is always pointing at HEAD. That dissolves the static/living tension entirely — there's no frozen snapshot, just a live spec the agent reads when it needs to. It's also heavier infrastructure than you need today.

For now I think you've got it right: the conventional accessibility paths don't fit, and forcing one would distort the artifact. Keep building reference apps, let the spec sharpen against them, and the accessibility question can wait until the spec is stable enough that other people want to build against it. At that point the path will be obvious — probably a tagged release plus whichever consumption format has won by then.
