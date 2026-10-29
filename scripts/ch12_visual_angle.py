#!/usr/bin/env python3
"""FIG ch12-02: visual-angle text sizing (computed, no external data)."""
# SPDX-License-Identifier: MIT
import json
import math
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from ch12_plot_utils import FIG12, save_figure, setup_rc, chinese_font  # noqa: E402

# Small-angle error < 0.1% for distances and sizes used here (see plan §FIG 02).


def same_angle_pt(distance_m: float, ref_pt: float = 9.0, ref_d: float = 0.4) -> float:
    return ref_pt * distance_m / ref_d


def slide_pt(d_over_h: float, screen_h_pt: float = 540.0) -> float:
    return 0.00785 * d_over_h * screen_h_pt


def assert_sample_points() -> dict:
    d15 = same_angle_pt(1.5)
    assert abs(d15 - 33.75) < 0.05
    dh6 = slide_pt(6.0)
    assert abs(dh6 - 25.416) < 0.1
    return {"pt_at_1.5m": d15, "pt_at_D_over_H_6": dh6}


def render(language: str) -> None:
    font = chinese_font() if language == "zh" else None
    labels = {
        "zh": {
            "a_title": "a  与论文 9 pt@40 cm 相同视角",
            "b_title": "b  16:9 幻灯片正文下限",
            "x_dist": "观看距离（m）",
            "y_pt": "字号（pt）",
            "x_dh": "最后一排距离 ÷ 屏幕高度",
            "band": "7–10 pt@40 cm 等效",
            "paper": "论文 9 pt@0.4 m",
            "body": "海报正文 34 pt@1.5 m",
            "block": "海报区块 45 pt@2 m",
            "title": "海报标题 ≈100 pt@4–5 m",
        },
        "en": {
            "a_title": "a  Same angle as 9 pt at 40 cm",
            "b_title": "b  16:9 slide body text",
            "x_dist": "Viewing distance (m)",
            "y_pt": "Text size (pt)",
            "x_dh": "Back-row distance ÷ screen height",
            "band": "7–10 pt@40 cm equivalent",
            "paper": "Paper 9 pt@0.4 m",
            "body": "Poster body 34 pt@1.5 m",
            "block": "Poster block 45 pt@2 m",
            "title": "Poster title ≈100 pt@4–5 m",
        },
    }[language]

    setup_rc(9)
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.6))
    fig.subplots_adjust(left=0.11, right=0.97, top=0.88, bottom=0.16, wspace=0.28)

    ax = axes[0]
    d = np.logspace(math.log10(0.3), math.log10(6.0), 200)
    pt = same_angle_pt(d)
    ax.loglog(d, pt, color="#1B7F86", linewidth=2.0)
    ax.fill_between(
        d,
        same_angle_pt(d, 7.0),
        same_angle_pt(d, 10.0),
        color="#E4E8E8",
        alpha=0.9,
        label=labels["band"],
    )
    ax.scatter([0.4], [9], color="#B9652B", s=40, zorder=5)
    ax.scatter([1.5], [34], color="#6E6E6E", s=40, zorder=5)
    ax.scatter([2.0], [45], color="#6E6E6E", s=40, zorder=5)
    ax.plot([4.0, 5.0], [100, 100], color="#23363E", linewidth=2.5)
    ax.text(0.4, 9, labels["paper"], fontproperties=font, fontsize=8, va="bottom")
    ax.text(1.5, 34, labels["body"], fontproperties=font, fontsize=8, va="bottom")
    ax.text(2.0, 45, labels["block"], fontproperties=font, fontsize=8, va="bottom")
    ax.text(4.5, 105, labels["title"], fontproperties=font, fontsize=8, ha="center")
    ax.set_xlabel(labels["x_dist"], fontproperties=font)
    ax.set_ylabel(labels["y_pt"], fontproperties=font)
    ax.set_title(labels["a_title"], fontproperties=font, loc="left", fontsize=10)
    ax.grid(True, which="both", color="#E4E8E8", linewidth=0.5)

    ax = axes[1]
    dh = np.linspace(2, 10, 200)
    ax.semilogy(dh, slide_pt(dh), color="#1B7F86", linewidth=2.0)
    for ref, col in ((18, "#9A9A9A"), (24, "#6E6E6E"), (32, "#23363E")):
        ax.axhline(ref, color=col, linestyle=(0, (4, 3)), linewidth=1.2)
        ax.text(2.05, ref, f"{ref} pt", fontsize=8, va="center", color=col)
    y6 = slide_pt(6.0)
    ax.scatter([6], [y6], color="#B9652B", s=40, zorder=5)
    ax.text(6.1, y6, f"{y6:.1f} pt", fontsize=8, va="center")
    ax.set_xlabel(labels["x_dh"], fontproperties=font)
    ax.set_ylabel(labels["y_pt"], fontproperties=font)
    ax.set_title(labels["b_title"], fontproperties=font, loc="left", fontsize=10)
    ax.set_xlim(2, 10)
    ax.set_ylim(15, 45)
    ax.grid(True, which="both", color="#E4E8E8", linewidth=0.5)

    save_figure(fig, FIG12 / "ch12-02-visual-angle-text-size", language, dpi=300)


def main() -> None:
    samples = assert_sample_points()
    for lang in ("zh", "en"):
        render(lang)
    print(json.dumps(samples))


if __name__ == "__main__":
    main()
