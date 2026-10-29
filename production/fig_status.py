#!/usr/bin/env python3
"""List each FIG in production/plans/chNN.md with kind and whether its files exist."""
import re, sys
from pathlib import Path
B = Path(__file__).resolve().parents[1]
for nn in sys.argv[1:]:
    plan = (B / f"production/plans/ch{nn}.md").read_text(encoding="utf-8")
    blocks = re.split(r"\n(?=###\s+FIG)", plan)
    print(f"== ch{nn}")
    for b in blocks:
        m = re.match(r"###\s+FIG\s+(\S+)", b)
        if not m: continue
        kind = (re.search(r"kind:\s*\**\s*([a-z-]+)", b) or [None, "?"])[1]
        files = re.findall(r"figures/ch\d\d/[\w.\-{},/]+", b.split("教学目的")[0])
        found = sorted({p.name for p in (B / f"figures/ch{nn}").glob(m[1].replace('ch', 'ch', 1) + "*")} | {p.name for p in (B / f"figures/ch{nn}").glob(f"ch{nn}-{m[1].split('-')[-1]}*")})
        print(f"  {m[1]:<28} {kind:<12} files_on_disk={len(found):>2}  {' '.join(found)[:110]}")
