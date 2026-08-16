#!/usr/bin/env python3
"""Batch-run dsh-qc report on all plugins listed in awesome-dsh-2026 README.

For each plugin: download the repo tarball from codeload.github.com (through
the Clash proxy — git smart-HTTP is unreliable through the proxy, HTTPS is
not), extract it, then run `dsh-qc report <local-dir> --json` which needs no
network. Collects verdicts/scores and prints a summary.

Usage:
    python3 scripts/qc_all_plugins.py [--json out.json]
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import tarfile
import tempfile
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DSH_QC_DIR = Path.home() / "projects" / "dsh-qc"
README = ROOT / "README.md"
NODE = "/opt/homebrew/bin/node"
PROXY = "http://127.0.0.1:7897"
SKIP = {"herdeny/dsh-qc"}  # our own repo (already QC'd)
OFFICIAL = {"deepseek-ai/deepseek-harness"}

REPO_RE = re.compile(r"\[[^\]]+\]\(https://github\.com/([^/\)]+/[^/\)]+)\)")


def extract_repos() -> list[str]:
    text = README.read_text(encoding="utf-8")
    seen: set[str] = set()
    repos = []
    for m in REPO_RE.finditer(text):
        repo = m.group(1).rstrip("/").lower()
        if repo in seen or repo in SKIP or repo in OFFICIAL:
            continue
        seen.add(repo)
        repos.append(repo)
    return repos


def download_extract(repo: str, dest: Path) -> bool:
    """Download tarball via codeload and extract into dest. Returns True on success."""
    # try main, then master
    for branch in ("main", "master"):
        url = f"https://codeload.github.com/{repo}/tar.gz/refs/heads/{branch}"
        req = urllib.request.Request(url, headers={"User-Agent": "dsh-qc-batch"})
        proxy_handler = urllib.request.ProxyHandler({
            "http": PROXY, "https": PROXY})
        opener = urllib.request.build_opener(proxy_handler)
        try:
            with opener.open(req, timeout=120) as r:
                data = r.read()
            with tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tf:
                tf.write(data)
                tgz = tf.name
            try:
                with tarfile.open(tgz, "r:gz") as tar:
                    members = tar.getmembers()
                    # strip the top-level dir
                    for m in members:
                        parts = Path(m.name).parts
                        if len(parts) <= 1:
                            continue
                        new_name = str(Path(*parts[1:]))
                        m.name = new_name
                    tar.extractall(dest)
                return True
            finally:
                Path(tgz).unlink(missing_ok=True)
        except Exception:
            continue
    return False


def qc_report(local_dir: Path, repo: str, timeout: int = 120) -> dict:
    r = subprocess.run(
        [NODE, "lib/cli.js", "report", str(local_dir), "--json", "-o", "/tmp/qc_one.json"],
        cwd=str(DSH_QC_DIR), capture_output=True, text=True, timeout=timeout)
    try:
        with open("/tmp/qc_one.json") as f:
            d = json.load(f)
        return {"repo": repo, "verdict": d.get("verdict"), "score": d.get("score"),
                "breakdown": d.get("scoreBreakdown", {})}
    except Exception as e:
        return {"repo": repo, "error": f"qc failed: {e}"}


def main() -> int:
    repos = extract_repos()
    print(f"# dsh-qc 批量质检 — {len(repos)} 个插件（zip 下载 + 本地检查）", flush=True)
    results = []
    workdir = Path(tempfile.mkdtemp(prefix="dsh-qc-batch-"))
    try:
        for i, repo in enumerate(repos, 1):
            print(f"[{i}/{len(repos)}] {repo} ...", end="", flush=True)
            dest = workdir / repo.replace("/", "__")
            dest.mkdir(parents=True, exist_ok=True)
            if not download_extract(repo, dest):
                print(" ❌ 下载失败")
                results.append({"repo": repo, "error": "download failed"})
                continue
            res = qc_report(dest, repo)
            if "error" in res:
                print(f" ❌ {res['error'][:50]}")
            else:
                print(f" {res['verdict']} {res['score']}/100")
            results.append(res)
            time.sleep(0.3)
    finally:
        import shutil
        shutil.rmtree(workdir, ignore_errors=True)

    ok = [r for r in results if r.get("verdict") == "PASS"]
    fail = [r for r in results if r.get("verdict") == "FAIL"]
    err = [r for r in results if "error" in r]
    print(f"\n## 汇总: PASS {len(ok)} / FAIL {len(fail)} / 错误 {len(err)} / 共 {len(results)}")
    ranked = sorted([r for r in results if "score" in r], key=lambda x: -x["score"])
    print("\n### 评分排行 (top 10)")
    for r in ranked[:10]:
        print(f"  {r['score']:>3}/100 {r['verdict']:<4} {r['repo']}")
    print("\n### 评分垫底 (bottom 8)")
    for r in ranked[-8:]:
        print(f"  {r['score']:>3}/100 {r['verdict']:<4} {r['repo']}")
    if err:
        print("\n### 失败/错误")
        for r in err:
            print(f"  ❌ {r['repo']}: {r.get('error', '')[:60]}")

    # save full json if requested
    if "--json" in sys.argv:
        idx = sys.argv.index("--json")
        if idx + 1 < len(sys.argv):
            with open(sys.argv[idx + 1], "w") as f:
                json.dump(results, f, ensure_ascii=False, indent=1)
            print(f"\n完整结果已保存: {sys.argv[idx + 1]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
