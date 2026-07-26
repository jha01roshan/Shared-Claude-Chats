# Moebius model code and weights availability

- Source: https://claude.ai/share/551c3dc8-17ce-4a4b-a0c9-8cbded6c7bf1
- Author: Simon
- Created: 2026-06-22
- Messages: 10

---

## Human

Clone https://github.com/hustvl/Moebius/ and tell me if they published the code and weights to run this model anywhere

---

## Assistant

I'll help you check out this repository. Let me clone it and investigate.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Let me read the README to understand what this is and check for code/weights availability.
```
This block is not supported on your current device yet.
```

The repository is cloned. Now let me verify the claims in the README — specifically whether the weights actually exist on Hugging Face (the README claims them, but I should confirm they're real and accessible).
```
This block is not supported on your current device yet.
```

Now let me verify the Hugging Face weights links are real and accessible, since the README claims them but I should confirm rather than trust the claim.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

The search confirms the README's claims match what's publicly stated, but I haven't yet verified the actual Hugging Face weights repository is live and populated. Let me confirm that directly.
```
This block is not supported on your current device yet.
```

Let me try to directly verify the Hugging Face repository is populated, since none of my searches have actually surfaced the live model repo page yet (they keep echoing the GitHub README).
```
This block is not supported on your current device yet.
```

The README claims are corroborated by the GitHub page, arXiv, and the project page, but search won't surface the live Hugging Face repo as a fetchable page for me to inspect its file listing directly. Let me at least confirm the cloned code is real and complete rather than stubs, since you asked about code too.
```
This block is not supported on your current device yet.
```

Cloned it and dug through both the repo and the public claims. Here's what I found.

**Short answer: Yes to both — code and weights are published.**

**Code (confirmed, it's in the clone):** The repository contains a complete, non-stub implementation:
- Full inference pipeline (`infer/infer_moebius.py` plus `utils.py`/`utils_dataset.py`) with a ready-to-run command in the README.
- A 519-line distillation training script (`train_distillation.py`) with DDP launch scripts.
- The actual model architecture — the "LλMI block" / lambda + depthwise-conv UNet is real code (`model_lib/nets/unet_lambda_prune_lite.py` is ~850 lines, plus the GLA UNet and supporting layers), with config files defining the 512px, 9-in/4-out-channel pruned UNet.
- `requirements.txt`, model configs, and example image/mask data.

So the code to both train and run the model is genuinely there.

**Weights (claimed, pointed to, but I couldn't independently verify the files are live):** The README states that on June 18, 2026 they released the training and inference code and open-sourced the model weights on Hugging Face. Specifically it points to:
- Four checkpoints at `huggingface.co/hustvl/Moebius`: `pretrained`, `ft_places2`, `ft_celebahq`, `ft_ffhq` (each a `diffusion_pytorch_model.bin`).
- A required VAE from the sister repo `huggingface.co/hustvl/PixelHacker/tree/main/vae`.

One honest caveat: I was able to confirm these *claims* across the GitHub README, the arXiv paper, and the project page, but my search tools kept returning the README text rather than surfacing the actual Hugging Face file listing, so I couldn't directly eyeball that the `.bin` files are uploaded and downloadable. The pointers are all consistent and specific (exact paths, file names, directory layout), which is a good sign, but if you want certainty before investing setup time, the quickest check is to open `https://huggingface.co/hustvl/Moebius/tree/main` in a browser and confirm the four folders each contain a `diffusion_pytorch_model.bin`, plus the VAE under PixelHacker.

To actually run it, you'd download those into `./weight/Moebius/...` and `./weight/vae/`, then use the provided inference command (the README example uses the `ft_celebahq` checkpoint with cfg 2.0). Note the listed environment is fairly bleeding-edge (torch 2.7.1, diffusers 0.38.0, flash-linear-attention 0.3.2, and an unusual `python=3.14.4`), so expect some dependency wrangling.

Want me to verify the Hugging Face file tree is populated, or try setting up the environment and a test inference run in this sandbox?

---

## Human

Everyting on https://huggingface.co/hustvl/PixelHacker/tree/main is one year old

---

## Assistant

You're right to flag that — let me actually look at the page rather than take the README's word for it.
```
This block is not supported on your current device yet.
```

---

## Human

but https://huggingface.co/hustvl/Moebius/tree/main is from 4 days ago so that looks good

---

## Assistant

Right, and that distinction is exactly the thing that matters.

The year-old timestamp on PixelHacker isn't a red flag — it's expected. PixelHacker is the *predecessor* paper (arXiv 2504.20438, from April 2025), and in the Moebius setup it plays two roles: it's the distillation teacher, and its repo is where the **VAE** lives. That VAE is a standard frozen autoencoder (`sdvae_f8d4` in the config) that Moebius reuses unchanged. A frozen component being a year old has no bearing on whether it works — it's not something that gets re-trained per project. So PixelHacker being stale is consistent with it being the older sister work, not a sign anything's missing.

What actually needed to be recent is `hustvl/Moebius` itself — the four `diffusion_pytorch_model.bin` checkpoints (pretrained, ft_places2, ft_celebahq, ft_ffhq) that the inference code loads. You've now confirmed that repo was updated 4 days ago, which lines up with the June 18 release date in the README and the June 19 "No. 1 on Hugging Face" news item. That's the timestamp that should be fresh, and it is.

So the picture is consistent: complete and current code in the GitHub clone, current Moebius weights (4 days old), and a year-old-but-irrelevant VAE inherited from PixelHacker. Both pieces you need to run the model are published and present.

If you want a final sanity check before committing setup time, the one thing worth eyeballing is that each of the four Moebius subfolders actually contains its `.bin` (and that the `vae` folder under PixelHacker has both `config.json` and `diffusion_pytorch_model.bin`) — that confirms the files are real blobs and not just empty directory placeholders. Want me to go ahead and try a setup + test inference run in the sandbox?

---

## Human

For Moebius what are the options for running it right now - Python and NVIDIA CUDA only or other options too?

---

## Assistant

Good question — this comes down to what the code actually hardcodes and which dependencies are CUDA-bound. Let me check the clone rather than guess.
```
This block is not supported on your current device yet.
```

The requirements pin a CUDA build, but the real question is whether the *model code itself* calls CUDA-only kernels at inference. Let me check what the lambda/attention blocks actually import.
```
This block is not supported on your current device yet.
```

The lambda blocks the actual Moebius config uses look like pure PyTorch (`torch.einsum`), while the CUDA-bound `fla`/Triton import sits in a *different* UNet variant. But that only matters if loading the Moebius model doesn't drag in the `fla` import chain. Let me trace the imports the inference path actually triggers.
```
This block is not supported on your current device yet.
```

One more link to nail down: `model_lib/__init__.py` unconditionally imports the GLA UNet (the teacher), and `build_removal_model` lives in `removal_model.py`. If that path imports `model_lib` as a package, the `fla` dependency gets pulled in even for the pure-PyTorch student. Let me confirm.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Confirmed the full chain. Here's the real picture, based on the code rather than the README's marketing.

**Officially: Python + NVIDIA CUDA only.** The `requirements.txt` pins `torch==2.7.1+cu130` (a CUDA 13.0 wheel) and `flash-linear-attention[cuda]==0.3.2`, the `--device` flag defaults to `cuda`, and all the speed claims (26 ms/step, 15×) are measured on a single NVIDIA GPU. That's the only path the authors actually tested and support.

The wrinkle that determines everything else: the inference import chain pulls in a CUDA-bound dependency *even though the Moebius model itself doesn't need it*. Specifically, `removal_model.py` does `from model_lib import *`, and `model_lib/__init__.py` unconditionally imports the GLA teacher UNet, which imports `fla` (flash-linear-attention, built on Triton). So just *loading* the package requires `fla` to be importable. Meanwhile the actual Moebius student network (`UNet2DLambdaDWConvMixFFNConditionModel...`) is pure PyTorch — its lambda blocks are plain `torch.einsum`, no GPU kernels called at runtime, and the pipeline runs in fp32. That mismatch is what makes non-CUDA options *possible but not turnkey*.

Concretely, your options right now:

1. **NVIDIA CUDA (Linux, Python)** — the intended path, works as documented.

2. **CPU** — realistic with a small edit. The student model is pure PyTorch fp32 and `--device cpu` is accepted, but you'd first need to get past the `fla` import: either install a CPU-importable Triton/fla, or comment out the teacher import (`from .nets.unet_gla import UNet2DGLAConditionModel` in `model_lib/__init__.py`, plus its `.layers.gla` import) so loading the student doesn't drag in Triton. After that, expect it to run — just slowly, since it's a diffusion model doing multi-step sampling.

3. **Apple Silicon / MPS** — plausible but unverified, and needs the same teacher-import surgery *plus* more, because Triton has no macOS support, so `import fla` will hard-fail on a Mac until that import is stripped. Once stripped, the student is plain PyTorch and `--device mps` *might* work, but some einsum/conv patterns occasionally error or silently fall back on MPS, so this would need actual testing.

4. **AMD ROCm (Linux)** — Triton/fla does have a ROCm backend, so a ROCm box could in principle run it, but the pinned `+cu130` wheel means you'd hand-install ROCm torch and a matching fla. Untested by the authors; experimental.

5. **No packaged non-Python runtime exists.** It's released as raw PyTorch `.bin` checkpoints — there's no GGUF, ONNX, TensorRT, CoreML, llama.cpp, web, or mobile export. The README's "edge devices" line is an aspiration justified by the 0.22B size, not a shipped runtime.

So the honest bottom line: **out of the box it's NVIDIA CUDA + Python.** CPU is the most achievable alternative and only needs a couple of lines commented out; MPS and ROCm are believable given the architecture but unverified and require more fiddling.

Since this sandbox is CPU-only, I could try the CPU route — strip the teacher import and attempt a load/forward pass of the student to confirm it actually runs without CUDA. Want me to test that? It won't be able to download the multi-GB weights here (Hugging Face isn't a reachable domain in this environment), but I can at least verify the model instantiates and runs a forward pass on random input, which is the real portability question.

---

## Human

Muse on the feasibility of porting it to Transformers.js or similar and running it in a browser

---

## Assistant

Porting it to the browser is one of those cases where the headline number ("0.2B params!") undersells how favorable the *shape* of the model is, and the realistic runtime path isn't the one the question names. Let me think through it from the compute graph outward.

The encouraging part is that almost everything working against full Stable-Diffusion-in-the-browser is absent here. Three things specifically. First, the conditioning isn't a CLIP text encoder — from the code, `RemovalModel` feeds `input_ids` through a plain `nn.Embedding` (the Latent Categories Guidance idea inherited from PixelHacker). That means there's no 60–120M-param text tower to port, no tokenizer, no BPE merges to ship; the entire "prompt" side collapses to a tiny lookup table whose relevant rows you can bake in as a constant. Second, the LλMI blocks replace quadratic attention with linear-matrix einsum ops and depthwise-separable convs. Browsers hate big attention score matrices (memory spikes, awkward WebGPU tiling); linear attention sidesteps exactly that, so the architecture is unusually friendly to a constrained GPU runtime. Third, the config has no mid-block and runs DDIM at ~20 steps — a short, simple sampling loop that's trivial arithmetic to reimplement in JS. And critically, the CUDA-bound `fla`/Triton dependency we traced earlier lives only in the *teacher's* import path; the student's actual forward graph is vanilla ops. So the thing you'd export is clean.

Now the runtime reality, and here's where I'd gently redirect the premise: **Transformers.js is probably the wrong tool, even though it's the obvious name to reach for.** Transformers.js is organized around a catalog of supported architectures plus the HF `pipeline()` abstraction and tokenizers — it's built to run *known* model classes, not to orchestrate a custom diffusion UNet through a hand-rolled denoising loop with classifier-free guidance and a VAE round-trip. There's no architecture entry for "UNet2DLambdaDWConvMixFFN," nothing to tokenize, and the scheduler loop isn't something the library drives. You'd spend your time fighting its assumptions.

The path that actually fits is the layer *underneath* Transformers.js: **ONNX Runtime Web on the WebGPU backend**, with you writing the glue. Concretely — export three graphs (VAE encoder, the student UNet, VAE decoder) to ONNX via `torch.onnx`/`torch.export`, then write the DDIM step math, the CFG double-pass, the 9-channel input assembly (latent + masked-image latent + mask), and the final paste-back compensation in TypeScript. That's a few hundred lines of orchestration around three model files. People have already shipped SD-Turbo to the browser this exact way; Moebius is smaller, has no text encoder, and uses cheaper attention, so it's *more* tractable than those demos, not less.

Where the effort and risk actually concentrate:

The ONNX export of a diffusers `UNet2DConditionModel` subclass is the main time sink — custom config plumbing and attention-processor wiring sometimes trace badly, and you'll be chasing op-coverage gaps. Einsum and GroupNorm are the ops I'd worry about: they exist in ONNX, but whether ORT-Web's *WebGPU* kernels cover them (versus silently falling back to WASM/CPU, which would tank throughput) is the thing to verify before promising anyone interactivity. Precision is the second unknown — the reference pipeline runs fp32, and nobody has tested whether the lambda layers stay numerically well-behaved under fp16 or int8. Diffusion models are precision-sensitive, and linear-attention accumulations can be touchy, so I'd expect fp16 to need validation and quantization to be a quality gamble rather than a free win. Memory is the third: ~226M params is ~450MB at fp16, plus the VAE — large but shippable on desktop, dicey on mobile given browser ArrayBuffer and WebGPU buffer ceilings.

On performance: 26 ms/step on a datacenter NVIDIA GPU becomes maybe several hundred ms to ~1.5s/step on a decent laptop via WebGPU, times ~20 steps times 2 for CFG — so think tens of seconds per inpaint on good hardware, and "go make coffee" on anything CPU/WASM. WebGPU isn't optional here; it's the whole ballgame.

If I were scoping it: a desktop-WebGPU proof-of-concept that produces a first correct inpaint is plausibly a focused week or two, *assuming* the ONNX export cooperates — that assumption is the entire schedule risk. A polished, quantized, mobile-tolerant version is a different and much longer project. And one honest caveat: browser-ML tooling moves fast, so Transformers.js/Candle/ORT-Web diffusion support may be further along than my snapshot — worth a fresh look before committing to an architecture.

Two "or similar" runtimes genuinely worth a glance over ONNX-RT-Web, by the way: **Candle** (HF's own Rust→WASM stack, which already has Stable Diffusion examples and would let you express the custom UNet directly rather than fighting an export), and a **WebGPU-native compile via TVM/MLC**, which the MLC folks have used for diffusion. Candle in particular might dodge the ONNX-export headache entirely, at the cost of reimplementing the blocks in Rust.

Want me to actually attempt the first link in that chain here — strip the teacher import, instantiate the student, and try a `torch.onnx` export of its forward pass on random inputs to see whether the graph traces cleanly? That's the single most informative experiment, and it's the one I can run in this sandbox without the weights.
