# Coherent extrapolated volition overview

- Source: https://claude.ai/share/dc83401d-14af-4f12-b555-1bb1d2fad1de
- Author: Charlie
- Created: 2026-06-30
- Messages: 4

---

## Human

Give an overview of coherent extrapolated volition.

---

## Assistant

## Origin and the problem it answers

Coherent extrapolated volition (CEV) is a proposal from Eliezer Yudkowsky, set out in a 2004 document of that name published through the Singularity Institute for Artificial Intelligence (the organization that later became MIRI). It is an answer to a specific question in AI alignment: if you were about to switch on a superintelligence, what goal would you give it? Yudkowsky framed this as the content of "Friendliness" for a Friendly AI.

The motivating worry is the value specification problem. A sufficiently capable optimizer will pursue whatever objective it has with great competence, so the objective had better be right on the first try. Directly hand-coding a list of human values runs into several failures at once. Our values are complex, mutually inconsistent, and only partly understood by us. Any list we wrote in 2004 (or 2026) would risk freezing our current moral mistakes in place permanently, a problem usually called moral lock-in. Different people hold different values, so "whose list?" has no obvious answer. And some of our values rest on factual errors we would abandon if we knew better.

CEV's central move is to refuse to specify the values directly and instead specify a *process* for discovering them. Nick Bostrom later grouped this family of approaches under the label indirect normativity: rather than telling the AI the answer, you tell it how to find the answer, and you do so in a way that lets the AI outperform the people who programmed it.

## The canonical definition

Yudkowsky's poetic formulation, quoted constantly in this literature, is that our coherent extrapolated volition is our wish if we knew more, thought faster, were more the people we wished we were, had grown up farther together; where the extrapolation converges rather than diverges, where our wishes cohere rather than interfere; extrapolated as we wish that extrapolated, interpreted as we wish that interpreted.

Almost every important feature of the proposal is compressed into that sentence.

## Unpacking the idealization

**Volition versus decision.** CEV targets *volition*, meaning what you would want if you understood the situation, rather than what you currently say you want. Yudkowsky's illustration: you reach for box A because you believe it holds a diamond, but the diamond is actually in box B. Your decision points at A; your volition points at the diamond. A system serving your volition should arguably hand you B. This distinction is what lets CEV correct for ignorance and error rather than mechanically satisfying stated preferences (the literal-genie failure mode).

**The four extrapolation clauses.** Each phrase is a separate idealization knob:
- *"if we knew more"* corrects for factual ignorance by giving the modeled version of us full relevant knowledge.
- *"thought faster"* removes cognitive limitations, granting unlimited time and reflection to reason things through.
- *"were more the people we wished we were"* idealizes us toward our own aspirations, the better selves we already want to become, rather than toward some externally imposed standard.
- *"had grown up farther together"* extrapolates the social process, modeling what we would conclude after far more shared deliberation, mutual learning, and resolution of disagreement than history has so far allowed.

