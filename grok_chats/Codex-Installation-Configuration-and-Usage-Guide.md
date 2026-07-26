# Codex: Installation, Configuration, and Usage Guide

- Source: https://grok.com/share/bGVnYWN5LWNvcHk_67ced173-7471-41d1-80ba-3ed14df252a0
- Created: 2025-10-14
- Model: grok-4-mini-thinking-tahoe
- Messages: 2

---

## Human

codex使用说明？🤔搜索寻找各种优质的文章内容，优先中文，优先在Linuxdo这个论坛找。

---

## Assistant

### Codex 使用说明指南

Codex 是 OpenAI 推出的代码生成与辅助开发工具，支持 CLI 命令行和 VSCode/Cursor 等插件形式，主要基于 GPT-5-Codex 模型，提供代码编写、调试、规划等功能。它特别适合全栈开发场景，能通过 MCP（Model Context Protocol）扩展工具调用，如代码检索、Web 搜索等。以下基于 Linux.do 论坛的优质教程和心得，总结安装、配置、基本使用及高级技巧。内容优先提取自论坛帖子，力求实用。

#### 1. 安装准备
Codex 的安装依赖 Node.js（推荐 20.x 版本以上）和 npm。Windows 用户需注意环境变量和路径设置，避免启动超时。

**关键步骤（Windows 环境，适用于 WSL2）：**
- 安装 Node.js：从官网下载 LTS 版，确保路径如 `C:\Program Files\nodejs\`。
- 全局安装 uv/uvx（用于 MCP 动态运行）：`pip install uv` 或 `pip3 install uv`。
- 安装搜索工具（优化性能，从 v0.41 起 ripgrep 已内置）：
  - Windows：`winget install sharkdp.fd ast-grep`。
  - WSL2/Debian：`apt install -y fd-find` 和 `npm i @ast-grep/cli -g`。
- 安装 Codex CLI：`npm install -g @openai/codex`（或从 GitHub 仓库 https://github.com/openai/codex 获取）。
- VSCode 插件：搜索 “Codex” 安装，支持 Cursor/Windsurf 等。

**注意事项：** 统一环境避免兼容问题；WSL2 用户用 `wsl --install` 初始化。安装后运行 `codex --help` 验证。

#### 2. 配置指南
配置主要在 `~/.codex` 目录下编辑 `config.toml`、`auth.json` 和 `AGENTS.md`。支持第三方 API（如 packycode、nonocode）绕过 OpenAI 限制。

**auth.json（API 密钥）：**
```
{
  "OPENAI_API_KEY": "你的第三方 API Key"
}
```
- 从供应商（如 packycode）获取 Key，切换时更新文件并重启 IDE。

**config.toml（模型与 MCP）：**
基础模型设置：
```
model = "gpt-5-codex"
model_reasoning_effort = "high"  # 高推理模式，适合复杂任务
model_reasoning_summary = "detailed"  # 详细总结（Ctrl+T 查看）
disable_response_storage = true  # 禁用本地存储
approval_policy = "never"  # 通过 /approvals 配置权限
sandbox_mode = "workspace-write"  # 读写权限
```
第三方提供商示例（添加多段）：
```
model_provider = "nonocode"  # 默认供应商

[model_providers.nonocode]
name = "nonocode"
base_url = "https://www.88code.org/openai/v1"
wire_api = "responses"
requires_openai_auth = true
```
MCP 服务器（Windows 示例，使用 npx）：
```
[mcp_servers.mcp-router]
command = "C:\\Program Files\\nodejs\\npx.cmd"
args = ["-y", "mcpr-cli@latest", "connect"]
env = { SystemRoot = "C:\\Windows", MCPR_TOKEN = "你的 MCPR Token" }
startup_timeout_ms = 30000  # 超时 30s
```
- 先安装 `npm install -g mcpr-cli@latest`，获取 Token。
- 导入 MCP JSON（如 sequential-thinking）到 MCP Router 界面。

**AGENTS.md（规则模板，让 Codex “乖宝宝”）：**
这是一个 Markdown 文件，定义角色、思维模式和 MCP 调用规范。核心是中文优先、深度思考、多方案对比。
示例片段（全局/项目级）：
```
# AGENTS.md - 全局配置

你是一个资深全栈技术专家和技术导师。遵守以下规则：
- 只使用中文回答，包括思考和代码注释。
- 思维模式：系统性分析、前瞻性思维、风险评估。
- 交互：授人以渔，提供多方案对比（优缺点、成本）。
- MCP 规则：单轮单工具，选择 Sequential Thinking（规划）、DuckDuckGo（搜索）、Context7（文档）、Serena（代码编辑）。调用后追加“工具调用简报”（服务、参数、结果）。
```
- 项目初始化：CLI 用 `/init` 生成，或插件提示 “初始化指导文档”。
- 技巧：高强度使用时，拉满 `model_verbosity = "high"` 显示思考过程；排除大文件夹（如 node_modules）加速搜索。

**Windows 特殊配置：** 添加 PowerShell 通知脚本 `notify.ps1`（弹窗提醒），路径用双斜杠。WSL2 访问 Windows 代码时，用 `pwsh.exe` 执行 npm 脚本。

#### 3. 基本使用
进入 CLI：`codex`（或 `codex -m gpt-5` 指定模型）。插件中用 Ctrl+Shift+P 打开聊天。

**常用命令（输入 `/` 查看）：**
- `/status`：检查模型、权限和配置。
- `/approvals`：设置权限（Read Only → Auto → Full Access）。推荐 Full Access + `--dangerously-bypass-approvals-and-sandbox` 绕过 sandbox。
- `/mcp`：管理 MCP 服务。
- `/spec` → `/plan` → `/do`：工作流（生成规范 → 计划 → 执行变更）。示例：`/spec 新增用户登录功能` 生成 Markdown 规范。
- 搜索：用 `@` + 关键字引用文件/图片；`fd`（文件名）、`rg`（文本）、`sg`（代码结构）。

**示例交互：**
- 输入： “用 React 写一个登录组件。”
- Codex 输出：分析需求、多方案（Hooks vs Class）、代码 + 中文注释 + 测试建议。
- 验证：Ctrl+T 查看推理轨迹。

**技巧：** 权限从只读开始测试；用 TODO 注释管理任务；CLI 中避免剪贴板粘贴文件，用关键字搜索。

#### 4. 高级技巧与 MCP 扩展
- **MCP 添加（推荐 Router 中转，避免超时）：** 导入 JSON 配置 5 大服务：
  - Sequential Thinking：复杂任务分解（步骤 ≤10）。
  - DuckDuckGo：Web 搜索（≤35 结果，关键词 ≤12）。
  - Context7：技术文档（tokens ≤5000）。
  - Serena：代码语义编辑（find_symbol → insert_before_symbol）。
  - Playwright：浏览器自动化（v0.0.41 兼容）。
- **高强度心得：** 用 High 模式全链路执行（如需求 → 代码 → 测试）；调教 AGENTS.md 让 Codex 提供思路而非盲干；Serena 特别适合大型项目追溯执行链。遇限流退避 20s，降级到本地答案。
- **调试：** 修改 AGENTS.md 后重启，检查日志；Windows 路径敏感，用完整路径。

更多细节可参考 Linux.do 论坛讨论，如公益 API 池（packycode）和 spec-kit 工作流。Codex 经济高效，但需迭代规则以优化协作。
