#!/usr/bin/env python3
"""Chapter 5 penguin figures: ch05-01, 02, 05, 08."""
# SPDX-License-Identifier: MIT
import io
from pathlib import Path

import colorspacious
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
from PIL import Image
from scipy import stats

from ch05_utils import (
    MARKER,
    RNG,
    SPECIES_COLOR,
    SPECIES_ORDER,
    SPECIES_ZH,
    bill_scatter_df,
    chinese_font,
    load_penguins_raw,
    pearson_r,
    penguins_by_species,
    penguins_by_species_sex,
    save_pair,
    setup_rc,
    species_mass_stats,
    species_sex_stats,
    style_spines,
)


def _species_xticks(ax, language: str, font) -> None:
    labels = [SPECIES_ZH[s] if language == "zh" else s for s in SPECIES_ORDER]
    ax.set_xticks(range(3), labels, fontproperties=font)


def _mass_ylabel(language: str, font) -> str:
    return "体重（g）" if language == "zh" else "Body mass (g)"


def _n_below(ax, ns: list[int]) -> None:
    """Sample sizes under the category names, clear of the tick labels."""
    for i, n in enumerate(ns):
        ax.annotate(
            f"n = {n}",
            xy=(i, 0),
            xycoords=ax.get_xaxis_transform(),
            xytext=(0, -15),
            textcoords="offset points",
            ha="center",
            va="top",
            fontsize=6.5,
            annotation_clip=False,
            clip_on=False,
        )


def fig_group_forms(language: str, df, mass_stats: dict) -> None:
    font = chinese_font() if language == "zh" else None
    titles = {
        "zh": [
            "A  均值柱 + SEM",
            "B  箱线图",
            "C  全部记录 + 均值 ± SD",
            "D  云雨图",
        ],
        "en": [
            "A  Mean bar + SEM",
            "B  Box plot",
            "C  All records\n+ mean ± SD",
            "D  Raincloud",
        ],
    }[language]
    fig, axes = plt.subplots(2, 2, figsize=(5.2, 4.9))
    fig.subplots_adjust(left=0.12, right=0.98, top=0.94, bottom=0.10, wspace=0.32, hspace=0.58)
    axes = axes.ravel()
    ns = [mass_stats[sp]["n"] for sp in SPECIES_ORDER]

    ax = axes[0]
    means = [mass_stats[s]["mean"] for s in SPECIES_ORDER]
    sems = [mass_stats[s]["sem"] for s in SPECIES_ORDER]
    colors = [SPECIES_COLOR[s] for s in SPECIES_ORDER]
    ax.bar(range(3), means, yerr=sems, capsize=3, color=colors, width=0.55, zorder=2)
    ax.set_ylim(0, 6800)
    ax.set_yticks([0, 2000, 4000, 6000])
    ax.set_title(titles[0], loc="left", fontsize=8, pad=4, fontweight="bold")
    style_spines(ax)

    for ax in axes[1:]:
        ax.set_ylim(2500, 6800)
        ax.set_yticks([3000, 4000, 5000, 6000])
        style_spines(ax)

    ax = axes[1]
    data = [df.loc[df["species"] == sp, "body_mass_g"].values for sp in SPECIES_ORDER]
    ax.boxplot(data, positions=range(3), widths=0.45, patch_artist=True)
    ax.set_title(titles[1], loc="left", fontsize=8, pad=4, fontweight="bold")

    ax = axes[2]
    for i, sp in enumerate(SPECIES_ORDER):
        y = df.loc[df["species"] == sp, "body_mass_g"].values
        jitter = RNG.uniform(-0.15, 0.15, size=len(y))
        ax.scatter(
            i + jitter,
            y,
            s=6,
            alpha=0.5,
            color=SPECIES_COLOR[sp],
            edgecolors="none",
            zorder=2,
        )
        m, sd = mass_stats[sp]["mean"], mass_stats[sp]["sd"]
        ax.hlines(m, i - 0.12, i + 0.12, colors="black", linewidth=1.2, zorder=3)
        ax.vlines(i, m - sd, m + sd, colors="black", linewidth=0.9, zorder=3)
    title = ax.set_title(titles[2], loc="left", fontsize=8, pad=2, fontweight="bold")
    # loc="left" is not ax.title. Default leading makes the two lines' font boxes meet.
    title.set_linespacing(2.5)

    ax = axes[3]
    for i, sp in enumerate(SPECIES_ORDER):
        y = df.loc[df["species"] == sp, "body_mass_g"].values
        jitter = RNG.uniform(-0.28, -0.08, size=len(y))
        ax.scatter(
            i + jitter,
            y,
            s=5,
            alpha=0.45,
            color=SPECIES_COLOR[sp],
            edgecolors="none",
            zorder=2,
        )
        ax.boxplot(
            y,
            positions=[i],
            widths=0.1,
            patch_artist=True,
            boxprops={"facecolor": "white", "linewidth": 0.7},
            medianprops={"color": "black", "linewidth": 1.0},
            whiskerprops={"linewidth": 0.7},
            capprops={"linewidth": 0.7},
            flierprops={"marker": "o", "markersize": 2, "alpha": 0.4},
        )
        kde = stats.gaussian_kde(y)
        y_grid = np.linspace(y.min(), y.max(), 120)
        dens = kde(y_grid)
        dens = dens / dens.max() * 0.32
        ax.fill_betweenx(
            y_grid,
            i + 0.06,
            i + 0.06 + dens,
            color=SPECIES_COLOR[sp],
            alpha=0.35,
            linewidth=0,
        )
    ax.set_title(titles[3], loc="left", fontsize=8, pad=4, fontweight="bold")

    for ax in axes:
        _species_xticks(ax, language, font)
        ax.tick_params(axis="x", pad=1)
        _n_below(ax, ns)
        ax.set_xlim(-0.55, 2.55)
    axes[0].set_ylabel(_mass_ylabel(language, font), fontproperties=font)
    axes[2].set_ylabel(_mass_ylabel(language, font), fontproperties=font)
    save_pair(fig, "ch05-01-group-forms", language)
    plt.close(fig)


