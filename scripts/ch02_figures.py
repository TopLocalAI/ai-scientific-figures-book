#!/usr/bin/env python3
"""Chapter 2 figure assets: reuse copies and provenance (no python-kind plots in ch02)."""
# SPDX-License-Identifier: MIT
import hashlib
import json
import shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures" / "ch02"
PROV = ROOT / "provenance" / "ch02"
DATA = ROOT / "data" / "ch02"

REUSE_MAP = [
    (
        ROOT / "figures" / "mechanism-codex.png",
        FIG / "ch02-02-abstract-mechanism.png",
        "FIG ch02-02 abstract-mechanism",
    ),
    (
        ROOT / "figures" / "paired-comparison-zh.pdf",
        FIG / "ch02-07-paired-comparison-zh.pdf",
        "FIG ch02-07 paired-comparison (zh PDF)",
    ),
    (
        ROOT / "figures" / "paired-comparison-en.pdf",
        FIG / "ch02-07-paired-comparison-en.pdf",
        "FIG ch02-07 paired-comparison (en PDF)",
    ),
    (
        ROOT / "figures" / "paired-comparison-zh.png",
        FIG / "ch02-07-paired-comparison-zh.png",
        "FIG ch02-07 paired-comparison (zh PNG)",
    ),
    (
        ROOT / "figures" / "paired-comparison-en.png",
        FIG / "ch02-07-paired-comparison-en.png",
        "FIG ch02-07 paired-comparison (en PNG)",
    ),
    (
        ROOT / "data" / "paired-example.csv",
        DATA / "paired-example.csv",
        "paired data archive for ch02-07 (simulated teaching data)",
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
    DATA.mkdir(parents=True, exist_ok=True)
    PROV.mkdir(parents=True, exist_ok=True)
    records: list[dict] = []
    missing: list[str] = []
    for source, target, label in REUSE_MAP:
        if not source.is_file():
            missing.append(f"{label}: missing source {source.relative_to(ROOT)}")
            continue
        shutil.copy2(source, target)
        records.append(
            {
                "label": label,
                "source": str(source.relative_to(ROOT)),
                "target": str(target.relative_to(ROOT)),
                "sha256": sha256(target),
                "bytes": target.stat().st_size,
            }
        )
    return records, missing


def assert_paired_data() -> dict:
    csv_path = DATA / "paired-example.csv"
    assert csv_path.is_file(), "paired-example.csv must be copied into data/ch02/"
    lines = csv_path.read_text(encoding="utf-8").strip().splitlines()
    assert len(lines) == 9, "header + 8 rows"
    body = lines[1:]
    assert len(body) == 8
    assert body[3].startswith("SIM04,"), "SIM04 row for highlight"
    parts = body[3].split(",")
    assert parts[1] == "18" and parts[2] == "17"
    return {
        "data_status": "simulated teaching data (reused from data/paired-example.csv)",
        "rows": 8,
        "columns": ["sample_id", "before", "after"],
        "sim04_before": 18,
        "sim04_after": 17,
        "inferential_tests": "none",
        "python_kind_figures_in_ch02": 0,
    }


def main() -> None:
    reuse_records, missing = copy_reuse()
    paired = assert_paired_data()
    summary = {
        "chapter": "02",
        "generated_on": date.today().isoformat(),
        "python_figures": [],
        "paired_data_assertions": paired,
        "reuse_copies": reuse_records,
        "missing_sources": missing,
    }
    (PROV / "data-check.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (PROV / "reuse-manifest.json").write_text(
        json.dumps({"copies": reuse_records, "missing": missing}, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if missing:
        raise SystemExit(f"Missing {len(missing)} reuse source(s); see data-check.json")


if __name__ == "__main__":
    main()
