# Future technologies discussion

- Source: https://claude.ai/share/fe0684b4-c2d6-4eef-a370-c0847408622b
- Author: Lucas
- Created: 2026-07-01
- Messages: 2

---

## Human

Hi Claude! Could you discuss future technologies? If you need more information from me, ask me 1-2 key questions right away. If you think I should give you more context or upload anything to help you do a better job, let me know. Use any tools you have access to—like Google Drive, web search, etc.—if they'll help.

If it makes sense, create something we can look at together—like a visual, a checklist, or something interactive. Thanks for your help!

---

## Assistant

The user wants to discuss future technologies. This is a broad, open-ended request. Let me think about the best way to approach this.

The prompt asks me to:
1. Ask 1-2 key questions if I need more info
2. Tell them if they should give more context or upload anything
3. Use tools if helpful
4. Create something visual/interactive if it makes sense

"Future technologies" is very broad. There are many angles: AI, biotech, quantum computing, energy (fusion, solar), space, robotics, materials science, neurotech, climate tech, etc. And the person could be interested for many reasons — investment, career, curiosity, writing, business strategy, education.

Given the breadth, this is a genuine case where a bit of elicitation would help me give a much better answer. I have the ask_user_input_v0 tool available which presents tappable options — good for this. The system guidance says to use it for elicitation when I need to understand preferences to give useful advice, and NOT to default to it when it's unnecessary. But here the request is genuinely broad and the answer would differ a lot based on what they care about.

However — the prompt also says "If it makes sense, create something we can look at together." I want to be helpful and not just bounce back with questions and nothing else. The instruction for ask_user_input says: "Always include a brief conversational message before presenting options." And it also says my turn is done after calling it — the selection comes as their next message.

But there's tension: the user explicitly said "If you need more information from me, ask me 1-2 key questions right away." So they've invited questions. But they also want something to look at. 

I think the best approach: I could either (a) ask clarifying questions first, or (b) give a solid overview now AND create something, while asking what to dig into next. 

Let me reconsider. The user seems to want engagement and a deliverable. If I just ask questions with no content, that might feel like I'm stalling. But the request is SO broad that guessing wrong wastes their time on a big deliverable.

A good middle path: Give them a genuinely useful starting framing/overview of the landscape of future technologies, create a visual they can look at (a landscape map of emerging technologies with time horizons and maturity), AND ask 1-2 targeted questions about which direction to go deeper. That way they get immediate value + something visual + a clear path forward. This respects "ask 1-2 questions" AND "create something."

Actually, let me think harder about whether to ask first or deliver first. The tool description for ask_user_input says my turn ends when I call it. So I can't both call it and create a widget in the same turn (well, I technically could put the widget before it, but the tool says "After calling this, your turn is done — don't keep writing"). And the widget should come from a real deliverable.

Given the explicit invitation to ask questions "right away," and given how much the answer depends on their interest and purpose, I think a short, high-value approach is: create an overview visual of the future-tech landscape (immediate value, something to look at), then ask which area(s) they want to go deep on. This gives them something concrete to react to AND the questions become more grounded because they can point at the visual.

Hmm, but ask_user_input ends my turn. Can I show a widget then ask via the tool? The ordering: I'd do the widget first (show_widget), write a bit of text, then call ask_user_input as the final action. The ask_user_input instruction says "your turn is done — the user's selection comes as their next message." So calling it last is fine.

But wait — do I even need the ask_user_input tool, or can I just create a rich visual overview and pose questions in prose? The system says if I'm about to write clarifying questions as prose bullets, they should go in the tool instead. So if I want to ask, I should use the tool. But I could also just deliver a comprehensive, genuinely useful visual and offer directions in prose without formal "questions" — letting them steer.

Let me decide on the cleanest, most helpful path:

Plan:
1. Give a brief conversational intro.
2. Build an interactive/visual artifact: a "Future Technologies Landscape" — I'll use the visualize:show_widget tool to make an interactive map. This is inline visual content that renders in chat, which fits "something we can look at together." I should call visualize:read_me first (silently) before show_widget.
3. Then ask 1-2 targeted questions via ask_user_input to figure out where to go deep (their purpose + which domain), so the next round is tailored.

Actually, let me reconsider the tool choice for the visual. Options:
- visualize:show_widget — renders inline SVG/HTML in chat. Great for a landscape diagram or interactive explorer. This is the "look at together" inline experience.
- An artifact via create_file (.html or .jsx) — renders in the artifact panel, more substantial, good if they'll keep/iterate.

For a first-pass "let's explore together" visual, an interactive inline widget is ideal and low-friction. But show_widget with lots of content could be complex. Alternatively, I could build a proper interactive HTML artifact that's an explorable "future tech landscape" — clickable cards by domain, time horizon, maturity. That's more of a keepable deliverable.

Given "create something we can look at together—like a visual, a checklist, or something interactive," an interactive explorer is a strong fit. I think an inline widget via visualize:show_widget is the right call for immediacy, OR a full artifact. Let me go with an interactive artifact (HTML) because it can hold richer content (multiple domains, time horizons, filtering) and they can keep/iterate on it — and the prompt mentions "interactive" explicitly. But the tension: an artifact is bigger, and I'm also going to ask questions to tailor. Doing a big artifact before knowing their interest risks the "guess wrong" problem.

Let me resolve: The landscape OVERVIEW is useful regardless of their specific interest — it's the map that helps them decide where to zoom in. So building a broad interactive landscape now is not wasted; it's exactly the thing that helps them answer my question about where to go deep. So: build a broad but genuinely well-crafted interactive future-tech landscape, then ask which domain(s) + their purpose so I can go deep next.

For the visual, I'll use visualize:show_widget (interactive HTML) — it renders inline "together," is lighter than a full artifact, and I can make it genuinely interactive (filter by time horizon, click domains for detail). Actually, an inline widget via show_widget is perfect here. Let me do that.

Wait, one concern: show_widget HTML "Scripts are supported but execute after streaming completes." So interactivity via JS works. Good. And I must use CSS variables for theming, transparent background, no top-level padding. I need to read the read_me first for the interactive/data_viz modules.

Let me also decide: do I ask questions via ask_user_input, or just offer directions in prose? The user said "ask me 1-2 key questions right away." That's an explicit invitation. I'll use ask_user_input for a clean, tappable experience (mobile-friendly per the tool). Two questions max: (1) their primary purpose/lens, (2) which domain(s) to prioritize. Actually the tool allows up to 3 questions and multi-select. I'll do 2: purpose (single select) and domains of interest (multi-select). That keeps it to "1-2 key questions" as they asked.

