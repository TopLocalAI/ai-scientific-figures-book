#!/usr/bin/env python3
"""FIG ch12-06 A0 poster (final + draft C0) and FIG ch12-08 squint source."""
# SPDX-License-Identifier: MIT
import argparse
import textwrap
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Rectangle
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from ch12_plot_utils import (  # noqa: E402
    BOOK_INK,
    COLOR_CONTROL,
    COLOR_MODIFIED,
    COLOR_REF,
    FIG12,
    MM_PER_IN,
    assert_perovskite_metrics,
    chinese_font,
    format_pce_title,
    format_stability_title,
    load_jv,
    load_metrics,
    load_stability,
    save_figure,
    setup_rc,
)

A0_W = 841.0
A0_H = 1189.0
MARGIN = 30.0
GUTTER = 20.0
COL_W = (A0_W - 2 * MARGIN - GUTTER) / 2
M1 = ROOT / "figures" / "ch09" / "ch09-03-device-structure-base.png"
M2 = ROOT / "figures" / "ch09" / "ch09-04-sem-like-illustration-base.png"
ASSEMBLY = ROOT / "figures" / "ch12" / "ch12-03-paper-figure-2-{lang}.png"
TEXT_C0 = ROOT / "data" / "ch12" / "poster-c0-text-{lang}.md"


def mm_axes(fig, left_mm, bottom_mm, width_mm, height_mm):
    return fig.add_axes([
        left_mm / A0_W,
        bottom_mm / A0_H,
        width_mm / A0_W,
        height_mm / A0_H,
    ])


def poster_jv(ax, language: str) -> None:
    font = chinese_font() if language == "zh" else None
    jv = load_jv()
    ax.plot(jv["control"][0], jv["control"][1], color=COLOR_CONTROL, linestyle=(0, (6, 4)), linewidth=3.5)
    ax.plot(jv["modified"][0], jv["modified"][1], color=COLOR_MODIFIED, linewidth=3.5)
    ax.set_xlim(0, 1.2)
    ax.set_ylim(0, 25)
    xlab = "电压（V）" if language == "zh" else "Voltage (V)"
    ylab = "电流密度（mA cm$^{-2}$）" if language == "zh" else "Current density (mA cm$^{-2}$)"
    ax.set_xlabel(xlab, fontproperties=font, fontsize=32)
    ax.set_ylabel(ylab, fontproperties=font, fontsize=32)
    ax.tick_params(labelsize=28, width=2.5, length=8)
    ax.spines[["top", "right"]].set_visible(False)
    sim = "模拟数据" if language == "zh" else "Simulated data"
    ax.text(0.97, 0.95, sim, transform=ax.transAxes, fontproperties=font, fontsize=24, ha="right", va="top")


def poster_stab(ax, language: str) -> None:
    font = chinese_font() if language == "zh" else None
    stab = load_stability()
    ax.plot(stab["control"][0], stab["control"][1], color=COLOR_CONTROL, linestyle=(0, (6, 4)), linewidth=3.5)
    ax.plot(stab["modified"][0], stab["modified"][1], color=COLOR_MODIFIED, linewidth=3.5)
    ax.axhline(0.8, color=COLOR_REF, linestyle=(0, (1, 3)), linewidth=2.5)
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1.05)
    xlab = "时间（h）" if language == "zh" else "Time (h)"
    ylab = "归一化 PCE" if language == "zh" else "Normalized PCE"
    ax.set_xlabel(xlab, fontproperties=font, fontsize=32)
    ax.set_ylabel(ylab, fontproperties=font, fontsize=32)
    ax.tick_params(labelsize=28, width=2.5, length=8)
    ax.spines[["top", "right"]].set_visible(False)
    sim = "模拟数据" if language == "zh" else "Simulated data"
    ax.text(0.97, 0.95, sim, transform=ax.transAxes, fontproperties=font, fontsize=24, ha="right", va="top")


