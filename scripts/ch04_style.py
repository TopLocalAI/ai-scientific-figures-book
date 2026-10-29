# SPDX-License-Identifier: MIT
"""Shared visual constants for chapter 4 (spec v1)."""
from __future__ import annotations

import subprocess
from pathlib import Path

import matplotlib.colors as mcolors
from matplotlib.font_manager import FontProperties

ROOT = Path(__file__).resolve().parents[1]
MM_TO_IN = 1.0 / 25.4

# Semantic colours (Okabe–Ito based)
ATM_CARBON = "#E69F00"
OCEAN_CARBON = "#0072B2"
LAND_CARBON = "#009E73"
HEAT = "#D55E00"
SEAWATER_PH = "#CC79A7"
EMISSIONS = "#3C3C3C"
WATER_TRANSPORT = "#56B4E9"
NEUTRAL_PALE = "#F2F2F2"
NEUTRAL_MID = "#BDBDBD"
NEUTRAL_DARK = "#7A7A7A"

SEMANTIC_SWATCHES = [
    (ATM_CARBON, "atm"),
    (OCEAN_CARBON, "ocean"),
    (LAND_CARBON, "land"),
    (HEAT, "heat"),
    (SEAWATER_PH, "ph"),
    (EMISSIONS, "emissions"),
]

PT_PANEL = 8
PT_AXIS = 7
PT_TICK = 6

LW_RAW = 0.5
LW_TREND = 1.2
LW_ANNUAL = 1.0
LW_AXIS = 0.6
LW_REF = 0.5

BAD_RED = "#d62728"
BAD_GREEN = "#2ca02c"
BAD_BLUE = "#1f77b4"
BAD_OHC_RED = "#e41a1c"
BAD_OHC_GREEN = "#4daf4a"


def tint(hex_color: str, amount: float) -> str:
    """Blend hex_color toward white; amount=1 keeps full colour."""
    r, g, b = mcolors.to_rgb(hex_color)
    w = 1.0 - amount
    return mcolors.to_hex((r * amount + w, g * amount + w, b * amount + w))


def chinese_font() -> FontProperties:
    font_path = subprocess.check_output(["kpsewhich", "FandolHei-Regular.otf"], text=True).strip()
    if not font_path:
        raise RuntimeError("FandolHei not found; install TeX Live Fandol fonts.")
    return FontProperties(fname=font_path, family="sans-serif")


def apply_good_rcparams() -> None:
    import matplotlib.pyplot as plt

    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
            "font.size": PT_TICK,
            "axes.linewidth": LW_AXIS,
            "axes.labelsize": PT_AXIS,
            "xtick.labelsize": PT_TICK,
            "ytick.labelsize": PT_TICK,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "axes.grid": False,
        }
    )


def style_axes(ax) -> None:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_linewidth(LW_AXIS)
    ax.spines["bottom"].set_linewidth(LW_AXIS)
    ax.tick_params(direction="out", length=3, width=0.6)


def panel_letter(ax, letter: str, font=None) -> None:
    ax.text(
        -0.08,
        1.06,
        letter,
        transform=ax.transAxes,
        fontsize=PT_PANEL,
        fontweight="bold",
        va="bottom",
        ha="right",
        fontproperties=font,
    )


def save_figure(fig, path_stem: Path, language: str, dpi: int = 300) -> None:
    import matplotlib
    import matplotlib.pyplot as plt

    path_stem.parent.mkdir(parents=True, exist_ok=True)
    for extension in ("pdf", "png"):
        use_pgf = language == "zh" and extension == "pdf"
        with matplotlib.rc_context(
            {
                "pgf.texsystem": "xelatex",
                "pgf.rcfonts": False,
                "pgf.preamble": (
                    r"\usepackage{fontspec}\usepackage{xeCJK}"
                    r"\setsansfont{texgyreheros-regular.otf}"
                    r"\setCJKmainfont{FandolHei-Regular.otf}"
                    r"\setCJKsansfont{FandolHei-Regular.otf}"
                ),
            }
        ):
            fig.savefig(
                path_stem.with_suffix(f".{extension}"),
                backend="pgf" if use_pgf else None,
                dpi=dpi,
                facecolor="white",
                metadata={"Creator": "ai-scientific-figures-book ch04"},
            )
    plt.close(fig)
