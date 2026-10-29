#!/usr/bin/env python3
"""Chapter 1 nitrate figures: vague draft (FIG ch01-03) and brief panel (FIG ch01-04)."""
# SPDX-License-Identifier: MIT
import argparse
import csv
import json
import subprocess
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data/ch01/ch01-raccoon-2016.csv"
FIG_DIR = ROOT / "figures/ch01"
CFS_TO_M3S = 0.028316846592

MM_TO_IN = 1 / 25.4


def load_csv() -> pd.DataFrame:
    with CSV_PATH.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    assert len(rows) == 366
    frame = pd.DataFrame(rows)
    frame["date"] = pd.to_datetime(frame["date"])
    for col in ("nitrate_mgL_as_N", "discharge_cfs"):
        frame[col] = pd.to_numeric(frame[col], errors="coerce")
    assert frame["nitrate_mgL_as_N"].notna().sum() == 363
    assert frame["discharge_cfs"].notna().sum() == 366
    return frame


def run_assertions(frame: pd.DataFrame) -> dict:
    missing = frame.loc[frame["nitrate_mgL_as_N"].isna(), "date"].dt.strftime("%Y-%m-%d").tolist()
    assert missing == ["2016-09-18", "2016-09-19", "2016-12-14"]
    assert frame.loc[frame["date"] == "2016-05-13", "nitrate_mgL_as_N"].iloc[0] == 13.9
    assert frame.loc[frame["date"] == "2016-09-16", "nitrate_mgL_as_N"].iloc[0] == 3.19
    assert (frame["nitrate_mgL_as_N"] > 10).sum() == 162
    monthly = frame.dropna(subset=["nitrate_mgL_as_N"]).copy()
    monthly["month"] = monthly["date"].dt.month
    means = monthly.groupby("month")["nitrate_mgL_as_N"].mean()
    assert abs(means[5] - 12.84) < 0.01
    assert abs(means[9] - 5.36) < 0.01
    assert int(frame.loc[frame["date"] == "2016-05-01", "discharge_cfs"].iloc[0]) == 16300
    assert int(frame.loc[frame["date"] == "2016-09-06", "discharge_cfs"].iloc[0]) == 411
    assert frame["discharge_qual"].str.contains("e", na=False).sum() == 58
    return {
        "rows": int(len(frame)),
        "nitrate_valid": int(frame["nitrate_mgL_as_N"].notna().sum()),
        "nitrate_missing_dates": missing,
        "nitrate_max": 13.9,
        "nitrate_min": 3.19,
        "days_above_10_mgL": 162,
        "may_mean": round(float(means[5]), 2),
        "september_mean": round(float(means[9]), 2),
        "discharge_max_cfs": 16300,
        "discharge_min_cfs": 411,
        "discharge_ae_days": 58,
    }


def chinese_font() -> FontProperties:
    font_path = subprocess.check_output(["kpsewhich", "FandolHei-Regular.otf"], text=True).strip()
    if not font_path:
        raise RuntimeError("FandolHei not found; install TeX Live Fandol fonts.")
    return FontProperties(fname=font_path, family="sans-serif")


def save_figure(fig, path_stem: Path, language: str) -> None:
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
                dpi=300,
                facecolor="white",
                metadata={"Creator": "ai-scientific-figures-book ch01_figures.py"},
            )


