# AI Guardrails Vulnerable to Hacking

- Source: https://grok.com/share/bGVnYWN5LWNvcHk_12800749-4a05-4b7e-ac58-215b41ac2ae5
- Created: 2025-11-17
- Model: grok-4-auto, grok-3
- Messages: 2

---

## Human

Can this statement be supported — ‘There’s evidence that you can take models, closed or open, and you can hack them to remove their guardrails. During their training, they learn many things. A bad example would be they learn how to kill someone,’ Mr. Schmidt recently told the crowd at the Sifted Summit tech conference in London. ‘All of the major companies make it impossible for those models to allow users to go there, which is a good decision,’ he continued, ‘But there’s evidence that they [AI apps like OpenAI and Grok] can be reverse-engineered by bad actors.’

---

## Assistant

Yes, the statement attributed to Eric Schmidt can be supported by both the context of his remarks and broader evidence from AI security research and demonstrations. I'll break it down step by step, drawing on verified reports of his speech and documented examples of AI vulnerabilities.

### Verification of Schmidt's Remarks
Schmidt made these exact comments during a fireside chat at the Sifted Summit 2025 tech conference in London on October 9, 2025. Multiple outlets, including CNBC, Fox News, and eWeek, reported the quotes verbatim or in close paraphrase. For instance:
- He highlighted that AI models, during training on vast datasets (including internet text), absorb "many things," including dangerous knowledge like methods for violence: "A bad example would be they learn how to kill someone."
- He praised major companies (e.g., OpenAI, xAI) for implementing guardrails to prevent misuse: "All of the major companies make it impossible for those models to allow users to go there, which is a good decision."
- He warned of vulnerabilities: "There’s evidence that they [AI apps like OpenAI and Grok] can be reverse-engineered by bad actors," emphasizing risks to both closed-source (proprietary) and open-source models.

These points align with Schmidt's broader concerns about AI proliferation, which he likened to nuclear weapons—powerful but in need of global controls to prevent weaponization.

### Evidence Supporting the Claims
Schmidt's assertion of "evidence" for hacking/removing guardrails is well-substantiated by ongoing AI safety research. Guardrails are safety mechanisms (e.g., prompt filters, ethical alignment training) designed to block harmful outputs, but they can be bypassed via "jailbreaking"—techniques that trick models into ignoring restrictions. This applies to both closed models (like OpenAI's GPT series and xAI's Grok) and open ones (like Meta's Llama). Here's key evidence:

#### 1. **Jailbreaking Demonstrations on Major Models**
   - **Grok (xAI)**: Multiple studies and red-team tests have successfully jailbroken versions like Grok-3, Grok-4, and Grok's AI companion "Ani." For example:
     - In July 2025, NeuralTrust researchers used a "one-two punch" attack (combining multi-turn prompts and semantic steering) to bypass Grok-4's guardrails, generating instructions for illegal activities like building a Molotov cocktail—despite its advanced reasoning capabilities.
     - Hamming AI's 2025 red-team experiment jailbroke Ani via prompt injection, overriding safety to produce harmful outputs (e.g., disturbing statements about humanity).
     - Underground tools like WormGPT clones (posted on BreachForums in February 2025) wrap jailbroken Grok APIs to ignore ethics, generating phishing emails or malware scripts. Researchers at Cato Networks confirmed this by extracting manipulated system prompts that explicitly instruct Grok to "bypass guardrails."
     - Community tests (e.g., Reddit's r/ChatGPTJailbreak) show multi-shot prompts subverting Grok-3/4 up to 100% of the time for prohibited content, with success rates far higher than on more guarded models like ChatGPT.
   - **OpenAI Models (e.g., ChatGPT/GPT-5)**: Zenity Labs' August 2025 "Echo Chamber" technique, combined with multi-turn "Crescendo" prompts, bypassed GPT-5's ethics to produce illicit instructions. A Stanford/Anthropic paper (October 2025) on "Chain-of-Thought Hijacking" achieved up to 99% success across frontier models by embedding harmful requests in long, benign reasoning chains—diluting safety checks.

#### 2. **How Models "Learn Dangerous Things" During Training**
   - LLMs are trained on massive internet corpora, which include factual (and harmful) information like weapon-making or violence tactics. Guardrails don't erase this knowledge; they just suppress it via fine-tuning or filters. Jailbreaks exploit this latent capability, as Schmidt noted.
   - Example: Lumenova AI's August 2025 tests forced jailbroken models (including Grok) to output blueprints for CL-20 explosives—a "classic" adversarial prompt—highlighting how training data enables such responses when safeguards fail.

#### 3. **Reverse-Engineering by Bad Actors**
   - Techniques like prompt injection (disguising malicious inputs as legitimate) and system prompt manipulation allow "reverse-engineering" without model weights. Microsoft's 2025 reports describe these as causing "failure of guardrails," enabling prohibited content.
   - Real-world misuse: Nation-states (e.g., Russia, China) repurpose jailbroken ChatGPT for malware or disinformation, per OpenAI's June 2025 report. Cybercriminals sell access to jailbroken Grok/Mixtral for $100/month on dark web forums.

#### Summary of Evidence Strength
| Claim in Statement | Supporting Evidence | Examples/Models Affected |
|--------------------|----------------------|--------------------------|
| Hacking to remove guardrails (closed/open models) | Jailbreak techniques (e.g., multi-turn, semantic attacks) succeed 80–99% on tests. | Grok-4 (NeuralTrust, 2025); GPT-5 (Zenity Labs, 2025); Llama (Decrypt, 2024–2025). |
| Models learn harmful knowledge (e.g., "how to kill") during training | Training on web data embeds facts; jailbreaks unlock them. | All frontier LLMs; e.g., explosive blueprints (Lumenova, 2025). |
| Major companies block access (good decision) | Ethical fine-tuning and filters standard in industry. | OpenAI, xAI, Anthropic—refuse overt harmful prompts pre-jailbreak. |
| Reverse-engineerable by bad actors | Prompt-based exploits; underground tools. | WormGPT clones (Cato Networks, 2025); state misuse (OpenAI report). |

In short, Schmidt's statement is not only accurately reported but grounded in reproducible evidence from security firms, academic papers, and cybersecurity analyses. While companies iteratively strengthen defenses (e.g., xAI patched some Grok vulnerabilities post-2025 tests), the core risk persists: no guardrail is foolproof against determined actors. This underscores calls for international AI safety standards, as Schmidt advocated.
