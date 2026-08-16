#!/usr/bin/env python3
"""sync_audit.py — bilingual structure drift auditor (zh + en).

The two README files (README.md Chinese-first, README.en.md English) must stay
in lockstep. Headings are *translated*, so they cannot be compared by text.
What must match is the STRUCTURE:

  * the same number of headings, at the same levels, in the same order
  * the same list entries inside each positional section, in the same order,
    identified by the entry's first markdown link target (URLs are not
    translated)

Usage:
    python3 scripts/sync_audit.py             # full report, exit 1 on drift
    python3 scripts/sync_audit.py --summary   # totals + issue count only
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = {
    "zh": ROOT / "README.md",
    "en": ROOT / "README.en.md",
}

HEADING_RE = re.compile(r"^(#{2,3})\s+(.*?)\s*$")
ENTRY_RE = re.compile(r"^-\s+\[(?P<label>[^\]]+)\]\((?P<url>[^)\s]+)")


def norm_url(url: str) -> str:
    u = url.strip().rstrip("/")
    u = re.sub(r"^https?://", "", u)
    u = re.sub(r"^www\.", "", u)
    return u.lower()


def is_anchor(url: str) -> bool:
    """In-page anchors are derived from *translated* headings, so they are
    expected to differ between languages and carry no structural signal."""
    return url.startswith("#")


class Section:
    __slots__ = ("level", "title", "line", "urls")

    def __init__(self, level: int, title: str, line: int):
        self.level = level
        self.title = title
        self.line = line
        self.urls: list[str] = []

    def __repr__(self) -> str:
        return f"<{'#' * self.level} {self.title} @L{self.line} n={len(self.urls)}>"


def parse(path: Path) -> list[Section]:
    sections = [Section(0, "(preamble)", 0)]
    in_fence = False
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if raw.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        h = HEADING_RE.match(raw)
        if h:
            sections.append(Section(len(h.group(1)), h.group(2), lineno))
            continue
        e = ENTRY_RE.match(raw)
        if e:
            url = e.group("url")
            if not is_anchor(url):
                sections[-1].urls.append(norm_url(url))
    return sections


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--summary", action="store_true")
    args = ap.parse_args()

    parsed = {lang: parse(p) for lang, p in FILES.items()}
    zh, en = parsed["zh"], parsed["en"]

    issues = []

    # 1. heading count / level / order
    if len(zh) != len(en):
        issues.append(f"heading count differs: zh={len(zh)} en={len(en)}")
    else:
        for i, (a, b) in enumerate(zip(zh, en)):
            if a.level != b.level:
                issues.append(f"section {i}: level differs (zh={a.level} en={b.level}) at zh:{a.title!r} / en:{b.title!r}")

    # 2. entry URLs per positional section
    n = min(len(zh), len(en))
    for i in range(n):
        if zh[i].urls != en[i].urls:
            z, e = set(zh[i].urls), set(en[i].urls)
            only_zh = z - e
            only_en = e - z
            detail = ""
            if only_zh:
                detail += f" only-zh={sorted(only_zh)[:3]}"
            if only_en:
                detail += f" only-en={sorted(only_en)[:3]}"
            issues.append(f"section {i} ({zh[i].title!r}): {len(zh[i].urls)} vs {len(en[i].urls)} entries{detail}")

    if args.summary:
        print(f"zh={len(zh)} sections en={len(en)} sections, {len(issues)} issue(s)")
    else:
        for lang, secs in parsed.items():
            print(f"--- {lang} ---")
            for s in secs:
                if s.urls:
                    print(f"  {s.level} {s.title}: {len(s.urls)} entries")
        if issues:
            print("\nDRIFT DETECTED:")
            for i in issues:
                print(f"  ✗ {i}")
        else:
            print("\n✓ zh/en READMEs are in lockstep")

    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