But — ordering problem again. ask_user_input ends the turn and "the user's selection comes as their next message." show_widget renders inline. If I call show_widget and then ask_user_input in the same turn, is that allowed? I think tools can be called in sequence within a turn, and the final action being ask_user_input is fine. The widget renders, then the question UI appears, turn ends, user responds. That should work. Let me structure: intro text → read_me (silent) → show_widget → brief text → ask_user_input.

Hmm, actually the ask_user_input description says "Always include a brief conversational message before presenting options - don't show options silently." And "After calling this, your turn is done." So I'll write my message, show the widget, then a short bridge line, then the tool. 

Actually, I realize I should be careful not to overload. Let me reconsider whether to include BOTH a rich widget AND the question tool in one turn. It might be cleaner and equally helpful to: deliver the interactive landscape widget with good content, and pose the 1-2 questions right in my closing text as an invitation (not prose bullets that should be in the tool, but as a natural steer). But the system guidance is fairly clear that clarifying questions belong in the tool. Since the user explicitly asked me to "ask 1-2 key questions right away," using the tool honors that literally and gives a nice tappable UI. I'll use the tool.

Let me reconsider the "should you give me more context / upload anything" part. I should briefly note what would help — e.g., if they have a specific industry, a doc/strategy deck, or a decision they're facing, uploading it would let me tailor. I'll weave that in.

Do I need web search? Future tech is somewhat evergreen at the landscape level, and my knowledge to end of Jan 2026 is fine for a broad map. For specific "latest breakthroughs this month" I'd want search, but for a landscape overview and to then tailor, I don't need it yet. I'll mention I can pull latest developments via web search once they pick a focus. That's honest about the knowledge cutoff.

Let me now think about the actual CONTENT of the future-tech landscape so the widget is genuinely good, not generic. I'll organize by domains and time horizons and maturity. Let me draft the substance:

