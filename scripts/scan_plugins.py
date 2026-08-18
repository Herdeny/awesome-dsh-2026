#!/usr/bin/env python3
"""scan_plugins.py — discover new DSH plugins and audit existing ones.

Two jobs:
  1. SEARCH new DeepSeek Harness plugins on GitHub (multiple queries) and
     report candidates NOT already in the README.
  2. AUDIT existing entries: check each listed repo's current star count,
     archived status, and last-push date so stale entries can be flagged.

Output is plain text for a cron agent to consume. Exit 0 always (the agent
decides what to do with the findings).

Usage:
    python3 scripts/scan_plugins.py
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README_FILES = ["README.md", "README.en.md"]

# GitHub search queries for discovering new DSH plugins
SEARCH_QUERIES = [
    "deepseek harness plugin",
    "dsh-plugin",
    "dsh plugin",
    "deepseek harness skill",
    "dsh webui",
    "dsh vision",
    "dsh memory",
    "dsh theme",
    "dsh tool",
    "dsh mcp",
    "dsh agent",
    "deepseek harness ui",
    "deepseek harness theme",
    "deepseek harness extension",
    "dsh extension",
    "deepseek harness api",
]

# How many top-starred results per query to consider
PER_QUERY = 50
# Minimum stars to be worth reporting as a NEW candidate
MIN_NEW_STARS = 3


def gh_json(url: str) -> dict:
    """GET a GitHub API URL with proxy support, return parsed JSON.

    Uses GITHUB_TOKEN from the environment when present (5000 req/h instead of
    the anonymous 60 req/h, which otherwise rate-limits the audit step).
    """
    headers = {"User-Agent": "awesome-dsh-2026-scanner"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode())
    except Exception as e:
        return {"_error": str(e)}


def existing_repos() -> set[str]:
    """Collect all github.com owner/repo pairs already listed in the READMEs."""
    repos = set()
    pattern = re.compile(r"\[[^\]]+\]\(https://github\.com/([^/\)]+/[^/\)]+)\)")
    for f in README_FILES:
        p = ROOT / f
        if p.exists():
            text = p.read_text(encoding="utf-8")
            for m in pattern.finditer(text):
                owner_repo = m.group(1).rstrip("/")
                repos.add(owner_repo.lower())
    return repos


def search_new_plugins(existing: set[str]) -> list[dict]:
    """Search GitHub for DSH plugins, return candidates not in the README."""
    candidates: dict[str, dict] = {}
    for q in SEARCH_QUERIES:
        url = ("https://api.github.com/search/repositories?q=" +
               urllib.parse.quote(q) + f"&sort=stars&per_page={PER_QUERY}")
        data = gh_json(url)
        for item in data.get("items", []):
            full = item.get("full_name", "")
            if full.lower() in existing:
                continue
            if full.lower().startswith("herdeny/"):
                continue  # skip our own repos
            stars = item.get("stargazers_count", 0)
            if stars < MIN_NEW_STARS:
                continue
            # only keep repos that look DSH-related (name or description)
            hay = (full + " " + (item.get("description") or "")).lower()
            if not any(k in hay for k in ("dsh", "deepseek", "harness")):
                continue
            candidates[full] = {
                "full_name": full,
                "stars": stars,
                "desc": (item.get("description") or "")[:80],
                "pushed_at": (item.get("pushed_at") or "")[:10],
                "html_url": item.get("html_url", ""),
            }
    # sort by stars desc
    return sorted(candidates.values(), key=lambda x: -x["stars"])


def audit_existing(existing: set[str]) -> list[dict]:
    """Check each listed repo's stars / archived / pushed status."""
    out = []
    for repo in sorted(existing):
        data = gh_json(f"https://api.github.com/repos/{repo}")
        if "_error" in data:
            out.append({"repo": repo, "error": data["_error"][:60]})
            continue
        out.append({
            "repo": repo,
            "stars": data.get("stargazers_count", 0),
            "archived": data.get("archived", False),
            "pushed_at": (data.get("pushed_at") or "")[:10],
        })
        time.sleep(0.3)  # pace requests; no token = 60 req/h anonymous limit
    return out


def main() -> int:
    existing = existing_repos()
    print(f"# DSH plugin scan — {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())}")
    print(f"# 现有插件数: {len(existing)}")

    # Part 1: new candidates
    print("\n## 新插件候选 (按 star 排序)")
    new = search_new_plugins(existing)
    if not new:
        print("(无新候选)")
    for c in new[:30]:
        print(f"- {c['full_name']} (⭐{c['stars']}) | {c['desc']} | pushed {c['pushed_at']}")

    # Part 2: audit existing
    print("\n## 现有插件状态审计")
    audited = audit_existing(existing)
    problems = [a for a in audited if a.get("archived") or a.get("error")]
    stale = [a for a in audited
             if not a.get("archived") and not a.get("error")
             and a.get("pushed_at") and a["pushed_at"] < "2026-01-01"]
    if not problems and not stale:
        print("(全部正常)")
    for a in problems:
        if "error" in a:
            print(f"⚠️ {a['repo']}: 查询失败 {a['error']}")
        else:
            print(f"⚠️ {a['repo']}: 已归档 (⭐{a['stars']}, pushed {a['pushed_at']})")
    for a in stale:
        print(f"⚠️ {a['repo']}: 长期未更新 (⭐{a['stars']}, pushed {a['pushed_at']})")

    # Part 3: star changes summary (top movers)
    print("\n## 现有插件 star 速览 (top 15)")
    sorted_audit = sorted(
        [a for a in audited if "stars" in a], key=lambda x: -x["stars"])[:15]
    for a in sorted_audit:
        print(f"- {a['repo']} ⭐{a['stars']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
