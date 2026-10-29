#!/usr/bin/env python3
"""Chapter 5 CO₂ figures: ch05-04, 06, 07."""
# SPDX-License-Identifier: MIT
import re
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from ch05_utils import DATA, chinese_font, save_pair, setup_rc, style_spines

CO2_SNAPSHOT = DATA / "noaa-co2-mm-mlo-2026-10-09.csv"
EXPECTED_SHA = "d895fb5b4a59fb5e4cd98e69b7667fe5bef595c6581f630852b12cb41c07f675"


def load_co2() -> tuple[pd.DataFrame, dict]:
    from ch05_utils import sha256

    assert CO2_SNAPSHOT.is_file()
    assert sha256(CO2_SNAPSHOT) == EXPECTED_SHA
    header = CO2_SNAPSHOT.read_text(encoding="utf-8").splitlines()
    creation = next(l for l in header if "File Creation" in l)
    df = pd.read_csv(CO2_SNAPSHOT, comment="#")
    assert len(df) == 823
    first = df.iloc[0]
    assert int(first["year"]) == 1958 and int(first["month"]) == 3
    assert abs(first["average"] - 315.71) < 0.01
    assert abs(df["average"].min() - 312.42) < 0.01
    assert abs(df["average"].max() - 432.34) < 0.01
    meta = {
        "rows": len(df),
        "file_creation": creation.strip(),
        "first_month_average": float(first["average"]),
        "average_min": float(df["average"].min()),
        "average_max": float(df["average"].max()),
        "last_row": df.iloc[-1][["year", "month", "average"]].to_dict(),
    }
    return df, meta


def annual_series(df: pd.DataFrame) -> tuple[dict[int, float], dict[int, float]]:
    years = sorted(df["year"].unique())
    annual_mean: dict[int, float] = {}
    for y in years:
        sub = df.loc[df["year"] == y]
        if len(sub) == 12:
            annual_mean[y] = float(sub["average"].mean())
    growth: dict[int, float] = {}
    for y in range(1960, 2026):
        growth[y] = annual_mean[y] - annual_mean[y - 1]
    assert len(growth) == 66
    assert abs(min(growth.values()) - 0.42) < 0.02
    assert abs(max(growth.values()) - 3.52) < 0.02
    assert abs(growth[1960] - 0.93) < 0.02
    assert abs(growth[2025] - 2.74) < 0.02
    return annual_mean, growth


def _decimal_year(row) -> float:
    return float(row["decimal date"])


def _co2_ylabel(language: str) -> str:
    if language == "zh":
        return r"$\mathrm{CO_2}$ 摩尔分数（ppm）"
    return r"$\mathrm{CO_2}$ mole fraction (ppm)"


def fig_co2_series(language: str, df: pd.DataFrame) -> None:
    font = chinese_font() if language == "zh" else None
    fig, (ax_a, ax_b) = plt.subplots(2, 1, figsize=(5.2, 3.6), height_ratios=[2, 1])
    fig.subplots_adjust(left=0.16, right=0.97, top=0.95, bottom=0.12, hspace=0.32)
    x = df["decimal date"].values
    ax_a.plot(x, df["average"], color="#7FA7C9", linewidth=0.6, label="月均值" if language == "zh" else "Monthly mean")
    ax_a.plot(
        x,
        df["deseasonalized"],
        color="#1F4E79",
        linewidth=1.2,
        label="去季节趋势" if language == "zh" else "Deseasonalized",
    )
    interp = df[(df["year"] == 1975) & (df["month"] == 12)]
    if len(interp) == 1 and interp.iloc[0]["ndays"] < 0:
        row = interp.iloc[0]
        ax_a.scatter(
            row["decimal date"],
            row["average"],
            facecolors="none",
            edgecolors="#333",
            s=20,
            label="插补月" if language == "zh" else "Interpolated month",
        )
    mk_start = df[(df["year"] == 2022) & (df["month"] == 12)].iloc[0]["decimal date"]
    mk_end = df[(df["year"] == 2023) & (df["month"] == 7)].iloc[0]["decimal date"]
    ax_a.axvspan(
        mk_start,
        mk_end,
        color="#999999",
        alpha=0.25,
        label="测量临时在 Maunakea" if language == "zh" else "Measured at Maunakea",
    )
    ax_a.set_ylim(310, 440)
    ax_a.set_xlim(df["decimal date"].min(), df["decimal date"].max())
    ax_a.set_xticks([1960, 1980, 2000, 2020])
    ylabel = _co2_ylabel(language)
    ax_a.set_ylabel(ylabel, fontproperties=font)
    ax_a.legend(loc="upper left", frameon=False, prop=font, fontsize=6)
    style_spines(ax_a)

    win = df[(df["year"] >= 2021) & (df["year"] <= 2025)]
    ax_b.plot(win["decimal date"], win["average"], color="#1F4E79", linewidth=0.8)
    ax_b.scatter(win["decimal date"], win["average"], s=8, color="#1F4E79")
    ax_b.axvspan(mk_start, mk_end, color="#999999", alpha=0.25)
    ax_a.add_patch(
        plt.Rectangle(
            (win["decimal date"].min(), 310),
            win["decimal date"].max() - win["decimal date"].min(),
            130,
            fill=False,
            edgecolor="#666666",
            linewidth=0.8,
            linestyle="--",
        )
    )
    ax_b.set_xticks([2021, 2022, 2023, 2024, 2025, 2026])
    ax_b.set_xlabel("年份" if language == "zh" else "Year", fontproperties=font)
    ax_b.set_ylabel(ylabel, fontproperties=font)
    style_spines(ax_b)

    save_pair(fig, "ch05-04-co2-series", language)
    plt.close(fig)


