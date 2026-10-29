#!/usr/bin/env python3
"""Chapter 4 data figures: paper Fig. 2–4 (good and bad styles)."""
# SPDX-License-Identifier: MIT
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import gridspec

from ch04_data import load_gcb, load_hot, load_mlo, load_ohc_pair
from ch04_style import (
    ATM_CARBON,
    BAD_BLUE,
    BAD_GREEN,
    BAD_OHC_GREEN,
    BAD_OHC_RED,
    BAD_RED,
    EMISSIONS,
    HEAT,
    LAND_CARBON,
    LW_ANNUAL,
    LW_RAW,
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

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures" / "ch04"


def _font(language: str):
    return chinese_font() if language == "zh" else None


def _save_bad_png(fig, stem: Path) -> None:
    stem.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(stem.with_suffix(".png"), dpi=150, facecolor="white")
    plt.close(fig)


def plot_fig2(style: str, language: str) -> None:
    mlo = load_mlo()
    hot = load_hot()
    labels = {
        "zh": {
            "co2": "大气 CO₂（ppm）",
            "pco2": "海水 pCO₂（µatm）",
            "ph": "海水 pH",
            "year": "年份",
            "monthly": "月均值",
            "deseas": "去季节",
            "mk": "Maunakea",
            "titles": ["大气 CO₂", "海水 pCO₂", "海水 pH"],
        },
        "en": {
            "co2": "Atmospheric CO₂ (ppm)",
            "pco2": "Seawater pCO₂ (µatm)",
            "ph": "Seawater pH",
            "year": "Year",
            "monthly": "Monthly mean",
            "deseas": "Deseasonalized",
            "mk": "Maunakea",
            "titles": ["Atmospheric CO₂", "Seawater pCO₂", "Seawater pH"],
        },
    }[language]
    font = _font(language)

    if style == "good":
        apply_good_rcparams()
        fig, axes = plt.subplots(1, 3, figsize=(174 * MM_TO_IN, 60 * MM_TO_IN))
        fig.subplots_adjust(left=0.06, right=0.98, top=0.88, bottom=0.22, wspace=0.38)
        ax_a, ax_b, ax_c = axes
        ax_a.plot(
            mlo["decimal_date"],
            mlo["average"],
            color=tint(ATM_CARBON, 0.5),
            linewidth=LW_RAW,
        )
        ax_a.plot(
            mlo["decimal_date"],
            mlo["deseasonalized"],
            color=ATM_CARBON,
            linewidth=LW_TREND,
        )
        ax_a.axvline(2022 + 11 / 12, color=NEUTRAL_DARK, linewidth=LW_REF, linestyle="--")
        ax_a.set_xlim(1958, 2026)
        ax_a.set_ylabel(labels["co2"], fontproperties=font)
        y0, y1 = ax_a.get_ylim()
        ax_a.text(2022.95, y0 + 0.06 * (y1 - y0), labels["mk"], fontsize=6, color=NEUTRAL_DARK, fontproperties=font)
        ax_a.text(
            mlo["decimal_date"].iloc[-1] + 0.2,
            mlo["deseasonalized"].iloc[-1],
            labels["deseas"],
            fontsize=6,
            color=ATM_CARBON,
            fontproperties=font,
        )
        ax_a.text(
            mlo["decimal_date"].iloc[-1] + 0.2,
            mlo["average"].iloc[-1],
            labels["monthly"],
            fontsize=6,
            color=tint(ATM_CARBON, 0.5),
            fontproperties=font,
        )
        ax_b.scatter(hot["date"], hot["pCO2calc_insitu"], s=6.25, color=OCEAN_CARBON, linewidths=0)
        ax_c.scatter(hot["date"], hot["pHcalc_insitu"], s=6.25, color=SEAWATER_PH, linewidths=0)
        ax_b.set_xlim(pd.Timestamp("1988-01-01"), pd.Timestamp("2027-01-01"))
        ax_c.set_xlim(ax_b.get_xlim())
        ax_b.set_ylabel(labels["pco2"], fontproperties=font)
        ax_c.set_ylabel(labels["ph"], fontproperties=font)
        for ax in (ax_b, ax_c):
            ax.set_xlabel(labels["year"], fontproperties=font)
        for ax, letter in zip(axes, "abc"):
            style_axes(ax)
            panel_letter(ax, letter, font)
        save_figure(fig, FIG / f"ch04-05-fig2-carbonate-{language}", language)
    else:
        plt.rcParams.update({"font.family": "DejaVu Serif", "font.size": 11})
        fig, axes = plt.subplots(1, 3, figsize=(174 * MM_TO_IN, 60 * MM_TO_IN))
        ax_a, ax_b, ax_c = axes
        ax_a.plot(mlo["decimal_date"], mlo["average"], color=BAD_RED, linewidth=2)
        ax_a.plot(mlo["decimal_date"], mlo["deseasonalized"], color=BAD_RED, linewidth=2)
        ax_b.plot(hot["date"], hot["pCO2calc_insitu"], "-o", color=BAD_GREEN, markersize=3)
        ax_c.plot(hot["date"], hot["pHcalc_insitu"], "-", color=BAD_BLUE)
        for ax, title, tag in zip(axes, labels["titles"], ["(A)", "(B)", "(C)"]):
            ax.set_title(f"{tag} {title}", fontproperties=font, loc="left")
            ax.grid(True, alpha=0.4)
            ax.legend([title], loc="upper left", fontsize=8)
        _save_bad_png(fig, FIG / f"ch04-05-fig2-carbonate-bad-{language}")


def plot_fig3(style: str, language: str) -> plt.Figure | None:
    o700, o2000 = load_ohc_pair()
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

    if style == "good":
        apply_good_rcparams()
        fig, ax = plt.subplots(figsize=(85 * MM_TO_IN, 60 * MM_TO_IN))
        fig.subplots_adjust(left=0.16, right=0.96, top=0.88, bottom=0.18)
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
            ax.text(years.iloc[-1] + 0.8, series["WO"].iloc[-1], depth, fontsize=6, color=color, fontproperties=font)
        ax.axhline(0, color=NEUTRAL_DARK, linewidth=LW_REF, linestyle="--")
        ax.set_xlim(1955, 2025)
        ax.set_xlabel(labels["year"], fontproperties=font)
        ax.set_ylabel(labels["y"], fontproperties=font)
        style_axes(ax)
        panel_letter(ax, "a", font)
        save_figure(fig, FIG / f"ch04-06-fig3-ohc-{language}", language)
        return None

    plt.rcParams.update({"font.family": "Arial", "font.size": 9, "font.weight": "bold"})
    fig, ax = plt.subplots(figsize=(85 * MM_TO_IN, 60 * MM_TO_IN))
    ax.plot(years, o700["WO"] * 1e22, color=BAD_OHC_RED, linewidth=2)
    ax.plot(years, o2000["WO"] * 1e22, color=BAD_OHC_GREEN, linewidth=2)
    ax.set_title("Ocean Heat Content", fontsize=10, fontweight="bold")
    ax.text(-0.12, 1.05, "a)", transform=ax.transAxes, fontsize=11)
    ax.ticklabel_format(style="sci", axis="y", scilimits=(0, 0))
    _save_bad_png(fig, FIG / f"ch04-06-fig3-ohc-bad-{language}")
    return fig


def plot_fig4(style: str, language: str) -> None:
    gcb = load_gcb()
    years = gcb["Year"]
    labels = {
        "zh": {
            "flux": "碳通量（GtC yr⁻¹）",
            "pct": "海洋碳汇占总排放（%）",
            "year": "年份",
            "total": "总排放",
            "atm": "大气增长",
            "ocean": "海洋碳汇",
            "land": "陆地碳汇",
            "calc": "作者计算",
        },
        "en": {
            "flux": "Carbon flux (GtC yr⁻¹)",
            "pct": "Ocean sink share of emissions (%)",
            "year": "Year",
            "total": "Total emissions",
            "atm": "Atmospheric growth",
            "ocean": "Ocean sink",
            "land": "Land sink",
            "calc": "Calculated by the author",
        },
    }[language]
    font = _font(language)

    if style == "good":
        apply_good_rcparams()
        fig = plt.figure(figsize=(174 * MM_TO_IN, 65 * MM_TO_IN))
        gs = gridspec.GridSpec(1, 2, width_ratios=[3, 2], wspace=0.28)
        ax_a = fig.add_subplot(gs[0, 0])
        ax_b = fig.add_subplot(gs[0, 1])
        fig.subplots_adjust(left=0.07, right=0.98, top=0.88, bottom=0.2)
        ax_a.plot(years, gcb["total_emissions"], color=EMISSIONS, linewidth=LW_ANNUAL)
        ax_a.plot(years, gcb["atmospheric growth"], color=ATM_CARBON, linewidth=LW_ANNUAL)
        ax_a.plot(years, gcb["ocean sink"], color=OCEAN_CARBON, linewidth=LW_ANNUAL)
        ax_a.fill_between(years, gcb["ocean sink"] - 0.4, gcb["ocean sink"] + 0.4, color=OCEAN_CARBON, alpha=0.2, linewidth=0)
        ax_a.plot(years, gcb["land sink"], color=LAND_CARBON, linewidth=LW_ANNUAL)
        ax_a.fill_between(years, gcb["land sink"] - 0.5, gcb["land sink"] + 0.5, color=LAND_CARBON, alpha=0.2, linewidth=0)
        for text, yval, col in (
            (labels["total"], gcb["total_emissions"].iloc[-1], EMISSIONS),
            (labels["atm"], gcb["atmospheric growth"].iloc[-1], ATM_CARBON),
            (labels["ocean"], gcb["ocean sink"].iloc[-1], OCEAN_CARBON),
            (labels["land"], gcb["land sink"].iloc[-1], LAND_CARBON),
        ):
            ax_a.text(years.iloc[-1] + 0.5, yval, text, fontsize=6, color=col, va="center", fontproperties=font)
        ax_a.set_ylabel(labels["flux"], fontproperties=font)
        ax_a.set_xlabel(labels["year"], fontproperties=font)
        style_axes(ax_a)
        panel_letter(ax_a, "a", font)
        roll = gcb["ocean_share_pct"].rolling(window=10, center=True, min_periods=5).mean()
        ax_b.scatter(years, gcb["ocean_share_pct"], s=12, color=OCEAN_CARBON)
        ax_b.plot(years, roll, color=OCEAN_CARBON, linewidth=LW_TREND)
        ax_b.text(0.98, 0.95, labels["calc"], transform=ax_b.transAxes, ha="right", va="top", fontsize=6, color=NEUTRAL_DARK, fontproperties=font)
        ax_b.set_ylabel(labels["pct"], fontproperties=font)
        ax_b.set_xlabel(labels["year"], fontproperties=font)
        style_axes(ax_b)
        panel_letter(ax_b, "b", font)
        save_figure(fig, FIG / f"ch04-07-fig4-budget-{language}", language)
    else:
        plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8})
        fig, ax = plt.subplots(figsize=(174 * MM_TO_IN, 65 * MM_TO_IN))
        stack = np.vstack([gcb["atmospheric growth"], gcb["ocean sink"], gcb["land sink"]])
        colors = plt.cm.jet(np.linspace(0.2, 0.85, 3))
        ax.stackplot(years, stack, colors=colors)
        ax.plot(years, gcb["total_emissions"], color="black", linewidth=2.5)
        ax.text(-0.08, 1.05, "A", transform=ax.transAxes, fontsize=12, fontweight="bold")
        ax.legend(["Atm", "Ocean", "Land"], loc="center left", bbox_to_anchor=(1.02, 0.5))
        _save_bad_png(fig, FIG / f"ch04-07-fig4-budget-bad-{language}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fig", choices=("2", "3", "4", "all"), default="all")
    parser.add_argument("--style", choices=("good", "bad", "both"), default="both")
    parser.add_argument("--lang", choices=("zh", "en", "both"), default="both")
    args = parser.parse_args()
    langs = ("zh", "en") if args.lang == "both" else (args.lang,)
    styles = ("good", "bad") if args.style == "both" else (args.style,)
    figs = ("2", "3", "4") if args.fig == "all" else (args.fig,)
    for lang in langs:
        for style in styles:
            if "2" in figs:
                plot_fig2(style, lang)
            if "3" in figs:
                plot_fig3(style, lang)
            if "4" in figs:
                plot_fig4(style, lang)


if __name__ == "__main__":
    main()
