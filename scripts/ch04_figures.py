#!/usr/bin/env python3
"""Generate all chapter 4 python figures and provenance."""
# SPDX-License-Identifier: MIT
from __future__ import annotations

import json
import os
import subprocess
import sys
from datetime import date
from pathlib import Path

import colorspacious as cs
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures" / "ch04"
PROV = ROOT / "provenance" / "ch04"
SCRIPTS = ROOT / "scripts"

sys.path.insert(0, str(SCRIPTS))

from ch04_data import data_check_summary, load_ohc_pair  # noqa: E402
from ch04_ocean_figures import plot_fig3  # noqa: E402
from ch04_style import (  # noqa: E402
    ATM_CARBON,
    EMISSIONS,
    HEAT,
    LAND_CARBON,
    LW_REF,
    LW_TREND,
    MM_TO_IN,
    NEUTRAL_DARK,
    OCEAN_CARBON,
    SEAWATER_PH,
    apply_good_rcparams,
    chinese_font,
    panel_letter,
    save_figure,
    style_axes,
    tint,
)


def run_module(name: str, *args: str) -> None:
    env = {**os.environ, "PYTHONPATH": str(SCRIPTS)}
    subprocess.run(
        [sys.executable, str(SCRIPTS / name), *args],
        check=True,
        cwd=ROOT,
        timeout=600,
        env=env,
    )


def simulate_deuteranomaly(fig) -> np.ndarray:
    fig.canvas.draw()
    buf = np.asarray(fig.canvas.buffer_rgba())
    rgb = buf[:, :, :3].astype(np.float64) / 255.0
    flat = rgb.reshape(-1, 3)
    sim = cs.cspace_convert(
        flat,
        {"name": "sRGB1+CVD", "cvd_type": "deuteranomaly", "severity": 100},
        "sRGB1",
    )
    return np.clip(sim.reshape(rgb.shape), 0, 1)


def _ohc_axes(ax, o700, o2000, style: str, language: str) -> None:
    from ch04_ocean_figures import BAD_OHC_GREEN, BAD_OHC_RED, _font

    labels = {
        "zh": {"y": "海洋热含量距平（10²² J）", "year": "年份", "d700": "0–700 m", "d2000": "0–2000 m"},
        "en": {
            "y": "Ocean heat content anomaly (10²² J)",
            "year": "Year",
            "d700": "0–700 m",
            "d2000": "0–2000 m",
        },
    }[language]
    font = _font(language)
    years = o700["YEAR"]
    if style == "bad":
        ax.plot(years, o700["WO"], color=BAD_OHC_RED, linewidth=2)
        ax.plot(years, o2000["WO"], color=BAD_OHC_GREEN, linewidth=2)
        ax.legend(["0–700 m", "0–2000 m"], fontsize=6, loc="upper left")
    else:
        for series, depth, light in ((o2000, labels["d2000"], False), (o700, labels["d700"], True)):
            color = tint(HEAT, 0.55 if light else 1.0)
            ax.fill_between(
                years,
                series["WO"] - series["WOse"],
                series["WO"] + series["WOse"],
                color=color,
                alpha=0.2,
                linewidth=0,
            )
            ax.plot(years, series["WO"], color=color, linewidth=LW_TREND)
            ax.text(years.iloc[-1] + 0.5, series["WO"].iloc[-1], depth, fontsize=6, color=color, fontproperties=font)
        ax.axhline(0, color=NEUTRAL_DARK, linewidth=LW_REF, linestyle="--")
    ax.set_xlim(1955, 2025)
    ax.set_xlabel(labels["year"], fontproperties=font)
    ax.set_ylabel(labels["y"], fontproperties=font)
    style_axes(ax)


def render_cvd_check(language: str) -> None:
    o700, o2000 = load_ohc_pair()
    font = chinese_font() if language == "zh" else None
    row_titles = {
        "zh": ("不一致版", "规范版"),
        "en": ("Inconsistent", "Following the spec"),
    }[language]
    col_titles = {
        "zh": ("原色", "第二色盲模拟"),
        "en": ("Original", "Simulated deuteranomaly"),
    }[language]

    def single_panel(style: str) -> tuple[np.ndarray, np.ndarray]:
        apply_good_rcparams()
        fig, ax = plt.subplots(figsize=(85 * MM_TO_IN, 60 * MM_TO_IN))
        fig.subplots_adjust(left=0.16, right=0.96, top=0.88, bottom=0.18)
        _ohc_axes(ax, o700, o2000, style, language)
        fig.canvas.draw()
        buf = np.asarray(fig.canvas.buffer_rgba())[:, :, :3] / 255.0
        sim = simulate_deuteranomaly(fig)
        plt.close(fig)
        return buf, sim

    panels = [single_panel("bad"), single_panel("good")]
    fig, axes = plt.subplots(2, 2, figsize=(174 * MM_TO_IN, 110 * MM_TO_IN))
    fig.subplots_adjust(left=0.08, right=0.98, top=0.9, bottom=0.08, hspace=0.08, wspace=0.06)
    for row, (orig, sim) in enumerate(panels):
        axes[row, 0].imshow(orig)
        axes[row, 1].imshow(sim)
        for col in range(2):
            axes[row, col].axis("off")
        fig.text(0.03, 0.72 - row * 0.46, row_titles[row], rotation=90, va="center", fontproperties=font, fontsize=7)
    fig.text(0.28, 0.94, col_titles[0], ha="center", fontproperties=font, fontsize=7)
    fig.text(0.72, 0.94, col_titles[1], ha="center", fontproperties=font, fontsize=7)
    save_figure(fig, FIG / f"ch04-03-cvd-check-{language}", language)


