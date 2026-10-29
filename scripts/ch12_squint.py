#!/usr/bin/env python3
"""FIG ch12-08a/b: squint test (12 cm thumbnail + Gaussian blur)."""
# SPDX-License-Identifier: MIT
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from ch12_plot_utils import FIG12, save_figure, setup_rc  # noqa: E402

# Thumbnail height 12 cm at 150 dpi → ~709 px; blur σ ≈ 1.5 mm on thumbnail ≈ 8.9 px at 150 dpi.
THUMB_H_CM = 12.0
THUMB_DPI = 150
BLUR_SIGMA_PX = (1.5 / 10.0) * (THUMB_DPI / 2.54)  # 1.5 mm in thumbnail pixels


def thumbnail_and_blur(src: Path) -> tuple[np.ndarray, np.ndarray]:
    im = Image.open(src).convert("RGB")
    w, h = im.size
    target_h = int(THUMB_H_CM / 2.54 * THUMB_DPI)
    target_w = int(w * (target_h / h))
    thumb = im.resize((target_w, target_h), Image.Resampling.LANCZOS)
    blurred = thumb.filter(ImageFilter.GaussianBlur(radius=BLUR_SIGMA_PX))
    return np.array(thumb), np.array(blurred)


def compose_pair(c0: Path, final: Path, language: str, stem_a: str, stem_b: str) -> None:
    t0, b0 = thumbnail_and_blur(c0)
    t1, b1 = thumbnail_and_blur(final)
    setup_rc(10)
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.2))
    for ax, img, title in zip(
        axes,
        (t0, b0),
        ("12 cm thumbnail" if language == "en" else "12 cm 缩略图", "Blurred"),
    ):
        ax.imshow(img)
        ax.set_title(title, fontsize=10)
        ax.axis("off")
    save_figure(fig, FIG12 / stem_a, language, dpi=300, bbox_inches="tight", pad_inches=0.02)

    fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.2))
    for ax, img in zip(axes, (t1, b1)):
        ax.imshow(img)
        ax.axis("off")
    save_figure(fig, FIG12 / stem_b, language, dpi=300, bbox_inches="tight", pad_inches=0.02)


def main() -> None:
    poster = FIG12 / "poster"
    for language in ("zh", "en"):
        c0 = poster / f"poster-c0-{language}.png"
        final = poster / f"poster-a0-{language}.png"
        if not c0.is_file() or not final.is_file():
            raise SystemExit("Run ch12_poster.py --draft and ch12_poster.py first.")
        compose_pair(c0, final, language, "ch12-08a-dense-squint", "ch12-08b-focused-squint")
    print(f"blur_sigma_px={BLUR_SIGMA_PX:.2f}")


if __name__ == "__main__":
    main()
