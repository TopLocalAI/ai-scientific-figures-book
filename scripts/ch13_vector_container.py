#!/usr/bin/env python3
"""FIG ch13-05: vector PDF vs raster-in-PDF container (simulated J–V)."""
# SPDX-License-Identifier: MIT
import io
import subprocess
import sys
import tempfile
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
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
W_IN, H_IN = W_MM / MM_PER_IN, H_MM / MM_PER_IN
DPI_RASTER = 150
INSET = (0.52, 0.08, 0.38, 0.42)  # axis fraction for zoom on axis labels


def make_vector_pdf(path: Path, language: str):
    setup_rc(7)
    font = chinese_font() if language == "zh" else None
    labels = {
        "zh": {"x": "电压 (V)", "y": "电流密度 (mA/cm²)"},
        "en": {"x": "Voltage (V)", "y": "Current density (mA/cm²)"},
    }[language]
    fig, ax = plt.subplots(figsize=(W_IN, H_IN))
    groups = load_jv()
    plot_jv_on_ax(
        ax, groups,
        control_style={"linestyle": "--", "linewidth": 1.0},
        modified_style={"linestyle": "-", "linewidth": 1.0},
        labels=labels,
        font=font,
    )
    fig.savefig(path, format="pdf", facecolor="white", bbox_inches="tight", pad_inches=0.03)
    plt.close(fig)


def make_container_pdf(path: Path, language: str):
    setup_rc(7)
    labels = {
        "zh": {"x": "电压 (V)", "y": "电流密度 (mA/cm²)"},
        "en": {"x": "Voltage (V)", "y": "Current density (mA/cm²)"},
    }[language]
    fig, ax = plt.subplots(figsize=(W_IN, H_IN))
    groups = load_jv()
    plot_jv_on_ax(
        ax, groups,
        control_style={"linestyle": "--", "linewidth": 1.0},
        modified_style={"linestyle": "-", "linewidth": 1.0},
        labels=labels,
        font=chinese_font() if language == "zh" else None,
    )
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=DPI_RASTER, facecolor="white", bbox_inches="tight", pad_inches=0.03)
    plt.close(fig)
    buf.seek(0)
    img = Image.open(buf).convert("RGB")
    w_px = int(round(W_IN * DPI_RASTER))
    h_px = int(round(H_IN * DPI_RASTER))
    img = img.resize((w_px, h_px), Image.LANCZOS)
    fig2, ax2 = plt.subplots(figsize=(W_IN, H_IN))
    ax2.imshow(img, aspect="auto", extent=[0, W_IN, 0, H_IN * img.height / img.width])
    ax2.axis("off")
    fig2.savefig(path, format="pdf", facecolor="white", bbox_inches="tight", pad_inches=0)
    plt.close(fig2)


def pdf_to_panel(pdf_path: Path, title: str) -> np.ndarray:
    with tempfile.TemporaryDirectory() as tmp:
        prefix = Path(tmp) / "page"
        subprocess.run(
            ["pdftoppm", "-png", "-singlefile", "-r", "400", str(pdf_path), str(prefix)],
            check=True,
            timeout=60,
        )
        full = Image.open(f"{prefix}.png").convert("RGB")
    arr = np.asarray(full)
    h, w = arr.shape[:2]
    x0, y0, bw, bh = INSET
    ix0, iy0 = int(x0 * w), int((1 - y0 - bh) * h)
    ix1, iy1 = int((x0 + bw) * w), int((1 - y0) * h)
    crop = arr[iy0:iy1, ix0:ix1]
    mag = np.repeat(np.repeat(crop, 8, axis=0), 8, axis=1)

    canvas = np.ones((h, w + mag.shape[1] + 20, 3), dtype=np.uint8) * 255
    canvas[:, :w] = arr
    canvas[: mag.shape[0], w + 10 : w + 10 + mag.shape[1]] = mag[: canvas.shape[0], : mag.shape[1]]
    return canvas, title


def build(language: str):
    tmp = FIG / "_tmp-vector"
    tmp.mkdir(parents=True, exist_ok=True)
    vector_pdf = tmp / f"vector-{language}.pdf"
    container_pdf = tmp / f"container-{language}.pdf"
    make_vector_pdf(vector_pdf, language)
    make_container_pdf(container_pdf, language)

    titles = {
        "zh": ("矢量 PDF", "容器 PDF（150 ppi 位图）"),
        "en": ("Vector PDF", "Container PDF (150 ppi bitmap)"),
    }[language]
    left, t0 = pdf_to_panel(vector_pdf, titles[0])
    right, t1 = pdf_to_panel(container_pdf, titles[1])

    fig, axes = plt.subplots(1, 2, figsize=(W_IN * 2.2, H_IN * 1.05))
    font = chinese_font() if language == "zh" else None
    for ax, panel, title in zip(axes, (left, right), titles):
        ax.imshow(panel)
        ax.axis("off")
        ax.set_title(title, fontproperties=font, fontsize=9)
    save_figure(fig, FIG / "ch13-05-vector-vs-container", language)


def main():
    load_jv()
    for language in ("zh", "en"):
        build(language)
    print("vector/container panels written")


if __name__ == "__main__":
    main()
