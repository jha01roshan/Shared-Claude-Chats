# Unidentified image analysis

- Source: https://claude.ai/share/09b26949-62aa-46ae-ac67-48102ecb8226
- Author: Bill
- Created: 2026-05-18
- Messages: 2

---

## Human

what does this show?

---

## Assistant

This is a screenshot from a CCTV-13 *Xinwen Lianbo* (新闻联播) segment showing what appears to be a Chinese cross-region distributed AI training/inference network visualization. Here's what it depicts:

**The central diagram** shows a four-node distributed compute topology connecting:

- **呼和 (Hohhot)** — Ascend: 64 cards — Parameter Server 4
- **青海 (Qinghai)** — 平头哥 (Pingtouge/T-Head): 128 cards — Parameter Server 3
- **上海 (Shanghai)** — 沐曦 (MetaX): 64 cards — Parameter Server 1
- **贵安 (Gui'an, Guizhou)** — Ascend: 64 cards — Parameter Server 2

The lines between nodes show inter-data-center distances ranging from 1,300+ km to 2,200+ km, demonstrating cross-regional networking of compute clusters. This is significant because it shows **heterogeneous domestic Chinese AI chips** working together across long distances — Huawei Ascend (昇腾), Alibaba's T-Head (平头哥, likely Hanguang or PPU), and MetaX (沐曦) GPUs operating as a unified parameter-server training/inference fabric.

**Left sidebar** lists what appear to be additional chip types in the pool: Ascend 910B/910C, 海光 DCU (Hygon), 寒武纪 (Cambricon) something P800, 燧原 (Enflame) C500, 天数 (Iluvatar) S5000, 壁仞 (Biren) 104, 武 819E (likely 摩尔线程/Moore Threads or similar), 7HP280, and 其他 (others).

**Right sidebar** shows a Token throughput chart (单位：百万 / unit: millions) trending around 3,500+ million tokens, dated roughly Feb 28 – March 17, 2026, and a "模型请求数Top" (Top Model Requests) ranking featuring DeepSeek-V4-Pro (#5), MiniMax-M2.5 (#1), DeepSeek-V4-Flash (#2), and GLM-5 (#3).

**The takeaway:** This is propaganda showcasing China's progress on **heterogeneous-chip, cross-region "computing power network" (算力网络)** infrastructure — the "East Data West Compute" (东数西算) vision in action, with Qinghai and Gui'an (both western hub locations) tied into Shanghai and Hohhot, running mixed domestic accelerators to serve the leading domestic open-weight models. It's a visual argument that China can do frontier-scale AI training and serving without NVIDIA, using a stitched-together fabric of domestic chips across thousands of kilometers.

Worth noting the 2,200+ km Qinghai–Shanghai link — that kind of distance has serious implications for synchronous training (latency, bandwidth, gradient sync), so this is more plausibly an inference-serving or asynchronous/pipeline-parallel training setup than a tightly-coupled pretraining run, despite the "Parameter Server" labeling.
