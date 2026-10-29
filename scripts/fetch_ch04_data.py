#!/usr/bin/env python3
"""Download chapter 4 public datasets into data/ch04/raw/ and write SOURCES.json."""
# SPDX-License-Identifier: MIT
import hashlib
import json
import subprocess
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "ch04" / "raw"
RAW.mkdir(parents=True, exist_ok=True)

DOWNLOADS = [
    (
        "co2_mm_mlo.csv",
        "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.csv",
        "NOAA GML Mauna Loa CO2 monthly; US government, freely available with attribution",
    ),
    (
        "HOT_surface_CO2.txt",
        "https://hahana.soest.hawaii.edu/hot/hotco2/HOT_surface_CO2.txt",
        "HOT surface CO2; cite Dore et al. 2009 (no explicit open licence in file header)",
    ),
    (
        "pent_h22-w0-700m.dat",
        "https://www.ncei.noaa.gov/data/oceans/woa/DATA_ANALYSIS/3M_HEAT_CONTENT/DATA/basin/pentad/pent_h22-w0-700m.dat",
        "NOAA NCEI pentadal OHC 0-700 m; US government work",
    ),
    (
        "pent_h22-w0-2000m.dat",
        "https://www.ncei.noaa.gov/data/oceans/woa/DATA_ANALYSIS/3M_HEAT_CONTENT/DATA/basin/pentad/pent_h22-w0-2000m.dat",
        "NOAA NCEI pentadal OHC 0-2000 m; US government work",
    ),
    (
        "GlobalCarbonBudget_v2025.xlsx",
        "https://globalcarbonbudget.org/download/2341/",
        "Global Carbon Budget v2025 xlsx; Fair Use Statement on globalcarbonbudget.org",
    ),
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fetch_one(name: str, url: str) -> Path:
    target = RAW / name
    subprocess.run(
        ["curl", "-m", "60", "-fsSL", "-L", "-o", str(target), url],
        check=True,
        timeout=90,
    )
    return target


def main() -> None:
    records = []
    for name, url, licence_note in DOWNLOADS:
        path = RAW / name
        if not path.is_file() or path.stat().st_size == 0:
            fetch_one(name, url)
        records.append(
            {
                "file": f"data/ch04/raw/{name}",
                "url": url,
                "downloaded_on": date.today().isoformat(),
                "sha256": sha256(path),
                "bytes": path.stat().st_size,
                "licence_note": licence_note,
            }
        )
    payload = {
        "chapter": "04",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "sources": records,
    }
    out = ROOT / "data" / "ch04" / "SOURCES.json"
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