def render_vague(frame: pd.DataFrame, language: str) -> None:
    labels = {
        "zh": {
            "nitrate": "硝酸盐 (mg/L)",
            "flow": "流量",
            "title": "硝酸盐污染危机",
            "exceed": "超标！",
            "circles": ["①", "②", "③", "④", "⑤", "⑥"],
        },
        "en": {
            "nitrate": "Nitrate (mg/L)",
            "flow": "Flow",
            "title": "Nitrate pollution crisis",
            "exceed": "Exceeds limit!",
            "circles": ["①", "②", "③", "④", "⑤", "⑥"],
        },
    }[language]
    font = chinese_font() if language == "zh" else None
    plot_frame = frame.copy()
    plot_nitrate = plot_frame["nitrate_mgL_as_N"].interpolate(method="linear")
    assert plot_frame["nitrate_mgL_as_N"].isna().sum() == 3
    assert plot_nitrate.notna().all()
    assert plot_frame["nitrate_mgL_as_N"].equals(frame["nitrate_mgL_as_N"])

    fig, ax1 = plt.subplots(figsize=(174 * MM_TO_IN, 85 * MM_TO_IN))
    ax2 = ax1.twinx()
    ax1.plot(
        plot_frame["date"],
        plot_nitrate,
        color="#d62728",
        linewidth=2.5,
        zorder=3,
    )
    ax2.plot(
        plot_frame["date"],
        plot_frame["discharge_cfs"],
        color="#2ca02c",
        linewidth=2.5,
        zorder=2,
    )
    ax1.axhline(10, color="#d62728", linewidth=2.0, zorder=1)
    ax1.text(
        plot_frame["date"].iloc[-1],
        10.3,
        labels["exceed"],
        color="#d62728",
        fontsize=9,
        ha="right",
        fontproperties=font,
    )
    ax1.set_ylabel(labels["nitrate"], fontproperties=font, fontsize=10)
    ax2.set_ylabel(labels["flow"], fontproperties=font, fontsize=10)
    fig.suptitle(labels["title"], fontproperties=font, fontsize=12, y=0.98)
    ax1.xaxis.set_major_locator(mdates.MonthLocator(bymonthday=[1, 15]))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    plt.setp(ax1.get_xticklabels(), rotation=45, ha="right", fontsize=7)
    ax1.grid(True, which="both", linewidth=0.8, alpha=0.7)
    ax2.grid(False)

    gap_date = pd.Timestamp("2016-09-18")
    ax1.annotate(
        "",
        xy=(gap_date, plot_nitrate.loc[plot_frame["date"] == gap_date].iloc[0]),
        xytext=(0.02, 0.55),
        xycoords=("data", "data"),
        textcoords="axes fraction",
        arrowprops={"arrowstyle": "->", "color": "#c0392b", "lw": 1.0},
    )
    markers = [
        (0.88, 0.55, labels["circles"][0]),
        (0.52, 0.42, labels["circles"][1]),
        (0.04, 0.92, labels["circles"][2]),
        (0.78, 0.72, labels["circles"][3]),
        (0.35, 0.96, labels["circles"][4]),
        (0.45, 0.02, labels["circles"][5]),
    ]
    for x_frac, y_frac, text in markers:
        ax1.text(
            x_frac,
            y_frac,
            text,
            transform=ax1.transAxes,
            fontsize=14,
            color="#c0392b",
            ha="center",
            va="center",
            bbox=dict(boxstyle="circle,pad=0.25", edgecolor="#c0392b", facecolor="white", lw=1.2),
            fontproperties=font,
        )

    fig.subplots_adjust(left=0.08, right=0.92, top=0.88, bottom=0.22)
    stem = FIG_DIR / f"ch01-03-nitrate-draft-vague-{language}"
    save_figure(fig, stem, language)
    plt.close(fig)


def month_ticks(ax, language: str, font) -> None:
    months = pd.date_range("2016-01-01", "2016-12-01", freq="MS")
    ax.set_xticks(months)
    if language == "zh":
        ax.set_xticklabels([f"{m}月" for m in range(1, 13)], fontproperties=font, fontsize=7)
    else:
        ax.set_xticklabels(
            ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
            fontsize=7,
        )


