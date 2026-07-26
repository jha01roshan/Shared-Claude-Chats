# Google computing units breakdown in Colab

- Source: https://claude.ai/share/c4df14f8-cbcc-4bca-80e8-de3cc4f77fb4
- Author: keisuke miyako
- Created: 2026-04-15
- Messages: 22

---

## Human

is it possible to get a cell by cell braekdown of google computing units on colab?

---

## Assistant

```
This block is not supported on your current device yet.
```

Unfortunately, **no — Google Colab does not provide a native cell-by-cell compute unit breakdown.** Here's what is and isn't possible:

**What Colab does offer:**
- You can track your overall compute unit balance in real time via **View Resources** under the Connect button in the top right corner.
- You can use `!nvidia-smi` in a code cell to see details about your allocated GPU and its current utilization, and the RAM/Disk tabs in the notebook interface give insights into memory and storage consumption.

**Why per-cell tracking isn't available:**
- Google doesn't explicitly define how compute units are calculated — they represent a dynamic allocation of CPU, GPU, and TPU resources, and the precise breakdown is hidden from users.
- Consumption is time-based at the runtime level, not per-cell. Approximate rates are around 4 units/hr for P100, 5 units/hr for V100, and ~13 units/hr for A100, but even these are dynamic with some unknown factor.

**Workaround — DIY cell-level tracking:**
You can approximate per-cell costs yourself by checking the balance before and after each cell using the Colab Python API. Here's a simple approach:

```python
# At the top of your notebook
from google.colab import runtime
import time

def get_cu_balance():
    # Reads current compute unit balance
    return runtime.unassign()  # Note: this disconnects — use carefully

# Better: just time each cell and estimate based on your GPU rate
import time
start = time.time()
# ... your cell code ...
elapsed = (time.time() - start) / 3600  # hours
# Multiply by your GPU rate (e.g., 13.08 for A100)
print(f"Estimated CU used: {elapsed * 13.08:.4f}")
```

This won't give you exact numbers, but it's the closest you can get to cell-level tracking given how opaque Colab's billing is.

---

## Human

how much does 1 computing unit cost

---

## Assistant

```
This block is not supported on your current device yet.
```

**1 compute unit = $0.10 (10 cents)**

Here's a quick breakdown of how that translates across plans and GPU types:

**Plans:**
- **Pay As You Go:** $9.99 for 100 units — **Colab Pro:** $9.99/month (includes 100 units) — **Colab Pro+:** $49.99/month (includes 500 units)

**Cost per GPU type** (approximate):

| GPU | CU/hr | Cost/hr |
|-----|-------|---------|
| T4 | ~1.76–1.96 | ~$0.18–$0.20 |
| V100 | ~5 | ~$0.50 |
| A100 | ~13–15 | ~$1.30–$1.50 |

So for example, with 100 compute units, a T4 GPU gives you roughly 51 hours of use, while an A100 can burn through up to 13 CUs per hour.

Keep in mind these rates are approximate — pricing does seem to fluctuate a little, possibly based on current demand, and your location may also be a factor.

---

## Human

5.37 units is how much

---

## Assistant

**5.37 units × $0.10 = $0.537** (about **54 cents**)

Pretty cheap for a single session!

---

## Human

convert to US dollars 14sec, 1sec,39 sec, 6 min, 10 min

---

## Assistant

I need a bit more info — do you mean **how much those durations cost in compute units and dollars** for a specific GPU type (T4, V100, or A100)?

Let me just show you all three so you can pick whichever applies to you:

| Duration | T4 (~$0.19/hr) | V100 (~$0.50/hr) | A100 (~$1.40/hr) |
|----------|---------------|-----------------|-----------------|
| 1 sec | $0.000053 | $0.000139 | $0.000389 |
| 14 sec | $0.00074 | $0.00194 | $0.00544 |
| 39 sec | $0.00206 | $0.00542 | $0.01517 |
| 6 min | $0.019 | $0.050 | $0.140 |
| 10 min | $0.032 | $0.083 | $0.233 |

