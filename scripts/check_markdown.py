#!/usr/bin/env python3
"""check_markdown.py — structural sanity checks for README.md.

Catches the failure modes a link checker cannot see:
  * in-page anchors (#-foo) that don't resolve to a real heading
  * malformed table rows (inconsistent column counts inside one table)
  * unbalanced markdown link/bracket syntax on list entries
  * unclosed code fences

Exit code 1 if any problem is found.

Usage:
    python3 scripts/check_markdown.py
"""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = ["README.md"]

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
LINK_RE = re.compile(r"\[(?:[^\[\]]|\[[^\]]*\])*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def slugify(text: str) -> str:
    """Approximate GitHub's heading -> anchor algorithm."""
    s = text.strip().lower()
    s = re.sub(r"`([^`]*)`", r"\1", s)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)  # links -> label
    s = re.sub(r"[*_~]", "", s)
    out = []
    for ch in s:
        if ch.isalnum() or ch in "-_":
            out.append(ch)
        elif ch.isspace():
            out.append("-")
        elif unicodedata.category(ch).startswith("M"):
            out.append(ch)
        # everything else (punctuation, emoji) is dropped
    return "".join(out)


def check(path: Path) -> int:
    lines = path.read_text(encoding="utf-8").split("\n")
    problems = 0

    # ---- collect anchors (auto-generated heading slugs + manual <a id="...">)
    anchors: set[str] = set()
    fence = False
    for l in lines:
        if l.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        m = HEADING_RE.match(l)
        if m:
            base = slugify(m.group(2))
            anchors.add(base)
            for n in range(1, 6):
                anchors.add(f"{base}-{n}")
        # manual anchors: <a id="foo"></a>
        for mid in re.findall(r'<a\s+id="([^"]+)"', l):
            anchors.add(mid)
    if fence:
        print(f"  [FENCE] unclosed code fence in {path.name}")
        problems += 1

    # ---- in-page anchor targets
    fence = False
    bad_anchors = []
    for i, l in enumerate(lines, 1):
        if l.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        for url in LINK_RE.findall(l):
            if not url.startswith("#"):
                continue
            target = url[1:]
            if target and target not in anchors:
                bad_anchors.append((i, url))
    if bad_anchors:
        print(f"  [ANCHOR] {len(bad_anchors)} broken in-page anchor(s) in {path.name}:")
        for ln, u in bad_anchors[:20]:
            print(f"    line {ln}: {u}")
        problems += len(bad_anchors)

    # ---- table column-count consistency
    in_table = False
    col_counts: set[int] = set()
    for i, l in enumerate(lines, 1):
        if l.strip().startswith("|") and "|" in l.strip()[1:]:
            # count columns by splitting on unescaped pipes
            cols = l.strip().strip("|").split("|")
            n = len(cols)
            if not in_table:
                in_table = True
                col_counts = {n}
            else:
                col_counts.add(n)
        else:
            if in_table:
                if len(col_counts) > 1:
                    print(f"  [TABLE] inconsistent column counts {col_counts} in {path.name}")
                    problems += 1
                in_table = False
                col_counts = set()

    # ---- unbalanced brackets on list entries
    for i, l in enumerate(lines, 1):
        if l.startswith("- [") and "](http" in l:
            opens = l.count("[")
            closes = l.count("]")
            if opens != closes:
                print(f"  [BRACKET] unbalanced [] on line {i}: {l[:80]}")
                problems += 1

    return problems


def main() -> int:
    total = 0
    for f in FILES:
        p = ROOT / f
        if p.exists():
            n = check(p)
            if n:
                print(f"✗ {f}: {n} problem(s)")
            else:
                print(f"✓ {f}: OK")
            total += n
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
