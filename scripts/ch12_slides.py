#!/usr/bin/env python3
"""FIG ch12-04: talk slide sequence (4 thumbnails + full-size slide PNGs)."""
# SPDX-License-Identifier: MIT
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from ch12_plot_utils import (  # noqa: E402
    BOOK_INK,
    COLOR_ACCENT,
    COLOR_CONTROL,
    COLOR_MODIFIED,
    COLOR_REF,
    FIG12,
    assert_perovskite_metrics,
    chinese_font,
    format_pce_title,
    format_stability_title,
    load_jv,
    load_metrics,
    load_stability,
    save_figure,
    setup_rc,
)

SLIDE_W_IN = 13.333
SLIDE_H_IN = 7.5
M1 = ROOT / "figures" / "ch09" / "ch09-03-device-structure-base.png"
JV_LIMS = ((0, 1.2), (0, 25))
STAB_LIMS = ((0, 1000), (0, 1.05))


def slide_labels(language: str) -> dict:
    if language == "zh":
        return {
            "s1_title": "只在钙钛矿/空穴层界面加了一层钝化",
            "bul1": "其余各层与对照相同",
            "bul2": "示意，不按比例",
            "control": "对照",
            "modified": "改性",
            "sim": "模拟数据",
            "voc": "V$_{oc}$ (V)",
            "ff": "FF",
            "pce": "PCE (%)",
            "x_v": "电压（V）",
            "y_j": "电流密度（mA cm$^{-2}$）",
            "x_t": "时间（h）",
            "y_pce": "归一化 PCE",
            "t80": "T80 ≈ 210 h",
            "layers": [
                (0.72, 0.88, "Au"),
                (0.72, 0.78, "spiro-OMeTAD"),
                (0.72, 0.68, "钝化层"),
                (0.72, 0.56, "钙钛矿"),
                (0.72, 0.44, "SnO₂"),
                (0.72, 0.36, "FTO"),
                (0.72, 0.22, "玻璃"),
            ],
        }
    return {
        "s1_title": "A passivation layer was added at the perovskite/HTL interface",
        "bul1": "All other layers match the control",
        "bul2": "Schematic, not to scale",
        "control": "Control",
        "modified": "Modified",
        "sim": "Simulated data",
        "voc": "V$_{oc}$ (V)",
        "ff": "FF",
        "pce": "PCE (%)",
        "x_v": "Voltage (V)",
        "y_j": "Current density (mA cm$^{-2}$)",
        "x_t": "Time (h)",
        "y_pce": "Normalized PCE",
        "t80": "T80 ≈ 210 h",
        "layers": [
            (0.72, 0.88, "Au"),
            (0.72, 0.78, "spiro-OMeTAD"),
            (0.72, 0.68, "Passivation"),
            (0.72, 0.56, "Perovskite"),
            (0.72, 0.44, "SnO₂"),
            (0.72, 0.36, "FTO"),
            (0.72, 0.22, "Glass"),
        ],
    }


def draw_slide1(fig, language: str) -> None:
    lab = slide_labels(language)
    font = chinese_font() if language == "zh" else None
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.text(
        0.05, 0.92, lab["s1_title"], fontproperties=font, fontsize=34, color=BOOK_INK,
        ha="left", va="top", wrap=True,
    )
    img_ax = fig.add_axes([0.05, 0.12, 0.45, 0.72])
    img_ax.axis("off")
    if M1.is_file():
        img_ax.imshow(np.array(Image.open(M1)))
    else:
        img_ax.text(0.5, 0.5, "M1 missing", ha="center")
    # Highlight passivation band (approximate region in base art)
    rect = Rectangle((0.08, 0.58), 0.84, 0.08, fill=False, edgecolor=COLOR_ACCENT, linewidth=3)
    img_ax.add_patch(rect)
    for x, y, text in lab["layers"]:
        img_ax.text(
            x, y, text, transform=img_ax.transAxes, fontproperties=font,
            fontsize=20, color=BOOK_INK, ha="left", va="center",
        )
    ax.text(0.55, 0.55, lab["bul1"], fontproperties=font, fontsize=22, ha="left", va="top")
    ax.text(0.55, 0.42, lab["bul2"], fontproperties=font, fontsize=22, ha="left", va="top", color="#6E6E6E")


