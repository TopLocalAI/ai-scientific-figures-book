# SPDX-License-Identifier: MIT
"""Load and assert chapter 4 public datasets."""
from __future__ import annotations

from io import StringIO
from pathlib import Path

import numpy as np
import openpyxl
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "ch04" / "raw"


def load_mlo() -> pd.DataFrame:
    lines = []
    with (RAW / "co2_mm_mlo.csv").open(encoding="utf-8") as stream:
        for line in stream:
            if line.startswith("#") or not line.strip():
                continue
            lines.append(line)
    assert len(lines) >= 800
    frame = pd.read_csv(StringIO("".join(lines)))
    assert int(frame.iloc[0]["year"]) == 1958 and int(frame.iloc[0]["month"]) == 3
    assert (frame["average"] > 0).all()
    assert (frame["average"] != -99.99).all()
    frame["decimal_date"] = pd.to_numeric(frame["decimal date"], errors="coerce")
    return frame


def load_hot() -> pd.DataFrame:
    frame = pd.read_csv(RAW / "HOT_surface_CO2.txt", sep="\t", skiprows=8)
    frame["date"] = pd.to_datetime(frame["date"], format="%d-%b-%y")
    assert frame["date"].min().year == 1988 and frame["date"].min().month == 10
    for col in ("pCO2calc_insitu", "pHcalc_insitu"):
        frame[col] = pd.to_numeric(frame[col], errors="coerce")
        frame.loc[frame[col] <= -900, col] = np.nan
    assert frame["pCO2calc_insitu"].notna().sum() > 200
    assert frame["pHcalc_insitu"].notna().sum() > 200
    return frame


def load_ohc(depth: str) -> pd.DataFrame:
    name = f"pent_h22-w0-{depth}m.dat"
    frame = pd.read_csv(RAW / name, sep=r"\s+", engine="python")
    for col in ("YEAR", "WO", "WOse"):
        frame[col] = pd.to_numeric(frame[col], errors="coerce")
    assert frame["YEAR"].min() <= 1958 and frame["YEAR"].max() >= 2020
    return frame


def load_ohc_pair() -> tuple[pd.DataFrame, pd.DataFrame]:
    shallow = load_ohc("700")
    deep = load_ohc("2000")
    assert len(shallow) == len(deep)
    assert np.allclose(shallow["YEAR"].values, deep["YEAR"].values)
    return shallow, deep


def load_gcb() -> pd.DataFrame:
    path = RAW / "GlobalCarbonBudget_v2025.xlsx"
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    ws = wb["Global Carbon Budget"]
    rows = list(ws.iter_rows(values_only=True))
    header_idx = next(i for i, row in enumerate(rows) if row and row[0] == "Year")
    header = rows[header_idx]
    data_rows = []
    for row in rows[header_idx + 1 :]:
        if row[0] is None or not isinstance(row[0], (int, float)):
            continue
        data_rows.append(dict(zip(header, row)))
    frame = pd.DataFrame(data_rows)
    frame["Year"] = frame["Year"].astype(int)
    assert frame["Year"].iloc[0] == 1959
    assert frame["Year"].is_monotonic_increasing
    assert frame["Year"].diff().dropna().eq(1).all()
    for col in (
        "fossil emissions excluding carbonation",
        "land-use change emissions",
        "atmospheric growth",
        "ocean sink",
        "land sink",
    ):
        frame[col] = pd.to_numeric(frame[col], errors="coerce")
    frame["total_emissions"] = (
        frame["fossil emissions excluding carbonation"] + frame["land-use change emissions"]
    )
    frame["ocean_share_pct"] = frame["ocean sink"] / frame["total_emissions"] * 100.0
    return frame


def data_check_summary() -> dict:
    mlo = load_mlo()
    hot = load_hot()
    o700, o2000 = load_ohc_pair()
    gcb = load_gcb()
    return {
        "mlo_rows": int(len(mlo)),
        "mlo_first": "1958-03",
        "mlo_last": f"{int(mlo.iloc[-1]['year'])}-{int(mlo.iloc[-1]['month']):02d}",
        "mlo_mean_average_ppm": round(float(mlo["average"].mean()), 4),
        "hot_rows": int(len(hot)),
        "hot_valid_pco2": int(hot["pCO2calc_insitu"].notna().sum()),
        "hot_valid_ph": int(hot["pHcalc_insitu"].notna().sum()),
        "hot_first_cruise": hot["date"].min().strftime("%Y-%m-%d"),
        "ohc_pentad_rows": int(len(o700)),
        "ohc_year_min": float(o700["YEAR"].min()),
        "ohc_year_max": float(o700["YEAR"].max()),
        "ohc_wo_700_mean": round(float(o700["WO"].mean()), 4),
        "ohc_wo_2000_mean": round(float(o2000["WO"].mean()), 4),
        "gcb_rows": int(len(gcb)),
        "gcb_first_year": int(gcb["Year"].iloc[0]),
        "gcb_last_year": int(gcb["Year"].iloc[-1]),
        "gcb_mean_ocean_sink": round(float(gcb["ocean sink"].mean()), 4),
        "gcb_mean_ocean_share_pct": round(float(gcb["ocean_share_pct"].mean()), 4),
    }
