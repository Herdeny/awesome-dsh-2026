#!/usr/bin/env python3
"""Regenerate bilingual READMEs with dsh-qc scores + Ecosystem category.

Builds both README.md (Chinese-first) and README.en.md (English) from
/tmp/merged_entries.json. Section layout is defined here (not read from the
existing README), so running it twice never duplicates sections.

Each entry: `- [owner/repo](url) - desc (⭐N) 🛡️QC:NN`
Ecosystem repos (non-plugin projects) live in their own section.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path("/Users/herdeny/projects/awesome-dsh-2026")
SCORE_MAP = {r["repo"].lower(): r.get("score")
             for r in json.load(open("/tmp/qc_all_results.json"))}
SCORE_MAP["ggbond2424648901/deep-whale-day-night-theme"] = 66

# (slug, emoji, zh_title, en_title, [repo,...]) — order matters
SECTIONS = [
    ("development-tools", "🔌", "开发框架与工具", "Development tools",
     ["deepseek-ai/deepseek-harness", "xiaobright/dsh-anchored-standard"]),
    ("design-creative", "🎨", "设计与创意", "Design & creative",
     ["devin-axis/deepseek-design", "zseven-w/dsh-openpencil"]),
    ("vision", "👁️", "视觉与多模态", "Vision",
     ["liustack/modlens", "anionex/dsh-vision-toolkit", "ysr666/dsh-vision-router",
      "xiincs/claude-code-vision-skill", "oil-oil/dsh-vision"]),
    ("web-ui", "🖥️", "Web UI 与界面", "Web UI",
     ["sanqi-normal/dsh-webui-market-plugin", "francis-xavier-code/dsh-balance-plugin",
      "william-jin-cmu/dsh-stickers", "hsiangnianian/dsh-auto-continue",
      "buhuikongpan/dsh-pluginmanager"]),
    ("themes-appearance", "🎨", "主题与外观", "Themes & appearance",
     ["ggbond2424648901/deep-whale-day-night-theme", "kingao294/dsh-skin"]),
    ("models-quota", "💰", "模型与额度", "Models & quota",
     ["feibi-mochi/deepseek-harness-wallet", "franksong2702/dsh-codex-connect"]),
    ("testing-qa", "🧪", "测试与质检", "Testing & QA",
     ["herdeny/dsh-qc", "omdsh-dev/dsh-plugin-skills", "suimi8/dsh-test-runner",
      "whyihaveyou/dsh-suite"]),
    ("examples-templates", "📦", "示例与模板", "Examples & templates",
     ["bugmaker2/dsh-plugin-template", "sunshine-lang/dsh-plugin-template",
      "omdsh-dev/plugin-template", "onezero-y/dsh-plugin-kit"]),
    ("sessions-messages", "💬", "会话与消息", "Sessions & messages",
     ["anionex/dsh-turn-rewind", "hellodigua/dsh-emoji"]),
    ("just-for-fun", "🎮", "趣味", "Just for fun",
     ["lhh010/dsh-minigames"]),
    ("mcp-integrations", "🧩", "MCP 与集成", "MCP & integrations",
     []),
    ("memory-context", "🧠", "记忆与上下文", "Memory & context",
     ["csyangwen/dsh-memory-evolve", "omdsh-dev/dsh-mnemon", "aik358/dsh-auto-memory",
      "modusensus/dsh-mneme"]),
    ("security-audit", "🔒", "安全与审计", "Security & audit",
     ["micromilo/upstream-radar", "jkrandom-sudo/dsh-plugin-audit",
      "nanshan1995/dsh-plugin-market"]),
    ("desktop-clients", "💻", "桌面与客户端", "Desktop & clients",
     ["omdsh-dev/dsh-genui"]),
    ("platforms-channels", "🌐", "平台与渠道", "Platforms & channels",
     ["walkinglabs/awesome-deepseek-harness-plugins"]),
]

# non-plugin projects -> Ecosystem
ECOSYSTEM = [
    "anywhere-labs/deepseek-harness-desktop", "crafter-station/petdex",
    "devin-axis/ipollowork", "haohao-end/openagent", "nexu-io/open-design",
    "sandbaseai/sandbase-harness", "whiteguo233/openbiliclaw",
    "xiufengsun/tokentracker", "zhayujie/cowagent", "zhu1090093659/dsh-web-ui",
]


def score_badge(repo: str) -> str:
    s = SCORE_MAP.get(repo.lower())
    if s is None:
        return ""
    color = "🟢" if s >= 70 else "🟡" if s >= 50 else "🟠" if s >= 30 else "🔴"
    return f" 🛡️QC:{s}"


def dist_block() -> str:
    scores = [s for s in SCORE_MAP.values() if s is not None]
    dist = {"🟢 70-100": 0, "🟡 50-69": 0, "🟠 30-49": 0, "🔴 0-29": 0}
    for s in scores:
        if s >= 70: dist["🟢 70-100"] += 1
        elif s >= 50: dist["🟡 50-69"] += 1
        elif s >= 30: dist["🟠 30-49"] += 1
        else: dist["🔴 0-29"] += 1
    lines = "\n".join(f"- {k}: {v}" for k, v in dist.items())
    return f"""## 质量评分分布（dsh-qc 检测） / Quality score distribution (dsh-qc)

