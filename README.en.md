# awesome-dsh-2026

面向国内开发者、按质量精选并持续维护的 DeepSeek Harness（DSH）2026 插件生态列表。<br>
A quality-focused, annually maintained collection of DeepSeek Harness (DSH) plugins for 2026, with Chinese-first descriptions.

> 📖 中文主版：[README.md](README.md) · English version: this page

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Last updated: 2026-08](https://img.shields.io/badge/last--updated-2026--08-brightgreen.svg)
![Plugins: 50](https://img.shields.io/badge/plugins-50-orange.svg)
![Contributors](https://img.shields.io/github/contributors/Herdeny/awesome-dsh-2026.svg)

## Contents

- [Curation criteria](#curation-criteria)
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
- [Official resources](#official-resources)
- [Contributing](#contributing)

<a id="curation-criteria"></a>

## Curation criteria

This list prioritizes projects that are actively maintained in 2026 (or explicitly long-term maintained), have basic install/config documentation, and fit a clear category. Malicious/phishing plugins, pure advertisements, and placeholder repos are excluded. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full rules and PR process.

<a id="development-tools"></a>

## 🔌 Development tools

- [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) - Official DeepSeek Harness repo, the "everything is a plugin" framework (⭐122294)
- [nexu-io/open-design](https://github.com/nexu-io/open-design) - Open-source design plugin for DSH, a Claude Design alternative (⭐87154)
- [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) - Two-phase DSH preset: minimal-aligned bootstrap then full-standard alignment (⭐2573)
- [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) - Next-generation AI workspace with a self-evolving agent runtime (⭐4115)
- [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) - Local-first AI token usage & cost tracker for 31 coding tools (⭐1327)

<a id="design-creative"></a>

## 🎨 Design & creative

- [nexu-io/open-design](https://github.com/nexu-io/open-design) - Open-source Claude Design alternative, provides DSH design capability (⭐87154)
- [Devin-AXIS/deepseek-design](https://github.com/Devin-AXIS/deepseek-design) - Editable design system: AI generation, visual editing, template marketplace and PPT (⭐38)
- [ZSeven-W/dsh-openpencil](https://github.com/ZSeven-W/dsh-openpencil) - OpenPencil preview, inspect and edit plugin (⭐92)

<a id="vision"></a>

## 👁️ Vision

- [liustack/modlens](https://github.com/liustack/modlens) - The first vision plugin for DSH, a vision bridge for text-only agents (⭐2114)
- [Anionex/dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit) - Intent-based image QA, long-screenshot OCR and UI restoration for text-only models (⭐474)
- [ysr666/dsh-vision-router](https://github.com/ysr666/dsh-vision-router) - Built-in free vision chain for text-only DSH agents (⭐259)
- [xiincs/claude-code-vision-skill](https://github.com/xiincs/claude-code-vision-skill) - Doubao/Qwen/GPT-4o vision for screenshot, UI and chart analysis (⭐165)
- [oil-oil/dsh-vision](https://github.com/oil-oil/dsh-vision) - Near-native image understanding for DeepSeek Harness (⭐47)

<a id="web-ui"></a>

## 🖥️ Web UI

- [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) - Plugin and skin collection for DSH Web UI (⭐3010)
- [Sanqi-normal/dsh-webui-market-plugin](https://github.com/Sanqi-normal/dsh-webui-market-plugin) - Browse the awesome-dsh-plugin.com directory and one-click install/uninstall (⭐60)
- [Francis-Xavier-code/dsh-balance-plugin](https://github.com/Francis-Xavier-code/dsh-balance-plugin) - Balance monitoring and usage statistics (⭐21)
- [william-jin-cmu/dsh-stickers](https://github.com/william-jin-cmu/dsh-stickers) - Bidirectional sticker reactions between user and agent (⭐18)
- [HsiangNianian/dsh-auto-continue](https://github.com/HsiangNianian/dsh-auto-continue) - Auto-sends "continue" to resume interrupted requests (⭐18)
- [buhuikongpan/dsh-pluginmanager](https://github.com/buhuikongpan/dsh-pluginmanager) - Layered plugin manager for DSH (⭐5)

<a id="themes-appearance"></a>

## 🎨 Themes & appearance

- [GGBond2424648901/deep-whale-day-night-theme](https://github.com/GGBond2424648901/deep-whale-day-night-theme) - Complete Deep Whale day/night theme UI pack with whale visuals (⭐56)
- [KinGao294/dsh-skin](https://github.com/KinGao294/dsh-skin) - Skin switcher + custom wallpaper (⭐15)

<a id="models-quota"></a>

## 💰 Models & quota

- [feibi-mochi/deepseek-harness-wallet](https://github.com/feibi-mochi/deepseek-harness-wallet) - Balance monitoring, per-session spend and token tracking (⭐17)
- [franksong2702/dsh-codex-connect](https://github.com/franksong2702/dsh-codex-connect) - ChatGPT OAuth and Codex models for DSH (⭐11)

<a id="testing-qa"></a>

## 🧪 Testing & QA

- [Herdeny/dsh-qc](https://github.com/Herdeny/dsh-qc) - DSH plugin quality checker CLI with static analysis and dynamic validation (⭐1)
- [omdsh-dev/dsh-plugin-skills](https://github.com/omdsh-dev/dsh-plugin-skills) - Agent skills for building and testing DSH plugins (⭐9)
- [suimi8/dsh-test-runner](https://github.com/suimi8/dsh-test-runner) - Structured test runner providing the `test_run` tool (⭐2)
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - The living DSH plugin directory, refreshed hourly (⭐35)

<a id="examples-templates"></a>

## 📦 Examples & templates

- [bugmaker2/dsh-plugin-template](https://github.com/bugmaker2/dsh-plugin-template) - Template for DeepSeek Harness plugin development (⭐22)
- [sunshine-lang/dsh-plugin-template](https://github.com/sunshine-lang/dsh-plugin-template) - Ready-to-publish skeleton: bundle format and tool registration (⭐3)
- [omdsh-dev/plugin-template](https://github.com/omdsh-dev/plugin-template) - Template built from the Turtle UI official repo (⭐6)
- [OneZero-Y/dsh-plugin-kit](https://github.com/OneZero-Y/dsh-plugin-kit) - Agent skills and a working template for plugin development (⭐3)

<a id="sessions-messages"></a>

## 💬 Sessions & messages

- [Anionex/dsh-turn-rewind](https://github.com/Anionex/dsh-turn-rewind) - Rewind conversation and code state, replay historical turns (⭐61)
- [hellodigua/dsh-emoji](https://github.com/hellodigua/dsh-emoji) - Custom emoji for AI replies: Bilibili, Xiaohongshu, Tieba and more (⭐19)

<a id="just-for-fun"></a>

## 🎮 Just for fun

- [lhh010/dsh-minigames](https://github.com/lhh010/dsh-minigames) - 18 offline minigames in the Web UI side panel (⭐18)
- [crafter-station/petdex](https://github.com/crafter-station/petdex) - A public gallery of animated pets for Codex, Claude Code, DSH and more (⭐3842)

<a id="mcp-integrations"></a>

## 🧩 MCP & integrations

- [sandbaseai/sandbase-harness](https://github.com/sandbaseai/sandbase-harness) - Open-source CMA-compatible agent runtime with MCP tools (⭐596)
- [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent) - Open-source super AI assistant & Agent Harness (⭐46523)
- [Haohao-end/openagent](https://github.com/Haohao-end/openagent) - OpenAI Deep Research + Dify combined into one platform (⭐788)

<a id="memory-context"></a>

## 🧠 Memory & context

- [csyangwen/dsh-memory-evolve](https://github.com/csyangwen/dsh-memory-evolve) - Cross-session long-term memory + background self-evolution, five-track memory with git versioning (⭐103)
- [omdsh-dev/dsh-mnemon](https://github.com/omdsh-dev/dsh-mnemon) - Cross-agent, local-first persistent memory plugin (⭐42)
- [Aik358/dsh-auto-memory](https://github.com/Aik358/dsh-auto-memory) - Three-layer auto memory (user/project/daily) with auto-inject and retrieval (⭐16)
- [modusensus/dsh-mneme](https://github.com/modusensus/dsh-mneme) - Persistent, self-consolidating memory plugin (⭐16)

<a id="security-audit"></a>

## 🔒 Security & audit

- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - DSH plugin security and dependency monitoring (⭐4)
- [jkrandom-sudo/dsh-plugin-audit](https://github.com/jkrandom-sudo/dsh-plugin-audit) - Static permission audit for DSH plugins (⭐4)
- [nanshan1995/DSH-Plugin-Market](https://github.com/nanshan1995/DSH-Plugin-Market) - Plugin market with pre-install static security audit gate (⭐4)

<a id="desktop-clients"></a>

## 💻 Desktop & clients

- [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) - Modern desktop solution for the DSH plugin ecosystem (⭐7423)
- [omdsh-dev/dsh-genui](https://github.com/omdsh-dev/dsh-genui) - GenUI: interactive UI component rendering (⭐120)

<a id="platforms-channels"></a>

## 🌐 Platforms & channels

- [Sanqi-normal/dsh-webui-market-plugin](https://github.com/Sanqi-normal/dsh-webui-market-plugin) - Plugin market entry for DSH Web UI (⭐60)
- [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) - Local, private, self-evolving cross-platform AI content discovery agent (⭐2659)
- [walkinglabs/awesome-deepseek-harness-plugins](https://github.com/walkinglabs/awesome-deepseek-harness-plugins) - Bilingual list of verified DeepSeek Harness plugins (⭐5)

<a id="official-resources"></a>

## Official resources

- [DeepSeek Harness repo](https://github.com/deepseek-ai/deepseek-harness) - Source code, releases and project documentation
- [DeepSeek Harness docs](https://github.com/deepseek-ai/deepseek-harness/tree/master/docs) - Development and architecture docs in the official repo

<a id="contributing"></a>

## Contributing

Contributions are welcome — recommend a new plugin, update star counts, or fix broken links via Pull Request. Read [CONTRIBUTING.md](CONTRIBUTING.md) first and confirm the project meets the curation criteria.

## License

This project is licensed under the [MIT License](LICENSE).
