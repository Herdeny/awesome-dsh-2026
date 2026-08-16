#!/usr/bin/env python3
"""refresh_counts.py — keep the advertised plugin count honest.

The README header badge quotes a plugin count ("plugins-50-orange"). That
number is written by hand and drifts as entries are added/removed. This script
recounts every entry from the file itself and rewrites the badge.

    python3 scripts/refresh_counts.py             # report, exit 1 if drift
    python3 scripts/refresh_counts.py --write     # fix the badge in place

Counting rules
--------------
* An entry is a top-level `- [...]` list item whose link points to
  github.com (badge URLs, in-page anchors and prose bullets are excluded).
* The count includes every classified plugin section; the "官方资源 /
  Official resources" section is excluded (those are docs, not plugins).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = ["README.md", "README.en.md"]

ENTRY_RE = re.compile(r"^-\s*\[[^\]]+\]\(https://github\.com/")
BADGE_RE = re.compile(r"plugins-(\d+)-")
EXCLUDE_SECTIONS = ("official-resources", "官方资源", "生态项目", "ecosystem")


def section_counts(text: str) -> dict[str, int]:
    """heading-slug -> number of top-level github.com entries."""
    counts: dict[str, int] = {}
    current: str | None = None
    for line in text.split("\n"):
        if line.startswith("## "):
            title = line[3:].strip()
            # derive a slug from the title (drop emoji/&/—/spaces)
            slug = re.sub(r"[^\w\s\u4e00-\u9fff-]", "", title.lower())
            slug = slug.strip().replace(" ", "-")
            current = slug
            counts.setdefault(current, 0)
        elif current is not None and ENTRY_RE.match(line):
            counts[current] += 1
    return counts


def total_plugins(counts: dict[str, int]) -> int:
    return sum(n for slug, n in counts.items()
               if not any(x in slug for x in EXCLUDE_SECTIONS))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="rewrite the badge in place")
    args = ap.parse_args()

    for f in FILES:
        p = ROOT / f
        text = p.read_text(encoding="utf-8")
        counts = section_counts(text)
        actual = total_plugins(counts)

        m = BADGE_RE.search(text)
        claimed = int(m.group(1)) if m else None

        if claimed is None:
            print(f"✗ {f}: no plugins badge found")
            return 1

        if claimed == actual:
            print(f"✓ {f}: badge matches ({actual} plugins)")
        else:
            print(f"✗ {f}: badge claims {claimed}, actual {actual}")
            if args.write:
                new_text = BADGE_RE.sub(f"plugins-{actual}-", text)
                p.write_text(new_text, encoding="utf-8")
                print(f"  → rewrote badge to plugins-{actual}")
            else:
                return 1

        # per-section breakdown
        for slug, n in sorted(counts.items(), key=lambda x: -x[1]):
            if n and not any(x in slug for x in EXCLUDE_SECTIONS):
                print(f"    {slug}: {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