def fig_dual_axis(language: str, annual_mean: dict, growth: dict) -> None:
    font = chinese_font() if language == "zh" else None
    years = sorted(y for y in annual_mean if 1959 <= y <= 2025)
    conc = [annual_mean[y] for y in years]
    growth_years = sorted(growth)
    growth_vals = [growth[y] for y in growth_years]
    mean_g = float(np.mean(growth_vals))
    ylab1 = r"年均 $\mathrm{CO_2}$（ppm）" if language == "zh" else r"Annual mean $\mathrm{CO_2}$ (ppm)"
    ylab2 = r"年增长量（ppm/年）" if language == "zh" else r"Annual increase (ppm yr$^{-1}$)"
    badge = "X  误导示例" if language == "zh" else "X  Misleading"
    badge_ok = "OK  修改后" if language == "zh" else "OK  Revised"

    fig_bad, ax = plt.subplots(figsize=(5.2, 2.15))
    fig_bad.subplots_adjust(left=0.10, right=0.90, top=0.84, bottom=0.16)
    ax.plot(years, conc, color="#1F77B4", linewidth=1.2)
    ax.set_ylim(300, 700)
    ax.set_yticks([300, 400, 500, 600, 700])
    ax2 = ax.twinx()
    ax2.plot(growth_years, growth_vals, color="#FF7F0E", linewidth=1.2)
    ax2.set_ylim(0, 3.6)
    ax2.set_yticks([0, 1, 2, 3])
    ax.set_title(badge, loc="left", color="#D62728", fontsize=9, fontweight="bold", pad=3)
    save_pair(fig_bad, "ch05-06-dual-axis-bad", language)
    plt.close(fig_bad)

    fig_good, (g1, g2) = plt.subplots(2, 1, figsize=(5.2, 3.15), sharex=True)
    fig_good.subplots_adjust(hspace=0.28, left=0.18, right=0.97, top=0.90, bottom=0.14)
    g1.plot(years, conc, color="#1F4E79", linewidth=1.0)
    g1.set_ylim(310, 440)
    g1.set_yticks([320, 360, 400, 430])
    g1.set_ylabel(ylab1, fontproperties=font)
    g1.set_title(badge_ok, loc="left", color="#2E7D32", fontsize=9, fontweight="bold", pad=3)
    style_spines(g1)
    g2.bar(growth_years, growth_vals, width=0.8, color="#7FA7C9")
    g2.axhline(mean_g, color="#BBBBBB", linewidth=0.8)
    g2.set_ylim(0, 4.0)
    g2.set_yticks([0, 1, 2, 3])
    g2.set_ylabel(ylab2, fontproperties=font)
    g2.set_xticks([1960, 1980, 2000, 2020])
    g2.set_xlabel("年份" if language == "zh" else "Year", fontproperties=font)
    fig_good.subplots_adjust(right=0.96)
    style_spines(g2)
    save_pair(fig_good, "ch05-06-dual-axis-good", language)
    plt.close(fig_good)


