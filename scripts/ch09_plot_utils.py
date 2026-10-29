#!/usr/bin/env python3
"""Shared plotting helpers for chapter 9 perovskite panel figures."""
# SPDX-License-Identifier: MIT
import csv
import subprocess
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures" / "ch09"
MM_PER_IN = 25.4

COLOR_CONTROL = "#6E6E6E"
COLOR_MODIFIED = "#1B7F86"
COLOR_REF = "#9A9A9A"

# Fixed axis box within an 84 × 56 mm panel (mm from panel origin).
PANEL_W_MM = 84.0
PANEL_H_MM = 56.0
AX_LEFT_MM = 12.0
AX_BOTTOM_MM = 10.0
AX_WIDTH_MM = PANEL_W_MM - AX_LEFT_MM
AX_HEIGHT_MM = PANEL_H_MM - AX_BOTTOM_MM

DATA_AX_POSITION = (
    AX_LEFT_MM / PANEL_W_MM,
    AX_BOTTOM_MM / PANEL_H_MM,
    AX_WIDTH_MM / PANEL_W_MM,
    AX_HEIGHT_MM / PANEL_H_MM,
)


def chinese_font() -> FontProperties:
    font_path = subprocess.check_output(
        ["kpsewhich", "FandolHei-Regular.otf"], text=True, timeout=30
    ).strip()
    if not font_path:
        raise RuntimeError("Install TeX Live Fandol fonts for Chinese labels.")
    return FontProperties(fname=font_path, family="sans-serif")


def setup_rc(font_size: float = 8.0) -> None:
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
        "font.size": font_size,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "axes.linewidth": 0.6,
        "lines.linewidth": 1.2,
    })


def load_jv():
    path = ROOT / "data/sim-perovskite-jv.csv"
    groups = {"control": ([], []), "modified": ([], [])}
    with path.open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream):
            v = float(row["voltage_V"])
            j = float(row["current_density_mA_cm2"])
            groups[row["group"]][0].append(v)
            groups[row["group"]][1].append(j)
    assert len(groups["control"][0]) > 100
    assert len(groups["modified"][0]) > 100
    return groups


def load_stability():
    path = ROOT / "data/sim-perovskite-stability.csv"
    groups = {"control": ([], []), "modified": ([], [])}
    with path.open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream):
            t = float(row["time_h"])
            y = float(row["normalized_pce"])
            groups[row["group"]][0].append(t)
            groups[row["group"]][1].append(y)
    return groups


def load_metrics():
    path = ROOT / "data/sim-perovskite-jv-metrics.csv"
    with path.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    assert len(rows) == 2
    return {row["group"]: row for row in rows}


def load_t80():
    path = ROOT / "data/sim-perovskite-stability-t80.csv"
    with path.open(encoding="utf-8", newline="") as stream:
        rows = {row["group"]: row["T80_h"] for row in csv.DictReader(stream)}
    assert rows["control"] == "210"
    assert rows["modified"] == ">1000"
    return rows


def apply_data_ax_position(ax) -> None:
    ax.set_position(DATA_AX_POSITION)


def _keep_last_xtick_inside(ax) -> None:
    """Rightmost tick label sits fully left of the spine (canvas edge is close)."""
    labels = ax.get_xticklabels()
    if labels:
        labels[-1].set_horizontalalignment("right")


def _series_label(ax, x, y, text, color, font, *, ha="right", va="center") -> None:
    ax.text(
        x, y, text,
        fontproperties=font,
        fontsize=8,
        color=color,
        ha=ha,
        va=va,
        clip_on=True,
        zorder=5,
        bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.92, "pad": 0.12},
    )


def plot_panel_c(ax, language: str, *, good: bool = True) -> None:
    font = chinese_font() if language == "zh" else None
    groups = load_jv()
    metrics = load_metrics()
    if good:
        c_style = {"linestyle": (0, (4, 2))}
        m_style = {"linestyle": "-"}
        xlabel = "电压（V）" if language == "zh" else "Voltage (V)"
        ylabel = "电流密度（mA cm$^{-2}$）" if language == "zh" else "Current density (mA cm$^{-2}$)"
        lbl_c = "对照" if language == "zh" else "Control"
        lbl_m = "改性" if language == "zh" else "Modified"
        sim_note = "模拟数据" if language == "zh" else "Simulated data"
        ax.plot(groups["control"][0], groups["control"][1], color=COLOR_CONTROL, **c_style)
        ax.plot(groups["modified"][0], groups["modified"][1], color=COLOR_MODIFIED, **m_style)
    else:
        xlabel = "Voltage (V)"
        ylabel = "Current density (mA/cm2)"
        lbl_c, lbl_m = "control", "modified"
        ax.plot(groups["control"][0], groups["control"][1], color="#1f77b4", linestyle="-")
        ax.plot(groups["modified"][0], groups["modified"][1], color="#ff7f0e", linestyle="-")
        ax.set_title("J-V curve", fontsize=11)
        ax.legend([lbl_c, lbl_m], loc="upper right", frameon=True)

    ax.set_xlim(0, 1.2)
    ax.set_ylim(0, 25)
    ax.set_xlabel(xlabel, fontproperties=font if good else None)
    ax.set_ylabel(ylabel, fontproperties=font if good else None)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", color="#E4E8E8", linewidth=0.5, zorder=0)

    if good:
        # Blank interior left of each falling edge, clear of the spines.
        _series_label(ax, 1.00, 5.0, lbl_c, COLOR_CONTROL, font)
        _series_label(ax, 0.96, 15.5, lbl_m, COLOR_MODIFIED, font)
        pce_c = float(metrics["control"]["PCE"])
        pce_m = float(metrics["modified"]["PCE"])
        note = f"PCE {pce_c:.2f}% / {pce_m:.2f}%"
        ax.text(
            0.03, 0.04, note, transform=ax.transAxes, ha="left", va="bottom",
            fontsize=8, color=BookInk_fallback(), clip_on=True,
        )
        ax.text(
            0.97, 0.98, sim_note, transform=ax.transAxes,
            ha="right", va="top", fontproperties=font, fontsize=8,
            color=BookInk_fallback(), clip_on=True,
        )
        _keep_last_xtick_inside(ax)


