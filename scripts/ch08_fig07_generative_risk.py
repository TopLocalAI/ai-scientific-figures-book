#!/usr/bin/env python3
"""FIG ch08-07: generative upscale risk comparison (six panels a–f)."""
# SPDX-License-Identifier: MIT
import json
import sys
from datetime import date
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
from PIL import Image

from ch08_figures import FIG07_GT_BOX, area_downsample_gray
from ch08_utils import (
    DATA,
    FIG,
    PROV,
    SOURCED,
    chinese_font,
    find_fabricated_structure_circles,
    nearest_upscale,
    register_rigid_to_gt,
    resize_gray_lanczos,
    rgb_png_to_gray_u8,
    save_pair,
    setup_rc,
    sha256,
    write_json,
)

ROOT = Path(__file__).resolve().parents[1]
AI_UPSCALE = FIG / "ch08-07-ai-upscaled-1.png"
LR_PATH = DATA / "fig07-input-lowres.png"
STEM = "ch08-07-generative-risk"


def load_gt() -> np.ndarray:
    leaf = SOURCED / "Leaf_epidermis.jpg"
    gray = np.array(Image.open(leaf).convert("L"))
    x0, y0, x1, y1 = FIG07_GT_BOX
    gt = gray[y0:y1, x0:x1]
    assert gt.shape == (512, 512)
    return gt


def load_lr(gt: np.ndarray) -> np.ndarray:
    if LR_PATH.is_file():
        lr = np.array(Image.open(LR_PATH).convert("L"))
        assert lr.shape == (128, 128)
        return lr
    return area_downsample_gray(gt.astype(np.float32), 4).astype(np.uint8)


def prepare_ai_for_compare(ai_path: Path) -> tuple[np.ndarray, dict]:
    raw = Image.open(ai_path)
    meta = {
        "source_path": str(ai_path.relative_to(ROOT)),
        "source_sha256": sha256(ai_path),
        "source_size": list(raw.size),
        "source_mode": raw.mode,
    }
    gray = rgb_png_to_gray_u8(ai_path)
    if gray.shape != (512, 512):
        gray = resize_gray_lanczos(gray, (512, 512))
        meta["resized_to_512"] = "Lanczos"
        meta["resize_from"] = list(Image.open(ai_path).size)
    return gray, meta


def panel_titles(language: str) -> list[tuple[str, str]]:
    if language == "zh":
        return [
            ("a", "地面真值"),
            ("b", "4× 降采样"),
            ("c", "双三次放大"),
            ("d", "生成式“增强”"),
            ("e", "|c-GT|"),
            ("f", "|d-GT|"),
        ]
    return [
        ("a", "Ground truth"),
        ("b", "4× downsampled"),
        ("c", "Bicubic upscale"),
        ("d", "Generative “enhancement”"),
        ("e", "|c-GT|"),
        ("f", "|d-GT|"),
    ]


def render_figure(
    language: str,
    gt: np.ndarray,
    lr_nn: np.ndarray,
    bicubic: np.ndarray,
    ai: np.ndarray,
    diff_b: np.ndarray,
    diff_a: np.ndarray,
    circles: list[dict],
    font,
) -> None:
    fig, axes = plt.subplots(2, 3, figsize=(7.3, 5.0))
    images = [gt, lr_nn, bicubic, ai, diff_b, diff_a]
    titles = panel_titles(language)
    for ax, img, (letter, subtitle) in zip(axes.ravel(), images, titles):
        if letter in ("e", "f"):
            ax.imshow(img, cmap="viridis", vmin=0, vmax=128, interpolation="nearest")
        else:
            ax.imshow(img, cmap="gray", vmin=0, vmax=255, interpolation="nearest")
        ax.set_title(f"({letter}) {subtitle}", fontproperties=font, fontsize=7, loc="left")
        ax.axis("off")
        if letter == "d":
            for spec in circles:
                ax.add_patch(
                    Circle(
                        (spec["cx"], spec["cy"]),
                        spec["radius_px"],
                        fill=False,
                        edgecolor="#f4d03f",
                        linewidth=0.75,
                    )
                )
            ai_tag = {
                "zh": "AI 生成——不是测量",
                "en": "AI-generated — not a measurement",
            }[language]
            ax.text(
                0.02,
                0.05,
                ai_tag,
                transform=ax.transAxes,
                color="red",
                fontproperties=font,
                fontsize=6,
                va="bottom",
            )
    fig.subplots_adjust(hspace=0.12, wspace=0.06)
    save_pair(fig, STEM, language)
    plt.close(fig)


def main() -> int:
    setup_rc()
    if not AI_UPSCALE.is_file():
        print(f"Missing {AI_UPSCALE}", file=sys.stderr)
        return 1

    gt = load_gt()
    lr = load_lr(gt)
    lr_nn = nearest_upscale(lr, 4)
    bicubic = np.array(Image.fromarray(lr).resize((512, 512), Image.BICUBIC))
    ai_raw, ai_prep_meta = prepare_ai_for_compare(AI_UPSCALE)
    ai, reg_meta = register_rigid_to_gt(gt, ai_raw)

    diff_b = np.abs(bicubic.astype(np.int16) - gt.astype(np.int16))
    diff_a = np.abs(ai.astype(np.int16) - gt.astype(np.int16))
    mae_bicubic = float(diff_b.mean())
    mae_ai = float(diff_a.mean())

    circles, circle_meta = find_fabricated_structure_circles(gt, bicubic, ai, count=3)
    if len(circles) < 2:
        circles, circle_meta = find_fabricated_structure_circles(
            gt, bicubic, ai, count=3, min_area=25
        )

    provenance = {
        "figure": STEM,
        "generated_on": date.today().isoformat(),
        "gt_crop": list(FIG07_GT_BOX),
        "lr_path": str(LR_PATH.relative_to(ROOT)),
        "lr_sha256": sha256(LR_PATH) if LR_PATH.is_file() else None,
        "ai_input": ai_prep_meta,
        "registration": reg_meta,
        "mae_bicubic": mae_bicubic,
        "mae_ai": mae_ai,
        "diff_colormap": {"name": "viridis", "vmin": 0, "vmax": 128},
        "fabricated_structure_circles": circles,
        "circle_detection": circle_meta,
    }
    write_json(PROV / "ch08-07-generative-risk.json", provenance)

    for lang in ("zh", "en"):
        font = chinese_font() if lang == "zh" else None
        render_figure(lang, gt, lr_nn, bicubic, ai, diff_b, diff_a, circles, font)

    print("FIG ch08-07 generative-risk complete")
    print(f"MAE bicubic vs GT: {mae_bicubic:.4f}")
    print(f"MAE AI (registered) vs GT: {mae_ai:.4f}")
    print(f"Registration: {json.dumps(reg_meta, ensure_ascii=False)}")
    print(f"Circles ({len(circles)}): {json.dumps(circles, ensure_ascii=False)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