def fig_case_final(language: str, df, sex_stats: dict) -> None:
    font = chinese_font() if language == "zh" else None
    fig, ax = plt.subplots(figsize=(3.5, 3.15))
    fig.subplots_adjust(left=0.18, right=0.98, top=0.90, bottom=0.24)
    offsets = {"female": -0.18, "male": 0.18}
    n_labels = []
    for si, sp in enumerate(SPECIES_ORDER):
        for sex, off in offsets.items():
            sub = df.loc[(df["species"] == sp) & (df["sex"] == sex)]
            y = sub["body_mass_g"].values
            jitter = RNG.uniform(-0.07, 0.07, size=len(y))
            x = si + off + jitter
            face = "none" if sex == "female" else SPECIES_COLOR[sp]
            ax.scatter(
                x,
                y,
                s=10,
                facecolors=face,
                edgecolors=SPECIES_COLOR[sp],
                linewidths=0.8,
                alpha=0.85 if sex == "male" else 1.0,
                zorder=2,
            )
            st = sex_stats[(sp, sex)]
            cx = si + off + 0.10
            ax.hlines(st["mean"], cx - 0.04, cx + 0.04, colors="black", linewidth=1.2, zorder=4)
            ax.vlines(cx, st["mean"] - st["sd"], st["mean"] + st["sd"], colors="black", linewidth=0.9, zorder=4)
            n_labels.append(f"n = {st['n']}")

    _species_xticks(ax, language, font)
    ax.tick_params(axis="x", pad=1)
    ax.set_ylim(2500, 6600)
    ax.set_yticks([3000, 4000, 5000, 6000])
    ax.set_ylabel(_mass_ylabel(language, font), fontproperties=font)
    ax.set_xlim(-0.55, 2.55)
    for si in range(3):
        ax.annotate(
            n_labels[si * 2],
            xy=(si, 0),
            xycoords=ax.get_xaxis_transform(),
            xytext=(0, -20),
            textcoords="offset points",
            ha="center",
            va="top",
            fontsize=6.5,
            annotation_clip=False,
            clip_on=False,
        )
        ax.annotate(
            n_labels[si * 2 + 1],
            xy=(si, 0),
            xycoords=ax.get_xaxis_transform(),
            xytext=(0, -34),
            textcoords="offset points",
            ha="center",
            va="top",
            fontsize=6.5,
            annotation_clip=False,
            clip_on=False,
        )

    if language == "zh":
        leg = [
            plt.Line2D([0], [0], marker="o", linestyle="none", markerfacecolor="none", markeredgecolor="#666", label="雌"),
            plt.Line2D([0], [0], marker="o", linestyle="none", markerfacecolor="#666", label="雄"),
            plt.Line2D([0], [0], color="black", label="横线：均值；竖线：± 1 SD"),
        ]
    else:
        leg = [
            plt.Line2D([0], [0], marker="o", linestyle="none", markerfacecolor="none", markeredgecolor="#666", label="Female"),
            plt.Line2D([0], [0], marker="o", linestyle="none", markerfacecolor="#666", label="Male"),
            plt.Line2D([0], [0], color="black", label="Tick: mean; line: ±1 SD"),
        ]
    ax.legend(handles=leg, loc="upper left", frameon=False, prop=font, fontsize=6.5)
    style_spines(ax)
    save_pair(fig, "ch05-02-case-final", language)
    plt.close(fig)