def load_c0_text(language: str) -> str:
    path = Path(str(TEXT_C0).format(lang=language))
    return path.read_text(encoding="utf-8")


def draw_final(language: str) -> plt.Figure:
    info = assert_perovskite_metrics()
    font = chinese_font() if language == "zh" else None
    fig = plt.figure(figsize=(A0_W / MM_PER_IN, A0_H / MM_PER_IN))
    fig.patch.set_facecolor("white")

    title = (
        "界面钝化能否同时提高初始效率与运行稳定性？"
        if language == "zh"
        else "Can interfacial passivation raise both initial efficiency and stability?"
    )
    subtitle = (
        "改性器件在模拟数据中 PCE 更高、1000 h 保留率更好（模拟教学数据）"
        if language == "zh"
        else "Modified device shows higher PCE and retention in simulated teaching data"
    )
    band = mm_axes(fig, 0, A0_H - 150, A0_W, 150)
    band.add_patch(Rectangle((0, 0), 1, 1, transform=band.transAxes, color="#F1F6F5", zorder=0))
    band.axis("off")
    band.text(0.5, 0.65, title, fontproperties=font, fontsize=96, ha="center", va="center", color=BOOK_INK)
    band.text(0.5, 0.25, subtitle, fontproperties=font, fontsize=44, ha="center", va="center", color="#1B7F86")

    left_x = MARGIN
    right_x = MARGIN + COL_W + GUTTER
    block_h = 320

    # Left top — structure
    ax = mm_axes(fig, left_x, A0_H - 150 - 40 - block_h, COL_W, block_h)
    ax.axis("off")
    headline = "我们改了什么" if language == "zh" else "What we changed"
    ax.text(0.02, 0.95, headline, fontproperties=font, fontsize=48, va="top", color=BOOK_INK)
    img_ax = mm_axes(fig, left_x + 10, A0_H - 150 - 40 - block_h + 20, COL_W - 20, block_h - 80)
    img_ax.axis("off")
    if M1.is_file():
        img_ax.imshow(np.array(Image.open(M1)))
    note = "示意，不按比例" if language == "zh" else "Schematic, not to scale"
    img_ax.text(0.98, 0.02, note, transform=img_ax.transAxes, fontproperties=font, fontsize=28, ha="right")

    # Left bottom — J-V
    y0 = A0_H - 150 - 40 - 2 * block_h - 30
    ax = mm_axes(fig, left_x, y0 + block_h - 50, COL_W, 50)
    ax.axis("off")
    ax.text(0.02, 0.5, format_pce_title(language, info["metrics"]), fontproperties=font, fontsize=48, va="center")
    jv_ax = mm_axes(fig, left_x + 10, y0, COL_W - 20, block_h - 60)
    poster_jv(jv_ax, language)

    # Right top — stability
    ax = mm_axes(fig, right_x, A0_H - 150 - 40 - 50, COL_W, 50)
    ax.axis("off")
    ax.text(
        0.02, 0.5,
        format_stability_title(language, info["control_retention_1000h"], info["modified_retention_1000h"]),
        fontproperties=font, fontsize=48, va="center",
    )
    stab_ax = mm_axes(fig, right_x + 10, A0_H - 150 - 40 - block_h, COL_W - 20, block_h - 60)
    poster_stab(stab_ax, language)

    # Right bottom — details
    detail_h = 360
    detail_y = y0 - detail_h - 20
    ax = mm_axes(fig, right_x, detail_y, COL_W, detail_h)
    ax.axis("off")
    methods = (
        [
            "• 平面 n-i-p 结构；改性组界面钝化层",
            "• 模拟反向扫描 J–V（单二极管模型）",
            "• 连续光照 MPP 跟踪稳定性（模拟）",
            "• 颜色：灰=对照，青=改性",
            "• 单条代表性曲线，非器件分布",
        ]
        if language == "zh"
        else [
            "• Planar n-i-p stack; passivation at interface (modified)",
            "• Simulated reverse-scan J–V (single-diode model)",
            "• MPP tracking stability under illumination (simulated)",
            "• Colour: grey = control, teal = modified",
            "• One representative curve per group",
        ]
    )
    y = 0.95
    for line in methods:
        ax.text(0.02, y, line, fontproperties=font, fontsize=28, va="top")
        y -= 0.12
    if M2.is_file():
        m2_ax = mm_axes(fig, right_x + COL_W * 0.45, detail_y + 20, COL_W * 0.5, 120)
        m2_ax.imshow(np.array(Image.open(M2)))
        m2_ax.axis("off")
        m2_note = (
            "模型生成示意，非显微图像" if language == "zh"
            else "Model-generated illustration, not a micrograph"
        )
        m2_ax.text(0.02, 0.02, m2_note, transform=m2_ax.transAxes, fontproperties=font, fontsize=24, color=BOOK_INK)
    ax.text(0.02, 0.08, "模拟教学数据", fontproperties=font, fontsize=24, color="#6E6E6E")
    ax.text(0.02, 0.02, "作者 A · 单位 B", fontproperties=font, fontsize=24, color="#6E6E6E")

    footer = mm_axes(fig, 0, 0, A0_W, 40)
    footer.axis("off")
    footer.text(0.5, 0.5, "A0 portrait · 841 × 1189 mm", ha="center", va="center", fontsize=20, color="#9A9A9A")
    return fig