def placeholder_schematic(kind: str, path: Path) -> Path:
    if path.is_file():
        return path
    path.parent.mkdir(parents=True, exist_ok=True)
    img = Image.new("RGB", (1600, 900), (240, 245, 250))
    draw = ImageDraw.Draw(img)
    draw.text((40, 40), f"{kind} (codex-image pending)", fill=(60, 60, 60))
    img.save(path)
    return path


def load_panel(path: Path, size: tuple[int, int]) -> Image.Image:
    path = placeholder_schematic(path.stem, path)
    img = Image.open(path).convert("RGB")
    img.thumbnail(size, Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", size, (255, 255, 255))
    ox = (size[0] - img.width) // 2
    oy = (size[1] - img.height) // 2
    canvas.paste(img, (ox, oy))
    return canvas


def contact_sheet(style: str, language: str) -> None:
    font = chinese_font() if language == "zh" else None
    w_mm, h_mm = 174, 150
    fig = plt.figure(figsize=(w_mm * MM_TO_IN, h_mm * MM_TO_IN))
    gs = fig.add_gridspec(2, 2, hspace=0.08, wspace=0.06, left=0.04, right=0.96, top=0.92, bottom=0.12 if style == "good" else 0.06)
    panel_size = (820, 460)
    paths = {
        "schematic": FIG / ("ch04-04a-schematic-bad.png" if style == "bad" else "ch04-04b-schematic-base.png"),
        "fig2": FIG / f"ch04-05-fig2-carbonate-{'bad-' if style == 'bad' else ''}{language}.png",
        "fig3": FIG / f"ch04-06-fig3-ohc-{'bad-' if style == 'bad' else ''}{language}.png",
        "fig4": FIG / f"ch04-07-fig4-budget-{'bad-' if style == 'bad' else ''}{language}.png",
    }
    labels = ["Fig. 1", "Fig. 2", "Fig. 3", "Fig. 4"]
    for idx, key in enumerate(("schematic", "fig2", "fig3", "fig4")):
        ax = fig.add_subplot(gs[idx // 2, idx % 2])
        img = load_panel(paths[key], panel_size)
        ax.imshow(np.asarray(img))
        ax.axis("off")
        ax.text(0.02, 0.98, labels[idx], transform=ax.transAxes, fontsize=7, color=NEUTRAL_DARK, va="top")
    if style == "bad":
        markers = [(0.22, 0.78, "①"), (0.08, 0.55, "②"), (0.72, 0.78, "③"), (0.75, 0.28, "④"), (0.52, 0.05, "⑤"), (0.18, 0.92, "⑥")]
        for ax, _ in zip(fig.axes[:4], range(4)):
            for x, y, t in markers:
                ax.text(x, y, t, transform=ax.transAxes, fontsize=8, ha="center", va="center", bbox=dict(boxstyle="circle", edgecolor="black", facecolor="white", lw=0.5))
    else:
        swatch_labels = {
            "zh": ["大气碳", "海洋碳", "陆地碳", "热", "海水 pH", "人为排放"],
            "en": ["Atmospheric carbon", "Ocean carbon", "Land carbon", "Heat", "Seawater pH", "Emissions"],
        }[language]
        colors = [ATM_CARBON, OCEAN_CARBON, LAND_CARBON, HEAT, SEAWATER_PH, EMISSIONS]
        ax_bar = fig.add_axes([0.06, 0.02, 0.88, 0.06])
        ax_bar.set_xlim(0, len(colors))
        ax_bar.set_ylim(0, 1)
        ax_bar.axis("off")
        for i, (c, lab) in enumerate(zip(colors, swatch_labels)):
            ax_bar.add_patch(plt.Rectangle((i, 0.35), 0.92, 0.45, color=c))
            ax_bar.text(i + 0.46, 0.08, lab, ha="center", fontsize=5, fontproperties=font)
    name = "ch04-01-inconsistent-set" if style == "bad" else "ch04-08-consistent-set"
    save_figure(fig, FIG / f"{name}-{language}", language)


def main() -> None:
    PROV.mkdir(parents=True, exist_ok=True)
    FIG.mkdir(parents=True, exist_ok=True)
    run_module("fetch_ch04_data.py")
    run_module("ch04_ocean_figures.py")
    run_module("ch04_spec_page.py")
    for lang in ("zh", "en"):
        render_cvd_check(lang)
        contact_sheet("bad", lang)
        contact_sheet("good", lang)
    codex = []
    for name in ("ch04-04a-schematic-bad.png", "ch04-04b-schematic-base.png"):
        if not (FIG / name).is_file():
            codex.append(name)
    summary = {
        "chapter": "04",
        "generated_on": date.today().isoformat(),
        "datasets": data_check_summary(),
        "figures_python": [
            "ch04-01-inconsistent-set",
            "ch04-02-spec-page",
            "ch04-03-cvd-check",
            "ch04-05-fig2-carbonate",
            "ch04-06-fig3-ohc",
            "ch04-07-fig4-budget",
            "ch04-08-consistent-set",
        ],
        "codex_pending": codex,
        "reuse_figures_in_plan": 0,
        "sourced_figures_in_plan": 0,
    }
    (PROV / "data-check.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
