#!/usr/bin/env python3
"""Chapter 11 assets: reuse copies and optional diff figure."""
# SPDX-License-Identifier: MIT
import hashlib
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures" / "ch11"
PROV = ROOT / "provenance" / "ch11"
CASE_IMG = ROOT / "cases" / "ch07-insulin-glut4" / "images"

REUSE_MAP = [
    (
        CASE_IMG / "v2-brief.png",
        FIG / "ch11-07a-ch07-v2.png",
        "FIG ch11-07 panel a (ch07 v2-brief)",
    ),
    (
        CASE_IMG / "v3-revised-alt1.png",
        FIG / "ch11-07b-ch07-v3-alt1.png",
        "FIG ch11-07 panel b (ch07 v3-revised-alt1)",
    ),
    (
        CASE_IMG / "v3-revised.png",
        FIG / "ch11-07c-ch07-v3.png",
        "FIG ch11-07 panel c (ch07 v3-revised)",
    ),
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def copy_reuse() -> tuple[list[dict], list[str]]:
    FIG.mkdir(parents=True, exist_ok=True)
    PROV.mkdir(parents=True, exist_ok=True)
    records: list[dict] = []
    missing: list[str] = []
    for source, target, label in REUSE_MAP:
        if not source.is_file():
            missing.append(f"{label}: missing {source.relative_to(ROOT)}")
            continue
        if not target.exists() or sha256(source) != sha256(target):
            target.write_bytes(source.read_bytes())
        records.append(
            {
                "label": label,
                "source": str(source.relative_to(ROOT)),
                "target": str(target.relative_to(ROOT)),
                "sha256": sha256(target),
                "bytes": target.stat().st_size,
                "copied_on": date.today().isoformat(),
            }
        )
    return records, missing


def main() -> None:
    records, missing = copy_reuse()
    payload = {"reuse": records, "missing_sources": missing, "date": date.today().isoformat()}
    (PROV / "reuse-copies.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if missing:
        print("WARNING: some reuse sources missing", file=sys.stderr)
    diff_script = ROOT / "scripts" / "ch11_diff_check.py"
    subprocess.run([sys.executable, str(diff_script)], check=True, cwd=ROOT, timeout=300)


if __name__ == "__main__":
    main()
