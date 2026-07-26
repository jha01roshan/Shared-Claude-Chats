# Motion vector ML models comparison

- Source: https://claude.ai/share/4edc67ba-7401-4f2b-931f-b99028e20290
- Author: Jan
- Created: 2026-07-12
- Messages: 4

---

## Human

Give an overview of various motion vector ML models, and include NVidia’s hardware option as well. Use Flame motion vectors, Nuke’s smart vectors and RAFT as the comparison baseline.

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

Here's a grounded comparison — I'll flag what's confirmed classical vs. actual deep learning, since that distinction is exactly where vendor marketing gets loose.

**Baseline three, as requested:**

- **Flame's native Motion Vector Generator** (pre-2025.x) is a classical GPU optical-flow solver, not a deep model. Flame only got genuine ML into its motion tools starting with 2025.1: Timewarp added a machine learning frame interpolation mode that uses two frames to generate an intermediate frame. By 2025.2 this extended to Morph and a general-purpose ONNX Inference node: Flame 2025.2 introduced a machine-learning slow-mo option in Timewarp and an Inference node for applying custom ONNX AI models.

- **Nuke's Smart Vector toolset** (SmartVector/VectorDistort/VectorCornerPin, native NukeX) is also classical — Foundry's own docs describe it as generating vectors from one worked frame to propagate paint/warp fixes across a sequence, with no ML claim anywhere in the toolset documentation: the vectors are generated in the SmartVector node and then piped into VectorDistort to warp the work, so you only need to render the motion vectors once. If you want an actual ML-based Smart Vector generator in Nuke, that's a third-party plugin, not native — see NNFlowVector below.

- **RAFT** (Teed & Deng, ECCV 2020) is the academic deep-learning baseline everything else gets measured against: it extracts per-pixel features, builds multi-scale 4D correlation volumes for all pairs of pixels, and iteratively updates a flow field through a recurrent unit that performs lookups on the correlation volumes. Reference: arXiv:2003.12039.

**Two concrete ML models that actually touch your stack:**

1. **RIFE**, running inside Flame via the open-source `flameTimewarpML` (talosh) — this is the closest thing to an "ML motion vector model in Flame" outside Autodesk's own ONNX Inference node: it added a slower model that uses RAFT to pre-calculate initial flow, and a faster model trained for rational timewarps that doesn't need iterations for ratios other than 0.5. So on akflame4/5 you could literally run RAFT-seeded RIFE flow alongside Autodesk's native ML Timewarp for comparison.

2. **NNFlowVector** (Pixelmania) — an actual ML-based Smart Vector generator for Nuke, filling the gap native Nuke doesn't: it uses deep learning technology and can produce both classic motion vectors free, and the more advanced Smart Vectors in the paid version, with internal stitching of inference patches so high-resolution images can be processed without needing large amounts of GPU VRAM.

**NVIDIA's hardware option — NVOFA:**

Not a software model at all — a dedicated silicon block. Turing-generation and later NVIDIA GPUs contain a hardware accelerator (NVOFA) for computing optical flow and stereo disparity between frames, working independently of graphics/CUDA cores, exposed through the Optical Flow SDK, which taps into Turing, Ampere, and Ada architecture GPUs to compute relative pixel motion in real time. Your akflame4's RTX PRO 6000 Blackwell qualifies (Blackwell continues the NVOFA lineage from Turing/Ampere/Ada). One honest caveat worth knowing: NVIDIA has not disclosed whether NVOFA's algorithm is classical or deep-learning based, or what publication it's based on — so don't take vendor slides at face value if anyone claims it's "AI-powered" without specifics.

**Quick take:** Flame-native and Nuke-native motion vectors are classical optical flow dressed as "motion vectors" / "Smart Vectors" — the ML upgrade path in each ecosystem comes from bolt-ons (Autodesk's own ONNX Inference node, or talosh's RIFE/RAFT script for Flame; NNFlowVector for Nuke), not the legacy nodes themselves. NVOFA is hardware acceleration, useful for speed, but its internals are a black box.

---

## Human

