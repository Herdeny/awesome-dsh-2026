# awesome-dsh-2026

面向国内开发者、按质量精选并持续维护的 DeepSeek Harness（DSH）2026 插件生态列表。<br>
A quality-focused, annually maintained collection of DeepSeek Harness (DSH) plugins for 2026, with Chinese-first descriptions.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Last updated: 2026-08](https://img.shields.io/badge/last--updated-2026--08-brightgreen.svg)
![Contributors](https://img.shields.io/github/contributors/Herdeny/awesome-dsh-2026.svg)

> 本列表中的星标数来自 2026-08-16 的 GitHub 调研快照，仅用于反映收录时的社区关注度。

## 目录 / Contents

- [收录原则 / Curation criteria](#curation-criteria)
- [🔌 开发框架与工具 / Development tools](#development-tools)
- [🎨 设计与创意 / Design & creative](#design-creative)
- [👁️ 视觉与多模态 / Vision](#vision)
- [🖥️ Web UI 与界面 / Web UI](#web-ui)
- [🎨 主题与外观 / Themes & appearance](#themes-appearance)
- [💰 模型与额度 / Models & quota](#models-quota)
- [🧪 测试与质检 / Testing & QA](#testing-qa)
- [📦 示例与模板 / Examples & templates](#examples-templates)
- [💬 会话与消息 / Sessions & messages](#sessions-messages)
- [🎮 趣味 / Just for fun](#just-for-fun)
- [🧩 MCP 与集成 / MCP & integrations](#mcp-integrations)
- [🧠 记忆与上下文 / Memory & context](#memory-context)
- [🔒 安全与审计 / Security & audit](#security-audit)
- [💻 桌面与客户端 / Desktop & clients](#desktop-clients)
- [🌐 平台与渠道 / Platforms & channels](#platforms-channels)
- [官方资源 / Official resources](#official-resources)
- [贡献指南 / Contributing](#contributing)

<a id="curation-criteria"></a>

## 收录原则 / Curation criteria

本列表优先收录在 2026 年内活跃维护（或明确长期维护）、有基本安装或配置文档且分类清晰的可用项目。不收录恶意或钓鱼插件、纯广告以及无实际功能的占位仓库。完整规则与提交流程请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。

<a id="development-tools"></a>

## 🔌 开发框架与工具 / Development tools

- [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) - DeepSeek Harness 官方主仓库，践行“一切皆插件”的扩展理念 (⭐122294)
- [nexu-io/open-design](https://github.com/nexu-io/open-design) - 面向 DSH 的开源设计插件，可作为 Claude Design 的替代方案 (⭐87154)
- [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) - 两阶段 DSH 预设：先进行最小对齐引导，再完成标准化对齐 (⭐2573)
- [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) - 集成自进化 Agent 运行时的下一代 AI 工作空间 (⭐4115)
- [xiufengsun/TokenTracker](https://github.com/xiufengsun/TokenTracker) - 本地优先的 AI Token 用量与成本追踪器，支持 31 种编程工具 (⭐1327)

<a id="design-creative"></a>

## 🎨 设计与创意 / Design & creative

- [nexu-io/open-design](https://github.com/nexu-io/open-design) - 开源 Claude Design 替代方案，提供 DSH 设计能力 (⭐87154)
- [Devin-AXIS/deepseek-design](https://github.com/Devin-AXIS/deepseek-design) - 可编辑设计系统，支持 AI 生成、可视化编辑、模板市场与 PPT (⭐38)
- [ZSeven-W/dsh-openpencil](https://github.com/ZSeven-W/dsh-openpencil) - OpenPencil 预览、检查与编辑插件 (⭐92)

<a id="vision"></a>

## 👁️ 视觉与多模态 / Vision

- [liustack/modlens](https://github.com/liustack/modlens) - DSH 视觉桥接插件，为纯文本 Agent 提供视觉能力 (⭐2114)
- [Anionex/dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit) - 让纯文本模型完成意图图片问答、长截图 OCR 与 UI 还原 (⭐474)
- [ysr666/dsh-vision-router](https://github.com/ysr666/dsh-vision-router) - 为纯文本 DSH Agent 提供内置免费视觉链路 (⭐259)
- [xiincs/claude-code-vision-skill](https://github.com/xiincs/claude-code-vision-skill) - 接入豆包、通义千问与 GPT-4o，支持截图、UI 和图表分析 (⭐165)
- [oil-oil/dsh-vision](https://github.com/oil-oil/dsh-vision) - 为 DeepSeek Harness 提供接近原生体验的图像理解能力 (⭐47)

<a id="web-ui"></a>

## 🖥️ Web UI 与界面 / Web UI

- [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) - DSH Web UI 的插件与皮肤合集 (⭐3010)
- [Sanqi-normal/dsh-webui-market-plugin](https://github.com/Sanqi-normal/dsh-webui-market-plugin) - 浏览 awesome-dsh-plugin.com 插件目录并一键安装或卸载 (⭐60)
- [Francis-Xavier-code/dsh-balance-plugin](https://github.com/Francis-Xavier-code/dsh-balance-plugin) - 提供余额监控与用量统计能力 (⭐21)
- [william-jin-cmu/dsh-stickers](https://github.com/william-jin-cmu/dsh-stickers) - 支持双向发送与展示表情贴纸 (⭐18)
- [HsiangNianian/dsh-auto-continue](https://github.com/HsiangNianian/dsh-auto-continue) - 自动发送“继续”，恢复被中断的请求 (⭐18)
- [buhuikongpan/dsh-pluginmanager](https://github.com/buhuikongpan/dsh-pluginmanager) - 面向 DSH 的分层插件管理器 (⭐5)

<a id="themes-appearance"></a>

## 🎨 主题与外观 / Themes & appearance

- [GGBond2424648901/deep-whale-day-night-theme](https://github.com/GGBond2424648901/deep-whale-day-night-theme) - 完整 Deep Whale 昼夜主题 UI 包，含鲸鱼主视觉 (⭐56)
- [KinGao294/dsh-skin](https://github.com/KinGao294/dsh-skin) - 皮肤切换器 + 自定义壁纸 (⭐15)

<a id="models-quota"></a>

## 💰 模型与额度 / Models & quota

- [feibi-mochi/deepseek-harness-wallet](https://github.com/feibi-mochi/deepseek-harness-wallet) - 余额监控、会话级花费与 Token 追踪 (⭐17)
- [franksong2702/dsh-codex-connect](https://github.com/franksong2702/dsh-codex-connect) - ChatGPT OAuth 与 Codex 模型接入 (⭐11)

<a id="testing-qa"></a>

## 🧪 测试与质检 / Testing & QA

- [Herdeny/dsh-qc](https://github.com/Herdeny/dsh-qc) - DSH 插件质量检测 CLI，支持静态分析与动态验证 (⭐1)
- [omdsh-dev/dsh-plugin-skills](https://github.com/omdsh-dev/dsh-plugin-skills) - 用于构建和测试 DSH 插件的 Agent Skills (⭐9)
- [suimi8/dsh-test-runner](https://github.com/suimi8/dsh-test-runner) - 提供 `test_run` 能力的结构化测试运行器 (⭐2)
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - 支持实时刷新的 DSH 插件目录 (⭐35)

<a id="examples-templates"></a>

## 📦 示例与模板 / Examples & templates

- [bugmaker2/dsh-plugin-template](https://github.com/bugmaker2/dsh-plugin-template) - DeepSeek Harness 插件开发模板 (⭐22)
- [sunshine-lang/dsh-plugin-template](https://github.com/sunshine-lang/dsh-plugin-template) - 可直接发布的插件骨架，包含打包格式与工具注册示例 (⭐3)
- [omdsh-dev/plugin-template](https://github.com/omdsh-dev/plugin-template) - 基于 Turtle UI 官方仓库构建的插件模板 (⭐6)
- [OneZero-Y/dsh-plugin-kit](https://github.com/OneZero-Y/dsh-plugin-kit) - 集成 Agent Skills 与可运行模板的插件开发套件 (⭐3)

<a id="sessions-messages"></a>

## 💬 会话与消息 / Sessions & messages

- [Anionex/dsh-turn-rewind](https://github.com/Anionex/dsh-turn-rewind) - 对话与代码状态回退插件，可重放历史回合 (⭐61)
- [hellodigua/dsh-emoji](https://github.com/hellodigua/dsh-emoji) - AI 回复自定义表情，支持 B 站、小红书、贴吧等多平台表情包 (⭐19)

<a id="just-for-fun"></a>

## 🎮 趣味 / Just for fun

- [lhh010/dsh-minigames](https://github.com/lhh010/dsh-minigames) - Web UI 右侧小游戏面板：18 款离线小游戏 (⭐18)
- [crafter-station/petdex](https://github.com/crafter-station/petdex) - Codex、Claude Code、DSH 等平台的动画宠物画廊 (⭐3842)

<a id="mcp-integrations"></a>

## 🧩 MCP 与集成 / MCP & integrations

- [sandbaseai/sandbase-harness](https://github.com/sandbaseai/sandbase-harness) - 集成 MCP 工具的开源 CMA 兼容 Agent 运行时 (⭐596)
- [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent) - 开源超级 AI 助手与 Agent Harness (⭐46523)
- [Haohao-end/openagent](https://github.com/Haohao-end/openagent) - 融合 OpenAI Deep Research 与 Dify 的一体化平台 (⭐788)

<a id="memory-context"></a>

## 🧠 记忆与上下文 / Memory & context

- [csyangwen/dsh-memory-evolve](https://github.com/csyangwen/dsh-memory-evolve) - 跨会话长期记忆 + 后台自我进化，五轨记忆 · git 分版本 (⭐103)
- [omdsh-dev/dsh-mnemon](https://github.com/omdsh-dev/dsh-mnemon) - 跨 Agent、本地优先的持久记忆插件 (⭐42)
- [Aik358/dsh-auto-memory](https://github.com/Aik358/dsh-auto-memory) - 三层自动记忆（用户级/项目笔记/每日日志）自动注入与检索 (⭐16)
- [modusensus/dsh-mneme](https://github.com/modusensus/dsh-mneme) - 持久化、自动整合的记忆插件 (⭐16)

<a id="security-audit"></a>

## 🔒 安全与审计 / Security & audit

- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - DSH 插件安全与依赖监控 (⭐4)
- [jkrandom-sudo/dsh-plugin-audit](https://github.com/jkrandom-sudo/dsh-plugin-audit) - 插件静态权限审计 (⭐4)
- [nanshan1995/DSH-Plugin-Market](https://github.com/nanshan1995/DSH-Plugin-Market) - 插件市场：安装前静态安全审计闸门 (⭐4)

<a id="desktop-clients"></a>

## 💻 桌面与客户端 / Desktop & clients

- [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) - 为 DSH 插件生态打造的现代化桌面端解决方案 (⭐7423)
- [omdsh-dev/dsh-genui](https://github.com/omdsh-dev/dsh-genui) - GenUI：交互式 UI 组件渲染 (⭐120)

<a id="platforms-channels"></a>

## 🌐 平台与渠道 / Platforms & channels

- [Sanqi-normal/dsh-webui-market-plugin](https://github.com/Sanqi-normal/dsh-webui-market-plugin) - 面向 DSH Web UI 的插件市场入口 (⭐60)
- [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) - 本地私有、自进化跨平台 AI 内容发现 Agent (⭐2659)
- [walkinglabs/awesome-deepseek-harness-plugins](https://github.com/walkinglabs/awesome-deepseek-harness-plugins) - 经过验证的 DeepSeek Harness 插件双语目录 (⭐5)

<a id="official-resources"></a>

## 官方资源 / Official resources

- [DeepSeek Harness 主仓库](https://github.com/deepseek-ai/deepseek-harness) - 源代码、发布记录与项目说明
- [DeepSeek Harness 官方文档](https://github.com/deepseek-ai/deepseek-harness/tree/master/docs) - 官方仓库中的开发与架构文档

<a id="contributing"></a>

## 贡献指南 / Contributing

欢迎通过 Pull Request 推荐新插件、更新星标数或修正失效链接。提交前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，并确认项目符合本列表的收录标准。

## 许可证 / License

本项目采用 [MIT License](LICENSE)。
