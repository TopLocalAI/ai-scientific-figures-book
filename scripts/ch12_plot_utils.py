#!/usr/bin/env python3
"""Shared helpers for chapter 12 figures (reuses ch09 perovskite data)."""
# SPDX-License-Identifier: MIT
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from ch09_plot_utils import (  # noqa: E402
    COLOR_CONTROL,
    COLOR_MODIFIED,
    COLOR_REF,
    MM_PER_IN,
    chinese_font,
    load_jv,
    load_metrics,
    load_stability,
    load_t80,
    save_figure,
    setup_rc,
)

FIG12 = ROOT / "figures" / "ch12"
COLOR_ACCENT = "#B9652B"
BOOK_INK = "#23363E"

__all__ = [
    "ROOT",
    "FIG12",
    "COLOR_CONTROL",
    "COLOR_MODIFIED",
    "COLOR_REF",
    "COLOR_ACCENT",
    "BOOK_INK",
    "MM_PER_IN",
    "chinese_font",
    "load_jv",
    "load_metrics",
    "load_stability",
    "load_t80",
    "save_figure",
    "setup_rc",
    "assert_perovskite_metrics",
    "format_pce_title",
    "format_stability_title",
]


def assert_perovskite_metrics() -> dict:
    metrics = load_metrics()
    t80 = load_t80()
    pce_c = float(metrics["control"]["PCE"])
    pce_m = float(metrics["modified"]["PCE"])
    assert abs(pce_c - 19.21) < 0.15
    assert abs(pce_m - 20.98) < 0.15
    assert t80["control"] == "210"
    assert t80["modified"] == ">1000"
    stab = load_stability()
    y_c_end = stab["control"][1][-1]
    y_m_end = stab["modified"][1][-1]
    assert abs(y_c_end - 0.47) < 0.02
    assert abs(y_m_end - 0.86) < 0.02
    return {
        "control_PCE": pce_c,
        "modified_PCE": pce_m,
        "control_T80_h": t80["control"],
        "control_retention_1000h": y_c_end,
        "modified_retention_1000h": y_m_end,
        "metrics": metrics,
    }


def format_pce_title(language: str, metrics: dict) -> str:
    pce_c = float(metrics["control"]["PCE"])
    pce_m = float(metrics["modified"]["PCE"])
    if language == "zh":
        return f"改性器件 PCE 从 {pce_c:.1f} % 提高到 {pce_m:.1f} %（模拟数据）"
    return f"Modified device PCE rises from {pce_c:.1f}% to {pce_m:.1f}% (simulated data)"


def format_stability_title(language: str, y_c: float, y_m: float) -> str:
    pc = round(y_c * 100)
    pm = round(y_m * 100)
    if language == "zh":
        return f"1000 h 后改性器件保留约 {pm} % 初始效率，对照约 {pc} %（模拟数据）"
    return (
        f"After 1000 h, modified retains ~{pm}% of initial efficiency, "
        f"control ~{pc}% (simulated data)"
    )
