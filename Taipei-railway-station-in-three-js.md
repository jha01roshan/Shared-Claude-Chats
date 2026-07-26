# Taipei railway station in three.js

- Source: https://claude.ai/share/9bad6fb6-20e8-437a-94b9-bf1cefe4aa7c
- Author: Yao
- Created: 2026-06-10
- Messages: 2

---

## Human

Generate Taipei railway station in three.js

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

Taipei Main Station in Three.js (r128, no external control deps) — set at dusk to match your dark-theme preference.

What's modeled:

- **The icon**: cream six-story block with procedural window grids (canvas map + emissive map, ~55% lit), dark cornice band, and the grand vermilion hip roof built from a custom `BufferGeometry` (trapezoid slopes + triangular hips), with ridge beam, simplified end ornaments, white eave fascia, and tiled-course texture
- **臺北車站** signage on front and rear parapets (canvas-rendered Noto Sans TC), plus a columned entrance canopy with its own small hip roof
- **Context**: gridded plaza, Zhongxiao W. Rd. with looping taxis and a bus (headlight/taillight glow), street lamps with point lights, trees, and a ring of distant city silhouettes with sparse lit windows
- **Interaction**: drag to orbit, wheel/pinch to zoom, auto-orbit after 3.5 s idle, and **L** toggles dusk → full night (sun drops, window emissives ramp up)

The hip-roof helper (`hipRoofGeometry(w, d, h, ridgeLength)`) is reusable if you want to add the secondary roof tier or adapt it for other Chinese palace-style massing.
