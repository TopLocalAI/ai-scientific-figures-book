#!/usr/bin/env python3
"""FIG ch12-05a/b: pasted paper figure vs rebuilt slide (119 mm print width)."""
# SPDX-License-Identifier: MIT
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from ch12_plot_utils import (  # noqa: E402
    COLOR_ACCENT,
    FIG12,
    chinese_font,
    save_figure,
    setup_rc,
)

SLIDE_W_IN = 13.333
SLIDE_H_IN = 7.5
PRINT_W_MM = 119.0
PAPER_FIG = FIG12 / "ch12-03-paper-figure-2-zh.png"
SLIDE_2B = FIG12 / "slides" / "slide-2b-zh.png"

ISSUES_ZH = [
    (0.02, 0.55, "①"),
    (0.02, 0.45, "②"),
    (0.02, 0.35, "③"),
    (0.02, 0.25, "④"),
    (0.02, 0.15, "⑤"),
]
ISSUES_EN = ISSUES_ZH


def raster_paper(language: str) -> np.ndarray:
    path = FIG12 / f"ch12-03-paper-figure-2-{language}.png"
    if not path.is_file():
        raise FileNotFoundError(f"Missing {path}; run ch12_reuse.py first.")
    return np.array(Image.open(path))


def draw_pasted(language: str) -> plt.Figure:
    font = chinese_font() if language == "zh" else None
    title = "结果" if language == "zh" else "Results"
    fig = plt.figure(figsize=(SLIDE_W_IN, SLIDE_H_IN))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis("off")
    ax.text(0.05, 0.92, title, fontproperties=font, fontsize=36, ha="left", va="top")
    img = raster_paper(language)
    img_ax = fig.add_axes([0.05, 0.08, 0.9, 0.78])
    img_ax.imshow(img)
    img_ax.axis("off")
    issues = ISSUES_ZH if language == "zh" else ISSUES_EN
    for x, y, num in issues:
        circ = Circle((x, y), 0.018, transform=ax.transAxes, fill=True, color=COLOR_ACCENT, zorder=10)
        ax.add_patch(circ)
        ax.text(
            x, y, num, transform=ax.transAxes, fontproperties=font,
            color="white", fontsize=14, ha="center", va="center", zorder=11,
        )
    return fig


def draw_rebuilt(language: str) -> plt.Figure:
    path = FIG12 / "slides" / f"slide-2b-{language}.png"
    if not path.is_file():
        raise FileNotFoundError(f"Missing {path}; run ch12_slides.py first.")
    img = np.array(Image.open(path))
    fig = plt.figure(figsize=(SLIDE_W_IN, SLIDE_H_IN))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.imshow(img)
    ax.axis("off")
    return fig


def save_book_pair(fig_a, fig_b, language: str, stem_a: str, stem_b: str) -> None:
    """Export each slide at 119 mm width for print verification."""
    w_in = PRINT_W_MM / 25.4
    h_in = w_in * (SLIDE_H_IN / SLIDE_W_IN)
    for fig, stem in ((fig_a, stem_a), (fig_b, stem_b)):
        fig.set_size_inches(w_in, h_in)
        save_figure(fig, FIG12 / stem, language, dpi=300, bbox_inches="tight", pad_inches=0)
        if plt.fignum_exists(fig.number):
            plt.close(fig)


def main() -> None:
    setup_rc(10)
    for language in ("zh", "en"):
        pasted = draw_pasted(language)
        rebuilt = draw_rebuilt(language)
        save_book_pair(
            pasted,
            rebuilt,
            language,
            "ch12-05a-pasted",
            "ch12-05b-rebuilt",
        )
    print(f"Print width target: {PRINT_W_MM} mm")


if __name__ == "__main__":
    main()
