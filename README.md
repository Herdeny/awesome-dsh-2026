# awesome-dsh-2026

面向国内开发者、按质量精选并持续维护的 DeepSeek Harness（DSH）2026 插件生态列表。<br>
A quality-focused, annually maintained collection of DeepSeek Harness (DSH) plugins for 2026, with Chinese-first descriptions.

> 📖 English: [README.en.md](README.en.md)

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Last updated: 2026-08](https://img.shields.io/badge/last--updated-2026--08-brightgreen.svg)
![Plugins: 55](https://img.shields.io/badge/plugins-55-orange.svg)
![Contributors](https://img.shields.io/github/contributors/Herdeny/awesome-dsh-plugins-2026.svg)

## 目录 / Contents

- [🔌 开发框架与工具](#development-tools)
- [🎨 设计与创意](#design-creative)
- [👁️ 视觉与多模态](#vision)
- [🖥️ Web UI 与界面](#web-ui)
- [🎨 主题与外观](#themes-appearance)
- [💰 模型与额度](#models-quota)
- [🧪 测试与质检](#testing-qa)
- [📦 示例与模板](#examples-templates)
- [💬 会话与消息](#sessions-messages)
- [🎮 趣味](#just-for-fun)
- [🧩 MCP 与集成](#mcp-integrations)
- [🧠 记忆与上下文](#memory-context)
- [🔒 安全与审计](#security-audit)
- [💻 桌面与客户端](#desktop-clients)
- [🌐 平台与渠道](#platforms-channels)
- [🌱 生态项目 / Ecosystem](#ecosystem)
- [官方资源 / Official resources](#official-resources)
- [贡献指南 / Contributing](#contributing)

## 质量评分分布（dsh-qc 检测） / Quality score distribution (dsh-qc)

评分来自 [dsh-qc](https://github.com/Herdeny/dsh-qc) 静态+动态质检，100 分制。🟢 良好 / 🟡 及格 / 🟠 一般 / 🔴 待改进。<br>
Scores from [dsh-qc](https://github.com/Herdeny/dsh-qc), 100-point static+dynamic QC.

- 🟢 70-100: 3
- 🟡 50-69: 22
- 🟠 30-49: 6
- 🔴 0-29: 15

<a id="development-tools"></a>

## 🔌 开发框架与工具

- [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) - DeepSeek Harness 官方主仓库，践行“一切皆插件”的扩展理念 (⭐137671)
- [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) - 两阶段 DSH 预设：先进行最小对齐引导，再完成标准化对齐 (⭐3188) 🛡️QC:31

<a id="design-creative"></a>

## 🎨 设计与创意

- [devin-axis/deepseek-design](https://github.com/devin-axis/deepseek-design) - 可编辑设计系统，支持 AI 生成、可视化编辑、模板市场与 PPT (⭐69) 🛡️QC:17
- [zseven-w/dsh-openpencil](https://github.com/zseven-w/dsh-openpencil) - OpenPencil 预览、检查与编辑插件 (⭐102) 🛡️QC:64

<a id="vision"></a>

## 👁️ 视觉与多模态

- [liustack/modlens](https://github.com/liustack/modlens) - DSH 视觉桥接插件，为纯文本 Agent 提供视觉能力 (⭐2491) 🛡️QC:43
- [anionex/dsh-vision-toolkit](https://github.com/anionex/dsh-vision-toolkit) - 让纯文本模型完成意图图片问答、长截图 OCR 与 UI 还原 (⭐559) 🛡️QC:65
- [ysr666/dsh-vision-router](https://github.com/ysr666/dsh-vision-router) - 为纯文本 DSH Agent 提供内置免费视觉链路 (⭐478) 🛡️QC:52
- [xiincs/claude-code-vision-skill](https://github.com/xiincs/claude-code-vision-skill) - 接入豆包、通义千问与 GPT-4o，支持截图、UI 和图表分析 (⭐165) 🛡️QC:17
- [oil-oil/dsh-vision](https://github.com/oil-oil/dsh-vision) - 为 DeepSeek Harness 提供接近原生体验的图像理解能力 (⭐55) 🛡️QC:69
- [Yts1919/dsh-vision-complete](https://github.com/Yts1919/dsh-vision-complete) - 多模态「眼睛和耳朵」插件：看图/OCR/物体检测/视频理解/语音转写/截图直读 (⭐33) 🛡️QC:25
- [william-jin-cmu/dsh-vision](https://github.com/william-jin-cmu/dsh-vision) - view_image 工具桥接任意 OpenAI 兼容 VLM（默认智谱免费档，实测 4 厂商 10 模型） (⭐32) 🛡️QC:47
- [tianmingwan/dsh-vision-any](https://github.com/tianmingwan/dsh-vision-any) - 让纯文本 DSH Agent 直接粘贴图片，支持任意 OpenAI 兼容 / Anthropic / Gemini 视觉 API (⭐19) 🛡️QC:61

<a id="web-ui"></a>

## 🖥️ Web UI 与界面

- [ccch1mneyyy/dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) - 官方公众号收录的 Claude Code 风 TUI 补位插件：鲸鱼顶栏/实时状态/流式思考/双击 Esc 回滚，npm 一键安装 (⭐1642) 🛡️QC:33
- [sanqi-normal/dsh-webui-market-plugin](https://github.com/sanqi-normal/dsh-webui-market-plugin) - 面向 DSH Web UI 的插件市场入口 (⭐66) 🛡️QC:61
- [francis-xavier-code/dsh-balance-plugin](https://github.com/francis-xavier-code/dsh-balance-plugin) - 提供余额监控与用量统计能力 (⭐27) 🛡️QC:61
- [hsiangnianian/dsh-auto-continue](https://github.com/hsiangnianian/dsh-auto-continue) - 自动发送“继续”，恢复被中断的请求 (⭐22) 🛡️QC:72
- [william-jin-cmu/dsh-stickers](https://github.com/william-jin-cmu/dsh-stickers) - 支持双向发送与展示表情贴纸 (⭐19) 🛡️QC:66
- [buhuikongpan/dsh-pluginmanager](https://github.com/buhuikongpan/dsh-pluginmanager) - 面向 DSH 的分层插件管理器 (⭐9) 🛡️QC:61

<a id="themes-appearance"></a>

## 🎨 主题与外观

- [WYH66666666/DSH-Transparent-UI-Plugin](https://github.com/WYH66666666/DSH-Transparent-UI-Plugin) - 高自由度玻璃质感主题：模糊度/磨砂度/背景自由调节，不改 DSH 源码 (⭐171) 🛡️QC:53
- [ggbond2424648901/deep-whale-day-night-theme](https://github.com/ggbond2424648901/deep-whale-day-night-theme) - 完整 Deep Whale 昼夜主题 UI 包，含鲸鱼主视觉 (⭐68) 🛡️QC:66
- [RevolutionLA/dsh-dream-skin](https://github.com/RevolutionLA/dsh-dream-skin) - 换肤/壁纸/主题包插件：8 套 Mirage 主题、每用户强调色、主题包导入导出与收藏 (⭐34) 🛡️QC:67
- [147228/dsh-xiaoyao-skins](https://github.com/147228/dsh-xiaoyao-skins) - 夕小瑶 × DSH Web 皮肤合集、安装器与社区创作工具链 (⭐24) 🛡️QC:33
- [oil-oil/dsh-theme](https://github.com/oil-oil/dsh-theme) - 实时主题编辑器：精选调色板与字体排印控制 (⭐19) 🛡️QC:66
- [kingao294/dsh-skin](https://github.com/kingao294/dsh-skin) - 皮肤切换器 + 自定义壁纸 (⭐17) 🛡️QC:64
- [LAN-TINA-WS/dsh-gui-customization](https://github.com/LAN-TINA-WS/dsh-gui-customization) - DSH 时装工坊：主题配色/自定义背景/视频背景/可调氛围灯，中英双语 (⭐14) 🛡️QC:33

<a id="models-quota"></a>

## 💰 模型与额度

- [feibi-mochi/deepseek-harness-wallet](https://github.com/feibi-mochi/deepseek-harness-wallet) - 余额监控、会话级花费与 Token 追踪 (⭐21) 🛡️QC:58
- [franksong2702/dsh-codex-connect](https://github.com/franksong2702/dsh-codex-connect) - ChatGPT OAuth 与 Codex 模型接入 (⭐16) 🛡️QC:68

<a id="testing-qa"></a>

## 🧪 测试与质检

- [herdeny/dsh-qc](https://github.com/herdeny/dsh-qc) - DSH 插件质量检测 CLI，支持静态分析与动态验证 (⭐2)
- [omdsh-dev/dsh-plugin-skills](https://github.com/omdsh-dev/dsh-plugin-skills) - 用于构建和测试 DSH 插件的 Agent Skills (⭐9) 🛡️QC:17
- [suimi8/dsh-test-runner](https://github.com/suimi8/dsh-test-runner) - 提供 `test_run` 能力的结构化测试运行器 (⭐2) 🛡️QC:53
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - 支持实时刷新的 DSH 插件目录 (⭐35) 🛡️QC:23

<a id="examples-templates"></a>

## 📦 示例与模板

- [bugmaker2/dsh-plugin-template](https://github.com/bugmaker2/dsh-plugin-template) - DeepSeek Harness 插件开发模板 (⭐22) 🛡️QC:66
- [sunshine-lang/dsh-plugin-template](https://github.com/sunshine-lang/dsh-plugin-template) - 可直接发布的插件骨架，包含打包格式与工具注册示例 (⭐3) 🛡️QC:58
- [omdsh-dev/plugin-template](https://github.com/omdsh-dev/plugin-template) - 基于 Turtle UI 官方仓库构建的插件模板 (⭐8) 🛡️QC:64
- [onezero-y/dsh-plugin-kit](https://github.com/onezero-y/dsh-plugin-kit) - 集成 Agent Skills 与可运行模板的插件开发套件 (⭐3) 🛡️QC:25

<a id="sessions-messages"></a>

## 💬 会话与消息

- [anionex/dsh-turn-rewind](https://github.com/anionex/dsh-turn-rewind) - 对话与代码状态回退插件，可重放历史回合 (⭐61) 🛡️QC:74
- [hellodigua/dsh-emoji](https://github.com/hellodigua/dsh-emoji) - AI 回复自定义表情，支持 B 站、小红书、贴吧等多平台表情包 (⭐23) 🛡️QC:77

<a id="just-for-fun"></a>

## 🎮 趣味

- [lhh010/dsh-minigames](https://github.com/lhh010/dsh-minigames) - Web UI 右侧小游戏面板：18 款离线小游戏 (⭐20) 🛡️QC:63

<a id="mcp-integrations"></a>

## 🧩 MCP 与集成

- [Lum1104/dsh-browser](https://github.com/Lum1104/dsh-browser) - Chrome 侧边栏扩展，让 DSH 无需视觉能力即可直接操控浏览器 (⭐216) 🛡️QC:28

<a id="memory-context"></a>

## 🧠 记忆与上下文

- [adoresever/graph-memory](https://github.com/adoresever/graph-memory) - 知识图谱记忆插件：从对话提取结构化三元组，压缩上下文 75%，跨会话复用经验 (⭐530) 🛡️QC:33
- [mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon) - LLM 监督的持久记忆：图召回 + 跨会话知识，单二进制，兼容 DSH 与任意 Agent 运行时 (⭐465) 🛡️QC:38
- [csyangwen/dsh-memory-evolve](https://github.com/csyangwen/dsh-memory-evolve) - 跨会话长期记忆 + 后台自我进化，五轨记忆 · git 分版本 (⭐131) 🛡️QC:31
- [ZSeven-W/dsh-noema](https://github.com/ZSeven-W/dsh-noema) - Noema 长期记忆插件：持久、可检视的 Agent 记忆，带召回工具与设置页 (⭐90) 🛡️QC:64
- [omdsh-dev/dsh-mnemon](https://github.com/omdsh-dev/dsh-mnemon) - 跨 Agent、本地优先的持久记忆插件 (⭐62) 🛡️QC:59
- [modusensus/dsh-mneme](https://github.com/modusensus/dsh-mneme) - 持久化、自动整合的记忆插件 (⭐19) 🛡️QC:17
- [aik358/dsh-auto-memory](https://github.com/aik358/dsh-auto-memory) - 三层自动记忆（用户级/项目笔记/每日日志）自动注入与检索 (⭐11) 🛡️QC:61

<a id="security-audit"></a>

## 🔒 安全与审计

- [micromilo/upstream-radar](https://github.com/micromilo/upstream-radar) - DSH 插件安全与依赖监控 (⭐4) 🛡️QC:41
- [jkrandom-sudo/dsh-plugin-audit](https://github.com/jkrandom-sudo/dsh-plugin-audit) - 插件静态权限审计 (⭐4) 🛡️QC:51
- [nanshan1995/dsh-plugin-market](https://github.com/nanshan1995/dsh-plugin-market) - 插件市场：安装前静态安全审计闸门 (⭐4) 🛡️QC:55

<a id="desktop-clients"></a>

## 💻 桌面与客户端

- [omdsh-dev/dsh-genui](https://github.com/omdsh-dev/dsh-genui) - GenUI：交互式 UI 组件渲染 (⭐149) 🛡️QC:52
- [ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop) - Windows 桌面客户端：零配置安装，内置 Codex/插件/技能/SSH 远程访问与 11 款皮肤 (⭐66) 🛡️QC:11
- [qiannianhuanxiang/DSHA](https://github.com/qiannianhuanxiang/DSHA) - 安卓启动器：内置 proot+Ubuntu，免 ROOT 免 Termux 一键运行 DeepSeek Harness (⭐65) 🛡️QC:25
- [WEP-56/DSH-Launcher](https://github.com/WEP-56/DSH-Launcher) - webui 内嵌式启动器：包管理/配置管理/插件管理，兼容所有 webui 强化插件 (⭐17) 🛡️QC:33

<a id="platforms-channels"></a>

## 🌐 平台与渠道

- [dsh-market/dsh-market](https://github.com/dsh-market/dsh-market) - DSH 内置可视化插件市场：浏览、搜索、一键安装 (⭐650) 🛡️QC:64
- [walkinglabs/awesome-deepseek-harness-plugins](https://github.com/walkinglabs/awesome-deepseek-harness-plugins) - 经过验证的 DeepSeek Harness 插件双语目录 (⭐7) 🛡️QC:25

<a id="ecosystem"></a>

## 🌱 生态项目 / Ecosystem

与 DSH 生态相关但不是标准插件（无 cordis 插件清单）的项目，QC 评分为 0 属正常。

- [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) - 为 DSH 插件生态打造的现代化桌面端解决方案 (⭐9879)
- [crafter-station/petdex](https://github.com/crafter-station/petdex) - Codex、Claude Code、DSH 等平台的动画宠物画廊 (⭐3842)
- [devin-axis/ipollowork](https://github.com/devin-axis/ipollowork) - 集成自进化 Agent 运行时的下一代 AI 工作空间 (⭐4115)
- [haohao-end/openagent](https://github.com/haohao-end/openagent) - 融合 OpenAI Deep Research 与 Dify 的一体化平台 (⭐788)
- [nexu-io/open-design](https://github.com/nexu-io/open-design) - 开源 Claude Design 替代方案，提供 DSH 设计能力 (⭐87154)
- [sandbaseai/sandbase-harness](https://github.com/sandbaseai/sandbase-harness) - 集成 MCP 工具的开源 CMA 兼容 Agent 运行时 (⭐596)
- [whiteguo233/openbiliclaw](https://github.com/whiteguo233/openbiliclaw) - 本地私有、自进化跨平台 AI 内容发现 Agent (⭐2659)
- [xiufengsun/tokentracker](https://github.com/xiufengsun/tokentracker) - 本地优先的 AI Token 用量与成本追踪器，支持 31 种编程工具 (⭐1327)
- [zhayujie/cowagent](https://github.com/zhayujie/cowagent) - 开源超级 AI 助手与 Agent Harness (⭐46523)
- [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) - DSH Web UI 的插件与皮肤合集 (⭐3642)

<a id="official-resources"></a>

## 官方资源 / Official resources

- [DeepSeek Harness 主仓库](https://github.com/deepseek-ai/deepseek-harness) - 源代码、发布记录与项目说明
- [DeepSeek Harness 官方文档](https://github.com/deepseek-ai/deepseek-harness/tree/master/docs) - 官方仓库中的开发与架构文档

<a id="contributing"></a>

## 贡献指南 / Contributing

欢迎通过 Pull Request 推荐新插件、更新星标数或修正失效链接。提交前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，并确认项目符合本列表的收录标准。

## 许可证 / License

本项目采用 [MIT License](LICENSE)。