def fig_axis_bad(language: str, mass_stats: dict) -> None:
    font = chinese_font() if language == "zh" else None
    fig = plt.figure(figsize=(3.7, 2.9))
    ax = fig.add_subplot(111, projection="3d")
    fig.subplots_adjust(left=0.0, right=0.72, top=0.86, bottom=0.06)
    xs = np.arange(3)
    means = np.array([mass_stats[s]["mean"] for s in SPECIES_ORDER])
    colors = ["#D62728", "#FFEB3B", "#9467BD"]
    z0 = 3650.0
    # Stagger the three-decimal labels. The truncated 3D bars sit on top of
    # each other; the labels stay, but not in one pile.
    label_y = [0.05, 1.15, 0.05]
    label_z = [80, 160, 40]
    for i, (m, c) in enumerate(zip(means, colors)):
        ax.bar3d(i - 0.25, 0, z0, 0.5, 0.5, m - z0, color=c, alpha=0.85, shade=True)
        ax.text(i, label_y[i], m + label_z[i], f"{m:.3f} g", fontsize=7)
    ax.set_zlim(z0, 5200)
    ax.set_zticks([4000, 4500, 5000])
    ax.set_yticks([0])
    ax.set_ylim(0, 1.4)
    ax.view_init(elev=18, azim=-58)
    ax.set_xticks(xs)
    ax.set_xticklabels(
        [SPECIES_ZH[s] if language == "zh" else s for s in SPECIES_ORDER],
        fontproperties=font,
        fontsize=7,
    )
    zlabel = "平均体重" if language == "zh" else "Average weight"
    # A 3D axis label is placed again by XeLaTeX past the Agg extent, so the
    # tight crop clips it. A normal figure text stays inside the page.
    fig.text(
        0.93,
        0.48,
        zlabel,
        rotation=90,
        ha="center",
        va="center",
        fontsize=8,
        fontproperties=font,
    )
    badge = "X  误导示例" if language == "zh" else "X  Misleading"
    fig.text(0.08, 0.93, badge, color="#D62728", fontproperties=font, fontsize=9, fontweight="bold")
    save_pair(fig, "ch05-05-axis-bad", language)
    plt.close(fig)


def fig_axis_good(language: str, mass_stats: dict) -> None:
    font = chinese_font() if language == "zh" else None
    fig, ax = plt.subplots(figsize=(3.15, 2.85))
    fig.subplots_adjust(left=0.20, right=0.97, top=0.86, bottom=0.22)
    for i, sp in enumerate(SPECIES_ORDER):
        st = mass_stats[sp]
        ax.errorbar(
            i,
            st["mean"],
            yerr=st["ci_half_width"],
            fmt="o",
            color=SPECIES_COLOR[sp],
            markersize=7,
            capsize=4,
            elinewidth=1.0,
        )
    _species_xticks(ax, language, font)
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(2500, 6600)
    ax.set_yticks([3000, 4000, 5000, 6000])
    ax.set_ylabel(_mass_ylabel(language, font), fontproperties=font)
    note = (
        "非柱状图纵轴可不从 0 开始"
        if language == "zh"
        else "Non-bar charts need not start at zero"
    )
    fig.text(0.58, 0.03, note, ha="center", va="bottom", fontsize=6.5, fontproperties=font)
    badge = "OK  修改后" if language == "zh" else "OK  Revised"
    ax.set_title(badge, loc="left", color="#2E7D32", fontsize=9, fontweight="bold", pad=4)
    style_spines(ax)
    save_pair(fig, "ch05-05-axis-good", language)
    plt.close(fig)


def _panel_title(ax, text: str, color: str = "black", pad: float = 3) -> None:
    ax.set_title(text, loc="left", fontsize=7.5, pad=pad, fontweight="bold", color=color)


