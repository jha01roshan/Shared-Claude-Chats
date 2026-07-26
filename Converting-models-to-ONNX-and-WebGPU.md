# Converting models to ONNX and WebGPU

- Source: https://claude.ai/share/d11b8f2b-a52d-4ca2-be75-a710eaf18572
- Author: Simon
- Created: 2026-06-22
- Messages: 2

---

## Human

Clone https://github.com/simonw/moebius-web/ and use it to teach me all about the model and ONNX and the process of converting a model to ONNX and WebGPU and basically everything I'd need to know in order to fully understand this repo

---

## Assistant

I'll start by cloning the repo and exploring what's actually in it, then build up the explanation from there.
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

I have a thorough picture now. Let me check a couple remaining pieces, then build the explanation.
```
This block is not supported on your current device yet.
```

This is a genuinely rich repo — it's a complete, working port of a research diffusion model to run entirely in your browser, with a detailed lab log of every problem solved along the way. I've read all of it: the model card, the Python export scripts, the TypeScript pipeline, and the notes. Let me build you a proper teaching guide grounded in this exact code.
```
This block is not supported on your current device yet.
```

No markdown skill needed — markdown is plain text. Writing the guide now.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

I cloned the repo, read everything in it (the model card, all the Python export scripts, the TypeScript pipeline, and the lab notes), and wrote you a complete teaching guide grounded in the actual code.

Here's the short version of what this repo actually is, so the guide lands in context:

It takes **Moebius** — a 0.22-billion-parameter research image-inpainting model that ships as a PyTorch checkpoint — and makes it run *entirely in your browser* on your GPU. The conversion path is the heart of it: export the model's neural-network graphs to **ONNX** (a portable format), ship those `.onnx` files plus a small TypeScript program that re-implements the denoising loop, and execute them via **ONNX Runtime Web** on the **WebGPU** backend.

The guide builds every concept you need from the ground up, then ties each one back to specific lines in the repo:

- **Diffusion/inpainting fundamentals** — VAE latent space, the UNet denoiser, the DDIM loop, classifier-free guidance — with no assumed prior knowledge.
- **What makes Moebius port-friendly** — no text encoder (conditioning is a tiny learned embedding table), linear "lambda" attention instead of quadratic attention, and a resolution-lock that forces the fixed 512×512 design.
- **The three exported graphs** and their exact tensor interfaces, including the 9-channel inpainting input and the custom `0.13025` scaling factor.
- **ONNX itself** — the graph/operator/opset model, ONNX Runtime, and execution providers.
- **The conversion process** — `torch.onnx.export` tracing, `dynamic_axes`, parity checks, and the Safari Conv3d→Conv2d fix, which is the single best real-world example of "exporting cleanly isn't enough; you have to land on ops your target backend actually supports."
- **WebGPU + ORT-Web** — why it's mandatory (CPU was ~2:48 per inpaint), and the op-coverage audit that protects against silent CPU fallback.
- **The engineering tail** — caching 1.27 GB past Hugging Face's rotating signed URLs, COOP/COEP, and the TypeScript port of the DDIM math.

It ends with a full data-flow diagram, a suggested reading order through the repo's files, and a glossary. The best way to use it: read sections 1–5 first for the mental model, then open `python/export_onnx.py` and `web/src/pipeline.ts` side-by-side with sections 6–7 in front of you.

One note on freshness — the repo cites Moebius as "ECCV'26" with a 2026 arXiv ID, which is around or past my reliable knowledge cutoff, so for the upstream model's latest details you'd want to check the live Hugging Face and GitHub pages directly. Everything in the guide about *this* repo's mechanics comes straight from the code I read, not from memory.

If you'd like, I can go deeper on any one layer — for instance, a line-by-line annotated read of `export_onnx.py`, or a from-scratch derivation of the DDIM step formula in `ddim.ts`.
