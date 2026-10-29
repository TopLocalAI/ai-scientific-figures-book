#!/usr/bin/env python3
"""FIG ch04-02: one-page visual specification."""
# SPDX-License-Identifier: MIT
from __future__ import annotations

import argparse
from pathlib import Path

import colorspacious as cs
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, PathPatch
from matplotlib.path import Path as MPath

from ch04_style import (
    ATM_CARBON,
    EMISSIONS,
    HEAT,
    LAND_CARBON,
    MM_TO_IN,
    NEUTRAL_DARK,
    NEUTRAL_MID,
    NEUTRAL_PALE,
    OCEAN_CARBON,
    PT_AXIS,
    PT_PANEL,
    PT_TICK,
    SEAWATER_PH,
    WATER_TRANSPORT,
    apply_good_rcparams,
    chinese_font,
    save_figure,
    tint,
)

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures" / "ch04"

SWATCHES = [
    (ATM_CARBON, "zh", "大气碳", "en", "Atmospheric CO₂"),
    (OCEAN_CARBON, "zh", "海洋碳", "en", "Ocean carbon"),
    (LAND_CARBON, "zh", "陆地碳", "en", "Land carbon"),
    (HEAT, "zh", "热", "en", "Heat"),
    (SEAWATER_PH, "zh", "海水 pH", "en", "Seawater pH"),
    (EMISSIONS, "zh", "人为排放", "en", "Emissions"),
    (WATER_TRANSPORT, "zh", "水体输运", "en", "Water transport"),
    (NEUTRAL_MID, "zh", "中性灰", "en", "Neutral"),
]


def rgb_hex(hex_color: str) -> np.ndarray:
    return np.array(mcolors.to_rgb(hex_color))


def min_delta_e(colors: list[str]) -> float:
    rgbs = [rgb_hex(c) for c in colors]
    best = 999.0
    for i in range(len(rgbs)):
        for j in range(i + 1, len(rgbs)):
            d = cs.deltaE(rgbs[i], rgbs[j], input_space="sRGB1", uniform_space="CAM02-UCS")
            best = min(best, d)
    return round(float(best), 1)


def simulate_row(colors: list[str], mode: str) -> list[str]:
    out = []
    for hex_color in colors:
        rgb = rgb_hex(hex_color)
        if mode == "orig":
            out.append(hex_color)
        elif mode == "gray":
            lab = cs.cspace_convert(rgb, "sRGB1", "CIELab")
            gray = lab[0] / 100.0
            out.append(mcolors.to_hex((gray, gray, gray)))
        else:
            sim = np.clip(
                cs.cspace_convert(
                    rgb,
                    {"name": "sRGB1+CVD", "cvd_type": mode, "severity": 100},
                    "sRGB1",
                ),
                0,
                1,
            )
            out.append(mcolors.to_hex(sim))
    return out


