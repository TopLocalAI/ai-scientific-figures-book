#!/usr/bin/env python3
"""FIG ch09-06 / ch09-07: v1 cluttered vs v2 final multi-panel assemblies."""
# SPDX-License-Identifier: MIT
import argparse
import json
import subprocess
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec
from matplotlib.font_manager import FontProperties
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures" / "ch09"
PROV = ROOT / "provenance" / "ch09"
sys.path.insert(0, str(ROOT / "scripts"))
from ch09_plot_utils import (  # noqa: E402
    MM_PER_IN,
    chinese_font,
    plot_panel_c,
    plot_panel_d,
    save_figure,
    setup_rc,
    DATA_AX_POSITION,
)

CANVAS_W = 174.0


def panel_letter_font() -> FontProperties:
    """TeX Gyre Heros Bold. Helvetica.ttc does not embed a separate bold face."""
    font_path = subprocess.check_output(
        ["kpsewhich", "texgyreheros-bold.otf"], text=True, timeout=30
    ).strip()
    if not font_path:
        raise RuntimeError("texgyreheros-bold.otf not found")
    # fname is the bold cut (PDF/PNG). weight=bold makes PGF emit \\bfseries.
    return FontProperties(family="sans-serif", weight="bold", size=10, fname=font_path)


def panel_a_path(_language: str) -> Path:
    return FIG / "ch09-03-device-structure-base.png"


def panel_b_path(_language: str) -> Path:
    return FIG / "ch09-04-sem-like-illustration-base.png"


def codex_assets_ready(language: str) -> bool:
    return panel_a_path(language).is_file() and panel_b_path(language).is_file()


def mm_axes(fig, left_mm, bottom_mm, width_mm, height_mm, canvas_h_mm):
    return fig.add_axes([
        left_mm / CANVAS_W,
        bottom_mm / canvas_h_mm,
        width_mm / CANVAS_W,
        height_mm / canvas_h_mm,
    ])


def purple_shift(img: np.ndarray) -> np.ndarray:
    """Deliberate v1 error: shift teal passivation toward purple."""
    out = img.astype(float)
    mask = (out[..., 1] > out[..., 0] * 0.9) & (out[..., 1] > out[..., 2] * 0.8)
    out[..., 0][mask] = np.clip(out[..., 0][mask] * 0.6 + 80, 0, 255)
    out[..., 1][mask] *= 0.5
    out[..., 2][mask] = np.clip(out[..., 2][mask] * 1.2 + 40, 0, 255)
    return out.astype(np.uint8)


# Layer names sit in the base image's right-hand white margin (content ends ~x=0.65).
_LAYER_X = 0.672


def draw_device_labels(ax, language: str) -> None:
    font = chinese_font() if language == "zh" else None
    # SnO2 subscript is mathtext: Fandol has no U+2082 glyph (it draws as a box).
    sno2 = r"$\mathrm{SnO_2}$"
    rows = (
        [
            (_LAYER_X, 0.86, "Au", "black", "left", "center", True),
            (_LAYER_X, 0.76, "spiro-OMeTAD", "black", "left", "center", True),
            (_LAYER_X, 0.67, "钝化层", "#1B7F86", "left", "center", True),
            (_LAYER_X, 0.56, "钙钛矿", "black", "left", "center", True),
            (_LAYER_X, 0.45, sno2, "black", "left", "center", False),
            (_LAYER_X, 0.39, "FTO", "black", "left", "center", True),
            (_LAYER_X, 0.25, "玻璃", "black", "left", "center", True),
            (0.30, 0.06, "入射光", "black", "left", "center", True),
            (0.985, 0.015, "不按比例", "black", "right", "bottom", True),
        ]
        if language == "zh"
        else [
            (_LAYER_X, 0.86, "Au", "black", "left", "center", True),
            (_LAYER_X, 0.76, "spiro-OMeTAD", "black", "left", "center", True),
            (_LAYER_X, 0.67, "Passivation layer", "#1B7F86", "left", "center", True),
            (_LAYER_X, 0.56, "Perovskite", "black", "left", "center", True),
            (_LAYER_X, 0.45, sno2, "black", "left", "center", False),
            (_LAYER_X, 0.39, "FTO", "black", "left", "center", True),
            (_LAYER_X, 0.25, "Glass", "black", "left", "center", True),
            (0.30, 0.06, "Light", "black", "left", "center", True),
            (0.985, 0.015, "Not to scale", "black", "right", "bottom", True),
        ]
    )
    for x, y, text, color, ha, va, use_cjk in rows:
        ax.text(
            x, y, text, transform=ax.transAxes,
            fontproperties=font if use_cjk else None,
            fontsize=8, color=color, ha=ha, va=va, clip_on=False, zorder=4,
        )