def BookInk_fallback():
    return "#23363E"


def plot_panel_d(ax, language: str, *, good: bool = True) -> None:
    font = chinese_font() if language == "zh" else None
    groups = load_stability()
    t_c, y_c = groups["control"]
    t_m, y_m = groups["modified"]
    if good:
        ax.plot(t_c, y_c, color=COLOR_CONTROL, linestyle=(0, (4, 2)))
        ax.plot(t_m, y_m, color=COLOR_MODIFIED, linestyle="-")
        ax.axhline(0.8, color=COLOR_REF, linestyle=(0, (1, 3)), linewidth=1.0, zorder=2)
        # After the control curve has fallen through 0.8, so the tag sits in the open band.
        _series_label(ax, 520, 0.808, "80%", COLOR_REF, font, ha="left", va="bottom")
        t80_h = 210
        ax.plot([t80_h, t80_h], [0.78, 0.82], color=COLOR_CONTROL, linewidth=1.0, zorder=3)
        t80_lbl = f"T80 ≈ {t80_h} h"
        _series_label(ax, t80_h + 16, 0.830, t80_lbl, COLOR_CONTROL, font, ha="left", va="bottom")
        xlabel = "时间（h）" if language == "zh" else "Time (h)"
        ylabel = "归一化 PCE" if language == "zh" else "Normalized PCE"
        sim_note = "模拟数据" if language == "zh" else "Simulated data"
        lbl_c = "对照" if language == "zh" else "Control"
        lbl_m = "改性" if language == "zh" else "Modified"
    else:
        ax.plot(t_c, y_c, color="#CC0000", linestyle="-")
        ax.plot(t_m, y_m, color="#2CA02C", linestyle="-")
        ax.set_title("Stability test", fontsize=11)
        ax.legend(["control", "modified"], loc="upper right", frameon=True)
        xlabel, ylabel, sim_note = "Time (h)", "Normalized PCE", ""
        lbl_c, lbl_m = "", ""

    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1.05)
    ax.set_xlabel(xlabel, fontproperties=font)
    ax.set_ylabel(ylabel, fontproperties=font)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", color="#E4E8E8", linewidth=0.5, zorder=0)

    if good:
        # Left of each line end, in the open band above that line.
        ax.set_yticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
        _series_label(ax, 860, 0.60, lbl_c, COLOR_CONTROL, font, ha="right", va="bottom")
        _series_label(ax, 700, 0.915, lbl_m, COLOR_MODIFIED, font, ha="right", va="bottom")
        ax.text(
            0.97, 0.98, sim_note, transform=ax.transAxes,
            ha="right", va="top", fontproperties=font, fontsize=8,
            color=BookInk_fallback(), clip_on=True,
        )
        _keep_last_xtick_inside(ax)


def save_figure(fig, stem: Path, language: str, *, dpi: int = 300, bbox_inches=None, pad_inches=0.02) -> None:
    import matplotlib

    stem.parent.mkdir(parents=True, exist_ok=True)
    for extension in ("pdf", "png"):
        use_pgf = language == "zh" and extension == "pdf"
        with matplotlib.rc_context({
            "pgf.texsystem": "xelatex",
            "pgf.rcfonts": False,
            "pgf.preamble": (
                r"\usepackage{fontspec}\usepackage{xeCJK}"
                r"\setsansfont{texgyreheros-regular.otf}["
                r"BoldFont=texgyreheros-bold.otf,"
                r"ItalicFont=texgyreheros-italic.otf,"
                r"BoldItalicFont=texgyreheros-bolditalic.otf]"
                r"\setCJKmainfont{FandolHei-Regular.otf}"
                r"\setCJKsansfont{FandolHei-Regular.otf}"
            ),
        }):
            kwargs = {"dpi": dpi, "facecolor": "white"}
            if bbox_inches is not None:
                kwargs["bbox_inches"] = bbox_inches
                kwargs["pad_inches"] = pad_inches
            fig.savefig(
                stem.with_name(stem.name + f"-{language}.{extension}"),
                backend="pgf" if use_pgf else None,
                **kwargs,
            )
    plt.close(fig)
