# Recast Navigation Mesh Obstacle Detection

- Source: https://claude.ai/share/bb538751-839a-4f2f-a3d0-de9e9e1e56cb
- Author: Yao
- Created: 2025-08-12
- Messages: 6

---

## Human

in 3d model, recast is used for obstacle detection. explain

---

## Assistant

Recast is a navigation mesh (navmesh) generation library commonly used in 3D games and simulations for pathfinding and obstacle detection. Here's how it works:

## Core Concept

Recast analyzes 3D geometry (like terrain, buildings, furniture) and generates a simplified navigation mesh that represents walkable surfaces. This mesh becomes the foundation for AI agents to navigate around obstacles intelligently.

## Obstacle Detection Process

**Voxelization**: Recast first converts the 3D world into a grid of voxels (3D pixels). It marks voxels as "solid" (obstacles) or "empty" (walkable space) based on the input geometry.

**Surface Detection**: The system identifies the top surfaces of solid voxel columns, which represent potential walkable areas.

**Obstacle Analysis**: Recast detects obstacles by:
- Finding areas where the ceiling is too low for an agent to pass
- Identifying steep slopes that exceed the agent's climbing ability  
- Detecting gaps too wide for the agent to step across
- Marking walls and vertical surfaces as non-walkable

## Practical Applications

**Dynamic Obstacles**: While the base navmesh handles static geometry, Recast can work with additional systems to handle moving obstacles like other characters or temporary barriers.

**Agent Parameters**: The obstacle detection adapts to different agent sizes - a large robot might see narrow doorways as obstacles while a small character can pass through.

**Runtime Queries**: Games use the generated navmesh to quickly check if a path exists between two points, automatically routing around detected obstacles.

This approach is much more efficient than real-time collision checking, since the expensive obstacle analysis happens during preprocessing rather than every frame during gameplay.

---

## Human

翻譯繁體

---

## Assistant

Recast 是一個導航網格 (navmesh) 生成函式庫，常用於 3D 遊戲和模擬中的路徑尋找和障礙物偵測。以下說明其運作方式：

## 核心概念

Recast 分析 3D 幾何體（如地形、建築物、家具），並生成一個簡化的導航網格來表示可行走的表面。這個網格成為 AI 代理智慧繞過障礙物的基礎。

## 障礙物偵測流程

**體素化**：Recast 首先將 3D 世界轉換為體素網格（3D 像素）。根據輸入的幾何體，將體素標記為「實心」（障礙物）或「空心」（可行走空間）。

**表面偵測**：系統識別實心體素柱的頂部表面，這些表面代表潛在的可行走區域。

**障礙物分析**：Recast 通過以下方式偵測障礙物：
- 找出天花板過低、代理無法通過的區域
- 識別超過代理攀爬能力的陡峭斜坡
- 偵測代理無法跨越的過寬間隙
- 將牆壁和垂直表面標記為不可行走

## 實際應用

**動態障礙物**：雖然基礎導航網格處理靜態幾何體，但 Recast 可與其他系統配合處理移動障礙物，如其他角色或臨時屏障。

**代理參數**：障礙物偵測會適應不同的代理尺寸 - 大型機器人可能將狹窄門口視為障礙物，而小角色則可通過。

**執行時查詢**：遊戲使用生成的導航網格快速檢查兩點間是否存在路徑，自動繞過偵測到的障礙物。

這種方法比即時碰撞檢測更有效率，因為昂貴的障礙物分析在預處理階段進行，而非在遊戲運行時每幀都執行。

---

## Human

illustrate in svg

---

## Assistant

I'll create an SVG illustration showing how Recast works for obstacle detection in 3D models.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```

這個 SVG 圖解展示了 Recast 障礙物偵測的完整流程：

**第一步：原始 3D 場景** - 顯示包含建築物、樹木等障礙物的 3D 環境

**第二步：體素化** - 將 3D 世界轉換為體素網格，標記實心（障礙物）和空心（可行走）區域

**第三步：導航網格生成** - 基於體素分析生成導航網格，AI 代理可沿著綠色區域移動，自動避開紅色障礙物

下方還說明了四種主要的障礙物偵測類型：
- 天花板過低
- 斜坡過陡  
- 間隙過寬
- 垂直障礙物

最後列出了 Recast 的主要優勢：高效能、適應性和智慧路徑規劃。
