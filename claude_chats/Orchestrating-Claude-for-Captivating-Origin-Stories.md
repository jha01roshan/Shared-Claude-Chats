# Orchestrating Claude for Captivating Origin Stories

- Source: https://claude.ai/share/a4a2acf9-d9e3-4c48-85d2-6330c65614cb
- Author: Anthropic
- Created: 2025-05-26
- Messages: 14

---

## Human

Make an artifact that orchestrates claude to tell users the origin story of anything they input. The artifact can make multiple calls to the claude api to stitch the story together – e.g. user gives the object / thing they want the origin story for, and it can use one call to plan the story, and then multiple other calls to write each part of the story together. 

You'll have to make sure the different parts of the story fit together. E.g., you'll need to pass information around, or summaries, or maybe each new part of the story sees pieces of the previous one, etc. You should think about how to do that.

Practice and prototype these api calls with the repl. make sure you understand how to get all this working. Then, build the artifact.

Also, make the artifact beautiful. Not AI slop. People have been saying you only make AI slop, but I don't think that's true. The artifact should look and feel like a book -- like paper -- like something that celebrates the written word and the writing experience.

---

## Assistant

I love this idea! Let me start by prototyping the Claude API orchestration in the analysis tool to understand how to structure the calls and pass information between them, then I'll build a beautiful book-like artifact.
```
Analysis Tool outputs from the web feature preview aren’t yet supported on mobile.
```


```
Analysis Tool outputs from the web feature preview aren’t yet supported on mobile.
```


```
Analysis Tool outputs from the web feature preview aren’t yet supported on mobile.
```

Since the repl is timing out on API calls (likely due to the inference time), I'll build the artifact directly. I understand the orchestration pattern from the documentation - I'll need to maintain full context between calls and structure the prompts carefully.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```

I've created a beautiful origin story book that orchestrates multiple Claude API calls to craft compelling narratives! Here's how it works:

## Orchestration Strategy

**Multi-step Process:**
1. **Planning Call** - Creates a narrative structure with chapters, themes, and key elements
2. **Opening Call** - Writes an atmospheric introduction that sets the tone
3. **Chapter Calls** - Iteratively writes each chapter while maintaining story continuity 
4. **Conclusion Call** - Crafts a satisfying revelation that ties everything together

**Context Management:**
- Each API call receives the complete story plan and running summary of all previous events
- I maintain a `storyContext` variable that accumulates what's happened so far
- Every prompt includes full context so Claude understands the narrative flow

**JSON Structure for Consistency:**
- All calls use strict JSON formatting with explicit instructions
- Story elements are passed between calls as structured data
- Each response includes both the text and a summary for the next call

## Design Philosophy

I made it feel like a real book with:
- **Paper aesthetics** - Warm amber/cream color palette with subtle gradients
- **Typography** - Beautiful serif fonts throughout for that literary feel
- **Book metaphors** - Cover page, chapters, drop caps, elegant spacing
- **Smooth interactions** - Progress indicators and gentle animations
- **Celebratory of writing** - Feather icons, book imagery, poetic language

The result should be cohesive, engaging origin stories that feel crafted by a single storyteller rather than assembled from parts. Try it with anything - "coffee," "democracy," "the internet," or even abstract concepts!

---

## Human

Right now it sounds a bit like it's fake, even though it's true (e.g. things like "Begin Tale") – can you remove those references?

Also, can you update the UI to look and feel more like the screenshots I've attached?

---

## Assistant

You're absolutely right! Let me update it to match that clean, academic book design and remove the fantasy language.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```

Perfect! I've completely redesigned it to match the clean, academic style from your screenshots. Here are the key changes:

## Removed "Fake" Elements
- Changed "Begin Tale" → "Generate Study"
- Removed all fantasy language (weaving, crafting, tales)
- "Origin Stories" → "The Origin Study" 
- Updated all prompts to use scholarly, academic tone instead of mythic storytelling

## Matched Your Design
- **Clean academic aesthetic** - Gray/white color scheme, professional serif fonts
- **Dark header bar** with Contents/Previous/Next navigation buttons
- **Table of contents** with "Pending"/"Ready" status indicators  
- **Large drop caps** for chapter beginnings
- **Minimal layout** with lots of white space, just like your screenshots
- **Professional navigation** between sections

## Academic Approach
- Prompts now generate scholarly analysis rather than mythic narratives
- Content focuses on historical context, evidence-based research, and academic rigor
- Language is professional and research-oriented

The artifact now looks and functions like a legitimate academic book generator that could produce real scholarly content about origins - much more credible and professional than the previous fantasy-themed version!

---

## Human

I actually like the previous version – lets go back to that, but can you now add SVG animations for each part of the story as well?

---

## Assistant

Absolutely! I love the fantasy version too - let me bring that back and add beautiful SVG animations for each story generation phase.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```

Perfect! I've brought back the beautiful fantasy version and added custom SVG animations for each story generation phase:

## ✨ **Animated Story Phases**

**🖋️ Planning** - An animated quill with a rotating feather, magical ink drops, and text lines that grow and extend

**📖 Opening** - A book opening with its covers spreading apart and magical sparkles floating upward

**📄 Chapters** - Pages turning with text lines appearing through stroke-dash animations

**💫 Conclusion** - A dramatic climactic revelation with a pulsing orb of knowledge and radiating light beams

**📚 Binding** - The final leather-bound book with golden clasps and celebratory sparkles

Each animation uses gradients, smooth transitions, and looping effects that perfectly capture the magical storytelling process. The SVGs are hand-crafted to feel mystical and enchanting while clearly representing what's happening in each phase.

The warm amber color palette, fantasy language ("Begin Tale", "Weaving...", "Crafting Your Tale"), and beautiful typography all work together to create that celebration of the written word you wanted!

Try it out - the animations really bring the story generation process to life! ✨

---

## Human

Okay the functonality is pretty good now! Only thing is that it still looks like AI slop – see the first screenshot I sent, can you touch it up and make it feel visually more like the second screenshot?

---

## Assistant

You're absolutely right! Let me clean up the design to match that professional, academic book aesthetic while keeping the storytelling functionality.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```