def _draw_scatter_panel(ax, df, mode: str, language: str, font, *, title: bool = True, axis_labels: bool = True) -> None:
    ax.set_xlim(30, 60)
    ax.set_ylim(13, 22.2)
    ax.set_xticks([30, 40, 50, 60])
    ax.set_yticks([14, 16, 18, 20, 22])
    if mode == "pooled":
        x = df["bill_length_mm"].values
        y = df["bill_depth_mm"].values
        r = pearson_r(x, y)
        assert abs(r - (-0.235)) < 0.01
        ax.scatter(x, y, s=8, c="#7F7F7F", alpha=0.5, edgecolors="none")
        coef = np.polyfit(x, y, 1)
        xs = np.array([30, 60])
        ax.plot(xs, coef[0] * xs + coef[1], color="#333333", linewidth=1.0)
        ax.text(
            0.98,
            0.04,
            f"r = {r:.2f}, n = 342",
            transform=ax.transAxes,
            ha="right",
            va="bottom",
            fontsize=6.5,
        )
        if title:
            _panel_title(ax, "A  不分组" if language == "zh" else "A  Pooled")
    elif mode == "bad_color":
        bad_colors = {"Adelie": "#D62728", "Chinstrap": "#2CA02C", "Gentoo": "#1F77B4"}
        for sp in SPECIES_ORDER:
            sub = df.loc[df["species"] == sp]
            name = SPECIES_ZH[sp] if language == "zh" else sp
            ax.scatter(
                sub["bill_length_mm"],
                sub["bill_depth_mm"],
                s=10,
                c=bad_colors[sp],
                alpha=0.65,
                label=name,
                edgecolors="none",
            )
            r = pearson_r(sub["bill_length_mm"].values, sub["bill_depth_mm"].values)
            coef = np.polyfit(sub["bill_length_mm"], sub["bill_depth_mm"], 1)
            xs = np.linspace(sub["bill_length_mm"].min(), sub["bill_length_mm"].max(), 50)
            ax.plot(xs, coef[0] * xs + coef[1], color=bad_colors[sp], linewidth=1.0)
        ax.legend(frameon=False, fontsize=6, loc="lower left", prop=font)
        if title:
            _panel_title(
                ax,
                "B  X  仅靠红绿区分" if language == "zh" else "B  X  Colour only",
                color="#D62728",
                pad=3,
            )
    elif mode == "good":
        rs = {"Adelie": 0.391, "Chinstrap": 0.654, "Gentoo": 0.643}
        ns = {"Adelie": 151, "Chinstrap": 68, "Gentoo": 123}
        label_pos = {
            "Adelie": (31.6, 18.2),
            "Chinstrap": (50.8, 19.4),
            "Gentoo": (40.2, 16.4),
        }
        r_lines = []
        for sp in SPECIES_ORDER:
            sub = df.loc[df["species"] == sp]
            ax.scatter(
                sub["bill_length_mm"],
                sub["bill_depth_mm"],
                s=12,
                c=SPECIES_COLOR[sp],
                marker=MARKER[sp],
                alpha=0.65,
                edgecolors="none",
            )
            r = pearson_r(sub["bill_length_mm"].values, sub["bill_depth_mm"].values)
            assert abs(r - rs[sp]) < 0.01
            coef = np.polyfit(sub["bill_length_mm"], sub["bill_depth_mm"], 1)
            xs = np.linspace(sub["bill_length_mm"].min(), sub["bill_length_mm"].max(), 50)
            ax.plot(xs, coef[0] * xs + coef[1], color=SPECIES_COLOR[sp], linewidth=1.0)
            lx, ly = label_pos[sp]
            name = SPECIES_ZH[sp] if language == "zh" else sp
            ax.text(lx, ly, name, fontsize=6.5, fontproperties=font, color=SPECIES_COLOR[sp], ha="left", va="bottom")
            r_lines.append(f"{name} r={r:.2f} (n={ns[sp]})")
        ax.text(
            0.02,
            0.98,
            "\n".join(r_lines),
            transform=ax.transAxes,
            ha="left",
            va="top",
            fontsize=5.5,
            fontproperties=font,
            linespacing=1.8,
        )
        if title:
            _panel_title(
                ax,
                "D  OK  颜色 + 形状 + 标注" if language == "zh" else "D  OK  Colour + shape",
                color="#2E7D32",
            )
    if axis_labels:
        xlabel = "嘴峰长度（mm）" if language == "zh" else "Bill length (mm)"
        ylabel = "嘴峰深度（mm）" if language == "zh" else "Bill depth (mm)"
        ax.set_xlabel(xlabel, fontproperties=font, fontsize=7)
        ax.set_ylabel(ylabel, fontproperties=font, fontsize=7)
    style_spines(ax)