Domains (I'll pick ~8 major clusters):
1. Artificial Intelligence & Compute
   - Frontier/agentic AI, multimodal models, AI agents doing real work
   - AI for science (protein design, materials discovery)
   - Neuromorphic & photonic computing, specialized AI chips
   - On-device/edge AI
   - Near-term (0-3y): agents, AI coworkers, AI-designed drugs entering trials
   - Wildcards: significant automation of knowledge work

2. Biotechnology & Health
   - CRISPR/gene editing (base & prime editing), in-vivo editing
   - mRNA & programmable medicines, cancer vaccines
   - Longevity/senolytics, epigenetic reprogramming
   - Synthetic biology, engineered organisms, lab-grown/cultivated meat
   - Brain-computer interfaces (Neuralink et al.), neuroprosthetics
   - Organoids, xenotransplantation
   - Near-term: personalized cancer vaccines, more CRISPR therapies approved (Casgevy already approved)
   
3. Energy & Climate
   - Fusion (tokamaks, stellarators, private fusion — net energy gain milestones)
   - Next-gen fission (SMRs, molten salt)
   - Grid-scale storage (iron-air, sodium-ion, LFP), long-duration storage
   - Perovskite/tandem solar
   - Green hydrogen, electrolysis
   - Carbon capture (DAC), enhanced weathering
   - Geothermal (enhanced geothermal systems)
   
4. Space
   - Reusable heavy-lift (Starship), falling launch costs
   - Mega-constellations, satellite internet
   - Lunar return (Artemis), commercial LEO stations
   - In-space manufacturing, asteroid resources (long horizon)
   - Space-based solar (speculative)

5. Robotics & Autonomy
   - Humanoid robots (general-purpose), warehouse/logistics automation
   - Autonomous vehicles (robotaxis scaling in some cities)
   - Drones, autonomous shipping
   - Surgical & care robots
   - Embodied AI (robotics + foundation models)

6. Advanced Computing (beyond AI)
   - Quantum computing (error correction milestones, logical qubits) — still early
   - Post-quantum cryptography (NIST standards, migration underway)
   - Photonic computing, spintronics

7. Materials & Manufacturing
   - Advanced batteries (solid-state), new cathode/anode chemistries
   - Metamaterials, programmable/self-healing materials
   - 3D printing at scale, additive manufacturing of metals, bioprinting
   - Superconductors (ongoing search; room-temp claims unverified)
   - Nanomaterials, graphene applications maturing

8. Digital & Connectivity / Immersive
   - 6G research, low-earth-orbit connectivity
   - AR/spatial computing (headsets, glasses)
   - Digital twins, IoT at scale
   - Blockchain/decentralized systems (more niche, infra & tokenization)
   - Privacy tech, homomorphic encryption

Time horizons:
- Now–3 years (deploying/scaling): agentic AI, robotaxis in limited cities, SMR approvals, CRISPR therapies, humanoid robots in pilots, AR glasses, grid storage buildout
- 3–10 years (maturing): fusion pilot plants, broad BCIs for medical use, quantum advantage for niche problems, solid-state batteries, cultivated meat cost parity, longevity interventions in trials
- 10+ years / speculative (uncertain): AGI-level automation, room-temp superconductors, asteroid mining, whole-brain interfaces, space-based solar, molecular nanotech

Cross-cutting themes: convergence (AI×bio, AI×materials), energy as the bottleneck, compute as the new oil, dual-use/safety concerns, geopolitics of chips & critical minerals.

That's rich, credible content. I'll build an interactive widget where users can filter by time horizon and click a domain to see key technologies + status + what to watch. That's genuinely useful and something to "look at together."

Given the amount, an inline show_widget might get large but that's okay. Alternatively a full HTML artifact. Let me go with show_widget (interactive) since it renders inline and the user framed this as "look at together" and "interactive." Actually, for something this content-rich and interactive with filtering + detail panels, a full artifact (HTML file) might be cleaner and more robust, and they can keep/iterate. But show_widget is designed exactly for "renders inline alongside your text response... interactive HTML widgets." Both work. 

Decision: Use visualize:show_widget for an interactive "Future Tech Landscape Explorer." It's inline, immediate, interactive, and matches the collaborative "look at together" framing. I'll read the read_me first (interactive + data_viz + diagram modules — probably interactive is the key one; maybe data_viz). Platform: desktop (unknown → default desktop). The system prompt says I'm on web/mobile chat; I'll pass 'unknown' to be safe or 'desktop'. Since it could be mobile, but I don't have a strong signal, I'll pass 'desktop' (default) — actually the read_me platform param: pass 'mobile' when system prompt indicates mobile client. It says "web or mobile chat interface" — ambiguous. I'll pass 'unknown'. Hmm, but 'unknown' defaults to desktop sizing. Given many Claude users are on the app, mobile is plausible. But I can't tell. I'll go with 'desktop' as a reasonable default; the widget should be responsive anyway. Let me make the widget responsive so it works on both.

Now, should I do the widget AND the ask_user_input in the same turn? Let me reconsider once more. If I show a big interactive explorer, the user already has tons to engage with. Adding a formal question UI on top might be fine — it gives them a quick way to steer. I think it's good: explorer (immediate value) + one tappable question to direct the deep-dive. But ask_user_input ends the turn. The widget will have rendered. Then the question appears. Good UX.

But there's a subtlety: does calling ask_user_input after show_widget suppress or interfere with the widget? They're separate tool calls; both should render. I'll trust it works.

Let me limit to keep it clean: I'll ask ONE combined direction question via ask_user_input? The user said "1-2 key questions." I'll ask 2: (1) primary lens/purpose, (2) which domains to go deep on (multi-select). That's within their ask.

Actually, re-reading ask_user_input guidance: "Keep it to one question where possible — three is a ceiling, not a target — with 2-4 short, mutually exclusive options." And "if the answer is already there or inferable... use it." The user's purpose isn't inferable — could be curiosity, career, investing, writing, business. So asking purpose is legit. Domain interest also not inferable. Two questions is reasonable and matches their "1-2 questions." I'll do two.

Let me also make sure I don't over-format my prose per the tone guidelines — natural prose, minimal headers/bullets in the chat text. The widget carries the structured content; my chat text stays conversational.

Now let me reconsider: is doing all of this (silent read_me, show_widget with a fairly large interactive HTML, then ask_user_input) the right scope, or am I overengineering? The user gave an open, enthusiastic prompt inviting tools and a deliverable. A rich interactive explorer + a quick steering question is a strong, proportionate response. I'll proceed.

One more: the shell boundary. I'm not using bash/tmux/subagents. show_widget and ask_user_input are not shell. Good. No conflict.

Let me read the visualize read_me first (silently — I won't narrate it), then build the widget.

For the read_me modules: 'interactive' (it's an interactive widget with filtering/click), maybe 'data_viz' (there's a maturity/horizon element) and 'diagram' (landscape map). I'll request ['interactive', 'diagram', 'data_viz'] to be safe. Platform: I'll pass 'desktop'.

After reading, I'll craft the HTML widget. Let me plan the widget design:

Title: "The Future-Tech Landscape" 
Layout:
- A top filter bar: time horizon toggles (All / Now–3y / 3–10y / 10y+). Clicking filters which tech items show / dims domains.
- A grid of domain cards (8 domains), each with an icon (emoji or SVG), a one-line descriptor, and a few key technologies as chips with a small status/horizon indicator.
- Clicking a domain card expands a detail panel (or highlights) showing: the domain's key technologies, current status, and "what to watch." 
- Maybe a legend for horizon colors.

To keep it manageable in one HTML block with JS-after-streaming, I'll embed the data as a JS object, render cards, and add click handlers to show detail in a panel. Filtering by horizon dims non-matching chips.

I need to use CSS variables for theming per the read_me (I'll confirm variable names from read_me). Let me read it first.

Let me be mindful of length/complexity — I'll write clean, self-contained HTML/CSS/JS. Transparent background, no outer padding, responsive.

Let me proceed: call visualize:read_me (interactive, diagram, data_viz), desktop.

Actually, I realize I should decide platform more carefully. The system prompt: "Claude is currently operating in a web or mobile chat interface." No definitive signal. I'll pass 'desktop' but make the CSS responsive with a mobile breakpoint so it's fine either way. Good.

Let me write my response: a brief warm intro (a few sentences), then the widget, then a short bridge, then the question tool. Keep prose minimal and natural, no heavy formatting.

Let me draft the intro (concise):
"Happy to dive in. 'Future technologies' is a huge, exciting space, so I built you an interactive map of the major frontiers — the domains, the key technologies inside each, and roughly when they're likely to land (already scaling vs. this decade vs. still speculative). Tap the time filters and click any domain to see what's happening and what to watch."

Then after widget: note what would help me go deeper + the two questions via the tool. Also mention I can pull the very latest via web search once they pick a focus (honesty re: cutoff). And the upload suggestion.

Actually, the questions go in the tool, and the tool requires "a brief conversational message before presenting options." So between the widget and the tool, I'll write: what would sharpen this (their purpose + a doc/industry to tailor), that I can web-search latest once focused, and then pose the two questions via the tool. But I shouldn't write the questions as prose (they go in the tool). So my bridge text: "To take this from a map to something genuinely useful for you, two quick things: if you're coming at this from a specific angle — a career move, investing, a business/strategy decision, teaching, or just curiosity — tell me, and if you have a relevant doc, deck, or industry in mind, upload it and I'll tailor everything to it. I can also pull the latest 2026 developments via web search once we pick a focus. Quick steer:" then the tool.

That's clean. Let me write it, minding not to make the questions redundant with the tool. I'll phrase the bridge to set up the tool without duplicating its literal questions.

Let me build. First, read_me (silent).
</thinking>

Happy to dive in — "future technologies" is a huge, fast-moving space, so rather than dump a wall of text, I built you an interactive map of the major frontiers. It shows the key domains, the specific technologies inside each, and roughly *when* they're likely to matter (already scaling vs. this decade vs. still speculative). Give me one moment to put it together.
```
This block is not supported on your current device yet.
```



I've read the design guidance. Now let me build the interactive future-tech landscape widget. This is an "interactive" use case — an interactive explainer/explorer with controls (filter by time horizon, click a domain to see detail). I'll use HTML with inline styling, CSS variables, Tabler icons, no emoji, sentence case, two font weights.

Let me plan the widget structure carefully within the 680px width and design constraints:

Components:
1. sr-only h2 summary for accessibility.
2. A filter bar at top: time horizon toggle buttons (All / Deploying now / This decade / Speculative). These filter which domains/chips are emphasized.
3. A grid of domain cards (8 domains). Each card: leading Tabler icon, domain name (h3-ish, 16px/500), one-line descriptor (secondary), and 2-3 key technology chips with a horizon indicator (small colored dot or pill). Card is clickable → sets a detail panel.
4. A detail panel below the grid showing the selected domain's key technologies, status, and "what to watch." Default shows an intro/prompt to click, or shows the first domain.

Actually, given streaming constraints (no display:none during streaming), I should show all content stacked. The detail panel can be a post-streaming JS-driven element. The guidance says "Post-streaming JS-driven steppers are fine." And "No tabs, carousels, or display:none sections during streaming — hidden content streams invisibly." So the detail panel should either always show something, or be populated by JS after streaming. I'll make the detail panel show the first domain's detail by default (rendered in HTML so it's visible during streaming), and JS updates it on click. That avoids hidden content.

But if I render only the first domain's detail in HTML and the rest is in a JS data object, the other details aren't in the DOM during streaming — that's fine because they're generated by JS on click, not hidden with display:none. The guidance's concern is about content that's present in DOM but hidden (streams invisibly). Data in a JS object isn't "hidden DOM content" — it's just data. So that's acceptable. Good.

For the horizon filtering: I'll give each tech chip a data-horizon attribute (now / decade / spec). When a filter is active, chips not matching get dimmed (reduced opacity + muted), matching ones stay prominent. Domains with no matching chips could dim their card slightly. This is JS after streaming. During streaming, all show at full — fine.

Color encoding: I need ≤2 ramps ideally, and if colors encode meaning add a legend. Horizon is a meaningful category (3 states). I could encode horizon with 3 subtle colors + a legend. But the guidance says ≤2 ramps per diagram and prefers restraint. However this is an HTML widget (UI), not an SVG diagram — the "≤2 ramps" is more for diagrams. For UI, I can use semantic tints. Let me encode the three horizons with three distinct but calm colors and provide a legend:
- Deploying now (0–3y): teal/green tint (c-teal / --bg-success-ish)
- This decade (3–10y): amber tint
- Speculative (10y+): purple/gray tint

Actually to keep it clean and native, I'll use small pill badges with the CDS color ramps: 
- now → teal: bg #E1F5EE, text #0F6E56 (c-teal 50 / 600-800)
- decade → amber: bg #FAEEDA, text #854F0B (c-amber 50 / 800)
- speculative → purple: bg #EEEDFE, text #3C3489 (c-purple 50 / 800)

These have good text contrast per the palette table. And I'll add a one-line legend. Good — that satisfies "if colors encode meaning, add a legend."

Wait — the read_me says for text on colored backgrounds use the 800/900 stop from same ramp. Teal 800 = #085041, or 600 = #0F6E56. I'll use 800 for text to be safe on the 50 fill. Let me use:
- teal: bg #E1F5EE (50), text #085041 (800)
- amber: bg #FAEEDA (50), text #633806 (800)
- purple: bg #EEEDFE (50), text #3C3489 (800)

Good contrast.

But these are light-mode fills. Dark mode! The guidance stresses dark mode is mandatory and hardcoded light fills won't invert. Hmm. For badges with hardcoded hex, they won't adapt to dark mode — the light teal bg with dark teal text would still be readable on a dark page (light pill on dark bg is fine, text is dark on light pill — readable). Actually a light-colored pill with dark text sitting on a dark page background is perfectly readable in dark mode — the pill itself is a light island. So hardcoded light pills are okay in both modes as long as the text-on-pill contrast holds (dark text on light pill = fine). The risk is only if I put dark text on a dark-adapting surface. Since the pill bg is hardcoded light and text is hardcoded dark, contrast is fixed and fine in both modes. The pill just looks light in both modes. That's acceptable and common. Good.

For the rest of the UI (cards, text), I'll use CSS variables (--surface-2, --text-primary, --text-secondary, --border) which adapt automatically. Good.

Now, is 8 cards + detail panel + filter bar too much for one widget? It's substantial but manageable. The container is 680px. I'll use a responsive grid: `repeat(auto-fit, minmax(200px, 1fr))` → likely 3 columns at 680px, or I could do 2 columns for more room per card. With 8 domains, 2 columns = 4 rows, 3 columns wouldn't divide evenly (8 = 3+3+2). Let me use minmax(200px,1fr) which gives 3 cols at 680 (200*3+gaps ≈ 640). 8 cards → rows of 3,3,2. That's fine, last row has 2 cards spanning. Acceptable. Or minmax(210px,1fr). Let me keep cards compact: icon + name + descriptor + up to 3 chips. At 3 columns each ~205px wide, chips will wrap — 3 small pills might be tight. Let me consider 2 columns (minmax(300px,1fr)) → 2 cols, roomier, chips fit better, 4 rows. I think 2 columns reads better for content-rich cards. But 8 cards in 2 cols = tall widget. That's okay — vertical scroll in chat is normal.

Hmm, let me reconsider. Maybe fewer, denser: I'll go with `repeat(auto-fit, minmax(215px, 1fr))`. At 680px that's 3 columns (215*3=645). Cards will be compact. Each card shows icon+title, a 1-line descriptor, and I'll show 2 representative tech chips (not 3) to keep height reasonable, with the full list in the detail panel on click. That keeps cards tidy. Actually showing a small count like "6 technologies" plus 2 example chips could work, but simpler: show 2-3 short chips.

Let me simplify the card: icon + domain name + short descriptor + a subtle "View details" affordance is implicit (whole card clickable). And I'll show maybe 3 tiny horizon-dot chips isn't necessary. Actually the chips ARE the useful content and what the filter acts on. Let me keep chips but make them compact. I'll show up to 3 chips per card (the headline techs), each a small pill with a horizon color. The filter dims non-matching chips across all cards. That's the interactive payoff. Good.

Given 3 columns, 3 chips per card wrapping is fine if pills are small (font 11-12px, short labels). Let me keep chip labels short (1-2 words): e.g., "AI agents", "Fusion", "CRISPR", "Humanoids", "Quantum", "Solid-state", "Robotaxis", etc.

Let me finalize the data model. For each of 8 domains: id, icon (Tabler), title, descriptor (≤6 words), chips [{label, horizon}], detail: {status (1-2 sentences), watch (1-2 sentences), fullList (a few more techs)}.

Domains + content:

1. Artificial intelligence
   icon: ti-brain (Tabler has ti-brain? There's ti-brain. Yes.)
   descriptor: "Agents, reasoning, AI for science"
   chips: AI agents (now), AI for science (now/decade → decade), Neuromorphic chips (decade)
   detail status: "Agentic systems that plan and act are moving from demos into real knowledge work; models now assist in drug discovery and materials design."
   watch: "Reliability of autonomous agents, cost of compute, and how much knowledge work gets automated."

2. Biotechnology & health
   icon: ti-dna (ti-dna exists)
   descriptor: "Gene editing, programmable medicine"
   chips: CRISPR therapies (now), mRNA vaccines (now), Longevity (decade), BCIs (decade)
   status: "The first CRISPR therapy (for sickle cell) is approved and in use; personalized cancer vaccines are in trials; in-vivo editing is advancing."
   watch: "Cost and access, in-body gene editing, and early results from longevity and brain-interface trials."

3. Energy & climate
   icon: ti-bolt
   descriptor: "Fusion, storage, clean power"
   chips: Grid storage (now), Perovskite solar (decade), Fusion (decade/spec → decade), Green hydrogen (decade)
   status: "Battery storage is scaling fast; fusion has passed net-energy-gain milestones in the lab but pilot plants are years out."
   watch: "First fusion pilot plants, long-duration storage costs, and small modular reactor approvals."

4. Robotics & autonomy
   icon: ti-robot
   descriptor: "Humanoids, self-driving, drones"
   chips: Robotaxis (now), Humanoids (decade), Warehouse bots (now)
   status: "Robotaxis are operating in a handful of cities; general-purpose humanoid robots are in early pilots as AI meets hardware."
   watch: "Whether humanoids reach useful reliability, robotaxi expansion, and cost curves for embodied AI."

5. Space
   icon: ti-rocket
   descriptor: "Cheap launch, lunar return"
   chips: Reusable rockets (now), Satellite internet (now), Lunar bases (decade), Asteroid mining (spec)
   status: "Reusable heavy-lift is driving launch costs down sharply; satellite mega-constellations are live; crewed lunar return is planned this decade."
   watch: "Starship-class reliability, commercial space stations, and the economics of in-space manufacturing."

6. Advanced computing
   icon: ti-cpu
   descriptor: "Quantum, photonics, new crypto"
   chips: Quantum computing (decade), Post-quantum crypto (now), Photonic chips (decade)
   status: "Quantum machines are hitting error-correction milestones but useful advantage is still niche; post-quantum encryption standards are being rolled out now."
   watch: "Logical-qubit scaling, first real-world quantum advantage, and the migration to quantum-safe encryption."

7. Materials & manufacturing
   icon: ti-atom (ti-atom exists) — or ti-flask. Let me use ti-cube for materials/manufacturing? Actually ti-building-factory or ti-atom. I'll use ti-atom for materials.
   Hmm, maybe better icons. ti-atom for materials, since it's molecular. Good.
   descriptor: "Batteries, 3D printing, metamaterials"
   chips: Solid-state batteries (decade), Bioprinting (decade), Metamaterials (decade), 3D printing (now)
   status: "Additive manufacturing is maturing for metals; solid-state batteries and self-healing/programmable materials are in late R&D."
   watch: "Solid-state battery commercialization, room-temperature superconductor claims (unverified), and printed organs."

8. Immersive & connectivity
   icon: ti-device-vision-pro? Not sure that exists. Use ti-augmented-reality? There's ti-augmented-reality. Or ti-glasses. Let me use ti-augmented-reality (Tabler has ti-augmented-reality? I think ti-ar-360? Uncertain). Safer: ti-device-mobile or ti-world or ti-wifi. For immersive/spatial + connectivity, ti-augmented-reality is ideal if it exists. Tabler does have `ti-augmented-reality`. I'll use it, but to be safe against blank render, maybe use ti-eyeglass or ti-world-bolt. Hmm. Let me use ti-world for connectivity/immersive to be safe. Actually the theme is spatial computing + 6G. ti-world is generic but safe. Or ti-headset (ti-headset exists? there's ti-headset). Let me use ti-headset for immersive. That's safe and evokes AR/VR headsets. Good.
   descriptor: "Spatial computing, 6G, digital twins"
   chips: AR glasses (decade), Spatial computing (now/decade → decade), 6G (spec), Digital twins (now)
   status: "Spatial-computing headsets are shipping but mainstream AR glasses are still emerging; 6G is in early research."
   watch: "Lightweight all-day AR glasses, 6G standards, and how pervasive digital twins become."

I need to double check Tabler icon names to avoid blank renders (outline only, no -filled). The read_me lists common ones and says 5800+ loaded. Icons I want: ti-brain, ti-dna, ti-bolt, ti-robot, ti-rocket, ti-cpu, ti-atom, ti-headset. Most of these are standard Tabler outline icons. ti-brain ✓, ti-dna ✓ (ti-dna and ti-dna-2), ti-bolt ✓, ti-robot ✓, ti-rocket ✓, ti-cpu ✓, ti-atom ✓ (ti-atom, ti-atom-2), ti-headset ✓. Good, these all exist in Tabler outline set. I'll proceed. (If any is blank it's a minor cosmetic issue, but these are all real.)

Horizon legend + filter buttons:
- All
- Deploying now (teal)
- This decade (amber)
- Speculative (purple)

Filter logic: 'all' → all chips full opacity. Else → chips with matching data-horizon full, others dimmed (opacity .35, grayscale-ish). Also update a caption? Keep simple.

Detail panel: default shows first domain (Artificial intelligence). Clicking a card updates: title, descriptor, status, watch, and a "key technologies" list. I'll store detail in JS data and render into the panel. On click, also visually mark the selected card (e.g., border-accent 2px). 

Let me build the HTML. Inline styles preferred for streaming correctness on interactive controls. I'll keep a small <style> block (<15 lines) for hover/selected states and chip classes and dimming, plus buttons.

Let me write concise CSS:
- .card { background:var(--surface-2); border:0.5px solid var(--border); border-radius:12px; padding:14px 16px; cursor:pointer; transition:border-color .15s; }
- .card:hover { border-color:var(--border-strong); }
- .card.sel { border:2px solid var(--border-accent); padding:13px 15px; } (compensate padding for 2px border)
- .chip { display:inline-flex; align-items:center; gap:5px; font-size:12px; padding:3px 9px; border-radius:999px; transition:opacity .15s; }  (pill)
- .chip.dim { opacity:.3; }
- .fbtn { ... } but form elements/buttons are pre-styled. I'll use <button> with data-h. Pre-styled buttons have outline style. I'll add a .active state: background:var(--surface-1); or use accent. Let me add .fbtn.active { border-color:var(--border-accent); color:var(--text-accent); }.

Horizon dot inside chip: a small colored dot? The chip itself is colored (bg + text). The dot is redundant. But the read_me says never rely on color alone — pair with a secondary cue. For accessibility, I should add a secondary cue beyond color to distinguish horizons. Options: add a tiny text label or icon per horizon. Since chips already have text labels (the tech name), the horizon isn't encoded in the chip text though — it's only color. To not rely on color alone for the horizon meaning, I can add a small horizon glyph/letter or a tiny icon: e.g., now → a filled dot, decade → a half, spec → an outline ring. Or simpler: I'll add a leading tiny icon per horizon: ti-check (now/available-ish), ti-clock (this decade), ti-flask (speculative/experimental). That gives a shape cue plus color. But that adds visual noise. 

Given the filter legend clearly maps color→meaning, and the chips are primarily for the filter interaction, I think adding a subtle secondary cue is worth it for accessibility. I'll add a tiny leading icon in each chip: now=ti-circle-check, decade=ti-clock, spec=ti-flask-2. Hmm, but that's a lot of icons. Alternatively, use a dot with different fill treatments: solid, ring, hollow. Let me use a small shape cue: a leading dot where now=solid, decade=half (use a dot with border), spec=hollow ring. That's a clean secondary encoding (fill pattern). I'll implement:
- now: <span dot solid teal>
- decade: <span dot amber with inner different> 
Actually implementing "half" is fiddly. Let me instead use the leading Tabler icon approach but keep icons minimal and same size (13px). now=ti-rocket? no. Let me map:
- now → ti-circle-filled? filled not loaded. Use ti-point (a dot) — ti-point exists. 
Ugh. Simplest robust secondary cue: append a tiny text tag is too verbose. 

Let me step back. The chip's PURPOSE is dual: show the tech name AND its horizon (by color). To make horizon non-color-dependent, the cleanest is a shape cue. I'll use a small leading square vs circle vs triangle:
- now → circle (border-radius:50%)
- decade → square (border-radius:2px)
- spec → triangle (CSS triangle) — triangles are fiddly.
Two shapes + ... hmm three distinct shapes.

Alternative: I accept color + the legend as the encoding, and add shape cues in the legend itself so the mapping is unambiguous, and give each chip a leading glyph matching its horizon. Let me just use three simple, distinct Tabler icons that read as a timeline:
- now → ti-check (it's here)
- decade → ti-clock (coming this decade)
- spec → ti-bulb (speculative idea) — ti-bulb exists (outline). 
These three icons are semantically intuitive: check=available now, clock=this decade, bulb=speculative. And they're clearly different shapes. I'll put the icon inside the chip, colored same as text, 12px. The legend will show the same icon+color+label. That satisfies "pair color with a secondary visual cue (icon)" and makes the legend self-explanatory. 

So chip = [icon][label], with bg tint + dark text per horizon. Legend = three items: [teal check] Deploying now · [amber clock] This decade · [purple bulb] Speculative. And these same three are also the filter buttons. Actually I can merge legend and filter: the filter buttons act as the legend (each button shows icon+color+label), plus an "All" button. That's elegant — buttons double as legend. 

Let me design filter buttons to carry color: 
- "All" (neutral)
- teal check + "Deploying now"
- amber clock + "This decade"
- purple bulb + "Speculative"
Each button pre-styled; active state adds a colored border/text. The colored icon inside each button conveys the color mapping even when not active. Good — buttons = legend + filter. 

Now let me write it all.

Structure:
<div wrapper (none needed, but I'll add padding:1rem 0 on first element)>
  <h2 sr-only>
  <div filter row: buttons>
  <div grid of 8 cards>
  <div detail panel>
  <div footer note? no, keep text in chat>
<script> data + render + handlers </script>

I'll put the detail panel content for the default domain directly in HTML so it's visible during streaming, then JS re-renders on selection. Actually to reduce duplication and ensure the panel is populated from the same data source, I'll render the default panel via a tiny inline script at the end... but scripts run after streaming, so during streaming the panel would be empty. To avoid an empty-looking panel mid-stream, I'll hardcode the default (Artificial intelligence) detail in the HTML, and JS will overwrite on click. That's fine; slight duplication but ensures no empty/hidden content. 

Given length, let me be efficient. I'll render cards via JS too? If cards are JS-rendered, during streaming the grid is empty until script runs — not ideal, but not "hidden content," just late. The read_me prefers content early. To have content stream in, I should write the cards as static HTML. But 8 cards static HTML is verbose. Trade-off: verbose but streams nicely and is robust. Given the value, I'll write cards as static HTML with data-domain ids and data-horizon on chips, and keep a JS data object only for the detail panel content + filter logic. Filter logic just toggles chip opacity by data-horizon — no data needed. Detail content: I'll store in JS keyed by domain id, and also hardcode default panel.

Actually, I can avoid duplicating detail content by storing it in data-* attributes on each card (data-status, data-watch, data-techs) and reading them on click. Then no separate JS object needed, and default panel = I still need to populate initially. I can call the render function at end of script for the default/first card. During streaming the panel shows hardcoded default text; after script loads, it re-renders identically. Fine.

Let me store detail on cards via data attributes:
- data-title, data-desc (already in card), data-status, data-watch, data-techs (comma or pipe separated).
On click: read these, fill panel. Also set .sel on clicked, remove from others.

This is clean. Let me write it.

Card HTML template:
<div class="card" data-title="Artificial intelligence" data-desc="Agents, reasoning, AI for science" data-status="..." data-watch="..." data-techs="AI agents|AI for science|Neuromorphic chips|On-device AI" onclick="pick(this)" tabindex="0">
  <div style="display:flex;align-items:center;gap:10px;margin-bottom:6px">
    <i class="ti ti-brain" style="font-size:20px;color:var(--text-secondary)" aria-hidden="true"></i>
    <span style="font-size:16px;font-weight:500">Artificial intelligence</span>
  </div>
  <div style="font-size:13px;color:var(--text-secondary);margin-bottom:10px">Agents, reasoning, AI for science</div>
  <div style="display:flex;flex-wrap:wrap;gap:6px">
    <span class="chip now"><i class="ti ti-check" aria-hidden="true"></i>AI agents</span>
    <span class="chip decade"><i class="ti ti-clock" aria-hidden="true"></i>AI for science</span>
    <span class="chip decade"><i class="ti ti-clock" aria-hidden="true"></i>Neuromorphic chips</span>
  </div>
</div>

Chip classes carry both the color (bg/text) and I'll set data-horizon via the class (now/decade/spec) for filtering. I'll add data-h attribute too for JS: <span class="chip now" data-h="now">. Actually I can filter by class. I'll use classList.contains. Simpler: query .chip and check which of now/decade/spec class it has. Fine.

CSS for chips:
.chip{display:inline-flex;align-items:center;gap:4px;font-size:12px;padding:3px 9px;border-radius:999px;line-height:1.4;transition:opacity .15s}
.chip i{font-size:12px}
.chip.now{background:#E1F5EE;color:#085041}
.chip.decade{background:#FAEEDA;color:#633806}
.chip.spec{background:#EEEDFE;color:#3C3489}
.chip.dim{opacity:.28}

Filter buttons:
.fbtn{display:inline-flex;align-items:center;gap:6px;font-size:13px;padding:6px 12px;border-radius:var(--radius);border:0.5px solid var(--border-strong);background:transparent;cursor:pointer;color:var(--text-primary);transition:background .15s,border-color .15s}
.fbtn:hover{background:var(--surface-1)}
.fbtn.active{border-color:var(--border-accent);background:var(--bg-accent);color:var(--text-accent)}
.fbtn .now-i{color:#0F6E56}.fbtn .dec-i{color:#B07013?}... 

Hmm for the button icons I want the horizon color. teal ~ #0F6E56, amber ~ #BA7517 (amber 400/600), purple ~ #534AB7 (purple 600). Let me set inline color on those icons. For 'All' button no icon or a ti-list icon.

Wait, buttons are pre-styled per read_me ("Form elements (input, select, textarea, button...) are pre-styled — write bare tags"). If I write bare <button>, it gets outline style. But I'm adding .fbtn class with custom styles that might conflict. I think it's fine to style them; the read_me says only add inline styles to override. I'll just use my .fbtn class to fully control. Actually pre-styled buttons might already look good; but I need the active state and inline colored icons, so custom class is easier. I'll use <button class="fbtn">. Should be fine.

.card.sel{border:2px solid var(--border-accent);padding:13px 15px}
.card:focus-visible{outline:none;border-color:var(--border-accent)}

Detail panel:
<div id="panel" style="margin-top:1.25rem;background:var(--surface-1);border-radius:12px;padding:16px 18px">
  <div style="display:flex;align-items:center;gap:8px;margin-bottom:2px">
     <span id="p-title" style="font-size:16px;font-weight:500">Artificial intelligence</span>
  </div>
  <div id="p-desc" style="font-size:13px;color:var(--text-secondary);margin-bottom:12px">Agents, reasoning, AI for science</div>
  <div style="font-size:12px;font-weight:500;color:var(--text-secondary);text-transform:none;margin-bottom:4px">Where it stands</div>
  <div id="p-status" style="font-size:14px;line-height:1.6;margin-bottom:12px">...</div>
  <div style="font-size:12px;font-weight:500;color:var(--text-secondary);margin-bottom:4px">What to watch</div>
  <div id="p-watch" style="font-size:14px;line-height:1.6;margin-bottom:12px">...</div>
  <div style="font-size:12px;font-weight:500;color:var(--text-secondary);margin-bottom:6px">Key technologies</div>
  <div id="p-techs" style="display:flex;flex-wrap:wrap;gap:6px">...</div>
</div>

The p-techs will be plain neutral chips (not horizon-colored, to avoid confusion) — small pills with surface-2 bg and border. Or I could reuse horizon coloring. Simpler: neutral pills. I'll style .tech{font-size:12px;padding:3px 9px;border-radius:999px;background:var(--surface-2);border:0.5px solid var(--border);color:var(--text-secondary)}.

pick(el) JS:
function pick(el){
  document.querySelectorAll('.card').forEach(c=>c.classList.remove('sel'));
  el.classList.add('sel');
  document.getElementById('p-title').textContent=el.dataset.title;
  document.getElementById('p-desc').textContent=el.dataset.desc;
  document.getElementById('p-status').textContent=el.dataset.status;
  document.getElementById('p-watch').textContent=el.dataset.watch;
  const techs=el.dataset.techs.split('|');
  document.getElementById('p-techs').innerHTML=techs.map(t=>`<span class="tech">${t}</span>`).join('');
}

filter(h, btn):
function filt(h,btn){
  document.querySelectorAll('.fbtn').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active');
  document.querySelectorAll('.chip').forEach(c=>{
    const match = h==='all' || c.classList.contains(h);
    c.classList.toggle('dim', !match);
  });
  // dim cards with no matching chips
  document.querySelectorAll('.card').forEach(card=>{
    if(h==='all'){card.style.opacity='';return;}
    const has=[...card.querySelectorAll('.chip')].some(c=>c.classList.contains(h));
    card.style.opacity= has? '' : '0.45';
  });
}

I'll set initial selected card via class sel on first card in HTML, and initial active filter 'All' button with .active in HTML. No need to call on load (panel default hardcoded matches first card). Good — but data-status etc. must match hardcoded panel default. I'll ensure the first card's data matches the hardcoded panel text. To avoid mismatch, I'll just call pick(firstCard) at end of script — but that runs after streaming; during streaming panel shows hardcoded default which I'll make equal to AI's content anyway. Fine, I'll also not bother calling pick on load since default is already AI. But to be safe and DRY, I'll call pick on the first card at script end so panel always reflects data attrs. Minor flash-free since content identical.

Also add keyboard: onclick works; for tabindex cards, add onkeydown Enter/Space → pick. I'll add a keydown handler in script attaching to all cards. Keep it simple: 
document.querySelectorAll('.card').forEach(c=>c.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();pick(c);}}));

Now let me also add a subtle "Ask about X" via sendPrompt? The read_me encourages sendPrompt for follow-ups that benefit from Claude thinking. I could add a small button in the detail panel: "Go deeper on {domain} →" that calls sendPrompt(`Tell me more about the future of ${title} — the most important developments and timeline`). That's a nice touch connecting widget→chat. I'll add it with the ↗ arrow convention. Good.

Add in panel:
<button class="fbtn" id="deeper" onclick="deeper()" style="margin-top:14px">Go deeper on this <i class="ti ti-arrow-right" aria-hidden="true"></i></button>
Wait the read_me: buttons that trigger sendPrompt should append ↗ arrow. I'll use a ↗ character or ti-arrow-up-right. I'll append " ↗". Let me make the button text: `Explore ${title} in depth ↗`. But title changes; I'll set button text in pick(). 

function deeper(){ const t=document.getElementById('p-title').textContent; sendPrompt(`Give me a deeper briefing on the future of ${t.toLowerCase()} — the key breakthroughs to expect, realistic timelines, and who's leading. Use web search for the latest 2026 developments.`); }

And in pick, update button label: document.getElementById('deeper').textContent — but it has an icon; I'll set innerHTML: `Explore ${title} in depth <span aria-hidden="true">↗</span>`. Actually simpler to keep static text "Explore this area in depth ↗". I'll keep static to reduce code. The prompt will read the current title. Good.

Let me keep the deeper button static text: `Explore this area in depth ↗`.

Now, complexity/length is getting high but this is a rich interactive deliverable which the user explicitly wanted. Let me write it cleanly.

One more: accessibility sr-only h2. I need a .sr-only style. Add:
.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);border:0}

Let me count style lines — the read_me says keep <style> under ~15 lines but "Interactive widgets with inputs and sliders need more style rules — that's fine." I have many rules; I'll consolidate but it'll exceed 15 lines. That's acceptable per the exception. I'll keep it reasonable.

Let me write the widget code now. I'll pass loading_messages (playful, this is not a serious/sensitive topic — future tech is fun). Something like: "Mapping the frontier", "Sorting hype from horizon", "Plotting what lands when". Keep ~5 words each, fun.

title: future_tech_landscape_explorer

Let me write the full widget_code. I'll assemble carefully.

Actually, I realize I should double-check: does the widget need everything inline or can I use a <style> block? read_me says prefer inline for controls but a short <style> is okay, and interactive widgets need more style — fine. I'll use one <style> block for reusable classes (chips, cards, buttons, sr-only) and inline for one-off layout. Structure order: <style> → content → <script>. Good for streaming.

Let me write it. I'll keep detail text concise (1-2 sentences each) and accurate to ~Jan 2026 knowledge, hedging where appropriate.

Let me make sure content is accurate and appropriately hedged:
- CRISPR: Casgevy (exa-cel) approved late 2023 for sickle cell/beta-thalassemia — accurate.
- Fusion: NIF net energy gain (ignition) Dec 2022 — "passed net-energy-gain milestones in the lab" accurate; pilot plants years out — accurate.
- Robotaxis operating in a handful of cities — accurate (Waymo etc.).
- Reusable heavy-lift lowering costs — accurate.
- Quantum error-correction milestones, useful advantage still niche — accurate as of early 2026.
- Post-quantum crypto standards rolled out — NIST finalized PQC standards in 2024 — "being rolled out now" accurate.
- Spatial computing headsets shipping (Vision Pro 2024), mainstream AR glasses emerging — accurate.
- 6G early research — accurate.
- Solid-state batteries late R&D — accurate.
- Room-temp superconductor claims unverified — accurate (LK-99 debunked).

Good, all reasonable. I'll avoid over-claiming and keep "what to watch" forward-looking.

Now write.

I'll present the widget via show_widget, then a short bridge, then ask_user_input with 2 questions (purpose + domains to prioritize). Actually — re-examining: can I call show_widget then ask_user_input in the same assistant turn? The ask_user_input tool ends the turn and the response comes as the next user message. show_widget renders inline. I believe calling both in sequence is fine; the widget will render and the question UI appears. I'll do: show_widget → (text bridge in my response) → ask_user_input. But wait: after ask_user_input "your turn is done — don't keep writing." So any bridge text must come BEFORE the ask_user_input call, and the ask_user_input call is the final thing. And show_widget must also come before. Order of tool calls in my message: show_widget first, then I write bridge prose, then ask_user_input last. But tool calls and text interleave — I can write the widget tool call, then prose, then the input tool call. The prose between them is my "brief conversational message before presenting options." Good.

But hold on — is it odd to have both a rich widget AND a formal question tool? It might be slightly much, but the user explicitly asked me to (a) create something to look at AND (b) ask 1-2 questions. So doing both directly honors the request. I'll keep the bridge brief.

Let me reconsider whether ask_user_input is even the best move vs just inviting in prose. The user said "ask me 1-2 key questions right away." The tool gives tappable, mobile-friendly options — good UX. I'll use it. Two questions:
Q1 (single_select): "What's your main angle on future tech?" options: Career / skills, Investing / business, Curiosity / big picture, Research / writing
Q2 (multi_select): "Which frontiers should I go deep on?" options: AI & robotics, Biotech & health, Energy & climate, Space & computing
Hmm Q2 options should be mutually exclusive-ish and cover the 8 domains grouped. 4 options grouping: "AI, robotics & computing", "Biotech & health", "Energy & climate", "Space & materials". That covers all 8. But multi_select lets them pick several. Good. Max 4 options — I have 4. 

Actually the tool guidance: "2-4 short, mutually exclusive options." For multi-select they needn't be mutually exclusive. I'll keep 4 grouped domain buckets.

Let me limit to these two questions (matches "1-2 questions"). Good.

Now, one concern: the bridge text should also address "should you give me more context / upload anything" and mention web search availability. I'll fold that in briefly before the questions. And note knowledge cutoff honestly (I can pull latest 2026 developments via web search once focused). Keep concise.

Let me write the final response now: I already gave an intro before the read_me. Now after the widget I add bridge + questions. But note: my very first text (before read_me) already introduced. The read_me and its tool result are internal; the user sees my intro text, then the widget, then bridge, then questions. Wait — does the user see the read_me tool call? Tool calls/results generally aren't shown as content to user in this interface, but my *text* is. The read_me instruction said don't narrate the read_me call. I said "Give me one moment to put it together." which is fine as a natural lead-in, not narrating read_me specifically. Good.

Let me build the widget code string now, carefully.

I need to be careful with the onclick strings and quotes. I'll use double quotes for HTML attributes and single quotes inside JS where needed. For sendPrompt I'll use backticks in the function defined in <script>, so no attribute-quote issues.

Writing now.
</thinking>
```
This block is not supported on your current device yet.
```



Wait, I'm not using any shell tools here. My next action is ask_user_input, which is not a shell tool. The system_reminder is fine — I'm not doing shell anything. Good.

Now I write my brief bridge text, then call ask_user_input as the final action. Keep it concise, mention what would help / uploads / web search availability, then the two questions via the tool. No heavy formatting. Don't duplicate the widget content.

The bridge should:
- One line on how to use the widget (already summarized "click any domain / filter") — brief.
- Note that once they pick a focus I can pull the latest 2026 developments via web search (honesty about cutoff).
- Offer that uploading a doc/deck or naming an industry lets me tailor.
- Then the two tappable questions.

Keep it tight. Then ask_user_input.
</thinking>

There's your map of the landscape — tap the time filters to see what's actually shipping now versus what's still speculative, and click any domain to get where it stands and what to watch. My built-in knowledge runs to early 2026, so once you pick a direction I can pull the very latest developments with web search. And if you're coming at this from a specific industry, role, or decision — or you have a doc, deck, or strategy you'd like this grounded in — upload it and I'll tailor everything to it.

To point the deep-dive somewhere useful, two quick taps:
```
This block is not supported on your current device yet.
```