def render_brief(frame: pd.DataFrame, language: str, size: str) -> None:
    labels = {
        "zh": {
            "nitrate": "硝酸盐（mg/L，以 N 计）",
            "flow": "流量（m$^3$/s，对数刻度）",
            "mcl": "美国 EPA 饮用水 MCL（仅作参照）",
            "legend": "浅色：冰期估算值",
            "year": "2016",
        },
        "en": {
            "nitrate": "Nitrate (mg/L as N)",
            "flow": "Discharge (m³/s, log scale)",
            "mcl": "US EPA drinking-water MCL (reference only)",
            "legend": "Light: ice-affected estimates",
            "year": "2016",
        },
    }[language]
    font = chinese_font() if language == "zh" else None
    if size == "panel":
        width_mm, height_mm = 108, 95
        suffix = "-panel"
    else:
        width_mm, height_mm = 174, 95
        suffix = ""

    discharge_m3s = frame["discharge_cfs"] * CFS_TO_M3S
    is_ae = frame["discharge_qual"].str.contains("e", na=False)

    fig, (ax_top, ax_bot) = plt.subplots(
        2,
        1,
        sharex=True,
        figsize=(width_mm * MM_TO_IN, height_mm * MM_TO_IN),
        gridspec_kw={"height_ratios": [1, 1], "hspace": 0.08},
    )
    ax_top.plot(frame["date"], frame["nitrate_mgL_as_N"], color="#1b6f73", linewidth=1.0)
    ax_top.axhline(10, color="#7a7a7a", linewidth=0.8, linestyle="--", zorder=0)
    ax_top.text(
        frame["date"].iloc[-1],
        10.15,
        labels["mcl"],
        fontsize=6,
        color="#555555",
        ha="right",
        va="bottom",
        fontproperties=font,
    )
    ax_top.set_ylim(0, 16)
    ax_top.yaxis.set_major_locator(MultipleLocator(4))
    ax_top.set_ylabel(labels["nitrate"], fontproperties=font, fontsize=8)
    ax_top.tick_params(labelsize=7)
    ax_top.spines[["top", "right"]].set_visible(False)

    ax_bot.plot(frame["date"], discharge_m3s, color="#4a6fa5", linewidth=1.0, zorder=2)
    for idx in range(len(frame) - 1):
        if is_ae.iloc[idx] or is_ae.iloc[idx + 1]:
            ax_bot.plot(
                frame["date"].iloc[idx : idx + 2],
                discharge_m3s.iloc[idx : idx + 2],
                color="#4a6fa5",
                alpha=0.35,
                linewidth=2.5,
                zorder=3,
            )
    ax_bot.set_yscale("log")
    ax_bot.set_ylim(10, 1000)
    ax_bot.set_ylabel(labels["flow"], fontproperties=font, fontsize=8)
    ax_bot.tick_params(labelsize=7)
    ax_bot.spines[["top", "right"]].set_visible(False)
    ax_bot.text(
        0.98,
        0.92,
        labels["legend"],
        transform=ax_bot.transAxes,
        ha="right",
        va="top",
        fontsize=6,
        color="#4a6fa5",
        fontproperties=font,
    )

    for highlight_date in ("2016-05-13", "2016-09-16"):
        row = frame.loc[frame["date"] == highlight_date].iloc[0]
        ax_top.plot(row["date"], row["nitrate_mgL_as_N"], "o", color="#1b6f73", markersize=3)

    month_ticks(ax_bot, language, font)
    ax_bot.set_xlabel(labels["year"], fontproperties=font, fontsize=8)
    fig.subplots_adjust(left=0.12, right=0.96, top=0.98, bottom=0.14)

    stem = FIG_DIR / f"ch01-04-nitrate-panel-brief-{language}{suffix}"
    save_figure(fig, stem, language)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--variant", choices=("vague", "brief", "all"), default="all")
    parser.add_argument("--size", choices=("full", "panel", "both"), default="both")
    args = parser.parse_args()

    frame = load_csv()
    checks = run_assertions(frame)
    checks["interpolate_only_in_vague_plot"] = True
    checks["data_file"] = str(CSV_PATH.relative_to(ROOT))
    provenance = ROOT / "provenance/ch01/data-check.json"
    provenance.write_text(json.dumps(checks, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    FIG_DIR.mkdir(parents=True, exist_ok=True)
    variants = ("vague", "brief") if args.variant == "all" else (args.variant,)
    for language in ("zh", "en"):
        if "vague" in variants:
            render_vague(frame, language)
        if "brief" in variants:
            sizes = ("full", "panel") if args.size == "both" else (args.size,)
            for size in sizes:
                render_brief(frame, language, size)
    print(json.dumps(checks, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
