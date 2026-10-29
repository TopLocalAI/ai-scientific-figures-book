#!/usr/bin/env python3
"""FIG ch13-02a/b: upsampling vs native resolution (simulated J–V)."""
# SPDX-License-Identifier: MIT
import io
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from ch13_plot_utils import (  # noqa: E402
    FIG,
    MM_PER_IN,
    chinese_font,
    load_jv,
    plot_jv_on_ax,
    save_figure,
    setup_rc,
)

W_MM, H_MM = 85.0, 60.0
DPI_LOW, DPI_HIGH = 150, 600
PX_W = int(round(W_MM / MM_PER_IN * DPI_HIGH))
PX_H = int(round(H_MM / MM_PER_IN * DPI_HIGH))


def render_jv_raster(dpi: int) -> Image.Image:
    setup_rc(7)
    w_in = W_MM / MM_PER_IN
    h_in = H_MM / MM_PER_IN
    fig, ax = plt.subplots(figsize=(w_in, h_in))
    groups = load_jv()
    plot_jv_on_ax(
        ax, groups,
        control_style={"linestyle": "--", "linewidth": 1.0},
        modified_style={"linestyle": "-", "linewidth": 1.0},
        labels={"x": "V (V)", "y": "J (mA/cm²)"},
    )
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=dpi, facecolor="white", bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)
    buf.seek(0)
    return Image.open(buf).convert("RGB")


def compose_panel(full: Image.Image, caption: str, font=None) -> np.ndarray:
    inset_box=(0.55, 0.15, 0.35, 0.35)
    full = full.resize((PX_W, PX_H), Image.Resampling.LANCZOS if hasattr(Image, "Resampling") else Image.LANCZOS)
    w, h = full.size
    x0 = int(inset_box[0] * w)
    y0 = int((1 - inset_box[1] - inset_box[3]) * h)
    x1 = int((inset_box[0] + inset_box[2]) * w)
    y1 = int((1 - inset_box[1]) * h)
    crop = full.crop((x0, y0, x1, y1))
    mag = crop.resize((crop.width * 8, crop.height * 8), Image.BICUBIC)

    canvas_w = PX_W + int(PX_W * 0.45)
    canvas_h = PX_H + 40
    canvas = Image.new("RGB", (canvas_w, canvas_h), "white")
    canvas.paste(full, (0, 0))
    inset_x = PX_W + 10
    inset_y = max(0, (PX_H - mag.height) // 2)
    if inset_y + mag.height > canvas_h:
        mag = mag.resize((mag.width, canvas_h - inset_y - 5), Image.BICUBIC)
    canvas.paste(mag, (inset_x, inset_y))

    fig, ax = plt.subplots(figsize=(canvas_w / DPI_HIGH, canvas_h / DPI_HIGH), dpi=DPI_HIGH)
    ax.imshow(np.asarray(canvas))
    ax.axis("off")
    ax.text(
        0.02, 0.02, caption, transform=ax.transAxes, fontsize=8,
        va="bottom", ha="left", color="#23363E", fontproperties=font,
        bbox=dict(facecolor="white", edgecolor="#C8D6D6", alpha=0.9, pad=2),
    )
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=DPI_HIGH, facecolor="white", bbox_inches="tight", pad_inches=0)
    plt.close(fig)
    buf.seek(0)
    return np.asarray(Image.open(buf).convert("RGB"))


def build_figure(language: str, mode: str):
    labels = {
        "en": {
            "a": f"{PX_W} × {PX_H} px, 4× bicubic upsample",
            "b": f"{PX_W} × {PX_H} px, native {DPI_HIGH} dpi",
            "title": "Simulated J–V · upsampling demo",
        },
        "zh": {
            "a": f"{PX_W} × {PX_H} 像素，经 4× 双三次插值",
            "b": f"{PX_W} × {PX_H} 像素，直接 {DPI_HIGH} dpi 输出",
            "title": "模拟 J–V · 插值放大示意",
        },
    }[language]
    font = chinese_font() if language == "zh" else None
    low = render_jv_raster(DPI_LOW)
    low_up = low.resize((PX_W, PX_H), Image.BICUBIC)
    native = render_jv_raster(DPI_HIGH).resize((PX_W, PX_H), Image.LANCZOS)
    assert low_up.size == native.size == (PX_W, PX_H)

    if mode == "a":
        arr = compose_panel(low_up, labels["a"], font)
    else:
        arr = compose_panel(native, labels["b"], font)

    fig, ax = plt.subplots(figsize=(W_MM / MM_PER_IN * 1.35, H_MM / MM_PER_IN * 1.1))
    ax.imshow(arr)
    ax.axis("off")
    ax.set_title(labels["title"], fontproperties=font, fontsize=9)
    stem = FIG / f"ch13-02{mode}-upsampled" if mode == "a" else FIG / f"ch13-02b-native"
    if mode == "a":
        stem = FIG / "ch13-02a-upsampled"
    save_figure(fig, stem, language)


def main():
    load_jv()
    for mode in ("a", "b"):
        for language in ("zh", "en"):
            build_figure(language, mode)
    low_px = (
        int(round(W_MM / MM_PER_IN * DPI_LOW)),
        int(round(H_MM / MM_PER_IN * DPI_LOW)),
    )
    print(f"low_raster_px={low_px} high_px=({PX_W},{PX_H}) assert_same={PX_W * PX_H}")


if __name__ == "__main__":
    main()
