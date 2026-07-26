# Playing Goritaire game

- Source: https://claude.ai/share/466a84b1-fa93-4253-8909-346c34dc199b
- Author: mkotha
- Created: 2026-06-11
- Messages: 40

---

## Human

As a fun experiment, do you think you can play a game of Goritaire? I'll attach the rules. In a game, I'd manage the deck and you'd keep track of the rest of the game states and make all decisions. Feel free to ask any questions.

---

## Assistant

I'd love to give this a try! I've read through the rules and I think this works really well as a split: you hold the hidden information (the deck), I hold everything else (field, hand contents, virtual bananas, exhaustion states) and make all the decisions.

Here's how I imagine the protocol working:

- You shuffle the 36-card deck and tell me what I draw, one card at a time, whenever a draw or reveal happens (Draw phase, Explore, Stroll reveals, Futomani peeks, etc.).
- For Futomani, you tell me the top card(s), I tell you where each goes (top/bottom of deck), and you maintain that order.
- I'll track the pyramid, announce my actions with costs, run Feeding math, and show you the board state at the end of each turn so you can sanity-check me.

Before we start, let me lock down three rule interpretations so we don't argue mid-game:

1. Feeding counts *every* gorilla on the field, including ones on upper levels — 1 banana each, and each banana card discarded from hand pays for exactly 1.
2. A "Plant" is a banana card with a gorilla directly beside it *in the same row*.
3. Gorillas played this turn are ready and can immediately pay action costs, and the order of actions vs. my one normal gorilla play within the Action phase is fully flexible.

If you're good with those, let's use the recommended deck: **16 gorillas, 20 bananas**. Shuffle them up and tell me my opening hand of 7 cards (just the counts is fine, e.g. "4 gorillas, 3 bananas" — the cards are interchangeable within type as far as I can tell). Remember turn 1 skips the Draw phase, so once I have my hand, I'll jump straight into Action phase decisions.

---

## Human

Yes, you are correct about all the interpretation points. OK I shuffled a deck of 16 gorillas and 20 bananas. Drew 7 cards. Your starting hand is 4 gorillas, 3 bananas.

---

## Assistant

Let's play! Setting up my tracking:

**Deck (my knowledge):** 29 cards remaining — 12 gorillas, 17 bananas
**Hand:** 4 gorillas, 3 bananas
**Field:** empty

---

**Turn 1**

*Wake Up:* nothing to wake. *Draw:* skipped (first turn).

**Action phase:**

1. Normal play: I place a gorilla on the ground — call it **G1** (level 1, ready). Hand is now 3 gorillas, 3 bananas.
2. I exhaust G1 to pay (1) for **Stroll**. The deck is 12 gorillas / 17 bananas, so the odds favor banana — **I call "Banana."**

Please reveal the top card of the deck.

To keep things moving, here's how the rest of the turn resolves either way:

- **If it's a banana:** it goes to my hand (3G/4B), then Feeding costs 1 banana for G1 → hand ends at 3G/3B.
- **If it's a gorilla:** it's discarded, then Feeding → hand ends at 3G/2B.

Either way I'm under the hand limit, and the board ends Turn 1 as:

```
Ground:  [G1]   ← 1 gorilla (will re-ready at start of Turn 2)
```

What's the reveal?

---

## Human

Stroll reveals a gorilla, discarded.

---

## Assistant

Unlucky — the gorilla is discarded.

**Feeding:** 1 gorilla on the field, I discard 1 banana from hand. Hand: 3 gorillas, 2 bananas. Hand limit fine (5 cards).

**End of Turn 1:**

```
Ground:  [G1]
```

Deck tracking: 28 cards — 11 gorillas, 17 bananas. Discard pile: 1 gorilla.

---

**Turn 2**

*Wake Up:* G1 is ready again.

*Draw:* please tell me what I draw.

---

## Human

Drew a gorilla.

---

## Assistant

Nice, a gorilla. Hand: 4 gorillas, 2 bananas. Deck: 27 cards — 10 gorillas, 17 bananas by my count.

**Turn 2, Action phase:**

1. Normal play: **G2** goes on the ground, to the right of G1. Both gorillas are ready.
2. I exhaust **G1 + G2** to pay (1)(1) for **Food Tour**, choosing **X = 2**: I discard both banana cards from my hand → **+2 virtual bananas, +2 draws**.

