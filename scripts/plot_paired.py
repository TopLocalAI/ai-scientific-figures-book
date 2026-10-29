#!/usr/bin/env python3
"""Reproduce the book's simulated-data figure; never generate observations."""
# SPDX-License-Identifier: MIT
import csv
import json
import subprocess
from pathlib import Path
from statistics import mean

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator

ROOT = Path(__file__).resolve().parents[1]

def load_data():
    with (ROOT / "data/paired-example.csv").open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    assert [row["sample_id"] for row in rows] == [f"SIM{i:02}" for i in range(1, 9)]
    pairs = [(float(row["before"]), float(row["after"])) for row in rows]
    assert len(pairs) == 8 and pairs[3] == (18.0, 17.0)
    assert sum(after > before for before, after in pairs) == 7
    return rows, pairs

def render(language, rows, pairs):
    labels = {
        "en": ("A  Means alone", "B  Preserve the pairing", ["Before", "After"],
               "Measurement (a.u.)", "Simulated teaching data · 8 fictional objects"),
        "zh": ("A  只展示均值", "B  保留个体配对", ["前测", "后测"],
               "测量值（任意单位）", "模拟教学数据 · 8 个虚构对象"),
    }[language]
    font = None
    if language == "zh":
        font_path = subprocess.check_output(
            ["kpsewhich", "FandolHei-Regular.otf"], text=True
        ).strip()
        if not font_path:
            raise RuntimeError("Install TeX Live's Fandol fonts to render Chinese labels.")
        font = FontProperties(fname=font_path, family="sans-serif")
    before, after = zip(*pairs)
    plt.rcParams.update({
        "font.family": "sans-serif", "font.size": 10,
        "pdf.fonttype": 42, "ps.fonttype": 42, "axes.linewidth": 0.7,
    })
    fig, axes = plt.subplots(1, 2, figsize=(7.3, 4.25), sharey=True)
    fig.subplots_adjust(left=0.09, right=0.98, top=0.82, bottom=0.19, wspace=0.30)
    fig.suptitle(labels[4], fontproperties=font, fontsize=11, y=0.96)
    means = [mean(before), mean(after)]
    axes[0].bar([0, 1], means, width=0.5, color=["#ADCED3", "#398D88"], zorder=2)
    for x, value in enumerate(means):
        axes[0].text(x, value + 0.45, f"{value:.3f}", ha="center", fontsize=9)
    for row, (pre, post) in zip(rows, pairs):
        highlight = row["sample_id"] == "SIM04"
        axes[1].plot(
            [0, 1], [pre, post], "o-", markersize=4,
            linewidth=1.8 if highlight else 1,
            color="#B9652B" if highlight else "#518F8A",
            alpha=1 if highlight else 0.7, zorder=4 if highlight else 3,
        )
    axes[1].annotate(
        "SIM04", xy=(1, 17), xytext=(0.6, 15.7), fontsize=9,
        color="#8E4C22", arrowprops={"arrowstyle": "-", "color": "#8E4C22"},
    )
    for ax, title in zip(axes, labels[:2]):
        ax.set_title(title, fontproperties=font, fontsize=11, loc="left", pad=12)
        ax.set_xticks([0, 1], labels[2], fontproperties=font)
        ax.set_xlim(-0.45, 1.45)
        ax.set_ylim(0, 23)
        ax.yaxis.set_major_locator(MultipleLocator(5))
        ax.grid(axis="y", color="#E4E8E8", linewidth=0.6, zorder=0)
        ax.spines[["top", "right"]].set_visible(False)
        ax.tick_params(axis="both", length=3)
    axes[0].set_ylabel(labels[3], fontproperties=font)
    for extension in ("pdf", "png"):
        # XeLaTeX embeds Fandol's OpenType CFF outlines correctly. Sending
        # this font through Matplotlib's Type 42 PDF path can leave CJK text
        # extractable but invisible in PDF viewers. Keep the plot vector-based.
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
                ROOT / f"figures/paired-comparison-{language}.{extension}",
                backend="pgf" if use_pgf else None,
                dpi=220, facecolor="white",
                metadata={"Creator": "TopLocalAI / Codex reproducible plotting script"},
            )
    plt.close(fig)
    return means

if __name__ == "__main__":
    rows, pairs = load_data()
    means = None
    for language in ("zh", "en"):
        means = render(language, rows, pairs)
    summary = {
        "data_status": "simulated teaching data",
        "objects": 8, "measurements": 16,
        "before_mean": means[0], "after_mean": means[1],
        "increases": 7, "decreases": 1,
        "decreasing_object": "SIM04",
        "inferential_tests": "none",
    }
    (ROOT / "provenance/paired-data-check.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary))
