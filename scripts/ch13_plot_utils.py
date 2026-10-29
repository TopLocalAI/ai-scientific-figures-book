#!/usr/bin/env python3
"""Shared helpers for chapter 13 Matplotlib figures."""
# SPDX-License-Identifier: MIT
import csv
import subprocess
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures" / "ch13"

MM_PER_IN = 25.4
COLOR_CONTROL = "#6E6E6E"
COLOR_MODIFIED = "#1B7F86"


def chinese_font() -> FontProperties:
    font_path = subprocess.check_output(
        ["kpsewhich", "FandolHei-Regular.otf"], text=True, timeout=30
    ).strip()
    if not font_path:
        raise RuntimeError("Install TeX Live Fandol fonts for Chinese labels.")
    return FontProperties(fname=font_path, family="sans-serif")


def save_figure(fig, stem: Path, language: str) -> None:
    stem.parent.mkdir(parents=True, exist_ok=True)
    font = chinese_font() if language == "zh" else None
    for extension in ("pdf", "png"):
        use_pgf = language == "zh" and extension == "pdf"
        with matplotlib.rc_context({
            "pgf.texsystem": "xelatex",
            "pgf.rcfonts": False,
            "pgf.preamble": (
                r"\usepackage{fontspec}\usepackage{xeCJK}"
                r"\setsansfont{texgyreheros-regular.otf}"
                r"\setCJKmainfont{FandolHei-Regular.otf}"
                r"\setCJKsansfont{FandolHei-Regular.otf}"
            ),
        }):
            fig.savefig(
                stem.with_name(stem.name + f"-{language}.{extension}"),
                backend="pgf" if use_pgf else None,
                dpi=300,
                facecolor="white",
                bbox_inches="tight",
                pad_inches=0.02,
            )
    plt.close(fig)


def load_jv():
    path = ROOT / "data/sim-perovskite-jv.csv"
    groups = {"control": ([], []), "modified": ([], [])}
    with path.open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream):
            v = float(row["voltage_V"])
            j = float(row["current_density_mA_cm2"])
            groups[row["group"]][0].append(v)
            groups[row["group"]][1].append(j)
    assert len(groups["control"][0]) > 100
    return groups


def load_stability():
    path = ROOT / "data/sim-perovskite-stability.csv"
    groups = {"control": ([], []), "modified": ([], [])}
    with path.open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream):
            t = float(row["time_h"])
            y = float(row["normalized_pce"])
            groups[row["group"]][0].append(t)
            groups[row["group"]][1].append(y)
    return groups


def load_metrics():
    path = ROOT / "data/sim-perovskite-jv-metrics.csv"
    with path.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    assert len(rows) == 2
    return {row["group"]: row for row in rows}


def setup_rc(font_size: float = 7.0):
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
        "font.size": font_size,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "axes.linewidth": 0.75,
    })


def plot_jv_on_ax(ax, groups, *, control_style, modified_style, labels, font=None):
    ax.plot(
        groups["control"][0], groups["control"][1],
        color=COLOR_CONTROL, **control_style,
    )
    ax.plot(
        groups["modified"][0], groups["modified"][1],
        color=COLOR_MODIFIED, **modified_style,
    )
    ax.set_xlim(0, 1.2)
    ax.set_ylim(0, 25)
    ax.set_xlabel(labels["x"], fontproperties=font)
    ax.set_ylabel(labels["y"], fontproperties=font)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", color="#E4E8E8", linewidth=0.5, zorder=0)