def draw_spec(language: str) -> None:
    font = chinese_font() if language == "zh" else None
    titles = {
        "zh": {
            "sem": "语义色",
            "cvd": "色觉模拟：原色 / 第二色盲 / 第一色盲 / 第三色盲 / 灰度",
            "type": "文字层级",
            "lines": "线型",
            "arrows": "示意箭头",
            "icons": "图标",
            "axes": "坐标轴与标注",
            "de": "最小 ΔE（相邻语义色）",
        },
        "en": {
            "sem": "Semantic colours",
            "cvd": "Simulated colour vision: original / deuteranomaly / protanomaly / tritanomaly / grayscale",
            "type": "Type hierarchy",
            "lines": "Line styles",
            "arrows": "Schematic arrows",
            "icons": "Icons",
            "axes": "Axes and labels",
            "de": "Min ΔE (adjacent semantics)",
        },
    }[language]
    apply_good_rcparams()
    fig = plt.figure(figsize=(174 * MM_TO_IN, 230 * MM_TO_IN))
    fig.subplots_adjust(left=0.06, right=0.96, top=0.96, bottom=0.04, hspace=0.55)
    colors = [s[0] for s in SWATCHES]
    pair_colors = [ATM_CARBON, OCEAN_CARBON, LAND_CARBON, EMISSIONS]
    min_de = min_delta_e(pair_colors + [tint(HEAT, 0.55), HEAT])

    ax0 = fig.add_axes([0.06, 0.86, 0.88, 0.1])
    ax0.set_title(titles["sem"], fontproperties=font, fontsize=PT_AXIS, loc="left")
    ax0.set_xlim(0, len(colors))
    ax0.set_ylim(0, 1)
    ax0.axis("off")
    for idx, sw in enumerate(SWATCHES):
        ax0.add_patch(plt.Rectangle((idx, 0.2), 0.9, 0.55, color=sw[0], ec=NEUTRAL_DARK, lw=0.3))
        name = sw[1 if language == "zh" else 3]
        ax0.text(idx + 0.45, 0.05, f"{name}\n{sw[0].replace('#', '')}", ha="center", va="top", fontsize=5, fontproperties=font)

    modes = [("orig", "原色"), ("deuteranomaly", "第二色盲"), ("protanomaly", "第一色盲"), ("tritanomaly", "第三色盲"), ("gray", "灰度")]
    if language == "en":
        modes = [
            ("orig", "Original"),
            ("deuteranomaly", "Deuteranomaly"),
            ("protanomaly", "Protanomaly"),
            ("tritanomaly", "Tritanomaly"),
            ("gray", "Grayscale"),
        ]
    ax1 = fig.add_axes([0.06, 0.68, 0.88, 0.14])
    ax1.set_title(titles["cvd"], fontproperties=font, fontsize=PT_AXIS, loc="left")
    ax1.axis("off")
    for row, (mode, label) in enumerate(modes):
        y = 0.85 - row * 0.18
        ax1.text(0, y, label, fontsize=5, va="center", fontproperties=font)
        row_colors = simulate_row(colors[:6], mode if mode != "orig" else "orig")
        for col, hex_c in enumerate(row_colors[:6]):
            ax1.add_patch(plt.Rectangle((0.12 + col * 0.11, y - 0.05), 0.1, 0.08, color=hex_c, ec="#ccc", lw=0.2))
        ax1.text(0.82, y, f"{titles['de']} {min_de}", fontsize=5, va="center", fontproperties=font)

    ax2 = fig.add_axes([0.06, 0.56, 0.88, 0.08])
    ax2.set_title(titles["type"], fontproperties=font, fontsize=PT_AXIS, loc="left")
    ax2.axis("off")
    samples = [
        (PT_PANEL, "bold", "a", "面板字母 / Panel"),
        (PT_AXIS, "normal", "大气 CO₂（ppm）", "轴标签 / Axis"),
        (PT_TICK, "normal", "2020", "刻度 / Tick"),
        (PT_TICK, "normal", "0–700 m", "注释 / Note"),
    ]
    for i, (size, weight, text, role) in enumerate(samples):
        ax2.text(0.02 + i * 0.24, 0.55, text, fontsize=size, fontweight=weight, fontproperties=font)
        ax2.text(0.02 + i * 0.24, 0.15, role, fontsize=5, fontproperties=font)

    ax3 = fig.add_axes([0.06, 0.42, 0.88, 0.1])
    ax3.set_title(titles["lines"], fontproperties=font, fontsize=PT_AXIS, loc="left")
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)
    ax3.axis("off")
    x = 0.02
    for lw, col, alpha, label in [
        (0.5, tint(ATM_CARBON, 0.5), 1, "月值 / Monthly"),
        (1.2, ATM_CARBON, 1, "趋势 / Trend"),
        (1.0, EMISSIONS, 1, "年值 / Annual"),
        (0.5, NEUTRAL_DARK, 1, "参考 / Ref"),
    ]:
        ax3.plot([x, x + 0.12], [0.6, 0.6], color=col, linewidth=lw, alpha=alpha, linestyle="--" if "Ref" in label or "参考" in label else "-")
        ax3.text(x + 0.06, 0.35, label, ha="center", fontsize=5, fontproperties=font)
        x += 0.22

    ax4 = fig.add_axes([0.06, 0.26, 0.88, 0.12])
    ax4.set_title(titles["arrows"], fontproperties=font, fontsize=PT_AXIS, loc="left")
    ax4.set_xlim(0, 1)
    ax4.set_ylim(0, 1)
    ax4.axis("off")
    ax4.add_patch(FancyArrowPatch((0.05, 0.6), (0.18, 0.6), arrowstyle="-|>", mutation_scale=8, color=EMISSIONS, linewidth=1))
    ax4.text(0.115, 0.35, "碳通量 / C", ha="center", fontsize=5, fontproperties=font)
    wave_x = np.linspace(0.28, 0.42, 40)
    wave_y = 0.6 + 0.03 * np.sin(wave_x * 40)
    ax4.plot(wave_x, wave_y, color=HEAT, linewidth=1)
    ax4.text(0.35, 0.35, "热通量 / Heat", ha="center", fontsize=5, fontproperties=font)
    ax4.add_patch(plt.Rectangle((0.5, 0.52), 0.14, 0.12, color=WATER_TRANSPORT, alpha=0.35, ec="none"))
    ax4.text(0.57, 0.35, "水体输运 / Water", ha="center", fontsize=5, fontproperties=font)

    ax5 = fig.add_axes([0.06, 0.12, 0.4, 0.1])
    ax5.set_title(titles["icons"], fontproperties=font, fontsize=PT_AXIS, loc="left")
    ax5.axis("off")
    ax5.plot([0.05, 0.25], [0.6, 0.6], color=NEUTRAL_DARK, lw=0.75)
    ax5.add_patch(plt.Circle((0.35, 0.6), 0.04, fc=NEUTRAL_PALE, ec=NEUTRAL_DARK, lw=0.75))
    ax5.plot([0.5, 0.52], [0.45, 0.75], color=NEUTRAL_DARK, lw=0.75)

    ax6 = fig.add_axes([0.5, 0.1, 0.44, 0.12])
    ax6.set_title(titles["axes"], fontproperties=font, fontsize=PT_AXIS, loc="left")
    ax6.plot([0.1, 0.9], [0.35, 0.75], color=OCEAN_CARBON, lw=1.2, transform=ax6.transAxes)
    ax6.plot([0.1, 0.9], [0.1, 0.1], color=NEUTRAL_DARK, lw=0.6, transform=ax6.transAxes)
    ax6.plot([0.1, 0.1], [0.1, 0.85], color=NEUTRAL_DARK, lw=0.6, transform=ax6.transAxes)
    ax6.text(0.02, 0.95, "a", fontsize=PT_PANEL, fontweight="bold", transform=ax6.transAxes)
    ax6.text(0.45, 0.02, "Year" if language == "en" else "年份", fontsize=PT_AXIS, transform=ax6.transAxes, fontproperties=font)
    ax6.axis("off")

    save_figure(fig, FIG / f"ch04-02-spec-page-{language}", language)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lang", choices=("zh", "en", "both"), default="both")
    args = parser.parse_args()
    langs = ("zh", "en") if args.lang == "both" else (args.lang,)
    for lang in langs:
        draw_spec(lang)


if __name__ == "__main__":
    main()