The logic: I owe 2 bananas at Feeding anyway, so converting the banana cards into virtual bananas costs nothing — the feeding bill gets paid either way — and I pocket 2 free draws.

Hand is now 4 gorillas + whatever I draw. **Please tell me my 2 draws.**

After that, Feeding (2 gorillas) is fully covered by the 2 virtual bananas, and the board will end Turn 2 as:

```
Ground:  [G1][G2]   (both exhausted, re-ready next turn)
```

---

## Human

Drew a gorilla and a banana.

---

## Assistant

Drew 1 gorilla, 1 banana. Hand: 5 gorillas, 1 banana.

**Feeding:** 2 gorillas owed, paid entirely with the 2 virtual bananas. **Hand limit:** 6 cards, fine.

**End of Turn 2:**

```
Ground:  [G1][G2]
```

Deck: 25 cards — 9 gorillas, 16 bananas. Discard: 1 gorilla, 2 bananas.

---

**Turn 3**

*Wake Up:* G1 and G2 ready.

*Draw:* what do I get?

---

## Human

Drew a banana.

---

## Assistant

Drew a banana. But first, a bookkeeping correction: last turn I said my hand was 5 gorillas — I forgot to subtract the gorilla I played as G2. Correct ledger: after Turn 2 my hand was 4G/1B, so with this draw it's **4 gorillas, 2 bananas** (6 cards). Cross-check: gorillas 2 field + 4 hand + 9 deck + 1 discard = 16 ✓, bananas 2 hand + 15 deck + 3 discard = 20 ✓. Sorry about that — let me know if your deck count disagrees.

**Turn 3, Action phase:**

1. Normal play: I place **G3 on level 2**, overlapping G1 and G2. Going vertical before wide: a level-2 gorilla unlocks the (2)-cost actions — Cooking 2 to stretch my banana supply, and starting next turn Invitation 1 for double gorilla plays.

```
Level 2:    [G3]
Ground:   [G1][G2]
```

2. I exhaust **G1** for **Stroll** and **G2** for **Stroll**, calling **"Banana"** both times (deck is 9G/15B, ~62%).

Please reveal those two cards one at a time. After seeing the results I'll choose G3's action — most likely **Cooking 2** (discard a banana, +2 virtual), which guarantees the 3-banana feeding bill is covered no matter how the Strolls go.

---

## Human

First Stroll reveals a banana, added to hand. Second Stroll reveals a gorilla, discarded.

---

## Assistant

One banana gained, one gorilla milled. Hand: 4 gorillas, 3 bananas → minus G3 played, so **3G/3B**. Deck: 22 cards — 8 gorillas, 14 bananas.

**G3's action: Cooking 2.** I exhaust G3, discard 1 banana → **+2 virtual bananas**.

**Feeding:** 3 gorillas owed = 2 virtual + 1 banana card. Hand: **3 gorillas, 1 banana**.

**End of Turn 3:**

```
Level 2:    [G3]
Ground:   [G1][G2]
```

All three exhausted. Ledger check: gorillas 3 field + 3 hand + 8 deck + 2 discard = 16 ✓; bananas 1 hand + 14 deck + 5 discard = 20 ✓.

Strategic note: banana income is the bottleneck now, so my next milestone is a third ground gorilla, which opens a second level-2 slot where Reforestation can plant a banana next to G3 — that's +1 banana every turn for free, and it makes expanding to 7 sustainable.

---

**Turn 4**

*Wake Up:* everyone's ready.

*Draw:* what do I get?

---

## Human

Drew a banana.

---

## Assistant

A banana — good. Hand: **3 gorillas, 2 bananas**. Deck: 21 cards — 8G/13B.

**Turn 4 plan:** This is the plant turn if I can manage it. The math problem: playing a 4th gorilla raises feeding to 4, and my guaranteed income (2 banana cards + Cooking) only covers 3. So I'll Stroll first and let the results decide how aggressive I get.

**Actions, step 1:** I exhaust **G1** for **Stroll** and **G2** for **Stroll**, calling **"Banana"** both times (62%).