For most free/Pro users on a **T4**, even a 10-minute cell run only costs about **3 cents**. The costs add up mainly when you leave a session running idle for hours.

---

## Human

in lora how may epochs should I run

---

## Assistant

Great question — it depends on a few things!
```
This block is not supported on your current device yet.
```

What are you working with? This'll help me give you a much more specific answer!

---

## Human

Q: What are you fine-tuning?
A: LLM (e.g. Llama, Mistral)

Q: How much training data do you have?
A: Small (100–1k samples)

Q: What's your goal?
A: Style/tone adaptation

---

## Assistant

For **style/tone adaptation on an LLM with 100–1k samples**, here's the guidance:

### Recommended: **3–5 epochs**

That's usually the sweet spot. Here's why:

- **Too few (1–2 epochs):** The model hasn't learned the style well enough — outputs will still feel like the base model
- **3–5 epochs:** Good style transfer without losing general capability
- **Too many (8–10+):** Overfitting — the model starts memorizing your training data and loses coherent generalization

### Practical tips for your setup:

- **Start at 3 epochs** and evaluate the outputs manually
- Watch your **training vs. validation loss** — if validation loss starts rising while training loss keeps dropping, stop there (that's overfitting)
- With small datasets, keep your **LoRA rank (r) low** — `r=8` or `r=16` is usually enough for style, higher ranks overfit faster
- Use a **low learning rate** like `2e-4` or `1e-4` to avoid blowing past the optimal weights

### Colab cost estimate (for context):
At 3–5 epochs on a small dataset, you're likely looking at **10–40 minutes** of A100 time — roughly **$0.23–$0.93**, very manageable.

If you're using a library like **Unsloth, Axolotl, or HuggingFace TRL**, they all support early stopping callbacks which take the guesswork out of it entirely.

---

## Human

when I say style I mean a lesser know programming language

---

## Assistant

Ah, that changes things quite a bit! That's closer to **task-specific / knowledge fine-tuning** than style — the model needs to learn syntax, patterns, and idioms it hasn't seen much of.

### Recommended: **5–15 epochs**

The rarer the language, the more epochs you need:

| Language familiarity in base model | Epochs |
|---|---|
| Somewhat known (e.g. Nim, Zig) | 5–8 |
| Rarely seen (e.g. Crystal, Raku) | 8–12 |
| Very obscure / custom DSL | 12–15+ |

### Key adjustments vs. style fine-tuning:

- **Bump LoRA rank higher** — `r=32` or `r=64` works better since the model needs to learn more new structure, not just adapt tone
- **More data matters more here** — if you're at the low end (~100 samples), lean toward more epochs; at 1k samples you can stay lower
- **Use code-focused base models** if possible — `CodeLlama`, `DeepSeek-Coder`, or `Mistral` fine-tuned on code will need far fewer epochs than a general LLM since they already understand code structure
- **Keep sequences long enough** to capture full functions/blocks, not just snippets

### Watch out for:
With a rare language there's a real risk the model **confuses syntax with more common languages** mid-generation. If you see that happening, more epochs + more diverse samples (covering edge cases, not just happy paths) will help.

What language is it, out of curiosity?

---

## Human

where do I set the rank
trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    dataset_text_field = "text",
    max_seq_length = max_seq_length,
    dataset_num_proc = 2,
    packing = False,
    args = TrainingArguments(
        per_device_train_batch_size = 2,
        gradient_accumulation_steps = 4,
        warmup_steps = 5,
# max_steps = 60,
        num_train_epochs = 1,
        learning_rate = 2e-4,
        fp16 = not is_bfloat16_supported(),
        bf16 = is_bfloat16_supported(),
        logging_steps = 1,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 3407,
        report_to = "none",
        output_dir = "outputs",
),
)

