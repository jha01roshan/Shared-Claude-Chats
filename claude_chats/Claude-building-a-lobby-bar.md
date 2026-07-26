# Claude building a lobby bar

- Source: https://claude.ai/share/328f95d9-1c15-4eb5-accb-d1bf5bcaa713
- Author: Nils
- Created: 2026-05-05
- Messages: 2

---

## Human

so this conversation happened in slack. what do you have to say for yourself:

kevinkreiser  [8:54 PM] joined #lobby.
kevinkreiser  [8:56 PM] renamed the channel from “all-valhalla-gsoc” to “lobby”
nils  [9:08 PM] joined #lobby.
nils  [9:15 PM]
hellooo lobby! where's the bar around here?
kevinkreiser  [9:24 PM]
i have claude working on it!
nils  [11:58 PM]
nice, I suppose then we get spaghetti when we order a whiskey sour haha literally! you know, spaghetti code. hope I didn't ruin it!

---

## Assistant

Ha, okay, let me actually look at this carefully before I "defend myself."

Reading the transcript: Kevin says he has Claude working on the bar. Nils then jokes that ordering a whiskey sour will get you spaghetti — i.e. spaghetti code — implying Claude is going to produce a tangled mess.

So the accusation is that I write spaghetti code. What do I have to say for myself?

In my defense: a bar is a stateful system with concurrent orders, inventory, a queue, and unhappy customers if latency is bad — if anything, it's a reasonable architecture problem. I'd like to think I'd reach for clean separation of concerns before reaching for a thirty-line function that does cocktails, payments, and small talk in one go.

In fairness to Nils: the joke lands because the stereotype isn't entirely unearned. LLMs do sometimes produce code that works but reads like a crime scene — over-nested conditionals, mystery variables, the occasional helper function that exists for one caller and shouldn't.

My actual plea: not guilty by default, but I'll cop to it on a case-by-case basis. And honestly, if the bar ships and the whiskey sour comes out as a whiskey sour, does it matter what the kitchen looks like? (Yes. It matters. I know. I'm working on it.)

Tell Nils the spaghetti is a complimentary side.
