#!/usr/bin/env python3
"""Generate all chapter 5 python figures and provenance/data-check.json."""
# SPDX-License-Identifier: MIT
import json
import shutil
import subprocess
from datetime import date
from pathlib import Path

from ch05_co2 import run_all as run_co2
from ch05_paired import run_all as run_paired
from ch05_penguins import run_all as run_penguins
from ch05_utils import (
    CO2_URL,
    DATA,
    PENGUINS_SHA,
    PENGUINS_URL,
    PROV,
    sha256,
    write_json,
)

ROOT = Path(__file__).resolve().parents[1]


def fetch_data() -> dict:
    DATA.mkdir(parents=True, exist_ok=True)
    records = []
    for url, name in (
        (PENGUINS_URL, "penguins.csv"),
        (CO2_URL, "co2_mm_mlo.csv"),
    ):
        dest = DATA / name
        subprocess.run(
            ["curl", "-m", "60", "-sL", "-o", str(dest), url],
            check=True,
            timeout=90,
        )
        records.append(
            {
                "file": str(dest.relative_to(ROOT)),
                "url": url,
                "downloaded": date.today().isoformat(),
                "sha256": sha256(dest),
            }
        )
    snap = DATA / "noaa-co2-mm-mlo-2026-10-09.csv"
    shutil.copy2(DATA / "co2_mm_mlo.csv", snap)
    paired_src = ROOT / "data" / "paired-example.csv"
    paired_dst = DATA / "paired-example.csv"
    if paired_src.is_file():
        shutil.copy2(paired_src, paired_dst)
        records.append(
            {
                "file": str(paired_dst.relative_to(ROOT)),
                "source": "data/paired-example.csv (simulated, CC BY 4.0)",
                "sha256": sha256(paired_dst),
            }
        )
    assert sha256(DATA / "penguins.csv") == PENGUINS_SHA
    return {"datasets": records}


def main() -> None:
    meta = fetch_data()
    penguin_checks = run_penguins()
    paired_checks = run_paired()
    co2_checks = run_co2()
    summary = {
        "chapter": "05",
        "generated_on": date.today().isoformat(),
        "data_downloads": meta,
        "penguins": penguin_checks,
        "paired_simulated": paired_checks,
        "co2": co2_checks,
        "figures": {
            "python": [
                "ch05-01-group-forms",
                "ch05-02-case-final",
                "ch05-03-paired-views",
                "ch05-04-co2-series",
                "ch05-05-axis-bad",
                "ch05-05-axis-good",
                "ch05-06-dual-axis-bad",
                "ch05-06-dual-axis-good",
                "ch05-07-colormap-bad",
                "ch05-07-colormap-good",
                "ch05-08-scatter-cvd",
            ],
            "tikz": [],
            "reuse": [],
            "sourced": [],
        },
        "notes": [
            "SciDraw scivis screenshots not in scope for this script.",
            "No kind:tikz or kind:reuse figures in ch05 plan.",
        ],
    }
    write_json(PROV / "data-check.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
