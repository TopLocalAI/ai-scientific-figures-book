#!/usr/bin/env python3
"""Download and parse USGS NWIS daily values for chapter 1 (site 05484500, 2016)."""
# SPDX-License-Identifier: MIT
import csv
import hashlib
import json
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RDB_PATH = ROOT / "data/ch01/usgs-05484500-2016.rdb"
CSV_PATH = ROOT / "data/ch01/ch01-raccoon-2016.csv"
PROVENANCE = ROOT / "provenance/ch01/data-download.json"

NWIS_URL = (
    "https://waterservices.usgs.gov/nwis/dv/?format=rdb&sites=05484500"
    "&parameterCd=99133,00060&startDT=2016-01-01&endDT=2016-12-31&statCd=00003"
)
CFS_TO_M3S = 0.028316846592


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_rdb(path: Path) -> list[dict]:
    lines = path.read_text(encoding="utf-8").splitlines()
    header_idx = next(i for i, line in enumerate(lines) if line.startswith("agency_cd\t"))
    headers = lines[header_idx].split("\t")
    rows: list[dict] = []
    for line in lines[header_idx + 2 :]:
        if not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) < len(headers):
            parts.extend([""] * (len(headers) - len(parts)))
        record = dict(zip(headers, parts))
        nitrate = record.get("43103_99133_00003", "").strip()
        discharge = record.get("43102_00060_00003", "").strip()
        rows.append(
            {
                "date": record["datetime"].strip(),
                "nitrate_mgL_as_N": nitrate if nitrate else "",
                "nitrate_qual": record.get("43103_99133_00003_cd", "").strip(),
                "discharge_cfs": discharge if discharge else "",
                "discharge_qual": record.get("43102_00060_00003_cd", "").strip(),
            }
        )
    return rows


def assert_dataset(rows: list[dict]) -> dict:
    assert len(rows) == 366
    nitrate_vals = [
        (r["date"], float(r["nitrate_mgL_as_N"]))
        for r in rows
        if r["nitrate_mgL_as_N"]
    ]
    assert len(nitrate_vals) == 363
    missing = [r["date"] for r in rows if not r["nitrate_mgL_as_N"]]
    assert missing == ["2016-09-18", "2016-09-19", "2016-12-14"]
    assert all(r["nitrate_qual"] in ("", "A") for r in rows if r["nitrate_mgL_as_N"])
    assert all(r["nitrate_qual"] == "A" for r in rows if r["nitrate_mgL_as_N"])

    by_date = {r["date"]: r for r in rows}
    assert float(by_date["2016-05-13"]["nitrate_mgL_as_N"]) == 13.9
    assert float(by_date["2016-09-16"]["nitrate_mgL_as_N"]) == 3.19
    above10 = sum(1 for _, v in nitrate_vals if v > 10.0)
    assert above10 == 162

    monthly: dict[int, list[float]] = {}
    for d_str, val in nitrate_vals:
        month = int(d_str[5:7])
        monthly.setdefault(month, []).append(val)
    month_means = {m: sum(v) / len(v) for m, v in monthly.items()}
    assert abs(month_means[5] - 12.84) < 0.01
    assert abs(month_means[9] - 5.36) < 0.01

    assert int(float(by_date["2016-05-01"]["discharge_cfs"])) == 16300
    assert int(float(by_date["2016-09-06"]["discharge_cfs"])) == 411
    ae_days = sum(1 for r in rows if "e" in r["discharge_qual"])
    assert ae_days == 58

    max_n_date, max_n = max(nitrate_vals, key=lambda item: item[1])
    min_n_date, min_n = min(nitrate_vals, key=lambda item: item[1])
    discharge_vals = [
        (r["date"], float(r["discharge_cfs"]))
        for r in rows
        if r["discharge_cfs"]
    ]
    assert len(discharge_vals) == 366
    max_q_date, max_q = max(discharge_vals, key=lambda item: item[1])
    min_q_date, min_q = min(discharge_vals, key=lambda item: item[1])

    return {
        "rows_2016": 366,
        "nitrate_valid_days": 363,
        "nitrate_missing_dates": missing,
        "nitrate_max_mgL_as_N": max_n,
        "nitrate_max_date": max_n_date,
        "nitrate_min_mgL_as_N": min_n,
        "nitrate_min_date": min_n_date,
        "nitrate_days_above_10_mgL": above10,
        "monthly_mean_may": round(month_means[5], 2),
        "monthly_mean_september": round(month_means[9], 2),
        "discharge_max_cfs": max_q,
        "discharge_max_date": max_q_date,
        "discharge_max_m3s": round(max_q * CFS_TO_M3S, 1),
        "discharge_min_cfs": min_q,
        "discharge_min_date": min_q_date,
        "discharge_min_m3s": round(min_q * CFS_TO_M3S, 1),
        "discharge_ae_days": ae_days,
    }


def write_csv(rows: list[dict]) -> None:
    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    with CSV_PATH.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames=[
                "date",
                "nitrate_mgL_as_N",
                "nitrate_qual",
                "discharge_cfs",
                "discharge_qual",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    if not RDB_PATH.is_file():
        raise SystemExit(f"Missing {RDB_PATH}; download with curl -m 60 first.")
    rows = parse_rdb(RDB_PATH)
    checks = assert_dataset(rows)
    write_csv(rows)
    meta = {
        "source_url": NWIS_URL,
        "download_date": date.today().isoformat(),
        "license": "U.S. Federal Government work / public domain (USGS data policy)",
        "citation": (
            "U.S. Geological Survey, USGS water data for the Nation, site 05484500, "
            "https://doi.org/10.5066/F7P55KJN"
        ),
        "rdb_sha256": sha256_file(RDB_PATH),
        "csv_sha256": sha256_file(CSV_PATH),
        "csv_path": str(CSV_PATH.relative_to(ROOT)),
        "checks": checks,
        "parsed_at": datetime.now(timezone.utc).isoformat(),
    }
    PROVENANCE.parent.mkdir(parents=True, exist_ok=True)
    PROVENANCE.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(meta, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
