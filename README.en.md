# awesome-dsh-2026

面向国内开发者、按质量精选并持续维护的 DeepSeek Harness（DSH）2026 插件生态列表。<br>
A quality-focused, annually maintained collection of DeepSeek Harness (DSH) plugins for 2026, with Chinese-first descriptions.

> 📖 中文主版：[README.md](README.md) · English version: this page

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Last updated: 2026-08](https://img.shields.io/badge/last--updated-2026--08-brightgreen.svg)
![Plugins: 55](https://img.shields.io/badge/plugins-113-orange.svg)
![Contributors](https://img.shields.io/github/contributors/Herdeny/awesome-dsh-plugins-2026.svg)

## 目录 / Contents

- [🔌 Development tools](#development-tools)
- [🎨 Design & creative](#design-creative)
- [👁️ Vision](#vision)
- [🖥️ Web UI](#web-ui)
- [🎨 Themes & appearance](#themes-appearance)
- [💰 Models & quota](#models-quota)
- [🧪 Testing & QA](#testing-qa)
- [📦 Examples & templates](#examples-templates)
- [💬 Sessions & messages](#sessions-messages)
- [🎮 Just for fun](#just-for-fun)
- [🧩 MCP & integrations](#mcp-integrations)
- [🧠 Memory & context](#memory-context)
- [🔒 Security & audit](#security-audit)
- [💻 Desktop & clients](#desktop-clients)
- [🌐 Platforms & channels](#platforms-channels)
- [🌱 Ecosystem](#ecosystem)
- [Official resources](#official-resources)
- [Contributing](#contributing)

## 质量评分分布（dsh-qc 检测） / Quality score distribution (dsh-qc)

评分来自 [dsh-qc](https://github.com/Herdeny/dsh-qc) 静态+动态质检，100 分制。🟢 良好 / 🟡 及格 / 🟠 一般 / 🔴 待改进。<br>
Scores from [dsh-qc](https://github.com/Herdeny/dsh-qc), 100-point static+dynamic QC.

- 🟢 70-100: 5
- 🟡 50-69: 37
- 🟠 30-49: 17
- 🔴 0-29: 24

<a id="development-tools"></a>

## 🔌 Development tools

- [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) - Official DeepSeek Harness repo, the "everything is a plugin" framework (⭐180722)
- [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) - Two-phase DSH preset: minimal-aligned bootstrap then full-standard alignment (⭐3550) 🛡️QC:31 🟠
- [edison7009/EchoBird](https://github.com/edison7009/EchoBird) - One-click install + model switch across 15+ coding agents: Claude Code, Codex, Grok, DSH, Kimi, Qwen, Aider and more (⭐3087) 🛡️QC:21 🔴
- [foryourhealth111-pixel/Vibe-Skills](https://github.com/foryourhealth111-pixel/Vibe-Skills) - General-purpose Skill router that auto-routes local Skills and orchestrates harness workflows, DSH included (⭐2910) 🛡️QC:0 🔴
- [tong-io/tongflow](https://github.com/tong-io/tongflow) - Multimodal workflow studio & engine (canvas + Python plugin engine) with the dsh-tongflow studio plugin (⭐872) 🛡️QC:30 🟠
- [SheberDavid/v4-flash-godmode-opencode-go](https://github.com/SheberDavid/v4-flash-godmode-opencode-go) - DSH agent preset that flips opencode-go's DeepSeek V4 Flash from ghost mode to god mode (⭐499) 🛡️QC:25 🔴
- [liceses/dsh-gitbash-preset](https://github.com/liceses/dsh-gitbash-preset) - One-click Git Bash (minimal mode) agent preset: maps DSH minimal mode's bash calls into a Git Bash environment (⭐135)
- [christopherarter/superpowers-reasonix](https://github.com/christopherarter/superpowers-reasonix) - Superpowers skill port to the Reasonix coding harness (DeepSeek-native terminal agent, DSH-ecosystem ready) (⭐94)
- [omdsh-dev/dsh_workflow](https://github.com/omdsh-dev/dsh_workflow) - Brings Claude Code's UltraCode mode to DSH: upgrades one-shot multi-agent dispatch into a generatable, savable, governable, observable, recoverable workflow layer (⭐93)

<a id="design-creative"></a>

## 🎨 Design & creative

- [shanliuling/dsh-image-gen](https://github.com/shanliuling/dsh-image-gen) - Generate images directly in DeepSeek Harness chats (⭐124)
- [worldwonderer/oh-story-dsh](https://github.com/worldwonderer/oh-story-dsh) - Novel writing and short-drama production for DSH, powered by Oh Story and Drama Skills (⭐104)
- [devin-axis/deepseek-design](https://github.com/devin-axis/deepseek-design) - Editable design system: AI generation, visual editing, template marketplace and PPT (⭐69) 🛡️QC:17 🔴
- [zseven-w/dsh-openpencil](https://github.com/zseven-w/dsh-openpencil) - OpenPencil preview, inspect and edit plugin (⭐102) 🛡️QC:64 🟡

<a id="vision"></a>

## 👁️ Vision

- [liustack/modlens](https://github.com/liustack/modlens) - The first vision plugin for DSH, a vision bridge for text-only agents (⭐3496) 🛡️QC:43 🟠
- [anionex/dsh-vision-toolkit](https://github.com/anionex/dsh-vision-toolkit) - Intent-based image QA, long-screenshot OCR and UI restoration for text-only models (⭐806) 🛡️QC:65 🟡
- [ysr666/dsh-vision-router](https://github.com/ysr666/dsh-vision-router) - Built-in free vision chain for text-only DSH agents (⭐842) 🛡️QC:52 🟡
- [xiincs/claude-code-vision-skill](https://github.com/xiincs/claude-code-vision-skill) - Doubao/Qwen/GPT-4o vision for screenshot, UI and chart analysis (⭐165) 🛡️QC:17 🔴
- [oil-oil/dsh-vision](https://github.com/oil-oil/dsh-vision) - Near-native image understanding for DeepSeek Harness (⭐83) 🛡️QC:69 🟡
- [Yts1919/dsh-vision-complete](https://github.com/Yts1919/dsh-vision-complete) - Multimodal plugin: image, OCR, object detection, video understanding, speech-to-text and screenshots (⭐33) 🛡️QC:25 🔴
- [william-jin-cmu/dsh-vision](https://github.com/william-jin-cmu/dsh-vision) - view_image tool bridging any OpenAI-compatible VLM (free Zhipu tier by default; 4 vendors, 10 models tested) (⭐32) 🛡️QC:47 🟠
- [jing-hy/picturereader](https://github.com/jing-hy/picturereader) - Pixel-to-text image reading for text-only models: image_scan/image_ocr/image_sample tools + image-reading skill, fully local (⭐21) 🛡️QC:44 🟠
- [tianmingwan/dsh-vision-any](https://github.com/tianmingwan/dsh-vision-any) - Paste images into text-only DSH agents; any OpenAI-compatible, Anthropic or Gemini vision API (⭐19) 🛡️QC:61 🟡
- [hisence999/DSH-vision](https://github.com/hisence999/DSH-vision) - Text-only models can send images directly: auto-converted to text descriptions; multimodal models pass through untouched; read_image tool works (⭐16) 🛡️QC:38 🟠

<a id="web-ui"></a>

## 🖥️ Web UI

- [omdsh-dev/DSH-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) - Open sidebar foundation with third-party page registration; built-in file render/edit, terminal, Git and sub-agent pages (⭐2328) 🛡️QC:51 🟡
- [ccch1mneyyy/dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) - Claude Code-style TUI companion plugin featured by DSH official: whale bar, live status, streaming thoughts, double-Esc rollback; one-click npm install (⭐1964) 🛡️QC:33 🟠
- [ccch1mneyyy/working-activity](https://github.com/ccch1mneyyy/working-activity) - Lively working-line (statusline) extension for pi CLI and DSH (⭐653) 🛡️QC:28 🔴
- [huiliyi37/dsh-tianshu-tui](https://github.com/huiliyi37/dsh-tianshu-tui) - Official interactive terminal UI plugin for DeepSeek Harness: custom minimal ANSI renderer, streaming Markdown and live status (⭐224)
- [liangmianya/dsh-synapse](https://github.com/liangmianya/dsh-synapse) - Visual non-linear conversation workspace for DSH: canvas-based session explorer and branching workspace (⭐144)
- [sanqi-normal/dsh-webui-market-plugin](https://github.com/sanqi-normal/dsh-webui-market-plugin) - Plugin market entry for DSH Web UI (⭐66) 🛡️QC:61 🟡
- [francis-xavier-code/dsh-balance-plugin](https://github.com/francis-xavier-code/dsh-balance-plugin) - Balance monitoring and usage statistics (⭐27) 🛡️QC:61 🟡
- [hsiangnianian/dsh-auto-continue](https://github.com/hsiangnianian/dsh-auto-continue) - Auto-sends "continue" to resume interrupted requests (⭐22) 🛡️QC:72 🟢
- [william-jin-cmu/dsh-stickers](https://github.com/william-jin-cmu/dsh-stickers) - Bidirectional sticker reactions between user and agent (⭐19) 🛡️QC:66 🟡
- [buhuikongpan/dsh-pluginmanager](https://github.com/buhuikongpan/dsh-pluginmanager) - Layered plugin manager for DSH (⭐9) 🛡️QC:61 🟡
- [lhh010/dsh-paste-input](https://github.com/lhh010/dsh-paste-input) - WebUI file input boost: Ctrl+V paste, drag-drop and file picker; files copied into the session workspace on send (⭐8) 🛡️QC:39 🟠

<a id="themes-appearance"></a>

## 🎨 Themes & appearance

- [Small-tailqwq/dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) - Whale Girl skin series for DeepSeek Harness (⭐1456) 🛡️QC:25 🔴
- [WYH66666666/DSH-Transparent-UI-Plugin](https://github.com/WYH66666666/DSH-Transparent-UI-Plugin) - Glassmorphism theme with freely adjustable blur, frost and background — no DSH source changes (⭐171) 🛡️QC:53 🟡
- [elysia395/dsh-wallpaper-engine](https://github.com/elysia395/dsh-wallpaper-engine) - Turn local Wallpaper Engine wallpapers into DSH web-UI backgrounds: live video, iframe-loaded web wallpapers, Scene static frames (⭐137)
- [d-dev0101/open-sea-skin](https://github.com/d-dev0101/open-sea-skin) - WebGPU ocean skin for DeepSeek Harness: Harness-only Chrome/Edge extension, static installer and native integration (⭐119) 🛡️QC:58 🟡
- [ggbond2424648901/deep-whale-day-night-theme](https://github.com/ggbond2424648901/deep-whale-day-night-theme) - Complete Deep Whale day/night theme UI pack with whale visuals (⭐68) 🛡️QC:66 🟡
- [RevolutionLA/dsh-dream-skin](https://github.com/RevolutionLA/dsh-dream-skin) - Skin/wallpaper/theme-pack plugin: 8 Mirage themes, per-user accent colors, theme pack import/export and favorites (⭐34) 🛡️QC:67 🟡
- [oil-oil/dsh-theme](https://github.com/oil-oil/dsh-theme) - Live theme editor with curated palettes and typography controls (⭐25) 🛡️QC:66 🟡
- [147228/dsh-xiaoyao-skins](https://github.com/147228/dsh-xiaoyao-skins) - Xiaoyao × DSH Web skin collection, installer and community creation toolchain (⭐24) 🛡️QC:33 🟠
- [kingao294/dsh-skin](https://github.com/kingao294/dsh-skin) - Skin switcher + custom wallpaper (⭐17) 🛡️QC:64 🟡
- [nevertoday/dsh-theme-plugin](https://github.com/nevertoday/dsh-theme-plugin) - Chinese traditional colors as a DeepSeek Harness theme pack (⭐17) 🛡️QC:72 🟢
- [LAN-TINA-WS/dsh-gui-customization](https://github.com/LAN-TINA-WS/dsh-gui-customization) - GUI workshop: theme colors, custom/video backgrounds, adjustable ambient light; bilingual (⭐14) 🛡️QC:33 🟠
- [suzike/freestyle-dsh-theme](https://github.com/suzike/freestyle-dsh-theme) - OKLCH theme proposal + theme designer, persisted across restarts (⭐12) 🛡️QC:59 🟡
- [Tommy00748/dsh-theme-cyberpunk2077](https://github.com/Tommy00748/dsh-theme-cyberpunk2077) - Cyberpunk 2077 / Night City theme for the DSH Web UI: CRT scanlines, Kiroshi lock-on, typewriter effects (⭐12) 🛡️QC:61 🟡
- [LaplaceYoung/dsh-qq2006](https://github.com/LaplaceYoung/dsh-qq2006) - Retro QQ2006 skin: registers qq2006 theme, mirrors body[data-ds-skin], full assets and global skin table (⭐12) 🛡️QC:67 🟡
- [yunxiiQwQ/dsh-maid-whale-webUI](https://github.com/yunxiiQwQ/dsh-maid-whale-webUI) - Whale maid theme for the DSH Web UI (⭐11) 🛡️QC:25 🔴

<a id="models-quota"></a>

## 💰 Models & quota

- [MeteorNOX/DeepSeek-Balance-Whale-Widget](https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget) - A whale-girl widget in the DSH corner that watches your DeepSeek balance: draggable, snap-able, animated counter (⭐210)
- [V1ki/dsh-plugin-subscriptions](https://github.com/V1ki/dsh-plugin-subscriptions) - Use ChatGPT (Codex), Claude and Grok (X Premium) subscriptions as DSH LLM providers — OAuth in the web UI, no API keys (⭐203)
- [Han-1413141/dsh-cost-meter](https://github.com/Han-1413141/dsh-cost-meter) - Session cost meter: session/daily cost, budget and history (⭐133)
- [yjh051108/dsh-router-standard](https://github.com/yjh051108/dsh-router-standard) - Task-aware reasoning-mode router: three measured behavior bands (spec/mixed/react) with phase-transition evidence; dual-attractor policy paper included (⭐347) 🛡️QC:23 🔴
- [feibi-mochi/deepseek-harness-wallet](https://github.com/feibi-mochi/deepseek-harness-wallet) - Balance monitoring, per-session spend and token tracking (⭐21) 🛡️QC:58 🟡
- [franksong2702/dsh-codex-connect](https://github.com/franksong2702/dsh-codex-connect) - ChatGPT OAuth and Codex models for DSH (⭐16) 🛡️QC:68 🟡
- [LiangYin233/dsh-provider-model-configurator](https://github.com/LiangYin233/dsh-provider-model-configurator) - One-click apply pi-ai presets or any provider's model context, output cap, reasoning tier and compat toggles; central model entry management (⭐11) 🛡️QC:69 🟡

<a id="testing-qa"></a>

## 🧪 Testing & QA

- [herdeny/dsh-qc](https://github.com/herdeny/dsh-qc) - DSH plugin quality checker CLI with static analysis and dynamic validation (⭐2)
- [vostride/agent-qa](https://github.com/vostride/agent-qa) - Open-source self-improving QA agent: natural-language tests for web & mobile with automatic regression catching; DSH support (⭐952) 🛡️QC:16 🔴
- [omdsh-dev/dsh-plugin-skills](https://github.com/omdsh-dev/dsh-plugin-skills) - Agent skills for building and testing DSH plugins (⭐9) 🛡️QC:17 🔴
- [suimi8/dsh-test-runner](https://github.com/suimi8/dsh-test-runner) - Structured test runner providing the `test_run` tool (⭐2) 🛡️QC:53 🟡
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - The living DSH plugin directory, refreshed hourly (⭐35) 🛡️QC:23 🔴

<a id="examples-templates"></a>

## 📦 Examples & templates

- [bugmaker2/dsh-plugin-template](https://github.com/bugmaker2/dsh-plugin-template) - Template for DeepSeek Harness plugin development (⭐22) 🛡️QC:66 🟡
- [sunshine-lang/dsh-plugin-template](https://github.com/sunshine-lang/dsh-plugin-template) - Ready-to-publish skeleton: bundle format and tool registration (⭐3) 🛡️QC:58 🟡
- [omdsh-dev/plugin-template](https://github.com/omdsh-dev/plugin-template) - Template built from the Turtle UI official repo (⭐8) 🛡️QC:64 🟡
- [onezero-y/dsh-plugin-kit](https://github.com/onezero-y/dsh-plugin-kit) - Agent skills and a working template for plugin development (⭐3) 🛡️QC:25 🔴

<a id="sessions-messages"></a>

## 💬 Sessions & messages

- [anionex/dsh-turn-rewind](https://github.com/anionex/dsh-turn-rewind) - Rewind conversation and code state, replay historical turns (⭐61) 🛡️QC:74 🟢
- [hellodigua/dsh-emoji](https://github.com/hellodigua/dsh-emoji) - Custom emoji for AI replies: Bilibili, Xiaohongshu, Tieba and more (⭐23) 🛡️QC:77 🟢

<a id="just-for-fun"></a>

## 🎮 Just for fun

- [yejiming/MuseAI](https://github.com/yejiming/MuseAI) - Create AI characters and step into story worlds — chat, adventure, transmigrate; supports DeepSeek Harness plugins (⭐590) 🛡️QC:38 🟠
- [hewzhew/dsh-agent-rp](https://github.com/hewzhew/dsh-agent-rp) - SillyTavern migration and next-generation Agent roleplay for DSH (⭐166)
- [cocofhu/anime-find](https://github.com/cocofhu/anime-find) - Anime search inside DSH: multi-source lookup with Bangumi ratings and details, magnet-link copy (⭐155)
- [lhh010/dsh-minigames](https://github.com/lhh010/dsh-minigames) - 18 offline minigames in the Web UI side panel (⭐20) 🛡️QC:63 🟡

<a id="mcp-integrations"></a>

## 🧩 MCP & integrations

- [agentrq/agentrq](https://github.com/agentrq/agentrq) - Human-in-the-loop realtime conversational task manager: self-hosted, control your agents from mobile, web or desktop (ACP/MCP) (⭐1081) 🛡️QC:17 🔴
- [NanmiCoder/dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) - AgentTeams plugin for DeepSeek Harness: build and manage multi-agent teams (⭐608) 🛡️QC:64 🟡
- [Lum1104/dsh-browser](https://github.com/Lum1104/dsh-browser) - Chrome sidebar extension that lets DSH operate your browser directly, no vision capabilities required (⭐216) 🛡️QC:28 🔴
- [liustack/modsearch](https://github.com/liustack/modsearch) - The web search plugin for DeepSeek Harness, and the search bridge for every mode (⭐191)
- [Utopia-V/mixagents](https://github.com/Utopia-V/mixagents) - Harness-native agent components for Codex and Pi: a DeepSeek V4 Flash subagent and a DSH Minimal mimic for V4 Pro (⭐177)
- [ZSeven-W/dsh-ios](https://github.com/ZSeven-W/dsh-ios) - Live iOS Simulator and USB-connected iPhone inside DSH conversations: 22 agent tools for booting, building and driving the UI by accessibility identity, OCR text or coordinates (⭐169)
- [anysearch-team/anysearch-dsh](https://github.com/anysearch-team/anysearch-dsh) - AnySearch web search provider and advanced search tools for DeepSeek Harness (⭐180)
- [weijiafu14/pi2dsh](https://github.com/weijiafu14/pi2dsh) - Bridge the Pi and DeepSeek Harness ecosystems: one Pi Host ABI runs unmodified Pi extensions as native DSH plugins (⭐153)
- [toolclub/dsh-agent-team-gui](https://github.com/toolclub/dsh-agent-team-gui) - Persistent multi-model workflow teams for DSH: dynamic lead planning, bounded DAGs, per-agent models/tools, Run Center and token insights (⭐115)
- [omdsh-dev/dsh-data-agent](https://github.com/omdsh-dev/dsh-data-agent) - Connect DSH to your database for conversational data analysis and actionable business insights (⭐105)
- [Tabbit-Browser/dsh-tabbit](https://github.com/Tabbit-Browser/dsh-tabbit) - Tabbit Browser plugins for DeepSeek Harness: browser automation through Tabbit (⭐92)
- [ZSeven-W/dsh-crew](https://github.com/ZSeven-W/dsh-crew) - Dispatch work to DSH agents from Claude Code / Codex with native subagent progress (⭐93) 🛡️QC:54 🟡

<a id="memory-context"></a>

## 🧠 Memory & context

- [adoresever/graph-memory](https://github.com/adoresever/graph-memory) - Knowledge-graph memory: extracts structured triples from conversations, compresses context 75%, reuses experience across sessions (⭐530) 🛡️QC:33 🟠
- [bowenliang123/dsh-context](https://github.com/bowenliang123/dsh-context) - All-in-one context insight & management: dashboard, browser and commands to see composition, evolution, compression and pruning (⭐482) 🛡️QC:59 🟡
- [mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon) - LLM-supervised persistent memory: graph recall + cross-session knowledge in a single binary; works with DSH and any agent runtime (⭐465) 🛡️QC:38 🟠
- [syncable-dev/memtrace-public](https://github.com/syncable-dev/memtrace-public) - Structural codebase memory: bi-temporal knowledge graph, MCP-native, zero LLM calls, millisecond queries (⭐454) 🛡️QC:25 🔴
- [csyangwen/dsh-memory-evolve](https://github.com/csyangwen/dsh-memory-evolve) - Cross-session long-term memory + background self-evolution, five-track memory with git versioning (⭐131) 🛡️QC:31 🟠
- [ZSeven-W/dsh-noema](https://github.com/ZSeven-W/dsh-noema) - Noema long-term memory: durable, inspectable agent memory with recall tools and a settings page (⭐90) 🛡️QC:64 🟡
- [omdsh-dev/dsh-mnemon](https://github.com/omdsh-dev/dsh-mnemon) - Cross-agent, local-first persistent memory plugin (⭐162) 🛡️QC:59 🟡
- [PerryLink/dsh-memento](https://github.com/PerryLink/dsh-memento) - Bounded, layered, approval-gated, auditable cross-session memory (⭐57) 🛡️QC:70 🟢
- [modusensus/dsh-mneme](https://github.com/modusensus/dsh-mneme) - Persistent, self-consolidating memory plugin (⭐19) 🛡️QC:17 🔴
- [aik358/dsh-auto-memory](https://github.com/aik358/dsh-auto-memory) - Three-layer auto memory (user/project/daily) with auto-inject and retrieval (⭐11) 🛡️QC:61 🟡

<a id="security-audit"></a>

## 🔒 Security & audit

- [lire1131/dsh-undo-savepoint](https://github.com/lire1131/dsh-undo-savepoint) - DSH crash-rescue plugin: undo config and plugin-code changes, secret-safe snapshots, one-click SAFE MODE, plus offline CLI/GUI for when DSH won't boot (⭐111)
- [micromilo/upstream-radar](https://github.com/micromilo/upstream-radar) - DSH plugin security and dependency monitoring (⭐4) 🛡️QC:41 🟠
- [jkrandom-sudo/dsh-plugin-audit](https://github.com/jkrandom-sudo/dsh-plugin-audit) - Static permission audit for DSH plugins (⭐4) 🛡️QC:51 🟡
- [nanshan1995/dsh-plugin-market](https://github.com/nanshan1995/dsh-plugin-market) - Plugin market with pre-install static security audit gate (⭐4) 🛡️QC:55 🟡

<a id="desktop-clients"></a>

## 💻 Desktop & clients

- [zouyuxuan122/Deepseek-Harness-EAC](https://github.com/zouyuxuan122/Deepseek-Harness-EAC) - DSH Windows/Linux desktop client: bundled Node.js + dsh CLI, one-click launch, 10 built-in UI skins (⭐952) 🛡️QC:0 🔴
- [hairyf/deepseek-harness-desktop](https://github.com/hairyf/deepseek-harness-desktop) - DeepSeek Harness Tauri desktop: 5MB installer, zero environment setup, preset plugins; Windows / macOS / Linux (⭐600) 🛡️QC:38 🟠
- [vibeinging/deepseek-harness-desktop-app](https://github.com/vibeinging/deepseek-harness-desktop-app) - Local AI desktop workspace for DSH sessions, projects, files, web research, plugins and Office artifacts (⭐491) 🛡️QC:18 🔴
- [op7418/pilot-harness](https://github.com/op7418/pilot-harness) - CodePilot-inspired desktop client and plugin suite for DeepSeek Harness on macOS, Windows and Linux (⭐240)
- [lencx/Minke](https://github.com/lencx/Minke) - DeepSeek Harness desktop client (⭐229) 🛡️QC:28 🔴
- [omdsh-dev/dsh-genui](https://github.com/omdsh-dev/dsh-genui) - GenUI: interactive UI component rendering (⭐223) 🛡️QC:52 🟡
- [QCYTSN/dsh-dafeiyu](https://github.com/QCYTSN/dsh-dafeiyu) - Desktop-native BigFish companion for DeepSeek Harness: real Agent status, always on top on Windows (⭐201)
- [whitelonng/dshcode](https://github.com/whitelonng/dshcode) - Community desktop companion for DeepSeek Harness: one-click Electron app for macOS and Windows (⭐146)
- [ChisaAlter/Deepseek-Harness-Desktop](https://github.com/ChisaAlter/Deepseek-Harness-Desktop) - DSH desktop shell with theme and background customization (Electron) (⭐132)
- [ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop) - Windows desktop client: zero-setup installer with Codex, plugins, skills, SSH remote access and 11 skins (⭐66) 🛡️QC:11 🔴
- [qiannianhuanxiang/DSHA](https://github.com/qiannianhuanxiang/DSHA) - Android launcher with built-in proot+Ubuntu: run DeepSeek Harness without ROOT or Termux (⭐65) 🛡️QC:25 🔴
- [WEP-56/DSH-Launcher](https://github.com/WEP-56/DSH-Launcher) - Launcher with embedded webui: package, config and plugin management, compatible with all webui plugins (⭐17) 🛡️QC:33 🟠

<a id="platforms-channels"></a>

## 🌐 Platforms & channels

- [dsh-market/dsh-market](https://github.com/dsh-market/dsh-market) - Visual plugin market inside DeepSeek Harness: browse, search, one-click install (⭐1237) 🛡️QC:64 🟡
- [Nagi-ovo/dsh-find-plugins](https://github.com/Nagi-ovo/dsh-find-plugins) - A DSH skill that finds, installs and verifies GitHub plugins (⭐160)
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - DSH plugin marketplace: browse, install and update GitHub plugins from the Web GUI (⭐129)
- [walkinglabs/awesome-deepseek-harness-plugins](https://github.com/walkinglabs/awesome-deepseek-harness-plugins) - Bilingual list of verified DeepSeek Harness plugins (⭐7) 🛡️QC:25 🔴

<a id="ecosystem"></a>

## 🌱 Ecosystem

DSH-ecosystem projects that are not standard plugins (no cordis manifest); a 0 QC score is expected.

- [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) - Modern desktop solution for the DSH plugin ecosystem (⭐17506)
- [crafter-station/petdex](https://github.com/crafter-station/petdex) - A public gallery of animated pets for Codex, Claude Code, DSH and more (⭐3842)
- [devin-axis/ipollowork](https://github.com/devin-axis/ipollowork) - Next-generation AI workspace with a self-evolving agent runtime (⭐4115)
- [haohao-end/openagent](https://github.com/haohao-end/openagent) - OpenAI Deep Research + Dify combined into one platform (⭐788)
- [nexu-io/open-design](https://github.com/nexu-io/open-design) - Open-source Claude Design alternative, provides DSH design capability (⭐87154)
- [sandbaseai/sandbase-harness](https://github.com/sandbaseai/sandbase-harness) - Open-source CMA-compatible agent runtime with MCP tools (⭐596)
- [whiteguo233/openbiliclaw](https://github.com/whiteguo233/openbiliclaw) - Local, private, self-evolving cross-platform AI content discovery agent (⭐2932)
- [xiufengsun/tokentracker](https://github.com/xiufengsun/tokentracker) - Local-first AI token usage & cost tracker for 31 coding tools (⭐1327)
- [zhayujie/cowagent](https://github.com/zhayujie/cowagent) - Open-source super AI assistant & Agent Harness (⭐46523)
- [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) - Plugin and skin collection for DSH Web UI (⭐5147)
- [text2future/flowix](https://github.com/text2future/flowix) - Local-first Markdown notebook: notes become agent memory, with the dsh-flowix-memory DSH plugin (MCP & CLI) (⭐314)
- [firstintent/ccteam](https://github.com/firstintent/ccteam) - Multi-agent orchestration: turns Claude Code / Codex / Grok / Kimi / DeepSeek Harness into one team; spawn, dispatch and collect work from any session (⭐289)
- [MemTensor/MemOS](https://github.com/MemTensor/MemOS) - Self-evolving memory OS: ultra-persistent memory, hybrid retrieval and cross-task skill reuse; 35.24% token savings; local & cloud DSH plugins (⭐10763)
- [Nagi-ovo/voyager](https://github.com/Nagi-ovo/voyager) - Enhancement suite for Gemini, AI Studio, Claude & ChatGPT, plus a prompt manager for any web UI — DeepSeek Harness included (⭐19647)
- [PM-Shawn/Abu-Cowork](https://github.com/PM-Shawn/Abu-Cowork) - Open-source Claude Cowork alternative: local-first AI agent desktop app, multi-model, self-evolving skills, with DeepSeek Harness integration (⭐334)
- [Hmbown/CodeWhale](https://github.com/Hmbown/CodeWhale) - Open-source, community-driven agent harness with native DeepSeek Harness (DSH) support (⭐40828)
- [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) - DeepSeek-native AI coding agent for your terminal, engineered around prefix-cache stability; DSH-ready (⭐34868)
- [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) - Harness engineering beginner tutorial, from 0 to 1 (⭐12563)
- [paean-ai/deeptide](https://github.com/paean-ai/deeptide) - Swift-native macOS coding agent built for DeepSeek — with DSH plugin support (⭐1085)
- [Electricitysheep/dsh-handbook](https://github.com/Electricitysheep/dsh-handbook) - In-depth DeepSeek Harness handbook: install, plugin dev, perf tuning and measured case studies (EN + CN) (⭐534)
- [hikariming/dshfind](https://github.com/hikariming/dshfind) - Learn DSH principles, plugin marketplace and best practices (⭐190)
- [zhaoolee/notes](https://github.com/zhaoolee/notes) - Open-source Hammer-note clone: one-click Docker self-hosting, skill invocation and dsh plugin support (⭐148)

<a id="official-resources"></a>

## Official resources

- [DeepSeek Harness repo](https://github.com/deepseek-ai/deepseek-harness) - Source code, releases and project documentation
- [DeepSeek Harness docs](https://github.com/deepseek-ai/deepseek-harness/tree/master/docs) - Development and architecture docs

<a id="contributing"></a>

## Contributing

Contributions are welcome — recommend a new plugin, update star counts, or fix broken links via Pull Request. Read [CONTRIBUTING.md](CONTRIBUTING.md) first.

## License

This project is licensed under the [MIT License](LICENSE).