Please add GMFlow, FlowFormer, SEADraft, VideoFlow, NeuFlow, and FlowSeek to this comparison

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

Quick flag first: **"SEADraft" isn't a real paper** — you likely mean **SEA-RAFT**, which does exist and is the correct entry. I've added that instead.

Here's where all six sit relative to your three baselines. None of these six ship natively in Flame or Nuke or as a shipped NVIDIA feature — they're research-lineage models you'd only meet via ComfyUI/PyTorch custom nodes or if a VFX plugin vendor quietly adopted one under the hood.

**The RAFT lineage, in order of appearance:**

- **GMFlow** (CVPR 2022) — the first serious break from RAFT's iterative-refinement approach: instead of many recurrent updates, it reformulates flow as global matching, using a Transformer for feature enhancement, a correlation/softmax layer for global matching, and self-attention for flow propagation. Result: outperforms 31-refinement RAFT with only one refinement, while running faster.

- **FlowFormer** (ECCV 2022) — takes RAFT's 4D cost volume and feeds it through a transformer encoder-decoder instead of a plain recurrent unit, tokenizing the cost volume and decoding it with dynamic positional cost queries. It beat the best published Sintel results by 15–17%. A later variant (FlowFormer++, 2023) added masked cost-volume pretraining for further gains.

- **SEA-RAFT** (ECCV 2024, Oral) — a cleanup pass on RAFT itself rather than a new architecture: new loss function (mixture of Laplace), a directly-regressed initial flow instead of starting from zero, and rigid-motion pretraining. Net effect: at least 2.3x faster than prior methods while improving cross-dataset generalization on KITTI and Spring.

- **VideoFlow** (ICCV 2023) — the multi-frame break: instead of two-frame pairs, it estimates bidirectional flow across three-frame windows (TROF module) and propagates motion across the whole sequence (MOP module), beating FlowFormer++ by 15% on Sintel final and 19% on KITTI-2015. This is the one most relevant to actual video (vs. single image-pair) work, since it exploits temporal context the way your ProPainter/WAN VACE pipelines implicitly need.

- **NeuFlow / NeuFlow v2** (2024) — the efficiency break, aimed at edge devices: a global-to-local scheme (coarse global matching at 1/16 res, refined locally), hitting 10–80x speedup over prior SOTA at comparable accuracy, running real-time (~30fps) on a Jetson Orin Nano. Not a quality leader — a speed/footprint leader.

- **FlowSeek** (ICCV 2025) — the newest, and possibly most relevant to your ComfyUI stack: it combines optical flow with monocular depth foundation models (built on Depth Anything v2) and classical low-dimensional motion parametrization, trained on a single consumer GPU at ~8x lower training cost than comparable methods, beating SEA-RAFT by 10–15% on Sintel Final/KITTI cross-dataset generalization.

**Where this leaves the comparison:**

Your three baselines (Flame's classical MV generator, Nuke's classical Smart Vector toolset, NVOFA hardware) are all pre-deep-learning or non-disclosed-algorithm tools built for production stability, not benchmark accuracy. The six models above are academic SOTA chasers — genuinely more accurate on Sintel/KITTI, but none has a production VFX plugin wrapper that I can confirm exists (unlike RIFE, which got the flameTimewarpML wrapper, or the unnamed model inside NNFlowVector). If you wanted one of these in your actual pipeline, GMFlow or SEA-RAFT would be the practical picks — both have clean, maintained GitHub repos you could wire into a ComfyUI custom node on akflame4's Blackwell card, whereas FlowFormer and VideoFlow are heavier and NeuFlow/FlowSeek are optimized for goals (edge speed, cheap training) that don't match your use case.

References: GMFlow (arXiv:2111.13680), FlowFormer (arXiv:2203.16194), SEA-RAFT (arXiv:2405.14793, github.com/princeton-vl/SEA-RAFT), VideoFlow (arXiv:2303.08340), NeuFlow (arXiv:2403.10425) / NeuFlow v2 (arXiv:2408.10161), FlowSeek (arXiv:2509.05297, github.com/mattpoggi/flowseek).