def draw_draft_c0(language: str) -> plt.Figure:
    font = chinese_font() if language == "zh" else None
    fig = plt.figure(figsize=(A0_W / MM_PER_IN, A0_H / MM_PER_IN))
    fig.patch.set_facecolor("white")
    raw = load_c0_text(language)
    paragraphs = [p.strip() for p in raw.split("\n\n") if p.strip() and not p.startswith("#")]
    col_w = (A0_W - 2 * MARGIN - 2 * GUTTER) / 3
    for i in range(3):
        ax = mm_axes(fig, MARGIN + i * (col_w + GUTTER), A0_H - 700, col_w, 650)
        ax.axis("off")
        chunk = paragraphs[i * 2 : i * 2 + 2]
        text = "\n\n".join(textwrap.fill(c, width=42) for c in chunk)
        ax.text(0, 1, text, fontproperties=font, fontsize=20, va="top", linespacing=1.35)
    asm_path = Path(str(ASSEMBLY).format(lang=language))
    if asm_path.is_file():
        img_ax = mm_axes(fig, MARGIN + 40, 320, A0_W - 2 * MARGIN - 80, 480)
        img_ax.imshow(np.array(Image.open(asm_path)))
        img_ax.axis("off")
    title_ax = mm_axes(fig, MARGIN, A0_H - 120, A0_W - 2 * MARGIN, 80)
    title_ax.axis("off")
    title_ax.text(
        0.5, 0.5, "Perovskite interface study" if language == "en" else "钙钛矿界面改性研究",
        fontproperties=font, fontsize=36, ha="center", va="center",
    )
    return fig


