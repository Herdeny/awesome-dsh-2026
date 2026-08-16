# awesome-dsh-2026 — DeepSeek Harness 插件精选列表（2026 年度版）

## 定位

面向 **DeepSeek Harness (DSH) 2026 生态**的插件精选列表，按年度维护、持续更新。
区别于现有 7 个 awesome 列表的核心差异：

1. **年度版标识**：`awesome-dsh-2026` 明确面向 2026 生态，收录以 2026 年活跃维护的插件为主
2. **中文优先 + 英文对照**：README 以中文为主（面向国内开发者），英文标题辅助
3. **质量导向**：收录标准明确（见下），避免"什么插件都收"的列表膨胀
4. **收录自己的项目**：dsh-qc（插件质检 CLI）和 dsh-hello-world（示例插件）收录其中，形成生态闭环

## 收录标准

只收录满足以下条件的插件（README 中公开声明）：

- **活跃维护**：最近一次 commit 在 2026 年内（或明确声明长期维护）
- **可用**：有基本的使用文档（README 含安装/配置说明）
- **分类清晰**：能归入下方某个分类
- **不收录**：恶意/钓鱼插件、纯广告、无实际功能的占位仓库

## 目录结构

```
awesome-dsh-2026/
├── README.md              # 主列表（中英双语，分类陈列）
├── CONTRIBUTING.md        # 收录/提交通道说明
├── LICENSE                # MIT
└── .github/
    └── workflows/         # (可选) 链接检查/PR 自动化
```

## README 结构（主列表）

1. **标题区**：`# awesome-dsh-2026` + 一句话描述（中英）
2. **徽章**：license、last-updated、contributors（可选）
3. **目录**：锚点跳转
4. **分类陈列**（每类一个小节，每个插件一行）：

   格式：`- [插件名](仓库URL) - 一句话中文简介 (⭐stars)`

   分类：
   - 🔌 开发框架与工具（Development tools）
   - 🎨 设计与创意（Design & creative）——如 open-design
   - 👁️ 视觉与多模态（Vision）——如 modlens
   - 🖥️ Web UI 与界面（Web UI）——如 dsh-web-ui
   - 🧪 测试与质检（Testing & QA）——**dsh-qc** 在此
   - 📦 示例与模板（Examples & templates）——**dsh-hello-world** 在此
   - 🧩 MCP 与集成（MCP & integrations）
   - 🌐 平台与渠道（Platforms & channels）

5. **官方资源**：deepseek-ai/deepseek-harness 主仓库、官方文档链接
6. **其他 awesome 列表**：收录现有 7 个列表（互相引用，生态互助）
7. **贡献指南**：指向 CONTRIBUTING.md

## 收录自己项目的写法（dsh-qc / dsh-hello-world）

```markdown
- [dsh-qc](https://github.com/Herdeny/dsh-qc) - DSH 插件质量检测 CLI，静态分析+动态验证 (⭐N)
- [dsh-hello-world](https://github.com/Herdeny/dsh-hello-world) - DSH 插件开发示例模板 (⭐N)
```

（⭐ 数量用真实数字，随更新维护）

## 验收标准

1. README 完整：标题/徽章/目录/8 个分类/官方资源/其他列表/贡献指南
2. 每个分类至少收录 1 个真实插件（从 GitHub 搜到的真实仓库，链接有效）
3. dsh-qc 和 dsh-hello-world 正确收录
4. 中英双语标题
5. LICENSE (MIT)
6. 链接全部有效（可以用脚本检查）
