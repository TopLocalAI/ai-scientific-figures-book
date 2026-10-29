#!/usr/bin/env python3
"""Shared helpers for chapter 5 Matplotlib figures."""
# SPDX-License-Identifier: MIT
import hashlib
import json
from pathlib import Path
from typing import Optional

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.font_manager import FontProperties
from scipy import stats

matplotlib.use("Agg")

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures" / "ch05"
DATA = ROOT / "data" / "ch05"
PROV = ROOT / "provenance" / "ch05"

RNG = np.random.default_rng(20261029)

SPECIES_ORDER = ["Adelie", "Chinstrap", "Gentoo"]
SPECIES_ZH = {"Adelie": "阿德利", "Chinstrap": "帽带", "Gentoo": "巴布亚"}
SPECIES_COLOR = {
    "Adelie": "#E69F00",
    "Chinstrap": "#56B4E9",
    "Gentoo": "#009E73",
}
MARKER = {"Adelie": "o", "Chinstrap": "^", "Gentoo": "s"}

PENGUINS_URL = (
    "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/v0.1.0/"
    "inst/extdata/penguins.csv"
)
PENGUINS_SHA = "f204db2c753b0937caac3cb35258562c14f073e4bbc76be24b4c51ce22767a93"
CO2_URL = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.csv"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def chinese_font():
    """Return None so labels use bookfig's Heros/Fandol fallback, not one file."""
    return None


def setup_rc(lang: str = "en") -> None:
    import bookfig

    bookfig.setup(lang)


def save_pair(fig: plt.Figure, stem: str, language: str, allow_overlap=None, pad_inches: float = 0.12) -> None:
    """Write PDF and 300 dpi PNG under figures/ch05/ after bookfig QC."""
    import bookfig

    bookfig.save(fig, FIG / stem, language, allow_overlap=allow_overlap, pad_inches=pad_inches)


def load_penguins_raw() -> pd.DataFrame:
    path = DATA / "penguins.csv"
    assert path.is_file(), "Run ch05_figures.py to fetch data/ch05/penguins.csv"
    assert sha256(path) == PENGUINS_SHA, "penguins.csv SHA-256 mismatch"
    df = pd.read_csv(path)
    assert len(df) == 344 and list(df.columns) == [
        "species",
        "island",
        "bill_length_mm",
        "bill_depth_mm",
        "flipper_length_mm",
        "body_mass_g",
        "sex",
        "year",
    ]
    assert df["sex"].isna().sum() == 11
    return df


def penguins_by_species(df: pd.DataFrame) -> pd.DataFrame:
    out = df.dropna(subset=["body_mass_g"]).copy()
    assert len(out) == 342
    return out


def penguins_by_species_sex(df: pd.DataFrame) -> pd.DataFrame:
    out = df.dropna(subset=["body_mass_g", "sex"]).copy()
    assert len(out) == 333
    return out


def species_mass_stats(df: pd.DataFrame) -> dict:
    """Return per-species n, mean, SD, SEM, median, CI half-width."""
    stats_out = {}
    expected_n = {"Adelie": 151, "Chinstrap": 68, "Gentoo": 123}
    expected_mean = {"Adelie": 3700.7, "Chinstrap": 3733.1, "Gentoo": 5076.0}
    expected_sem = {"Adelie": 37.3, "Chinstrap": 46.6, "Gentoo": 45.5}
    expected_median = {"Adelie": 3700, "Chinstrap": 3700, "Gentoo": 5000}
    for sp in SPECIES_ORDER:
        sub = df.loc[df["species"] == sp, "body_mass_g"]
        n = len(sub)
        mean = sub.mean()
        sd = sub.std(ddof=1)
        sem = sd / np.sqrt(n)
        ci_hw = stats.t.ppf(0.975, n - 1) * sem
        med = sub.median()
        stats_out[sp] = {
            "n": n,
            "mean": mean,
            "sd": sd,
            "sem": sem,
            "ci_half_width": ci_hw,
            "median": med,
        }
        assert n == expected_n[sp]
        assert abs(mean - expected_mean[sp]) < 0.15
        assert abs(sem - expected_sem[sp]) < 0.15
        assert med == expected_median[sp]
    return stats_out


def species_sex_stats(df: pd.DataFrame) -> dict:
    expected = {
        ("Adelie", "female"): (73, 3368.8, 269.4),
        ("Adelie", "male"): (73, 4043.5, 346.8),
        ("Chinstrap", "female"): (34, 3527.2, 285.3),
        ("Chinstrap", "male"): (34, 3939.0, 362.1),
        ("Gentoo", "female"): (58, 4679.7, 281.6),
        ("Gentoo", "male"): (61, 5484.8, 313.2),
    }
    out = {}
    for (sp, sex), (en, emean, esd) in expected.items():
        sub = df.loc[(df["species"] == sp) & (df["sex"] == sex), "body_mass_g"]
        n, mean, sd = len(sub), sub.mean(), sub.std(ddof=1)
        assert n == en and abs(mean - emean) < 0.15 and abs(sd - esd) < 0.15
        out[(sp, sex)] = {"n": n, "mean": mean, "sd": sd}
    return out


def bill_scatter_df(df: pd.DataFrame) -> pd.DataFrame:
    out = df.dropna(subset=["bill_length_mm", "bill_depth_mm"]).copy()
    assert len(out) == 342
    return out


def pearson_r(x: np.ndarray, y: np.ndarray) -> float:
    return float(np.corrcoef(x, y)[0, 1])



def panel_letter(ax, text: str, font: Optional[FontProperties]) -> None:
    ax.text(
        0.02,
        0.98,
        text,
        transform=ax.transAxes,
        va="top",
        ha="left",
        fontproperties=font,
        fontsize=9,
        fontweight="bold",
    )


def style_spines(ax) -> None:
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(axis="both", length=3)


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