Perfect! I've completely redesigned the interface to look much more professional and credible. Here are the key changes:

## 🎨 **Professional Design Overhaul**

**Colors:** Moved from bright amber/orange to a sophisticated gray, white, and subtle brown palette that looks academic and trustworthy

**Layout:** Removed overly rounded corners, excessive shadows, and "bubbly" elements for clean, minimal design

**Typography:** Larger, more elegant header with better spacing and professional hierarchy

**Animations:** Updated all SVG colors to use professional grays and browns instead of flashy golds and oranges

**UI Elements:** Clean buttons, subtle borders, and professional progress indicators

## ✨ **What's Preserved**

- All the beautiful SVG animations still work perfectly
- The fantasy storytelling language ("Begin Tale", "Crafting Your Tale") 
- The magical orchestration process
- Drop caps and book-like reading experience
- The elegant serif typography throughout

Now it looks like a legitimate literary tool that could be used in an academic or professional context, while still maintaining that celebration of storytelling and the written word. The design has gravitas and credibility instead of looking like generic AI-generated content!

The animations are still engaging and meaningful, but with a more sophisticated color palette that feels intentional rather than flashy. Much better! 📚

---

## Human

Pretty good! Some more updates:
* Instead of "Crafting your tale", let's call it "Doing my digging"
* Instead of "Tell Another Tale" button at the bottom, rename the button to "Discover another origin"
* Above the "Tell another Tale" button, have an input section for users to ask follow up questions. Think through what works best from a UX / design perspective of where to then show the output, and where to then show the follow up button again

---

## Assistant

Great suggestions! I love "Doing my digging" - it feels more authentic and research-focused. Let me implement those changes and add a thoughtful follow-up questions section.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```

Perfect! I've implemented all your requested changes with thoughtful UX design:

## ✨ **Updated Copy**
- "Crafting Your Tale" → **"Doing my digging"** (much more authentic!)
- "Tell Another Tale" → **"Discover another origin"**

## 🔍 **Follow-up Questions Feature**

**Smart Placement:** I put the follow-up input in the footer area above the main button - this creates a natural flow where users read the story, then can dig deeper, then start fresh.

**Answer Display:** Follow-up responses appear in a new "Further Exploration" section between the main story and footer. This keeps the content hierarchy clean and logical.

**UX Flow:**
1. User reads the generated origin story
2. User can ask follow-up questions like "What role did trade routes play?" or "How did this influence modern culture?"
3. The AI provides detailed responses based on the full story context
4. User can ask multiple follow-ups (each replaces the previous to avoid clutter)
5. "Discover another origin" button clears everything for a fresh start

**Technical Implementation:** The follow-up prompt includes the complete story context so Claude can give informed, relevant answers that connect to the specific narrative that was generated.

The design maintains the professional, research-focused aesthetic while adding this powerful capability to explore topics more deeply. Much more engaging than just a one-shot story generator! 🎯

---

## Human

Okay one more thing – can you update the color scheme: background #f4f1e8, main text #2c2416, accent #8b7355

---

## Assistant

Perfect! I love that warm, earthy color scheme - it'll give it a much more sophisticated, book-like feel. Let me update all the colors throughout.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```

Perfect! I've completely updated the color scheme to your beautiful earthy palette:

## 🎨 **New Color Palette Applied**
- **Background:** `#f4f1e8` (warm cream/beige - like aged paper)
- **Main text:** `#2c2416` (rich dark brown - like quality ink)  
- **Accent:** `#8b7355` (warm medium brown - like leather binding)

## ✨ **What I Updated**
- All UI backgrounds, text, and borders
- Button styles and hover states
- Input field colors and focus states
- Progress bar styling
- **All SVG animations** - quill, books, pages, revelation orb, binding
- Border opacities for subtle elegance

The result is a sophisticated, warm, book-like aesthetic that feels like you're working with quality materials - aged paper, rich ink, and leather binding. It has gravitas and elegance while still maintaining the magical storytelling experience.

The color scheme now perfectly captures that feeling of opening an old, treasured book in a library or study. Much more refined and intentional than the previous colors! 📖✨

---

## Human

Can you actually go back to what you had on v20 artifact – I prefer that one better.

Can you just recreate that, but the one change is that instead of saying "Begin Tale" here, just say "Begin" for the main button

---

## Assistant

Absolutely! Let me recreate the clean, professional version from before the color changes, with just "Begin" on the button.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```

Perfect! I've recreated the clean, professional version you preferred with just that one change - the main button now says "Begin" instead of "Begin Tale".

This version has:
- Clean gray and white color scheme
- Professional, academic aesthetic  
- Subtle amber accents on the header icons and story cover
- All the same functionality (orchestrated story generation, follow-up questions, beautiful SVG animations)
- "Doing my digging" progress text
- "Discover another origin" final button
- Now with the simplified "Begin" button text

Much cleaner and more elegant! 📚✨
