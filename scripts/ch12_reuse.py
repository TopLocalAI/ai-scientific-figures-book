#!/usr/bin/env python3
"""FIG ch12-03 reuse: copy chapter 9 final assembly into chapter 12 paths."""
# SPDX-License-Identifier: MIT
import hashlib
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures" / "ch12"
PROV = ROOT / "provenance" / "ch12"
CH09 = ROOT / "figures" / "ch09"

REUSE = [
    (
        CH09 / "ch09-07-assembly-final-zh.pdf",
        FIG / "ch12-03-paper-figure-2-zh.pdf",
    ),
    (
        CH09 / "ch09-07-assembly-final-zh.png",
        FIG / "ch12-03-paper-figure-2-zh.png",
    ),
    (
        CH09 / "ch09-07-assembly-final-en.pdf",
        FIG / "ch12-03-paper-figure-2-en.pdf",
    ),
    (
        CH09 / "ch09-07-assembly-final-en.png",
        FIG / "ch12-03-paper-figure-2-en.png",
    ),
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    FIG.mkdir(parents=True, exist_ok=True)
    PROV.mkdir(parents=True, exist_ok=True)
    records = []
    missing = []
    for source, target in REUSE:
        if not source.is_file():
            missing.append(str(source.relative_to(ROOT)))
            continue
        if not target.exists() or sha256(source) != sha256(target):
            target.write_bytes(source.read_bytes())
        records.append(
            {
                "source": str(source.relative_to(ROOT)),
                "target": str(target.relative_to(ROOT)),
                "sha256": sha256(target),
            }
        )
    payload = {"date": date.today().isoformat(), "reuse": records, "missing": missing}
    (PROV / "reuse-copies.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if missing:
        raise SystemExit("Missing ch09 assembly sources; run ch09 figure pipeline first.")


if __name__ == "__main__":
    main()