def _render_panel_rgb(draw_mode: str, df, language: str, figsize=(1.7, 1.25), dpi=160):
    font = chinese_font() if language == "zh" else None
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    fig.subplots_adjust(left=0.16, right=0.97, top=0.86, bottom=0.16)
    _draw_scatter_panel(ax, df, draw_mode, language, font, title=False, axis_labels=False)
    fig.canvas.draw()
    buf = np.asarray(fig.canvas.buffer_rgba())[..., :3] / 255.0
    plt.close(fig)
    return buf


def _simulate_cvd(rgb: np.ndarray) -> np.ndarray:
    out = colorspacious.cspace_convert(
        rgb,
        {"name": "sRGB1+CVD", "cvd_type": "deuteranomaly", "severity": 100},
        "sRGB1",
    )
    return np.clip(out, 0, 1)


def _greyscale_lab_l(rgb: np.ndarray) -> np.ndarray:
    lab = colorspacious.cspace_convert(rgb, "sRGB1", "CIELab")
    l = lab[..., 0]
    l_norm = (l - l.min()) / (l.max() - l.min() + 1e-9)
    return np.stack([l_norm, l_norm, l_norm], axis=-1)


def fig_scatter_cvd(language: str, df) -> None:
    font = chinese_font() if language == "zh" else None
    fig, axes = plt.subplots(2, 3, figsize=(5.2, 5.15))
    fig.subplots_adjust(left=0.09, right=0.98, top=0.94, bottom=0.07, hspace=0.55, wspace=0.42)

    _draw_scatter_panel(axes[0, 0], df, "pooled", language, font, axis_labels=True)
    _draw_scatter_panel(axes[0, 1], df, "bad_color", language, font, axis_labels=False)
    axes[0, 1].set_xlabel("嘴峰长度（mm）" if language == "zh" else "Bill length (mm)", fontsize=7)
    _draw_scatter_panel(axes[1, 0], df, "good", language, font, axis_labels=True)

    rgb_b = _render_panel_rgb("bad_color", df, language)
    rgb_d = _render_panel_rgb("good", df, language)
    cvd_b = _simulate_cvd(rgb_b)
    cvd_d = _simulate_cvd(rgb_d)
    grey_d = _greyscale_lab_l(rgb_d)

    if language == "zh":
        sim_titles = (
            "C  B 的红绿色盲模拟",
            "E  D 的红绿色盲模拟",
            "F  D 的灰度",
        )
    else:
        sim_titles = (
            "C  B, deuteranopia",
            "E  D, deuteranopia",
            "F  D, greyscale",
        )
    for ax, img, title in (
        (axes[0, 2], cvd_b, sim_titles[0]),
        (axes[1, 1], cvd_d, sim_titles[1]),
        (axes[1, 2], grey_d, sim_titles[2]),
    ):
        ax.imshow(img, aspect="auto")
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_axis_off()
        _panel_title(ax, title)

    save_pair(fig, "ch05-08-scatter-cvd", language)
    plt.close(fig)


def run_all() -> dict:
    setup_rc()
    raw = load_penguins_raw()
    by_sp = penguins_by_species(raw)
    by_sex = penguins_by_species_sex(raw)
    mass_stats = species_mass_stats(by_sp)
    sex_stats = species_sex_stats(by_sex)
    scatter_df = bill_scatter_df(raw)
    checks = {
        "species_mass": {k: {kk: round(vv, 4) if isinstance(vv, float) else vv for kk, vv in v.items()} for k, v in mass_stats.items()},
        "species_sex_groups": len(sex_stats),
        "pooled_bill_r": round(pearson_r(scatter_df["bill_length_mm"], scatter_df["bill_depth_mm"]), 3),
    }
    for language in ("zh", "en"):
        fig_group_forms(language, by_sp, mass_stats)
        fig_case_final(language, by_sex, sex_stats)
        fig_axis_bad(language, mass_stats)
        fig_axis_good(language, mass_stats)
        fig_scatter_cvd(language, scatter_df)
    return checks


if __name__ == "__main__":
    import json

    print(json.dumps(run_all(), indent=2))