评分来自 [dsh-qc](https://github.com/Herdeny/dsh-qc) 静态+动态质检，100 分制。🟢 良好 / 🟡 及格 / 🟠 一般 / 🔴 待改进。<br>
Scores from [dsh-qc](https://github.com/Herdeny/dsh-qc), 100-point static+dynamic QC.

{lines}

"""


def render(lang: str, entries: dict) -> str:
    is_zh = lang == "zh"
    switch = ("📖 English: [README.en.md](README.en.md)" if is_zh
              else "📖 中文主版：[README.md](README.md) · English version: this page")
    header = f"""# awesome-dsh-2026

面向国内开发者、按质量精选并持续维护的 DeepSeek Harness（DSH）2026 插件生态列表。<br>
A quality-focused, annually maintained collection of DeepSeek Harness (DSH) plugins for 2026, with Chinese-first descriptions.

> {switch}

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Last updated: 2026-08](https://img.shields.io/badge/last--updated-2026--08-brightgreen.svg)
![Plugins: 46](https://img.shields.io/badge/plugins-46-orange.svg)
![Contributors](https://img.shields.io/github/contributors/Herdeny/awesome-dsh-2026.svg)

"""

    toc = []
    body = [dist_block().rstrip(), ""]
    for slug, emoji, zh_t, en_t, repos in SECTIONS:
        zh_h = f"{emoji} {zh_t}"
        en_h = f"{emoji} {en_t}"
        heading = zh_h if is_zh else en_h
        toc.append(f"- [{heading}](#{slug})")
        body.append(f"<a id=\"{slug}\"></a>")
        body.append("")
        body.append(f"## {heading}")
        body.append("")
        for repo in repos:
            e = entries.get(repo)
            if not e:
                continue
            desc = e["zh_desc"] if is_zh else e["en_desc"]
            stars = e["stars"]
            body.append(f"- [{repo}](https://github.com/{repo}) - {desc} ({stars}){score_badge(repo)}")
        body.append("")

    # Ecosystem
    eco_slug = "ecosystem"
    eco_head = "🌱 生态项目 / Ecosystem" if is_zh else "🌱 Ecosystem"
    toc.append(f"- [{eco_head}](#{eco_slug})")
    body.append(f"<a id=\"{eco_slug}\"></a>")
    body.append("")
    body.append(f"## {eco_head}")
    body.append("")
    if is_zh:
        body.append("与 DSH 生态相关但不是标准插件（无 cordis 插件清单）的项目，QC 评分为 0 属正常。")
    else:
        body.append("DSH-ecosystem projects that are not standard plugins (no cordis manifest); a 0 QC score is expected.")
    body.append("")
    for repo in ECOSYSTEM:
        e = entries.get(repo)
        if not e:
            continue
        desc = e["zh_desc"] if is_zh else e["en_desc"]
        # ecosystem entries carry no QC badge — they are not plugins
        body.append(f"- [{repo}](https://github.com/{repo}) - {desc} ({e['stars']})")
    body.append("")

    # official resources + contributing + license
    off_slug, contrib_slug = "official-resources", "contributing"
    if is_zh:
        toc.append(f"- [官方资源 / Official resources](#{off_slug})")
        toc.append(f"- [贡献指南 / Contributing](#{contrib_slug})")
        body.extend([
            f"<a id=\"{off_slug}\"></a>", "",
            "## 官方资源 / Official resources", "",
            "- [DeepSeek Harness 主仓库](https://github.com/deepseek-ai/deepseek-harness) - 源代码、发布记录与项目说明",
            "- [DeepSeek Harness 官方文档](https://github.com/deepseek-ai/deepseek-harness/tree/master/docs) - 官方仓库中的开发与架构文档", "",
            f"<a id=\"{contrib_slug}\"></a>", "",
            "## 贡献指南 / Contributing", "",
            "欢迎通过 Pull Request 推荐新插件、更新星标数或修正失效链接。提交前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，并确认项目符合本列表的收录标准。", "",
            "## 许可证 / License", "",
            "本项目采用 [MIT License](LICENSE)。", "",
        ])
    else:
        toc.append(f"- [Official resources](#{off_slug})")
        toc.append(f"- [Contributing](#{contrib_slug})")
        body.extend([
            f"<a id=\"{off_slug}\"></a>", "",
            "## Official resources", "",
            "- [DeepSeek Harness repo](https://github.com/deepseek-ai/deepseek-harness) - Source code, releases and project documentation",
            "- [DeepSeek Harness docs](https://github.com/deepseek-ai/deepseek-harness/tree/master/docs) - Development and architecture docs", "",
            f"<a id=\"{contrib_slug}\"></a>", "",
            "## Contributing", "",
            "Contributions are welcome — recommend a new plugin, update star counts, or fix broken links via Pull Request. Read [CONTRIBUTING.md](CONTRIBUTING.md) first.", "",
            "## License", "",
            "This project is licensed under the [MIT License](LICENSE).", "",
        ])

    # assemble: header + toc + body
    toc_block = "## 目录 / Contents\n\n" + "\n".join(toc) + "\n"
    return header + toc_block + "\n" + "\n".join(body)


def main() -> None:
    entries = json.load(open("/tmp/merged_entries.json"))
    zh_out = render("zh", entries)
    en_out = render("en", entries)
    (ROOT / "README.md").write_text(zh_out, encoding="utf-8")
    (ROOT / "README.en.md").write_text(en_out, encoding="utf-8")
    print("✅ README.md + README.en.md regenerated")


if __name__ == "__main__":
    main()