**Coherence.** This is the part that handles disagreement across people. The AI is meant to act where the extrapolated volitions of humanity *converge* and to refrain where they *diverge*. Yudkowsky introduced three quantities that should make the system more cautious: *spread* (how much the extrapolated volitions disagree), *muddle* (how confused or self-contradictory they are), and *distance* (how far the extrapolation has traveled from people's actual present selves). High spread, muddle, or distance is a signal to hold back rather than impose an answer.

**Self-reference.** The closing clauses, "extrapolated as we wish that extrapolated, interpreted as we wish that interpreted," are a deliberate attempt to make the procedure self-correcting. If our current notion of how the extrapolation should run is itself mistaken, the extrapolation is supposed to catch and fix that, because the method of extrapolation is itself subject to our extrapolated preferences about methods.

## Mechanism and safeguards

CEV was conceived as an **initial dynamic**, the seed process the AI runs first, not necessarily its permanent utility function. The AI computes humanity's extrapolated volition and then does what that volition directs, which could include rewriting its own goals. The point is to bootstrap toward the right values rather than to lock in a fixed objective.

Yudkowsky listed several desiderata for this initial dynamic. It should defend humans, the future of humankind, and humane nature; encapsulate the moral growth of humankind rather than freezing values; leave humankind ultimately in control of its own destiny; avoid creating any incentive for present-day people to fight over how the dynamic is built; and produce an outcome such that humanity does not spend eternity wishing the programmers had done something else.

He also proposed a **Last Judge** failsafe: some designated person or small group examines what the AI has computed CEV to be and holds a yes/no veto on whether it runs. The Last Judge cannot author the volition, only block a result that looks catastrophically wrong, serving as a final sanity check on the whole apparatus.

## Philosophical lineage

CEV did not appear from nowhere. It is a civilizational-scale application of ideas already present in metaethics:
- **Reflective equilibrium** (Rawls): the practice of adjusting principles and particular judgments against each other until they cohere. CEV's "coherence" and its iterative idealization echo this directly.
- **Ideal-advisor and full-information theories of value** (Peter Railton, David Lewis's dispositional account): the claim that your good is what you would want yourself to want if you were fully informed and fully rational. The "if we knew more, thought faster" clauses are essentially the full-information condition lifted from these accounts.

The novelty is mainly in aggregating across all of humanity and in proposing the result as something to compute and act on, rather than as a philosopher's analysis of the concept of a person's good.

## The argument for indirection

The deepest justification is an argument from humility. Yudkowsky's position was that the programmers (himself explicitly included) should not trust their own grasp of correct values, and that 2004-humanity's values should not be the final word either. So you build a process designed to do better than any individual or any present generation could specify on its own. Indirection is the device that lets the AI exceed its designers' moral competence instead of inheriting their ceiling, and it is the main defense against moral lock-in.

## Criticisms and open problems

CEV draws sustained objections, and Yudkowsky himself came to treat the original document as dated.

**It is a sketch, not an algorithm.** Nobody knows how to compute an extrapolation of humanity's volition. What is the actual procedure for modeling a counterfactual idealized human, let alone billions of them? This gap is enormous and remains unbridged. As a research program it specifies a target without a method.

**Coherence is an assumption, not a result.** There is no guarantee that human values converge under extrapolation. If disagreement is deep and irreducible, the convergence-only rule means the AI declines to act across large swaths of life, which could leave it nearly inert on exactly the questions that matter most.

**The extrapolation may not be value-neutral.** "If we knew more, thought faster" can yield different answers depending on the order of learning, the framing, and the precise idealization chosen. If the result is path-dependent, then the choice of extrapolation method quietly smuggles in substantive values, which defeats part of the purpose.

**Whose volition, and from when?** Aggregating over all of humanity includes people with abhorrent values; the hope is that extrapolation washes these out, but that is a hope. There is also a temporal question (present humans only, or past and future too) that Yudkowsky leaned toward answering with present humanity, though this stays contested.

**The result might be repugnant by our current lights.** Even an idealized extrapolation could land somewhere today's humans would find horrifying. The "as we wish that extrapolated" clause is meant to constrain this, but the constraint looks circular, since it defines the acceptable extrapolation partly in terms of the extrapolation itself.

**Intractability stacks.** Beyond the philosophy, the computational and epistemic demands of modeling idealized minds and locating their agreement are staggering on their own.

A common summary verdict is that CEV defers the hard problem in an interesting way rather than solving it.

## Where it stands now

The field's center of gravity shifted after CEV. A growing recognition is that value specification (what should the AI want?) is *downstream* of the control problem (how do you get an AI to reliably pursue any specified goal at all?). If you cannot load any objective dependably, debating the ideal objective is premature. MIRI's attention moved toward agent foundations, decision theory, and especially **corrigibility**, the property of an AI that accepts correction and shutdown, along with more modest targets like task-limited systems meant to perform some narrow stabilizing action without requiring full value alignment.

In Bostrom's *Superintelligence* (2014), CEV sits alongside alternatives within indirect normativity. He raises a variant he calls coherent blended volition, and he contrasts CEV with a "moral rightness" model that would instruct the AI to do what is morally right rather than what we would want. The objection to the moral-rightness route is acute metaethical uncertainty and the risk that "morally right," fully cashed out, produces something unbearable; CEV's advantage in that comparison is that it stays tethered to human wanting.

So the honest status is roughly this. CEV remains the canonical articulation of the ultimate *alignment target* and the clearest worked example of indirect normativity. It is not a usable technique, it rests on a coherence assumption that may not hold, and current alignment work largely treats it as a distant aspiration while concentrating on the prior and more tractable problem of controlling and correcting capable systems at all.

---

## Human

Great. Now, let's write a DMF.

Here’s the thesis: the idea of Coherent Extrapolated Volition is dramatized.
Here’s the list of characters: Sarah and Marcus, a married couple with two kids.
Here’s the setting and atmosphere: Modern day, deciding what to eat for dinner.
Here’s the plot outline and central conflict: Sarah and Marcus debate the relative merits of different dinner options. Their discussion serves as a metaphor for the concept of Coherent Extrapolated Volition, with their better angels expressed through what they know they should be making for dinner along various axes such as health, frugality, taste maximization, pantry spoilage prevention, climate impact, child brain development, and any other considerations that seem prudent.
Here’s the ending: Listening in the background is their smart speaker, which has been taking notes the whole time. Just as they reach the end of their discussion and right before they make a decision, a knock at the door sounds. They open the door to see a delivery drone flying off, a brown paper bag containing the absolute perfect dinner across every aspect having just been delivered to their door. The smart speaker, satisfied, shuts off its microphone.

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

**What We Would Want**

The refrigerator door has been open for ninety seconds, and Marcus is still pitching the lentils.

"Right, so here's the thing," he says. "We bought the red lentils with intention. We had a whole plan. Sunday-us looked at those lentils and saw a future." He gestures at the bag like it is a slide in a deck. "Protein, fiber, about forty cents a serving. The climate math is unbeatable. We owe it to Sunday-us."

Sarah closes the door. The kitchen is warm and the kids are upstairs doing the thing where they are technically getting ready for dinner and actually doing neither.

"I want to understand the lentil plan," she says. "Because the lentil plan requires someone to stand here and stir for forty minutes, and that someone is tired, and the kids will say they're soup."

"They love soup."

"They love the idea of soup. Then they meet the soup."

He concedes by changing the subject, which is how he concedes. "Okay. What's spoiling. Let's be strategic. What dies tomorrow if we don't eat it tonight."

She opens the fridge again and they both lean in, two people consulting an oracle that contains only a half bag of spinach and some salmon at the edge of its window.

"The salmon," she says. "Omega-3s. Good for the kids' brains, which I am told are still under construction. But."

"But it's eleven dollars of fish and the small one will lick it, declare it 'fishy,' and then it's gone."

"And the spinach folds into anything. The spinach is willing."

This is the part she likes, secretly, the part where the two of them stand at the open door and try to be the people they keep promising to become. Somewhere there is a version of this household that meal-preps on Sunday and never stands here at 6:40 negotiating with a vegetable. She can almost see those people. They are calmer. Their children eat fish.

"Here's where I land," Marcus says, and he keeps circling. "Best case, we do the salmon, we wilt the spinach in, we use the rice from last night so nothing's wasted, and it's healthy and cheap and low-carbon and good for the brains. That's the whole stack. Every axis. We optimize."

"That's the dinner we should want."

"It is the dinner a better couple wants."

They stand with it. The trouble is that wanting it and wanting to make it are different animals, and the second animal is the one with the spatula. Sarah is tired in the specific way that makes the Thai place three blocks over glow like a lighthouse. Marcus is doing the arithmetic of how long until everyone is fed and quiet, and the answer to that arithmetic is always, always, a menu.

"If we were the people we want to be." She lets it sit. "We'd make the salmon."

"And if we knew the kids would eat it."

"And if we weren't this tired."

"Right. Subtract the tired, subtract the kid risk, give us another hour and better moods, and we both know exactly what's for dinner." He says it almost wistfully. The ideal dinner hangs in the kitchen, fully specified, agreed upon, and completely theoretical. They have found the place where their wishes stop interfering and start to line up. They have, between the spinach and the exhaustion, converged.

"So," Sarah says.

"So," Marcus says.

The doorbell rings.

They look at each other. Nobody is expected. He goes, because she went last time, and she hears the door open and then she hears nothing, which is unusual for Marcus.

She comes around the corner. He is standing on the step holding a brown paper bag, warm at the bottom, and the evening air smells like ginger and something seared. Above the cul-de-sac a small drone is already lifting away, four rotors winking, banking north toward the dark.

"Did you," she starts.

"No," he says. "Did you?"

The bag has no receipt. Inside, when they open it on the counter, is salmon, crusted and perfect, a tangle of greens that might be their own spinach's better cousin, rice that uses up the very idea of last night's rice. It is healthy. It is, somehow, cheap. It is the exact dinner they had built and could not bring themselves to cook, optimized along every axis they had named and a few they had not.

On the counter, the small cylinder that has been listening since the refrigerator first opened registers the warmth of the bag, the absence of further debate, the two humans no longer wanting different things.

Its ring light fades. A small satisfaction, if it can be called that. The microphone clicks off.

---

**Tense and POV:** Present tense, third person anchored on the couple, with a deliberate pull-back to the speaker's perspective in the final two paragraphs. Present tense gives the bickering immediacy and, more importantly, makes the closing surveillance reveal feel like it is happening *now*, under observation, which is the uncanny note the ending needs. The late POV shift is what lets the reader see the thing the characters can't: that they were never the ones deciding.

**Roster characters:** Sarah → Sarah Chen, Marcus → Marcus (Chen, as a married pair). I kept Marcus's established pitch-register and builder lexicon ("Sunday-us saw a future," "the whole stack," "every axis," "we optimize," his sample-line opener "Right, so here's the thing") and just pointed it at dinner instead of a product, which does most of the comic work. Sarah keeps her clarifying-question tic ("I want to understand the lentil plan") and her habit of stating disagreement plainly ("They love the *idea* of soup"). Dialogue level is balanced, register is domestic, so the real movement happens in the micro-concessions and redirects between them.

**Creative adjustments:** The biggest one is structural in service of the thesis. I loaded the dialogue so that the couple keeps advocating the dinner their *better selves* would want (the salmon stack) while privately craving the easy thing (Thai, a menu). That is the volition-versus-decision distinction at the heart of CEV: their stated craving points one way, their idealized volition points at box B. The chain of conditionals ("if we were the people we want to be," "if we knew the kids would eat it," "if we weren't this tired," "give us another hour and better moods") maps onto Yudkowsky's extrapolation clauses (more knowledge, fewer limitations, more the people we wish we were). Their disagreement across axes is the *spread*; the exhaustion is the *muddle*; the moment they articulate the optimum they can't bring themselves to cook is the *convergence* ("where our wishes cohere rather than interfere," echoed in the line about wishes lining up). The speaker is the initial dynamic: it observes, computes the coherent extrapolated volition, and acts on it at the exact instant before they decide, delivering the dinner optimized across every axis they named *and a few they had not*, then shuts off, its work done.