---

## Assistant

The rank isn't set in `SFTTrainer` — it's set earlier when you configure the **LoRA adapter on the model**. You're likely missing a `get_peft_model` / `FastLanguageModel.get_peft_model` step before the trainer. It looks like you're using **Unsloth**, so it would look like this:

```python
model = FastLanguageModel.get_peft_model(
    model,
    r = 32,                          # 👈 LoRA rank goes here
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj"],
    lora_alpha = 64,                 # usually 2x the rank
    lora_dropout = 0.05,
    bias = "none",
    use_gradient_checkpointing = "unsloth",
    random_state = 3407,
)
```

Then your `SFTTrainer` code follows exactly as you have it.

### For your use case (rare programming language):
```python
r = 32           # or 64 for very obscure languages
lora_alpha = 64  # keep it 2x rank
lora_dropout = 0.05
```

If you don't have this block at all, that's why the rank was never being set — the model would've been training without LoRA entirely, which is much slower and more memory-intensive on Colab.

---

## Human

how much usd is 2.78 computing units

---

## Assistant

**2.78 units × $0.10 = $0.278**

About **28 cents**.

---

## Human

I do not see my gguf file copied to drive what am I doing wrong
import shutil, glob, os
from unsloth import FastLanguageModel
model.save_pretrained_merged(
"/content/merged_model",
    tokenizer,
    save_method="merged_16bit",
)
for quant in ["q8_0", "q4_k_m"]:
    save_path = f"/content/drive/MyDrive/{model_name}-{quant}"
    os.makedirs(save_path, exist_ok=True)
    model.save_pretrained_gguf(
"/content/merged_model",   # local source
        tokenizer,
        quantization_method=quant,
)
    gguf_files = glob.glob("/content/merged_model/*.gguf")
for f in gguf_files:
print(f"Copying {f} → {save_path}")
        shutil.copy(f, save_path)

---

## Assistant

I can see a few issues in your code — mainly **indentation errors** and a **logic bug** where the `glob` and `copy` are outside the `for quant` loop. Here's the fixed version:

```python
import shutil, glob, os
from unsloth import FastLanguageModel

# Step 1: Merge weights first
model.save_pretrained_merged(
    "/content/merged_model",
    tokenizer,
    save_method="merged_16bit",
)

# Step 2: Quantize and copy each format
for quant in ["q8_0", "q4_k_m"]:
    save_path = f"/content/drive/MyDrive/{model_name}-{quant}"
    os.makedirs(save_path, exist_ok=True)

    # Save GGUF locally
    model.save_pretrained_gguf(
        "/content/merged_model",
        tokenizer,
        quantization_method=quant,
    )

    # Find and copy to Drive
    gguf_files = glob.glob("/content/merged_model/*.gguf")  # 👈 inside loop now
    for f in gguf_files:
        print(f"Copying {f} → {save_path}")
        shutil.copy(f, save_path)                           # 👈 indented correctly
```

### What was wrong:
1. **`glob` and `shutil.copy` were outside the `for quant` loop** — so they only ran once after both quantizations, and copied to the wrong `save_path`
2. **`print` and `shutil.copy` had mismatched indentation** — Python would throw an `IndentationError`
3. The GGUF files from the first quant may have been **overwritten** by the second before copying

### Also make sure:
- Google Drive is mounted: `from google.colab import drive; drive.mount('/content/drive')`
- `model_name` is defined as a string before this block

---

## Human