def style_data_ax(ax, language: str, xlabel: str, ylabel: str) -> None:
    font = chinese_font() if language == "zh" else None
    ax.set_xlabel(xlabel, fontproperties=font, fontsize=24)
    ax.set_ylabel(ylabel, fontproperties=font, fontsize=24)
    ax.tick_params(labelsize=20, width=2, length=6)
    for spine in ax.spines.values():
        spine.set_linewidth(2)
    ax.spines[["top", "right"]].set_visible(False)


def draw_slide2a(fig, language: str, title: str) -> dict:
    font = chinese_font() if language == "zh" else None
    lab = slide_labels(language)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis("off")
    ax.text(0.05, 0.92, title, fontproperties=font, fontsize=34, ha="left", va="top")
    plot_ax = fig.add_axes([0.08, 0.12, 0.78, 0.68])
    jv = load_jv()
    plot_ax.plot(
        jv["control"][0], jv["control"][1],
        color=COLOR_CONTROL, linestyle=(0, (6, 4)), linewidth=3,
    )
    plot_ax.set_xlim(*JV_LIMS[0])
    plot_ax.set_ylim(*JV_LIMS[1])
    style_data_ax(plot_ax, language, lab["x_v"], lab["y_j"])
    plot_ax.text(
        1.15, jv["control"][1][-1], lab["control"],
        fontproperties=font, fontsize=22, color=COLOR_CONTROL, ha="left", va="center",
    )
    plot_ax.text(
        0.98, 0.95, lab["sim"], transform=plot_ax.transAxes,
        fontproperties=font, fontsize=20, ha="right", va="top", color=BOOK_INK,
    )
    return {"xlim": plot_ax.get_xlim(), "ylim": plot_ax.get_ylim()}


