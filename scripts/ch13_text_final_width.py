#!/usr/bin/env python3
"""FIG ch13-03: text size when scaled vs drawn at final column width."""
# SPDX-License-Identifier: MIT
import io
import subprocess
import sys
from pathlib import Path
from statistics import mean

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.ticker import MultipleLocator

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from ch13_plot_utils import FIG, MM_PER_IN, chinese_font, save_figure, setup_rc  # noqa: E402
import plot_paired  # noqa: E402

W_MM = 85.0
ORIG_W_IN = 7.3
ORIG_W_MM = ORIG_W_IN * MM_PER_IN


def paired_raster(language: str):
    rows, pairs = plot_paired.load_data()
    plot_paired.render(language, rows, pairs)
    pdf = ROOT / f"figures/paired-comparison-{language}.pdf"
    prefix = FIG / f"_paired-{language}"
    subprocess.run(
        ["pdftoppm", "-png", "-singlefile", "-r", "400", str(pdf), str(prefix)],
        check=True,
        timeout=60,
    )
    return mpimg.imread(f"{prefix}.png"), rows, pairs


def draw_paired_at_final(ax, language, rows, pairs, font):
    setup_rc(7)
    labels = {
        "zh": ("A  只展示均值", "B  保留个体配对", ["前测", "后测"], "测量值（任意单位）"),
        "en": ("A  Means alone", "B  Preserve the pairing", ["Before", "After"], "Measurement (a.u.)"),
    }[language]
    before, after = zip(*pairs)
    ax_a = ax.inset_axes([0.02, 0.12, 0.42, 0.78])
    ax_b = ax.inset_axes([0.52, 0.12, 0.46, 0.78])
    ax_a.bar([0, 1], [mean(before), mean(after)], width=0.45, color=["#ADCED3", "#398D88"], zorder=2)
    ax_a.set_xticks([0, 1], labels[2], fontproperties=font, fontsize=7)
    ax_a.set_title(labels[0], fontproperties=font, fontsize=8, loc="left", pad=4)
    ax_a.set_ylabel(labels[3], fontproperties=font, fontsize=7)
    ax_a.set_ylim(0, 23)
    ax_a.yaxis.set_major_locator(MultipleLocator(5))
    ax_a.tick_params(labelsize=7, length=2)
    ax_a.spines[["top", "right"]].set_visible(False)
    ax_a.grid(axis="y", color="#E4E8E8", linewidth=0.5, zorder=0)

    for row, (pre, post) in zip(rows, pairs):
        highlight = row["sample_id"] == "SIM04"
        ax_b.plot(
            [0, 1], [pre, post], "o-", markersize=3,
            linewidth=0.75 if not highlight else 1.2,
            color="#B9652B" if highlight else "#518F8A",
            alpha=1 if highlight else 0.75,
        )
    ax_b.set_xticks([0, 1], labels[2], fontproperties=font, fontsize=7)
    ax_b.set_title(labels[1], fontproperties=font, fontsize=8, loc="left", pad=4)
    ax_b.set_ylim(0, 23)
    ax_b.tick_params(labelsize=7, length=2)
    ax_b.spines[["top", "right"]].set_visible(False)
    ax_b.grid(axis="y", color="#E4E8E8", linewidth=0.5, zorder=0)
    ax.axis("off")


def render(language: str):
    font = chinese_font() if language == "zh" else None
    notes = {
        "zh": (
            "作图 10 pt × 85/185.4 ≈ 4.6 pt",
            "最终 7 pt",
            "同一张图在 85 mm 单栏中的两种结果（模拟教学数据）",
        ),
        "en": (
            "Drawn 10 pt × 85/185.4 ≈ 4.6 pt",
            "Final 7 pt",
            "One figure at 85 mm column width (simulated teaching data)",
        ),
    }[language]
    img, rows, pairs = paired_raster(language)
    fig_h_mm = 118.0
    fig, axes = plt.subplots(
        2, 1, figsize=(W_MM / MM_PER_IN, fig_h_mm / MM_PER_IN),
        gridspec_kw={"height_ratios": [1, 1], "hspace": 0.08},
    )
    for ax in axes:
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis("off")

    axes[0].imshow(img, aspect="auto", extent=[0.02, 0.72, 0.05, 0.95])
    axes[0].text(0.76, 0.5, notes[0], fontproperties=font, fontsize=8, va="center", ha="left")

    draw_paired_at_final(axes[1], language, rows, pairs, font)
    axes[1].text(0.76, 0.5, notes[1], fontproperties=font, fontsize=8, va="center", ha="left")

    fig.suptitle(notes[2], fontproperties=font, fontsize=9, y=0.98)
    save_figure(fig, FIG / "ch13-03-text-at-final-width", language)
    (FIG / f"_paired-{language}.png").unlink(missing_ok=True)


def main():
    _, pairs = plot_paired.load_data()
    assert pairs[3] == (18.0, 17.0)
    for language in ("zh", "en"):
        render(language)
    scaled = 10 * W_MM / ORIG_W_MM
    print(f"scaled_font_pt={scaled:.2f}")


if __name__ == "__main__":
    main()