def assemble_v1(language: str) -> dict:
    if not codex_assets_ready(language):
        print(f"SKIP v1: missing codex PNGs for {language}", file=sys.stderr)
        sys.exit(2)
    canvas_h = 120.0
    fig = plt.figure(figsize=(CANVAS_W / MM_PER_IN, canvas_h / MM_PER_IN))
    gs = gridspec.GridSpec(2, 2, figure=fig, wspace=0.08, hspace=0.22)
    gs.update(left=0.06, right=0.98, top=0.94, bottom=0.08)
    provenance = {"version": "v1", "deliberate_errors": []}

    ax_a = fig.add_subplot(gs[0, 0])
    img_a = np.array(Image.open(panel_a_path(language)).convert("RGB"))
    img_a = purple_shift(img_a)
    provenance["deliberate_errors"].append({"id": 3, "note": "passivation purple not teal"})
    ax_a.imshow(img_a, aspect="auto")
    ax_a.axis("off")
    ax_a.text(0.02, 0.98, "A", fontsize=14, fontfamily="serif", va="top", transform=ax_a.transAxes)
    provenance["deliberate_errors"].append({"id": 1, "note": "panel letter styles mixed"})

    ax_b = fig.add_subplot(gs[0, 1])
    img_b = np.array(Image.open(panel_b_path(language)).convert("RGB"))
    ax_b.imshow(img_b, aspect="auto")
    provenance["deliberate_errors"].append({"id": 7, "note": "b stretched aspect auto"})
    ax_b.axis("off")
    ax_b.text(0.98, 0.98, "(b)", fontsize=9, ha="right", va="top", transform=ax_b.transAxes)
    provenance["deliberate_errors"].append({"id": 9, "note": "missing model-generated label on b"})

    ax_c = fig.add_subplot(gs[1, 0])
    setup_rc(10)
    fig_c, ax_jv = plt.subplots(figsize=(8, 6))
    plot_panel_c(ax_jv, language, good=False)
    fig_c.canvas.draw()
    buf = fig_c.canvas.buffer_rgba()
    arr = np.asarray(buf)[..., :3]
    pos_c_ax = ax_jv.get_position()
    plt.close(fig_c)
    ax_c.imshow(arr, aspect="auto")
    ax_c.axis("off")
    ax_c.text(0.02, 0.95, "c.", fontsize=8, transform=ax_c.transAxes)
    provenance["deliberate_errors"].extend([
        {"id": 2, "note": "c replotted at 8x6 then scaled ~4.5pt ticks"},
        {"id": 4, "note": "both solid lines greyscale indistinguishable"},
        {"id": 5, "note": "legend box on c"},
        {"id": 10, "note": "panel title duplicates caption"},
    ])

    ax_d = fig.add_subplot(gs[1, 1])
    setup_rc(8)
    fig_d, ax_st = plt.subplots(
        figsize=(84 / MM_PER_IN, 56 / MM_PER_IN),
    )
    ax_st.set_position(list(DATA_AX_POSITION))
    plot_panel_d(ax_st, language, good=False)
    pos_d_ax = ax_st.get_position()
    fig_d.canvas.draw()
    buf_d = fig_d.canvas.buffer_rgba()
    arr_d = np.asarray(buf_d)[..., :3]
    plt.close(fig_d)
    ax_d.imshow(arr_d, aspect="auto")
    ax_d.axis("off")
    provenance["deliberate_errors"].extend([
        {"id": 3, "note": "d uses red/green not book palette"},
        {"id": 9, "note": "no 0.8 reference line on d"},
    ])

    pos_c = ax_c.get_position()
    pos_d = ax_d.get_position()
    cell_w_mm = pos_c.width * CANVAS_W
    cell_h_mm = pos_c.height * canvas_h
    misalign = {
        "left_mm": abs(pos_c_ax.x0 - pos_d_ax.x0) * cell_w_mm,
        "bottom_mm": abs(pos_c_ax.y0 - pos_d_ax.y0) * cell_h_mm,
    }
    provenance["axis_misalignment_mm"] = misalign
    provenance["deliberate_errors"].append({"id": 6, "note": "axis boxes misaligned", **misalign})
    provenance["deliberate_errors"].append({"id": 8, "note": "uneven panel spacing from gridspec"})

    out = FIG / f"ch09-06-assembly-v1"
    save_figure(fig, out, language, dpi=300)
    return provenance