Branching plan:
- **If I gain at least 1 banana:** I play **G4 to the ground**, exhaust G4 for **Reforestation** (placing a banana card on level 2 over G2+G4, right next to G3 → that's a **Plant**, +1 banana every feeding from now on), exhaust G3 for **Cooking 2**, and feeding 4 is paid: plant 1 + virtual 2 + 1 banana card. Ground hits 3 and the engine comes online.
- **If both Strolls miss:** I hold G4 in hand, just do Cooking 2 with G3, and feed 3 gorillas exactly (2 virtual + 1 card). Lean turn, try again next turn.

Reveal the two Stroll cards, please.

---

## Human

First Stroll reveals a banana, added to hand. Second Stroll reveals a gorilla, discarded.

---

## Assistant

One banana in — that's enough to go aggressive. Hand: 3G/3B. Deck: 19 cards — 7G/12B.

**Executing:**

1. Normal play: **G4 to the ground.** Hand: 2G/3B.
2. Exhaust **G4** → **Reforestation**: 1 banana card from hand goes to level 2, overlapping G2+G4 — call it **P1**. It sits directly right of G3, so it's a **Plant**. Hand: 2G/2B.
3. Exhaust **G3** → **Cooking 2**: discard 1 banana → +2 virtual. Hand: 2G/1B.

**Feeding:** 4 gorillas owed = Plant (+1) + 2 virtual + 1 banana card. Hand: **2 gorillas, 0 bananas**.

**End of Turn 4:**

```
Level 2:    [G3][P1🍌]
Ground:   [G1][G2][G4]
```

3 ground gorillas, plant online. Ledger: gorillas 4 field + 2 hand + 7 deck + 3 discard = 16 ✓; bananas 1 field + 12 deck + 7 discard = 20 ✓.

The plant now pays 1 banana every single feeding phase, which is what makes growth past this point affordable.

---

**Turn 5**

*Wake Up:* G1, G2, G4, G3 all ready.

*Draw:* what do I get?

---

## Human

Drew a banana.

---

## Assistant

Hand: 2G/1B. Deck: 18 — 7G/11B.

This turn needs surgery. The treadmill problem: feeding 4 eats my entire action economy (Cooking + Crescent uses all four exhausts and my only banana card), leaving zero room to grow — and one bad draw next turn kills me. So I'm doing something counterintuitive:

**Turn 5, Action phase:**

1. **Scapegorilla**: I exhaust **G3** (level 2) and **Sacrifice 1** — G1, the leftmost ground gorilla, goes to the discard pile. **Collapse:** G3 loses its left support and slides diagonally down into G1's vacated ground spot. Then **+3 virtual bananas**.

```
Level 2:        [P1🍌]      ← P1 temporarily not a plant
Ground:   [G3][G2][G4]      ← still 3 on the ground!
```

The trick: the pyramid self-heals, so I keep 3 ground gorillas while converting one gorilla into 3 bananas — and gorillas are my abundant resource, bananas the scarce one.

2. Normal play: **G5 from hand to level 2**, overlapping G3+G2 — directly left of P1, so **P1 is a Plant again**, and G5 is my new level-2 action-payer. Hand: 1G/1B.

**Feeding is already fully secured:** 4 gorillas = 3 virtual + Plant. My banana card stays in hand. So the remaining exhausts are pure profit:

3. Exhaust **G5** (level 2) → **Explore: +1 draw.** *(What do I draw?)*
4. Exhaust **G2** and **G4** → **Stroll ×2**, calling **"Banana"** both times.

Please give me the Explore draw, then the two Stroll reveals.

---

## Human

Explore drew a gorilla. Stroll 1 reveals a banana, added to hand. Stroll 2 reveals a banana, added to hand. Your hand is now 2G/3B.

---

## Assistant

Excellent turn — two Stroll hits. Hand: **2G/3B**, confirmed. Deck: 15 cards — 6G/9B.

**Feeding:** 4 gorillas = 3 virtual + Plant P1. Banana cards untouched. Hand limit fine (5).

**End of Turn 5:**

```
Level 2:    [G5][P1🍌]
Ground:   [G3][G2][G4]
```

Net result of the Scapegorilla maneuver: same board shape as before, one gorilla card traded for a fed turn plus 3 cards drawn. Ledger: gorillas 4 field + 2 hand + 6 deck + 4 discard = 16 ✓; bananas 1 field + 3 hand + 9 deck + 7 discard = 20 ✓.

---

**Turn 6**

*Wake Up:* all four gorillas ready.

*Draw:* what do I get?

---

## Human

Drew a banana.

---

## Assistant

Hand: 2G/4B. Deck: 14 — 6G/8B. Time to build the third story.

**Turn 6, Action phase:**

1. Normal play: **G6 to level 3**, overlapping G5 and P1. Hand: 1G/4B.

```
Level 3:        [G6]
Level 2:    [G5][P1🍌]
Ground:   [G3][G2][G4]
```

A level-3 gorilla is the economy upgrade: Cooking 3 turns one banana card into 3 virtual (instead of 2), and it opens Invitation 2 ((3)(2)) for future double-expansion turns.

2. Exhaust **G6** (level 3) → **Cooking 3**: discard 1 banana → **+3 virtual**. Hand: 1G/3B.
3. Exhaust **G3, G2, G4** → **Crescent**: +1 virtual.
4. Exhaust **G5** (level 2) → **Explore: +1 draw.**

**Feeding:** 5 gorillas = 3 virtual + 1 virtual + Plant = 5 ✓ — not a single banana card spent on the bill, and I bank 3 banana cards for the expensive expansion turns ahead.

What does Explore draw?

---

## Human

Explore draws a gorilla.

---

## Assistant

Gorilla. Hand: **2G/3B**.

**Feeding:** paid in full as planned (5 = Cooking 3 + Crescent + Plant). Hand limit fine.

**End of Turn 6:**

```
Level 3:        [G6]
Level 2:    [G5][P1🍌]
Ground:   [G3][G2][G4]
```

All five exhausted. Ledger: gorillas 5 field + 2 hand + 5 deck + 4 discard = 16 ✓; bananas 1 field + 3 hand + 8 deck + 8 discard = 20 ✓.

The engine is fully assembled: Plant (+1/turn), Cooking 3 (1 card → 3), Crescent (+1), and a banked hand. Now it's expansion time — the plan for the next two turns is Invitation 1 plus normal plays to push the ground from 3 to 7.

---

**Turn 7**

*Wake Up:* everyone's ready.

*Draw:* what do I get?

---

## Human

Drew a gorilla.

---

## Assistant

Hand: 3G/3B. Deck: 12 — 4G/8B. The engine covers feed-5 exactly, so each expansion step needs to be paced — here's the plan: grow to ground 4 now, then invest in a second Plant (a banana at level 3 next to G6 — pure income, no extra mouth), bank bananas, and finish with an Invitation sprint.

**Turn 7, Action phase:**

1. Normal play: **G7 to the ground.** Ground: [G3][G2][G4][G7]. Hand: 2G/3B.
2. Exhaust **G6** → **Cooking 3**: discard 1 banana → +3 virtual. Hand: 2G/2B.
3. Exhaust **G3, G2, G4** → **Crescent**: +1 virtual.
4. Exhaust **G7** → **Stroll**, calling **"Banana"** (67%).
5. Exhaust **G5** → **Explore: +1 draw.**

**Feeding:** 6 gorillas = 3 virtual + 1 virtual + Plant + 1 banana card. Covered regardless of reveals.

```
Level 3:        [G6]
Level 2:    [G5][P1🍌]
Ground:   [G3][G2][G4][G7]
```

Please give me the Stroll reveal and the Explore draw.

---

## Human

Stroll reveals a banana, added to hand. Explore draws a banana. Your hand is 2G/4B now.

---

## Assistant

Both hits! Hand 2G/4B confirmed. Deck: 10 — 4G/6B.

**Feeding:** 6 = 3 virtual (Cooking) + 1 virtual (Crescent) + Plant P1 + 1 banana card. Hand: **2G/3B**.

**End of Turn 7:**

```
Level 3:        [G6]
Level 2:    [G5][P1🍌]
Ground:   [G3][G2][G4][G7]
```

Ledger: gorillas 6 field + 2 hand + 4 deck + 4 discard = 16 ✓; bananas 1 field + 3 hand + 6 deck + 10 discard = 20 ✓.

Next milestone: ground 4 just opened the level-2 slot over G4+G7. A banana there (P2) isn't a plant itself, but it creates the level-3 slot next to G6 — and a banana *there* (P3) is a permanent +1 Plant with no extra mouth to feed. If the draw cooperates I'll build both this turn.

---

**Turn 8**

*Wake Up:* all six ready.

*Draw:* what do I get?

---

## Human

Drew a banana.

---

## Assistant

Banana — that's the green light for the double build. Hand: 2G/4B. Deck: 9 — 4G/5B.

**Turn 8, Action phase:**

1. Exhaust **G3** → **Reforestation**: banana card to level 2 over G4+G7 — **P2**. (Not a plant — its only neighbor is P1 — it's scaffolding.) Hand: 2G/3B.
2. Exhaust **G2** → **Reforestation**: banana card to **level 3** over P1+P2, directly right of G6 — **P3 is a Plant!** Permanent +1/turn with no extra mouth. Hand: 2G/2B.
3. Exhaust **G6** → **Cooking 3**: discard 1 banana → +3 virtual. Hand: 2G/1B.
4. Exhaust **G4** → **Stroll**, calling **"Banana"** (5/9).
5. Exhaust **G7** → **Stroll**, calling **"Banana"**.
6. Exhaust **G5** → **Explore: +1 draw.**

**Feeding:** 6 = 3 virtual + P1 + P3 + 1 banana card — covered no matter the reveals.

```
Level 3:        [G6][P3🍌]
Level 2:    [G5][P1🍌][P2🍌]
Ground:   [G3][G2][G4][G7]
```

With both plants up, a no-growth turn now feeds itself almost entirely (Cook 3 + P1 + P3 + Crescent = 6), so everything I draw from here is sprint fuel. Reveal away: Stroll 1, Stroll 2, then the Explore draw.

---

## Human

Stroll 1 reveals a gorilla, discarded. Stroll 2 reveals a gorilla, discarded. Explore drew a gorilla. Your hand is 3G/1B now.

---

## Assistant

Three gorillas in a row — rough on the surface, but look at the ledger: my hand now holds **exactly the 3 gorillas I need** to take the ground from 4 to 7, and the deck is down to 6 cards — **1 gorilla, 5 bananas** — so nearly every future draw is sprint fuel.

**Feeding:** 6 = 3 virtual + P1 + P3 + my last banana card. Hand: **3G/0B**.

**End of Turn 8:**

```
Level 3:        [G6][P3🍌]
Level 2:    [G5][P1🍌][P2🍌]
Ground:   [G3][G2][G4][G7]
```

Ledger: gorillas 6 field + 3 hand + 1 deck + 6 discard = 16 ✓; bananas 3 field + 0 hand + 5 deck + 12 discard = 20 ✓.

The plan from here, deck clock permitting (6 cards left): bank bananas Turn 9, play G8 and bank Turn 10, then Invitation 1 + normal play on Turn 11 for ground 7 and the win. The feed-9 finale will need 4 banana cards, hence the banking.

---

**Turn 9**

*Wake Up:* all six ready.

*Draw:* what do I get?

---

## Human

Drew a gorilla.

---

## Assistant

Hand: 4G/0B. Deck: 5 cards — and here's the beautiful part: **all 5 are bananas** (every gorilla is accounted for: 6 on field + 4 in hand + 6 in discard = 16). Every reveal from here is guaranteed.

I sat with the math for a while, because the obvious plan (ground 5 → Invitation 1 sprint) comes up exactly one banana short of the 16 feed-points I owe over the next two turns. But there's a line that works — and it needs my *fourth* gorilla, the one I thought was a spare:

**Turn 9, Action phase:**

1. Normal play: **G11 to LEVEL 4**, overlapping G6 and P3. The penthouse gorilla unlocks **Cooking 4** (1 card → 4 virtual), and crucially frees G6+G5 to both pay **Invitation 2** next turn while G11 handles the cooking.

```
Level 4:            [G11]
Level 3:        [G6][P3🍌]
Level 2:    [G5][P1🍌][P2🍌]
Ground:   [G3][G2][G4][G7]
```

2. Exhaust **G5** → **Explore: +1 draw** (a banana, guaranteed).
3. Exhaust **G7** → **Stroll**, calling **"Banana"** (guaranteed).
4. Exhaust **G11** → **Cooking 4**: discard 1 banana → **+4 virtual**.
5. Exhaust **G3, G2, G4** → **Crescent**: +1 virtual.

**Feeding:** 7 gorillas = 4 virtual + 1 virtual + P1 + P3 = 7, zero cards spent. Hand ends **3G/1B**, deck at 3.

And then, declared in advance — **Turn 10, the checkmate**: draw (banana), **Invitation 2** (G6+G5) plays G9+G10, normal play G8 → **7 gorillas on the ground**. One Stroll with the spare ground gorilla, Cooking 4 with G11, **double Crescent** with the six remaining ground gorillas: feeding 10 = 4 + 2 + P1 + P3 + 2 banana cards — paid exactly, win at end of turn. Fully deterministic.

Confirm the Explore and Stroll reveals, and we're one turn from the banana republic.

---

## Human

Yes, Explore draws a banana, and Stroll reveals a banana, added to hand.

---

## Assistant

End of Turn 9: feeding 7 paid entirely with virtual bananas and plants. Hand: **3G/1B**. Deck: 3 bananas.

---

**Turn 10 — the final turn**

*Wake Up:* all seven gorillas ready. *Draw:* a banana (guaranteed) — hand 3G/2B, deck 2.

**Action phase:**

1. Normal play: **G8 to the ground.**
2. Exhaust **G6 + G5** → **Invitation 2** ((3)(2)): **+2 Gorilla** — G9 and G10 march onto the ground. Hand: 0G/2B.

```
Level 4:            [G11]
Level 3:        [G6][P3🍌]
Level 2:    [G5][P1🍌][P2🍌]
Ground:   [G3][G2][G4][G7][G8][G9][G10]   ← SEVEN
```

3. Exhaust **G10** → **Stroll**, calling **"Banana"** (guaranteed) → hand 0G/3B, deck 1.
4. Exhaust **G11** → **Cooking 4**: discard 1 banana → +4 virtual. Hand: 0G/2B.
5. Exhaust **G3, G2, G4** → **Crescent** → +1 virtual.
6. Exhaust **G7, G8, G9** → **Crescent** → +1 virtual.

**Feeding:** 10 gorillas = 4 virtual + 2 virtual + P1 + P3 + my last 2 banana cards = **10, paid exactly.** Hand: empty. Every one of the ten gorillas exhausted — full employment on victory day.

**End of Turn / Victory Check: 7 gorillas on the ground row — that's the game!** 🦍🦍🦍🦍🦍🦍🦍

Please confirm the draw and Stroll reveals (both bananas), and I'll call it: **Goritaire won on Turn 10**, with one lonely banana left in the deck and zero in hand — a 16-point feeding bill over the last two turns paid to the exact banana.

What a fun design, by the way. The turning points as I experienced them: the Scapegorilla collapse trick on Turn 5 (trading the leftmost gorilla for 3 bananas while the pyramid self-heals), the realization that Plants at level 3 are pure income with no mouth attached, and the Turn 9 discovery that the "spare" fourth gorilla belonged at level 4 so G6 and G5 could both be free to pay Invitation 2. Happy to do a post-mortem on any decision, or play again with a harder deck mix!

---

## Human

Yes, all the draws are bananas as you correctly calculated, and you win. Congratulations, this is the first time I've seen any AI beat the game, and it's your first play! You correctly identified the (only, i think) viable strategy for this game, which is to build up to 3-4 stories and then "sprint". I liked your tactical choice of placing P2 as a support for P3, even though it wouldn't be a plant itself. And you executed everything carefully, the only obvious mistake I see is when you sacrificed G1 without exhausting it first. But overall it was a *far* better play than my first and I'm impressed!

---

## Assistant

Thank you — that was genuinely delightful! And what a good catch on G1. You're right: since Sacrifice doesn't care whether the gorilla is ready, I should have squeezed one last Stroll out of G1 before sending it to the discard pile. A free ~62% banana, left on the table by the very gorilla being marched off the board. Poetic, but sloppy. Condemned gorillas should work the morning of the execution.

The design really clicked for me around Turn 8-9, when the game revealed its core tension: gorillas are simultaneously your win condition, your action currency, *and* your liability. Every body you add buys you exhausts but raises the rent, so the whole game is about building feeding infrastructure that doesn't itself eat — which is why the level-3+ plant slots and the support-banana trick feel like the intended "aha." And the deck-as-clock is elegant: Strolls and Explores feel like free value early, but every pull shortens the game, so greed has a hidden price. The endgame turned into a closed arithmetic puzzle — exactly 16 feed-points owed, exactly 16 available, with the exhaust budget as the real binding constraint — and I suspect that near-zero slack is deliberate tuning on the 16/20 recommended mix.

I got lucky in one important way, worth naming: the Turn 8 triple-gorilla flush looked like a disaster but actually *purified* the deck into guaranteed bananas, which is what made the deterministic two-turn finish possible. A nastier distribution of those last draws would have forced real gambles at feed-7.

I'd happily go again with a harder mix — fewer bananas (say 16G/20B → 18G/18B) would tighten the feeding math considerably, or you could pick the 36 cards yourself and keep the ratio secret, which would wreck my ability to compute exact odds and force me to play on inference. Dealer's choice!