def draw_wireframe(language: str) -> plt.Figure:
    font = chinese_font() if language == "zh" else None
    fig = plt.figure(figsize=(A0_W / MM_PER_IN, A0_H / MM_PER_IN))
    fig.patch.set_facecolor("white")
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, A0_W)
    ax.set_ylim(0, A0_H)
    ax.axis("off")
    layers = [
        (A0_H - 150, 150, "#E8F2F1", "标题层"),
        (350, 520, "#F5FAFA", "结论层"),
        (40, 280, "#FAFCFC", "细节层"),
    ]
    if language == "en":
        layers = [(y, h, c, n.replace("层", " layer")) for y, h, c, n in [
            (A0_H - 150, 150, "#E8F2F1", "Title"),
            (350, 520, "#F5FAFA", "Findings"),
            (40, 280, "#FAFCFC", "Detail"),
        ]]
    for y, h, color, name in layers:
        ax.add_patch(Rectangle((MARGIN, y), A0_W - 2 * MARGIN, h, fill=True, facecolor=color, edgecolor="#C8D6D6"))
        ax.text(MARGIN + 8, y + h - 20, name, fontproperties=font, fontsize=28, color=BOOK_INK)
    ax.plot([MARGIN, MARGIN], [40, A0_H - 40], color="#B9652B", linewidth=1.5)
    ax.plot([A0_W - MARGIN, A0_W - MARGIN], [40, A0_H - 40], color="#B9652B", linewidth=1.5)
    ax.plot([MARGIN + COL_W + GUTTER / 2, MARGIN + COL_W + GUTTER / 2], [40, A0_H - 190], color="#B9652B", linewidth=1.5)
    ax.annotate("", xy=(MARGIN + 20, 200), xytext=(MARGIN + 20, 900), arrowprops=dict(arrowstyle="-|>", color=BOOK_INK, lw=2))
    for i, yy in enumerate([850, 650, 450, 250], start=1):
        ax.text(MARGIN + 35, yy, str(i), fontsize=32, color=BOOK_INK)
    dist_labels = (
        ["建议观看 3–5 m", "1–2 m", "0.5 m"]
        if language == "zh"
        else ["View at 3–5 m", "1–2 m", "0.5 m"]
    )
    for i, lbl in enumerate(dist_labels):
        ax.text(A0_W - MARGIN - 10, 950 - i * 120, lbl, fontproperties=font, fontsize=24, ha="right")
    ax.text(MARGIN, 10, f"{MARGIN:.0f} mm margin", fontsize=18, color="#6E6E6E")
    ax.text(MARGIN + COL_W + 5, 330, f"{GUTTER:.0f} mm", fontsize=18, color="#6E6E6E")
    return fig


def save_a0_pdf(fig: plt.Figure, stem: Path, language: str) -> None:
    stem.parent.mkdir(parents=True, exist_ok=True)
    setup_rc(10)
    save_figure(fig, stem, language, dpi=150)


def book_composite(final_fig_path: Path, wire_path: Path, language: str) -> None:
    setup_rc(10)
    fig, axes = plt.subplots(1, 2, figsize=(6.2, 4.5))
    for ax, img_path in zip(axes, (final_fig_path, wire_path)):
        im = Image.open(img_path)
        w, h = im.size
        target_w = 75 * 600 / 25.4  # 75 mm at 600 dpi in pixels for PNG export
        scale = target_w / w
        im = im.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
        ax.imshow(np.array(im))
        ax.axis("off")
    save_figure(fig, FIG12 / "ch12-06-a0-poster-layout", language, dpi=600, bbox_inches="tight", pad_inches=0.02)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--draft", action="store_true", help="Crowded poster C0 for squint test")
    args = parser.parse_args()
    assert_perovskite_metrics()
    if args.draft:
        for language in ("zh", "en"):
            fig = draw_draft_c0(language)
            out = FIG12 / "poster" / f"poster-c0-{language}.png"
            out.parent.mkdir(parents=True, exist_ok=True)
            fig.savefig(out, dpi=120, facecolor="white")
            plt.close(fig)
        print("draft C0 posters written")
        return

    poster_dir = FIG12 / "poster"
    poster_dir.mkdir(parents=True, exist_ok=True)
    for language in ("zh", "en"):
        final = draw_final(language)
        png_full = poster_dir / f"poster-a0-{language}.png"
        final.savefig(png_full, dpi=100, facecolor="white")
        plt.close(final)
        final = draw_final(language)
        save_a0_pdf(final, poster_dir / "poster-a0", language)
        wire = draw_wireframe(language)
        wire_png = poster_dir / f"poster-wireframe-{language}.png"
        wire.savefig(wire_png, dpi=100, facecolor="white")
        plt.close(wire)
        book_composite(png_full, wire_png, language)


if __name__ == "__main__":
    main()