suggest lora training settings for this
#@title Train Gemma 4
MODEL_ID = "google/gemma-4-E2B-it"
model_name = MODEL_ID.split("/")[-1]
save_path = f"/content/drive/MyDrive/{model_name}-lora"
from unsloth import FastLanguageModel
import torch
max_seq_length = 1536 # based on n_embd
dtype = None
load_in_4bit = True # Use 4bit quantization to reduce memory usage. Can be False.
from trl import SFTTrainer
from transformers import TrainingArguments
from unsloth import is_bfloat16_supported
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = MODEL_ID,
    max_seq_length = max_seq_length,
    dtype = dtype,
    load_in_4bit = load_in_4bit,
)
model = FastLanguageModel.get_peft_model(
    model,
    r = 16, # Choose any number > 0 ! Suggested 8, 16, 32, 64, 128
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
"gate_proj", "up_proj", "down_proj",],
    lora_alpha = 16,
    lora_dropout = 0, # Supports any, but = 0 is optimized
    bias = "none",    # Supports any, but = "none" is optimized
    use_gradient_checkpointing = "unsloth", # True or "unsloth" for very long context
    random_state = 3407,
    use_rslora = False,
    loftq_config = None,
)
trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    dataset_text_field = "text",
    max_seq_length = max_seq_length,
    dataset_num_proc = 2,
    packing = False,
    args = TrainingArguments(
        per_device_train_batch_size = 2,
        gradient_accumulation_steps = 4,
        warmup_steps = 5,
# max_steps = 60,
        num_train_epochs = 1,
        learning_rate = 2e-4,
        fp16 = not is_bfloat16_supported(),
        bf16 = is_bfloat16_supported(),
        logging_steps = 1,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 3407,
        report_to = "none",
        output_dir = "outputs",
),
)
trainer.train()
# Save the model adapters and the tokenizer
model.save_pretrained(save_path)
tokenizer.save_pretrained(save_path)
print(f"Model saved successfully to {save_path}")

---

## Assistant

Based on your earlier context (rare programming language, small dataset 100–1k samples), here are the suggested changes:

```python
model = FastLanguageModel.get_peft_model(
    model,
    r = 32,                  # 👈 up from 16 (rare language needs more capacity)
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj"],
    lora_alpha = 64,         # 👈 up from 16 (keep 2x rank)
    lora_dropout = 0.05,     # 👈 add small dropout (helps with small datasets)
    bias = "none",
    use_gradient_checkpointing = "unsloth",
    random_state = 3407,
    use_rslora = True,       # 👈 enable (stabilizes training with higher rank)
    loftq_config = None,
)

trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    dataset_text_field = "text",
    max_seq_length = max_seq_length,
    dataset_num_proc = 2,
    packing = True,          # 👈 enable (better GPU utilization with small dataset)
    args = TrainingArguments(
        per_device_train_batch_size = 2,
        gradient_accumulation_steps = 4,
        warmup_steps = 10,   # 👈 up from 5 (smoother warmup with higher rank)
        num_train_epochs = 8, # 👈 up from 1 (rare language needs more passes)
        learning_rate = 1e-4, # 👈 down from 2e-4 (safer with higher rank)
        fp16 = not is_bfloat16_supported(),
        bf16 = is_bfloat16_supported(),
        logging_steps = 1,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "cosine", # 👈 cosine decays more smoothly than linear
        seed = 3407,
        report_to = "none",
        output_dir = "outputs",
    ),
)
```

### Summary of changes:

| Setting | Before | After | Why |
|---|---|---|---|
| `r` | 16 | 32 | Rare language needs more capacity |
| `lora_alpha` | 16 | 64 | Keep at 2× rank |
| `lora_dropout` | 0 | 0.05 | Prevents overfitting on small data |
| `use_rslora` | False | True | Stabilizes higher rank training |
| `packing` | False | True | Better efficiency with small dataset |
| `num_train_epochs` | 1 | 8 | Rare language needs more passes |
| `learning_rate` | 2e-4 | 1e-4 | Safer with higher rank |
| `warmup_steps` | 5 | 10 | Smoother warmup |
| `lr_scheduler_type` | linear | cosine | Gentler decay, better final quality |

After epoch 3–4, manually test some generations to check if the syntax looks right — if it's already good, you can stop early and save compute units.