def add_raster_panel(fig, left, bottom, width, height, img, canvas_h):
    """Place a raster at its own aspect. The axes box is exactly width × height mm."""
    ax = mm_axes(fig, left, bottom, width, height, canvas_h)
    ax.imshow(
        img,
        extent=(0, 1, 0, 1),
        origin="upper",
        aspect="auto",
        interpolation="lanczos",
        zorder=0,
    )
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("auto")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis("off")
    return ax


def _audit_v2(fig) -> list[str]:
    """Return human-readable text-placement lines. Raise if anything is clipped or < 8 pt."""
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    fw, fh = fig.canvas.get_width_height()
    dpi = fig.dpi
    lines = []
    problems = []
    for text in fig.findobj(match=lambda obj: isinstance(obj, plt.Text)):
        raw = text.get_text().replace("\n", " ")
        if not raw.strip() or not text.get_visible():
            continue
        size = float(text.get_fontsize())
        bb = text.get_window_extent(renderer=renderer)
        # 0.4 mm slack for antialiasing
        slack = 0.4 / 25.4 * dpi
        overflow = []
        if bb.x0 < -slack:
            overflow.append(f"left {bb.x0:.1f}px")
        if bb.y0 < -slack:
            overflow.append(f"bottom {bb.y0:.1f}px")
        if bb.x1 > fw + slack:
            overflow.append(f"right {bb.x1 - fw:.1f}px")
        if bb.y1 > fh + slack:
            overflow.append(f"top {bb.y1 - fh:.1f}px")
        flag = " CLIP" if overflow else ""
        if size < 7.99:
            flag += f" SMALL({size:.2f})"
            problems.append(f"{size:.2f} pt {raw!r}")
        if overflow:
            problems.append(f"clipped {raw!r}: {', '.join(overflow)}")
        lines.append(f"  {size:4.1f} pt{flag}  {raw}")
    if problems:
        raise SystemExit("v2 text audit failed:\n" + "\n".join(problems))
    return lines