def draw_slide2b(fig, language: str, title: str, lims: dict) -> None:
    font = chinese_font() if language == "zh" else None
    lab = slide_labels(language)
    metrics = load_metrics()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis("off")
    ax.text(0.05, 0.92, title, fontproperties=font, fontsize=34, ha="left", va="top")
    plot_ax = fig.add_axes([0.08, 0.12, 0.55, 0.68])
    jv = load_jv()
    plot_ax.plot(
        jv["control"][0], jv["control"][1],
        color=COLOR_CONTROL, linestyle=(0, (6, 4)), linewidth=3,
    )
    plot_ax.plot(jv["modified"][0], jv["modified"][1], color=COLOR_MODIFIED, linewidth=3)
    plot_ax.set_xlim(*lims["xlim"])
    plot_ax.set_ylim(*lims["ylim"])
    style_data_ax(plot_ax, language, lab["x_v"], lab["y_j"])
    plot_ax.text(
        1.15, jv["control"][1][-1], lab["control"],
        fontproperties=font, fontsize=22, color=COLOR_CONTROL, ha="left", va="center",
    )
    plot_ax.text(
        1.15, jv["modified"][1][-1], lab["modified"],
        fontproperties=font, fontsize=22, color=COLOR_MODIFIED, ha="left", va="center",
    )
    plot_ax.text(
        0.98, 0.95, lab["sim"], transform=plot_ax.transAxes,
        fontproperties=font, fontsize=20, ha="right", va="top", color=BOOK_INK,
    )
    table_ax = fig.add_axes([0.68, 0.35, 0.28, 0.35])
    table_ax.axis("off")
    rows = [
        [lab["voc"], f"{float(metrics['control']['Voc']):.2f}", f"{float(metrics['modified']['Voc']):.2f}"],
        [lab["ff"], f"{float(metrics['control']['FF']):.2f}", f"{float(metrics['modified']['FF']):.2f}"],
        [lab["pce"], f"{float(metrics['control']['PCE']):.2f}", f"{float(metrics['modified']['PCE']):.2f}"],
    ]
    col_labels = ["", lab["control"], lab["modified"]]
    table = table_ax.table(
        cellText=rows, colLabels=col_labels, loc="center", cellLoc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(18)
    for key, cell in table.get_celld().items():
        cell.set_linewidth(0.5)


def draw_slide3(fig, language: str, title: str) -> None:
    font = chinese_font() if language == "zh" else None
    lab = slide_labels(language)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis("off")
    ax.text(0.05, 0.92, title, fontproperties=font, fontsize=34, ha="left", va="top")
    plot_ax = fig.add_axes([0.08, 0.12, 0.78, 0.68])
    stab = load_stability()
    plot_ax.plot(
        stab["control"][0], stab["control"][1],
        color=COLOR_CONTROL, linestyle=(0, (6, 4)), linewidth=3,
    )
    plot_ax.plot(stab["modified"][0], stab["modified"][1], color=COLOR_MODIFIED, linewidth=3)
    plot_ax.axhline(0.8, color=COLOR_REF, linestyle=(0, (1, 3)), linewidth=2.5)
    plot_ax.plot([210, 210], [0.75, 0.85], color=COLOR_CONTROL, linewidth=2.5)
    plot_ax.text(225, 0.76, lab["t80"], fontproperties=font, fontsize=20, color=COLOR_CONTROL)
    plot_ax.set_xlim(*STAB_LIMS[0])
    plot_ax.set_ylim(*STAB_LIMS[1])
    style_data_ax(plot_ax, language, lab["x_t"], lab["y_pce"])
    plot_ax.text(
        0.98, 0.95, lab["sim"], transform=plot_ax.transAxes,
        fontproperties=font, fontsize=20, ha="right", va="top", color=BOOK_INK,
    )


def export_slide(fig, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=1920 / SLIDE_W_IN, facecolor="white")
    plt.close(fig)


def thumbnail_from_fig(builder, language: str, page_num: str, *args) -> plt.Figure:
    fig = plt.figure(figsize=(SLIDE_W_IN, SLIDE_H_IN))
    builder(fig, language, *args)
    return fig


def build_composite(language: str, pages: list[tuple]) -> None:
    setup_rc(10)
    fig, axes = plt.subplots(2, 2, figsize=(10.5, 5.9))
    fig.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.02, wspace=0.06, hspace=0.06)
    for ax, (png_path, num) in zip(axes.flat, pages):
        ax.imshow(np.array(Image.open(png_path)))
        ax.axis("off")
        ax.add_patch(Rectangle((0, 0), 1, 1, transform=ax.transAxes, fill=False, edgecolor="#C8D6D6", linewidth=1.5))
        ax.text(0.96, 0.04, num, transform=ax.transAxes, ha="right", va="bottom", fontsize=10, color="#6E6E6E")
    save_figure(fig, FIG12 / "ch12-04-slide-sequence", language, dpi=300, bbox_inches="tight", pad_inches=0.02)


def main() -> None:
    info = assert_perovskite_metrics()
    slide_dir = FIG12 / "slides"
    lims_store = {}
    for language in ("zh", "en"):
        setup_rc(10)
        title2 = format_pce_title(language, info["metrics"])
        title3 = format_stability_title(
            language, info["control_retention_1000h"], info["modified_retention_1000h"],
        )
        fig1 = plt.figure(figsize=(SLIDE_W_IN, SLIDE_H_IN))
        draw_slide1(fig1, language)
        p1 = slide_dir / f"slide-1-{language}.png"
        export_slide(fig1, p1)

        fig2a = plt.figure(figsize=(SLIDE_W_IN, SLIDE_H_IN))
        lims = draw_slide2a(fig2a, language, title2)
        lims_store[language] = lims
        p2a = slide_dir / f"slide-2a-{language}.png"
        export_slide(fig2a, p2a)

        fig2b = plt.figure(figsize=(SLIDE_W_IN, SLIDE_H_IN))
        draw_slide2b(fig2b, language, title2, lims)
        p2b = slide_dir / f"slide-2b-{language}.png"
        export_slide(fig2b, p2b)

        fig3 = plt.figure(figsize=(SLIDE_W_IN, SLIDE_H_IN))
        draw_slide3(fig3, language, title3)
        p3 = slide_dir / f"slide-3-{language}.png"
        export_slide(fig3, p3)

        assert lims["xlim"] == JV_LIMS[0] and lims["ylim"] == JV_LIMS[1]
        build_composite(
            language,
            [(p1, "1"), (p2a, "2a"), (p2b, "2b"), (p3, "3")],
        )
    print(json.dumps({"slide_limits": lims_store}))


if __name__ == "__main__":
    main()
