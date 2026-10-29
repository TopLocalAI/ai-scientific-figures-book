#!/usr/bin/env python3
"""Chapter 5 figure ch05-03: paired data views (simulated)."""
# SPDX-License-Identifier: MIT
import csv
import json
from pathlib import Path
from statistics import mean, stdev

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

from ch05_utils import RNG, chinese_font, save_pair, setup_rc, style_spines

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "ch05"


def load_paired() -> tuple[list[dict], list[tuple[float, float]]]:
    path = DATA / "paired-example.csv"
    assert path.is_file()
    with path.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    assert len(rows) == 8
    pairs = [(float(r["before"]), float(r["after"])) for r in rows]
    diffs = [after - before for before, after in pairs]
    assert diffs == [4, 3, 4, -1, 4, 5, 4, 4]
    assert abs(mean(diffs) - 3.375) < 1e-9
    before_m, after_m = mean(p[0] for p in pairs), mean(p[1] for p in pairs)
    assert abs(before_m - 13.125) < 1e-9 and abs(after_m - 16.5) < 1e-9
    return rows, pairs


def render(language: str, rows: list[dict], pairs: list[tuple[float, float]]) -> None:
    font = chinese_font() if language == "zh" else None
    labels = {
        "zh": {
            "suptitle": "模拟教学数据 · 8 个虚构对象",
            "panels": [
                "A 当作独立两组",
                "B 保留配对",
                "C 每个对象的差值",
            ],
            "x_ab": ["前测", "后测"],
            "y_ab": "测量值（任意单位）",
            "y_c": "差值（后测 − 前测，a.u.）",
            "x_c": "后测 − 前测",
        },
        "en": {
            "suptitle": "Simulated teaching data · 8 fictional objects",
            "panels": [
                "A Treated as two groups",
                "B Pairing preserved",
                "C Within-object\ndifference",
            ],
            "x_ab": ["Before", "After"],
            "y_ab": "Measurement (a.u.)",
            "y_c": "Difference (after − before, a.u.)",
            "x_c": "After − before",
        },
    }[language]
    diffs = [after - before for before, after in pairs]
    fig, axes = plt.subplots(1, 3, figsize=(5.2, 2.55))
    fig.subplots_adjust(left=0.12, right=0.98, top=0.74, bottom=0.16, wspace=0.46)
    fig.suptitle(labels["suptitle"], fontproperties=font, fontsize=9, y=0.98)

    before, after = zip(*pairs)
    # Panel A — wrong independent groups
    ax = axes[0]
    for col, values in enumerate((before, after)):
        jitter = RNG.uniform(-0.08, 0.08, size=len(values))
        ax.scatter(col + jitter, values, s=18, c="#7F7F7F", alpha=0.7, zorder=2)
        m = mean(values)
        sd = stdev(values)
        ax.hlines(m, col - 0.1, col + 0.1, colors="black", linewidth=1.1)
        ax.vlines(col, m - sd, m + sd, colors="black", linewidth=0.9)
    ax.text(0.04, 0.92, "X", transform=ax.transAxes, color="#D62728", fontsize=11, fontweight="bold", va="top")
    ax.set_title(labels["panels"][0], loc="left", fontproperties=font, fontsize=8, pad=4)
    ax.set_xticks([0, 1], labels["x_ab"], fontproperties=font)
    ax.set_xlim(-0.45, 1.45)
    ax.set_ylim(0, 23)
    ax.yaxis.set_major_locator(MultipleLocator(5))
    ax.set_ylabel(labels["y_ab"], fontproperties=font)
    style_spines(ax)

    # Panel B — paired lines
    ax = axes[1]
    for row, (pre, post) in zip(rows, pairs):
        highlight = row["sample_id"] == "SIM04"
        ax.plot(
            [0, 1],
            [pre, post],
            "o-",
            markersize=4,
            linewidth=1.8 if highlight else 1.0,
            color="#B9652B" if highlight else "#518F8A",
            alpha=1.0 if highlight else 0.7,
        )
    ax.annotate(
        "SIM04",
        xy=(1, 17),
        xytext=(0.55, 15.5),
        fontsize=8,
        color="#8E4C22",
        arrowprops={"arrowstyle": "-", "color": "#8E4C22"},
    )
    ax.set_title(labels["panels"][1], loc="left", fontproperties=font, fontsize=8, pad=4)
    ax.set_xticks([0, 1], labels["x_ab"], fontproperties=font)
    ax.set_xlim(-0.2, 1.2)
    ax.set_ylim(0, 23)
    style_spines(ax)

    # Panel C — differences
    ax = axes[2]
    jitter = RNG.uniform(-0.06, 0.06, size=len(diffs))
    colors = ["#B9652B" if rows[i]["sample_id"] == "SIM04" else "#518F8A" for i in range(8)]
    ax.scatter(jitter, diffs, s=22, c=colors, zorder=2)
    ax.axhline(0, color="#BBBBBB", linestyle="--", linewidth=0.8)
    ax.hlines(mean(diffs), -0.08, 0.08, colors="black", linewidth=1.2)
    ax.annotate("SIM04", xy=(0, -1), xytext=(0.12, -0.3), fontsize=8, color="#8E4C22")
    title = ax.set_title(labels["panels"][2], loc="left", fontproperties=font, fontsize=8, pad=2)
    title.set_linespacing(2.5)
    ax.set_xticks([0], [labels["x_c"]], fontproperties=font)
    ax.set_xlim(-0.35, 0.35)
    ax.set_ylim(-2, 6)
    ax.set_ylabel(labels["y_c"], fontproperties=font)
    style_spines(ax)

    save_pair(fig, "ch05-03-paired-views", language)
    plt.close(fig)


def run_all() -> dict:
    setup_rc()
    rows, pairs = load_paired()
    for language in ("zh", "en"):
        render(language, rows, pairs)
    diffs = [after - before for before, after in pairs]
    return {
        "data_status": "simulated teaching data",
        "n_objects": 8,
        "differences": diffs,
        "mean_difference": mean(diffs),
        "before_mean": mean(p[0] for p in pairs),
        "after_mean": mean(p[1] for p in pairs),
    }


if __name__ == "__main__":
    print(json.dumps(run_all(), indent=2))