def assemble_v2(language: str) -> None:
    if not codex_assets_ready(language):
        print(f"SKIP v2: missing codex PNGs for {language}", file=sys.stderr)
        sys.exit(2)

    # 2×2 frames. Column edges of a|c and b|d match the data spines.
    # Left block is the y-axis title plus tick labels; right pad keeps "1000" on the page.
    left_mm = 13.0
    ylabel_mm = 13.0
    col_gap_mm = 6.0
    right_mm = 4.0
    frame_w = (CANVAS_W - left_mm - col_gap_mm - ylabel_mm - right_mm) / 2.0
    col1 = left_mm
    col2 = left_mm + frame_w + col_gap_mm + ylabel_mm
    bottom_mm = 11.0
    data_h = 46.0
    row_gap = 8.0
    letter_gap = 1.0
    letter_band = 5.0
    assert abs(col2 + frame_w + right_mm - CANVAS_W) < 1e-6

    img_a = np.array(Image.open(panel_a_path(language)).convert("RGB"))
    img_b = np.array(Image.open(panel_b_path(language)).convert("RGB"))
    h_a = frame_w * img_a.shape[0] / img_a.shape[1]
    h_b = frame_w * img_b.shape[0] / img_b.shape[1]
    row_h = max(h_a, h_b)
    row_bottom = bottom_mm + data_h + row_gap
    canvas_h = row_bottom + row_h + letter_band

    fig = plt.figure(figsize=(CANVAS_W / MM_PER_IN, canvas_h / MM_PER_IN))
    fig.patch.set_facecolor("white")
    setup_rc(8)
    font = chinese_font() if language == "zh" else None

    ax_a = add_raster_panel(
        fig, col1, row_bottom + (row_h - h_a), frame_w, h_a, img_a, canvas_h,
    )
    draw_device_labels(ax_a, language)

    ax_b = add_raster_panel(
        fig, col2, row_bottom + (row_h - h_b), frame_w, h_b, img_b, canvas_h,
    )
    b_note = (
        "模型生成示意，非显微图像" if language == "zh"
        else "Model-generated illustration,\nnot a micrograph"
    )
    ax_b.text(
        0.025, 0.04, b_note,
        transform=ax_b.transAxes,
        fontproperties=font,
        fontsize=8,
        ha="left",
        va="bottom",
        color="black",
        zorder=5,
        bbox={
            "boxstyle": "square,pad=0.28",
            "facecolor": "white",
            "edgecolor": "none",
            "alpha": 0.88,
        },
    )

    ax_c = mm_axes(fig, col1, bottom_mm, frame_w, data_h, canvas_h)
    plot_panel_c(ax_c, language, good=True)
    ax_d = mm_axes(fig, col2, bottom_mm, frame_w, data_h, canvas_h)
    plot_panel_d(ax_d, language, good=True)

    pos_a, pos_b = ax_a.get_position(), ax_b.get_position()
    pos_c, pos_d = ax_c.get_position(), ax_d.get_position()
    assert abs(pos_a.x0 - pos_c.x0) < 1e-6
    assert abs(pos_a.x1 - pos_c.x1) < 1e-6
    assert abs(pos_b.x0 - pos_d.x0) < 1e-6
    assert abs(pos_b.x1 - pos_d.x1) < 1e-6
    assert abs(pos_c.y0 - pos_d.y0) < 1e-6
    assert abs(pos_c.height - pos_d.height) < 1e-6
    assert abs(pos_c.width - pos_d.width) < 1e-6
    assert abs(pos_a.y1 - pos_b.y1) < 1e-6

    row_top = row_bottom + row_h
    data_top = bottom_mm + data_h
    letters = {
        "a": (col1, row_top),
        "b": (col2, row_top),
        "c": (col1, data_top),
        "d": (col2, data_top),
    }
    letter_font = panel_letter_font()
    for letter, (x_mm, top_mm) in letters.items():
        fig.text(
            x_mm / CANVAS_W,
            (top_mm + letter_gap) / canvas_h,
            letter,
            fontproperties=letter_font,
            fontsize=10,
            va="bottom",
            ha="left",
            color="black",
            zorder=6,
        )

    audit_lines = _audit_v2(fig)
    stem = FIG / "ch09-07-assembly-final"
    stale_tif = FIG / "ch09-07-assembly-final-en-600dpi.tif"
    if stale_tif.exists():
        stale_tif.unlink()
    save_figure(fig, stem, language, dpi=300)
    print(
        json.dumps(
            {
                "lang": language,
                "canvas_mm": [CANVAS_W, round(canvas_h, 3)],
                "frame_w_mm": round(frame_w, 3),
                "columns_mm": [round(col1, 3), round(col2, 3)],
                "image_h_mm": [round(h_a, 3), round(h_b, 3)],
                "data_box_mm": [round(bottom_mm, 3), round(data_h, 3)],
                "texts": audit_lines,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", choices=("v1", "v2"), required=True)
    parser.add_argument("--lang", choices=("zh", "en"), required=True)
    args = parser.parse_args()
    PROV.mkdir(parents=True, exist_ok=True)
    if args.version == "v1":
        meta = assemble_v1(args.lang)
        (PROV / "ch09-06.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(meta, indent=2))
    else:
        assemble_v2(args.lang)
        print(f"v2 assembly written for {args.lang}")


if __name__ == "__main__":
    main()