def _greyscale_strip(cmap_name: str, width: int = 256) -> tuple[np.ndarray, np.ndarray]:
    from matplotlib import cm

    cmap = cm.get_cmap(cmap_name)
    t = np.linspace(0, 1, width)
    rgb = cmap(t)[:, :3]
    rgb_strip = rgb.reshape(1, width, 3)
    grey = np.dot(rgb, [0.299, 0.587, 0.114])
    grey_strip = np.stack([grey, grey, grey], axis=-1).reshape(1, width, 3)
    return rgb_strip, grey_strip


def fig_colormap(language: str, df: pd.DataFrame) -> None:
    font = chinese_font() if language == "zh" else None
    sub = df[(df["year"] >= 1959) & (df["year"] <= 2025)].copy()
    matrix = sub.pivot(index="year", columns="month", values="average")
    assert matrix.shape == (67, 12)
    vmin, vmax = float(matrix.values.min()), float(matrix.values.max())

    for stem, cmap, badge in (
        ("ch05-07-colormap-bad", "jet", ("X  彩虹色图", "X  Rainbow (jet)")),
        ("ch05-07-colormap-good", "viridis", ("OK  感知均匀", "OK  Uniform")),
    ):
        fig = plt.figure(figsize=(3.6, 3.85))
        gs = fig.add_gridspec(
            3,
            2,
            width_ratios=[12, 1.3],
            height_ratios=[11, 1.2, 1.2],
            left=0.20,
            right=0.84,
            top=0.86,
            bottom=0.06,
            hspace=0.62,
            wspace=0.08,
        )
        ax = fig.add_subplot(gs[0, 0])
        cax = fig.add_subplot(gs[0, 1])
        im = ax.imshow(matrix.values, aspect="auto", cmap=cmap, vmin=vmin, vmax=vmax, origin="upper")
        ax.set_yticks(np.arange(0, 67, 10))
        ax.set_yticklabels([str(1959 + i) for i in np.arange(0, 67, 10)], fontsize=6)
        ax.set_xticks(range(12))
        ax.set_xticklabels(range(1, 13), fontsize=6)
        ax.set_ylabel("年份" if language == "zh" else "Year", fontproperties=font, fontsize=7)
        ax.set_xlabel("月份" if language == "zh" else "Month", fontproperties=font, fontsize=7, labelpad=8)
        cbar = fig.colorbar(im, cax=cax)
        cbar.set_ticks([320, 360, 400, 420])
        cbar.set_label(
            r"$\mathrm{CO_2}$（ppm）" if language == "zh" else r"$\mathrm{CO_2}$ (ppm)",
            fontproperties=font,
            fontsize=7,
        )
        bzh, ben = badge
        badge_color = "#D62728" if "bad" in stem else "#2E7D32"
        ax.set_title(
            bzh if language == "zh" else ben,
            loc="left",
            color=badge_color,
            fontsize=8,
            fontweight="bold",
            pad=4,
        )

        rgb_strip, grey_strip = _greyscale_strip(cmap)
        for gi, (img, lab) in enumerate(
            (
                (rgb_strip, "色图" if language == "zh" else "Colormap"),
                (grey_strip, "灰度" if language == "zh" else "Grey"),
            ),
            start=1,
        ):
            axs = fig.add_subplot(gs[gi, 0])
            axs.imshow(img, aspect="auto")
            axs.set_yticks([])
            axs.set_xticks([])
            axs.set_ylabel(lab, fontproperties=font, fontsize=6)
        save_pair(fig, stem, language)
        plt.close(fig)


def run_all() -> dict:
    setup_rc()
    df, meta = load_co2()
    annual_mean, growth = annual_series(df)
    for language in ("zh", "en"):
        fig_co2_series(language, df)
        fig_dual_axis(language, annual_mean, growth)
        fig_colormap(language, df)
    return {
        "co2_meta": meta,
        "growth_min": min(growth.values()),
        "growth_max": max(growth.values()),
        "growth_1960": growth[1960],
        "growth_2025": growth[2025],
        "heatmap_shape": [67, 12],
        "greyscale_method": "ITU-R BT.601 luma on colormap strip",
    }


if __name__ == "__main__":
    import json

    print(json.dumps(run_all(), indent=2, default=str))
