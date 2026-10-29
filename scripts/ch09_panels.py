#!/usr/bin/env python3
"""FIG ch09-05: data panels c and d at final print size."""
# SPDX-License-Identifier: MIT
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from ch09_plot_utils import (  # noqa: E402
    FIG,
    MM_PER_IN,
    PANEL_H_MM,
    PANEL_W_MM,
    apply_data_ax_position,
    load_metrics,
    load_t80,
    plot_panel_c,
    plot_panel_d,
    save_figure,
    setup_rc,
    DATA_AX_POSITION,
)


def single_panel(which: str, language: str) -> None:
    setup_rc(8)
    fig = plt.figure(figsize=(PANEL_W_MM / MM_PER_IN, PANEL_H_MM / MM_PER_IN))
    ax = fig.add_axes(DATA_AX_POSITION)
    if which == "c":
        plot_panel_c(ax, language, good=True)
    else:
        plot_panel_d(ax, language, good=True)
    work = FIG / "work"
    save_figure(fig, work / f"panel-{which}", language)


def combined_panels(language: str) -> None:
    setup_rc(8)
    gap_mm = 6.0
    total_w = PANEL_W_MM * 2 + gap_mm
    fig = plt.figure(figsize=(total_w / MM_PER_IN, PANEL_H_MM / MM_PER_IN))
    w_frac = PANEL_W_MM / total_w
    gap_frac = gap_mm / total_w
    pos_c = (
        DATA_AX_POSITION[0] * w_frac,
        DATA_AX_POSITION[1],
        DATA_AX_POSITION[2] * w_frac,
        DATA_AX_POSITION[3],
    )
    pos_d = (
        w_frac + gap_frac + DATA_AX_POSITION[0] * w_frac,
        DATA_AX_POSITION[1],
        DATA_AX_POSITION[2] * w_frac,
        DATA_AX_POSITION[3],
    )
    ax_c = fig.add_axes(pos_c)
    ax_d = fig.add_axes(pos_d)
    plot_panel_c(ax_c, language, good=True)
    plot_panel_d(ax_d, language, good=True)
    save_figure(fig, FIG / "ch09-05-data-panels", language, bbox_inches="tight", pad_inches=0.01)


def assert_metrics() -> dict:
    metrics = load_metrics()
    t80 = load_t80()
    pce_c = float(metrics["control"]["PCE"])
    pce_m = float(metrics["modified"]["PCE"])
    assert abs(pce_c - 19.21) < 0.15
    assert abs(pce_m - 20.98) < 0.15
    assert t80["control"] == "210"
    return {"control_PCE": pce_c, "modified_PCE": pce_m, "control_T80_h": t80["control"]}


def assert_ax_alignment() -> None:
    setup_rc(8)
    fig1 = plt.figure(figsize=(PANEL_W_MM / MM_PER_IN, PANEL_H_MM / MM_PER_IN))
    ax1 = fig1.add_axes([0, 0, 1, 1])
    apply_data_ax_position(ax1)
    pos_c = ax1.get_position().bounds
    plt.close(fig1)
    fig2 = plt.figure(figsize=(PANEL_W_MM / MM_PER_IN, PANEL_H_MM / MM_PER_IN))
    ax2 = fig2.add_axes([0, 0, 1, 1])
    apply_data_ax_position(ax2)
    pos_d = ax2.get_position().bounds
    plt.close(fig2)
    assert pos_c == pos_d


def main() -> None:
    FIG.mkdir(parents=True, exist_ok=True)
    (FIG / "work").mkdir(parents=True, exist_ok=True)
    stats = assert_metrics()
    assert_ax_alignment()
    for language in ("zh", "en"):
        single_panel("c", language)
        single_panel("d", language)
        combined_panels(language)
    print("ch09_panels OK", stats)


if __name__ == "__main__":
    main()
