#!/usr/bin/env python3
"""Generate chapter 8 python figures and provenance."""
# SPDX-License-Identifier: MIT
import io
import json
from datetime import date
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
from PIL import Image

from ch08_fetch import fetch_bbbc, fetch_sourced, write_case_catalog, write_sourced_md
from ch08_utils import (
    BBBC_FILES,
    DATA,
    FIG,
    HOECHST_RANGE,
    MITO_RANGE,
    MACHADO_DEUTERANOPIA,
    MACHADO_PROTANOPIA,
    PROV,
    RAW,
    SOURCED,
    UM_PER_PX_U2OS,
    check_bbbc_array,
    chinese_font,
    draw_scale_bar,
    fraction_mapped_white,
    gamma_display_u8,
    linear_display_u8,
    load_tiff,
    merge_magenta_green,
    merge_red_green,
    nearest_upscale,
    panel_letter,
    save_pair,
    setup_rc,
    sha256,
    simulate_cvd,
    style_spines,
    write_json,
)

ROOT = Path(__file__).resolve().parents[1]

# Fixed ROIs for fig 8-02 (15×15 px on mito s1)
FIG02_ROIS = {
    "bright": (340, 210, 355, 225),
    "dim": (120, 380, 135, 395),
}

# Fig 8-04 crop on s1 fields
FIG04_CROP = (198, 110, 498, 410)

# Fig 8-05 leaf SEM (S3)
LEAF_UM_PER_PX = 200.0 / 720.0
FIG05_CROP = (480, 320, 1504, 1344)  # 1024×1024
FIG05_INSET = (900, 720, 1100, 920)  # 200×200 stomata region

# Fig 8-07 ground-truth crop (512×512 above data bar)
FIG07_GT_BOX = (640, 680, 1152, 1192)

# Fig 8-08 final inset (filled after cell search)
FIG08_INSET_BOX: Optional[Tuple[int, int, int, int]] = None


def roi_mean(arr: np.ndarray, box: Tuple[int, int, int, int]) -> float:
    x0, y0, x1, y1 = box
    return float(arr[y0:y1, x0:x1].mean())


def roi_ratio_raw(arr: np.ndarray, box_a, box_b, black: float) -> Tuple[float, float]:
    a = roi_mean(arr, box_a) - black
    b = roi_mean(arr, box_b) - black
    raw = a / b if b else float("inf")
    return raw, a


def display_ratio(disp_a: float, disp_b: float) -> float:
    return disp_a / disp_b if disp_b else float("inf")


def measure_leaf_scale_px(gray: np.ndarray) -> int:
    """Longest dark horizontal run on instrument scale rows."""
    rows = gray[2048:2054, :]
    best = (0, 0, 0)
    for row in rows:
        mask = row < 80
        x = 0
        while x < len(row):
            if not mask[x]:
                x += 1
                continue
            start = x
            while x < len(row) and mask[x]:
                x += 1
            length = x - start
            if length > best[0]:
                best = (length, start, x - 1)
    length, x0, x1 = best
    assert abs(length - 720) <= 2, f"scale bar length {length}, expected 720"
    return length


def pick_median_cell_box(hoechst: np.ndarray, mito: np.ndarray, size: int = 64) -> Tuple[int, int, int, int]:
    h, w = hoechst.shape
    scores = []
    boxes = []
    step = 16
    for y in range(40, h - size - 40, step):
        for x in range(40, w - size - 40, step):
            hb = hoechst[y : y + size, x : x + size]
            mb = mito[y : y + size, x : x + size]
            if hb.mean() < 200 or mb.mean() < 250:
                continue
            score = float(hb.mean() + mb.mean())
            scores.append(score)
            boxes.append((x, y, x + size, y + size))
    assert scores, "no candidate inset region"
    med = float(np.median(scores))
    idx = int(np.argmin(np.abs(np.array(scores) - med)))
    return boxes[idx]


def pick_brightest_cell(hoechst: np.ndarray, size: int = 64) -> Tuple[int, int, int, int]:
    h, w = hoechst.shape
    best = (-1.0, (0, 0, size, size))
    for y in range(40, h - size - 40, 8):
        for x in range(40, w - size - 40, 8):
            m = float(hoechst[y : y + size, x : x + size].mean())
            if m > best[0]:
                best = (m, (x, y, x + size, y + size))
    return best[1]


def area_downsample_gray(arr: np.ndarray, factor: int) -> np.ndarray:
    h, w = arr.shape
    h2, w2 = h // factor, w // factor
    block = arr[: h2 * factor, : w2 * factor].reshape(h2, factor, w2, factor)
    return block.mean(axis=(1, 3)).astype(np.float32)


def fig01(language: str, hoechst: np.ndarray, font) -> dict:
    labels = {
        "zh": {
            "cols": [
                "(a) 16 位全范围 0–65535",
                "(b) 最小值–最大值",
                "(c) 0.1%–99.9% 分位数",
            ],
            "x": "原始数值（12 位，a.u.）",
            "y": "像素数（对数）",
            "white": "映射为纯白的像素：{pct:.2f}%",
        },
        "en": {
            "cols": [
                "(a) Full 16-bit range 0–65535",
                "(b) Image min–max",
                "(c) 0.1th–99.9th percentile",
            ],
            "x": "Raw value (12-bit, a.u.)",
            "y": "Pixel count (log)",
            "white": "Pixels mapped to white: {pct:.2f}%",
        },
    }[language]
    vmin_max = [
        (0, 65535),
        (int(hoechst.min()), int(hoechst.max())),
        HOECHST_RANGE,
    ]
    meta = {"mappings": []}
    fig = plt.figure(figsize=(7.3, 5.6))
    gs = GridSpec(2, 3, figure=fig, height_ratios=[1.1, 1.0], hspace=0.35, wspace=0.25)
    for col, (vmin, vmax) in enumerate(vmin_max):
        disp = linear_display_u8(hoechst, vmin, vmax)
        pct = fraction_mapped_white(hoechst, vmin, vmax) * 100
        meta["mappings"].append({"vmin": vmin, "vmax": vmax, "white_fraction_pct": pct})
        ax = fig.add_subplot(gs[0, col])
        ax.imshow(disp, cmap="gray", vmin=0, vmax=255, interpolation="nearest")
        ax.set_title(labels["cols"][col], fontproperties=font, fontsize=8)
        ax.axis("off")
        ax.text(
            0.5,
            -0.06,
            labels["white"].format(pct=pct),
            transform=ax.transAxes,
            ha="center",
            fontproperties=font,
            fontsize=7,
        )
        axh = fig.add_subplot(gs[1, col])
        hist, edges = np.histogram(hoechst.ravel(), bins=80, range=(0, 4095))
        centers = 0.5 * (edges[:-1] + edges[1:])
        axh.semilogy(centers, hist + 1, color="#444444", linewidth=0.8)
        xs = np.linspace(0, 4095, 256)
        mapped = np.clip((xs - vmin) / (vmax - vmin), 0, 1) * 255
        axh2 = axh.twinx()
        axh2.plot(xs, mapped, color="#B5653A", linewidth=1.2)
        axh2.set_ylim(0, 280)
        axh2.set_yticks([])
        axh.axvline(vmin, color="#398D88", linewidth=0.8)
        axh.axvline(vmax, color="#398D88", linewidth=0.8)
        if col == 0:
            axh.set_ylabel(labels["y"], fontproperties=font)
        axh.set_xlabel(labels["x"], fontproperties=font)
        axh.set_xlim(0, 4095)
        style_spines(axh)
        axh.spines["right"].set_visible(False)
    save_pair(fig, "ch08-01-raw-display-mapping", language)
    plt.close(fig)
    return meta


def fig02(language: str, mito: np.ndarray, font) -> dict:
    vmin, vmax = MITO_RANGE
    p90 = float(np.percentile(mito, 90))
    meta = {
        "linear_range": [vmin, vmax],
        "gamma": 0.5,
        "clip_white_point": p90,
        "rois": FIG02_ROIS,
    }
    cols = [
        ("linear", linear_display_u8(mito, vmin, vmax), vmin, vmax, None),
        ("gamma", gamma_display_u8(mito, vmin, vmax, 0.5), vmin, vmax, "γ 0.5"),
        ("clip", linear_display_u8(mito, vmin, p90), vmin, p90, "✗"),
    ]
    meta["white_fraction_clip_pct"] = fraction_mapped_white(mito, vmin, p90) * 100
    fig = plt.figure(figsize=(7.3, 5.8))
    gs = GridSpec(2, 3, figure=fig, height_ratios=[1.0, 0.55], hspace=0.4)
    ratios = []
    for col, (_, disp, lo, hi, tag) in enumerate(cols):
        ax = fig.add_subplot(gs[0, col])
        ax.imshow(disp, cmap="gray", vmin=0, vmax=255, interpolation="nearest")
        ax.axis("off")
        titles = {
            "zh": ["(a) 线性", "(b) γ 0.5（须披露）", "(c) 白点过低 ✗"],
            "en": ["(a) Linear", "(b) γ 0.5 (disclose)", "(c) Low white point ✗"],
        }[language]
        ax.set_title(titles[col], fontproperties=font, fontsize=8)
        br, dr = FIG02_ROIS["bright"], FIG02_ROIS["dim"]
        ba = roi_mean(disp, br)
        da = roi_mean(disp, dr)
        raw_r, _ = roi_ratio_raw(mito, br, dr, vmin)
        disp_r = display_ratio(ba, da)
        ratios.append({"raw_ratio": raw_r, "display_ratio": disp_r})
        ax.plot([br[0], br[2]], [br[1], br[3]], color="#00FFFF", linewidth=0.6)
        ax.plot([dr[0], dr[2]], [dr[1], dr[3]], color="#FFFF00", linewidth=0.6)
    meta["intensity_ratios"] = ratios
    axc = fig.add_subplot(gs[1, :])
    xs = np.linspace(0, 1, 256)
    axc.plot(xs, xs, label="linear", color="#444444")
    axc.plot(xs, xs ** 0.5, label="γ 0.5", color="#B5653A")
    clip = np.clip((xs * (vmax - vmin) + vmin - vmin) / (p90 - vmin), 0, 1)
    axc.plot(xs, clip, label="clip", color="#888888")
    axc.set_xlim(0, 1)
    axc.set_ylim(0, 1)
    axc.legend(fontsize=7, loc="lower right")
    tbl = {
        "zh": ["原始比值", "显示比值"],
        "en": ["Raw ratio", "Display ratio"],
    }[language]
    text = "  ".join(f"{tbl[0]}: {ratios[0]['raw_ratio']:.2f}")
    for i, r in enumerate(ratios):
        text += f"  |  {tbl[1]} col{i+1}: {r['display_ratio']:.2f}"
    axc.text(0.02, 0.95, text, transform=axc.transAxes, fontproperties=font, fontsize=7, va="top")
    save_pair(fig, "ch08-02-linear-vs-gamma", language)
    plt.close(fig)
    return meta


def fig03(language: str, m1: np.ndarray, m2: np.ndarray, font) -> dict:
    shared = MITO_RANGE
    wrong = (196, 700)
    meta = {
        "mean_s1": float(m1.mean()),
        "mean_s2": float(m2.mean()),
        "wrong_range_s2": list(wrong),
        "shared_range": list(shared),
    }
    assert abs(meta["mean_s1"] - 373.2) < 0.05
    assert abs(meta["mean_s2"] - 366.3) < 0.05
    fig, axes = plt.subplots(2, 3, figsize=(7.3, 4.8), gridspec_kw={"width_ratios": [1, 1, 0.55]})
    rows = [
        (linear_display_u8(m1, *shared), linear_display_u8(m2, *wrong), "wrong"),
        (linear_display_u8(m1, *shared), linear_display_u8(m2, *shared), "ok"),
    ]
    row_titles = {
        "zh": ["分别调整（反例）", "同一显示设置（正确）"],
        "en": ["Separate settings (bad)", "Shared settings (ok)"],
    }[language]
    for r, (d1, d2, _) in enumerate(rows):
        for c, disp in enumerate((d1, d2)):
            axes[r, c].imshow(disp, cmap="gray", vmin=0, vmax=255, interpolation="nearest")
            axes[r, c].axis("off")
        axes[r, 0].set_ylabel(row_titles[r], fontproperties=font, fontsize=8)
    bars = axes[0, 2].bar([0, 1], [meta["mean_s1"], meta["mean_s2"]], color=["#518F8A", "#518F8A"])
    axes[1, 2].axis("off")
    ylab = {"zh": "原始平均强度（a.u.）", "en": "Mean raw intensity (a.u.)"}[language]
    axes[0, 2].set_ylabel(ylab, fontproperties=font, fontsize=7)
    axes[0, 2].set_xticks([0, 1], ["s1", "s2"])
    note = {"zh": "原始数值接近", "en": "Raw values similar"}[language]
    axes[0, 2].text(0.5, 0.9, note, transform=axes[0, 2].transAxes, ha="center", fontproperties=font, fontsize=7)
    fig.subplots_adjust(hspace=0.25, wspace=0.15)
    save_pair(fig, "ch08-03-consistent-display", language)
    plt.close(fig)
    return meta


def fig04(language: str, hoechst: np.ndarray, mito: np.ndarray, font) -> dict:
    x0, y0, x1, y1 = FIG04_CROP
    h = hoechst[y0:y1, x0:x1]
    m = mito[y0:y1, x0:x1]
    hn = linear_display_u8(h, *HOECHST_RANGE)
    mn = linear_display_u8(m, *MITO_RANGE)
    rg = merge_red_green(hn, mn)
    mg = merge_magenta_green(hn, mn)
    meta = {"crop": list(FIG04_CROP), "ranges": {"hoechst": HOECHST_RANGE, "mito": MITO_RANGE}}
    col_titles = {
        "zh": [
            "细胞核",
            "线粒体",
            "合成 红/绿 ✗",
            "绿色盲模拟",
            "品红/绿 ✓",
            "绿色盲",
            "红色盲",
            "图例",
        ],
        "en": [
            "Nuclei",
            "Mitochondria",
            "Merge red/green ✗",
            "Deuteranopia sim.",
            "Magenta/green ✓",
            "Deuteranopia",
            "Protanopia",
            "Key",
        ],
    }[language]
    panels = [
        hn,
        mn,
        rg,
        simulate_cvd(rg, MACHADO_DEUTERANOPIA),
        mg,
        simulate_cvd(mg, MACHADO_DEUTERANOPIA),
        simulate_cvd(mg, MACHADO_PROTANOPIA),
        None,
    ]
    fig, axes = plt.subplots(2, 4, figsize=(7.3, 4.2))
    for idx, ax in enumerate(axes.ravel()):
        if panels[idx] is None:
            ax.axis("off")
            legend = {
                "zh": "M=核\nG=线粒体",
                "en": "M=nuclei\nG=mito",
            }[language]
            ax.text(0.1, 0.6, legend, fontproperties=font, fontsize=7)
            continue
        if panels[idx].ndim == 2:
            ax.imshow(panels[idx], cmap="gray", vmin=0, vmax=255, interpolation="nearest")
        else:
            ax.imshow(panels[idx], interpolation="nearest")
        ax.set_title(col_titles[idx], fontproperties=font, fontsize=7)
        ax.axis("off")
    fig.subplots_adjust(hspace=0.35, wspace=0.08)
    save_pair(fig, "ch08-04-pseudocolor-colorblind", language)
    plt.close(fig)
    return meta


def fig05(language: str, leaf_path: Path, font) -> dict:
    gray = np.array(Image.open(leaf_path).convert("L"))
    scale_px = measure_leaf_scale_px(gray)
    meta = {
        "scale_px": scale_px,
        "um_per_px": LEAF_UM_PER_PX,
        "crop": list(FIG05_CROP),
        "inset_box": list(FIG05_INSET),
        "wrong_scale_deliberately_wrong": True,
    }
    fig = plt.figure(figsize=(7.3, 6.2))
    gs = GridSpec(2, 2, figure=fig, hspace=0.2, wspace=0.12)
    ax_a = fig.add_subplot(gs[0, 0])
    ax_a.imshow(gray, cmap="gray", vmin=0, vmax=255, interpolation="nearest")
    ax_a.set_title("(a)", fontproperties=font, fontsize=9, loc="left")
    ax_a.axis("off")
    note = {
        "zh": "200 µm = 720 px → 0.278 µm/px",
        "en": "200 µm = 720 px → 0.278 µm/px",
    }[language]
    ax_a.text(0.02, 0.02, note, transform=ax_a.transAxes, color="yellow", fontproperties=font, fontsize=6)
    ax_b = fig.add_subplot(gs[0, 1])
    small = gray[600:1200, 700:1300]
    bad = np.array(Image.fromarray(small).resize((small.shape[1] * 4, small.shape[0] * 4), Image.BICUBIC))
    ax_b.imshow(bad, cmap="gray", vmin=0, vmax=255, interpolation="nearest")
    ax_b.set_title("(b) ✗", fontproperties=font, fontsize=9, loc="left")
    ax_b.axis("off")
    wrong_px = 100.0 / LEAF_UM_PER_PX
    draw_scale_bar(ax_b, wrong_px, LEAF_UM_PER_PX, 50.0)
    x0, y0, x1, y1 = FIG05_CROP
    crop = gray[y0:y1, x0:x1]
    ax_c = fig.add_subplot(gs[1, 0])
    ax_c.imshow(crop, cmap="gray", vmin=0, vmax=255, interpolation="nearest")
    ix0, iy0, ix1, iy1 = FIG05_INSET
    rect = plt.Rectangle(
        (ix0 - x0, iy0 - y0),
        ix1 - ix0,
        iy1 - iy0,
        fill=False,
        edgecolor="white",
        linewidth=0.8,
    )
    ax_c.add_patch(rect)
    draw_scale_bar(ax_c, 360, LEAF_UM_PER_PX, 100.0)
    ax_c.set_title("(c)", fontproperties=font, fontsize=9, loc="left")
    ax_c.axis("off")
    inset = crop[iy0 - y0 : iy1 - y0, ix0 - x0 : ix1 - x0]
    inset_up = nearest_upscale(inset, 3)
    ax_d = fig.add_subplot(gs[1, 1])
    ax_d.imshow(inset_up, cmap="gray", vmin=0, vmax=255, interpolation="nearest")
    draw_scale_bar(ax_d, 72 * 3, LEAF_UM_PER_PX, 20.0)
    ax_d.set_title("(d)", fontproperties=font, fontsize=9, loc="left")
    ax_d.axis("off")
    save_pair(fig, "ch08-05-crop-inset-scalebar", language)
    plt.close(fig)
    return meta


def fig06(language: str, path: Path, font) -> dict:
    rgb = np.array(Image.open(path).convert("RGB"))
    meta = {"size": list(rgb.shape[:2][::-1]), "calibration": None}
    fig, axes = plt.subplots(2, 2, figsize=(7.0, 5.5))
    axes[0, 0].imshow(rgb, interpolation="nearest")
    axes[0, 0].set_title("(a)", fontproperties=font, loc="left")
    axes[0, 0].axis("off")
    card = {
        "zh": "8 位×3 · JPEG · 像素尺寸：未知",
        "en": "8-bit×3 · JPEG · pixel size: unknown",
    }[language]
    axes[0, 0].text(0.02, 0.05, card, transform=axes[0, 0].transAxes, color="white", fontproperties=font, fontsize=7)
    axes[0, 1].imshow(rgb, interpolation="nearest")
    axes[0, 1].set_title("(b) ✗", fontproperties=font, loc="left")
    axes[0, 1].axis("off")
    h, w = rgb.shape[:2]
    axes[0, 1].plot([w - 80, w - 20], [20, 20], color="white", linewidth=2)
    axes[1, 0].imshow(rgb, interpolation="nearest")
    tag = {"zh": "未校准", "en": "uncalibrated"}[language]
    axes[1, 0].text(0.7, 0.05, tag, transform=axes[1, 0].transAxes, color="yellow", fontproperties=font)
    axes[1, 0].set_title("(c)", fontproperties=font, loc="left")
    axes[1, 0].axis("off")
    patch = rgb[200:280, 200:280]
    up = nearest_upscale(patch, 4)
    axes[1, 1].imshow(up, interpolation="nearest")
    axes[1, 1].set_title("(d)", fontproperties=font, loc="left")
    axes[1, 1].axis("off")
    fig.subplots_adjust(hspace=0.15, wspace=0.08)
    save_pair(fig, "ch08-06-no-calibration", language)
    plt.close(fig)
    return meta


def prepare_fig07_input(leaf_path: Path) -> dict:
    gray = np.array(Image.open(leaf_path).convert("L"))
    x0, y0, x1, y1 = FIG07_GT_BOX
    gt = gray[y0:y1, x0:x1]
    assert gt.shape == (512, 512)
    lr = area_downsample_gray(gt.astype(np.float32), 4).astype(np.uint8)
    assert lr.shape == (128, 128)
    out = DATA / "fig07-input-lowres.png"
    Image.fromarray(lr).save(out)
    meta = {
        "gt_box": list(FIG07_GT_BOX),
        "downsample_factor": 4,
        "lr_path": str(out.relative_to(ROOT)),
        "gt_sha256": sha256(out),
    }
    return meta, gt, lr


def find_ai_upscale() -> Optional[Path]:
    for pattern in (
        FIG / "ch08-07-ai-upscaled-run1.png",
        FIG / "work/ch08-07-codex-upscaled-run1.png",
        FIG / "ch08-07-ai-upscaled.png",
    ):
        if pattern.is_file():
            return pattern
    return None


def fig07(language: str, gt: np.ndarray, lr: np.ndarray, font) -> Tuple[dict, bool]:
    bicubic = np.array(
        Image.fromarray(lr).resize((512, 512), Image.BICUBIC)
    )
    ai_path = find_ai_upscale()
    complete = ai_path is not None
    meta = {
        "gt_crop": list(FIG07_GT_BOX),
        "lr_shape": list(lr.shape),
        "codex_output": str(ai_path.relative_to(ROOT)) if ai_path else None,
        "complete": complete,
    }
    if not complete:
        save_pair_placeholder07(language, gt, lr, bicubic, font)
        return meta, False
    ai = np.array(Image.open(ai_path).convert("L"))
    if ai.shape != (512, 512):
        ai = np.array(Image.fromarray(ai).resize((512, 512), Image.LANCZOS))
        meta["ai_resized_to_512"] = True
    diff_b = np.abs(bicubic.astype(np.int16) - gt.astype(np.int16))
    diff_a = np.abs(ai.astype(np.int16) - gt.astype(np.int16))
    meta["mae_bicubic"] = float(diff_b.mean())
    meta["mae_ai"] = float(diff_a.mean())
    fig, axes = plt.subplots(2, 3, figsize=(7.3, 5.0))
    panels = [
        (gt, "(a) GT"),
        (lr, "(b) LR"),
        (bicubic, "(c) bicubic"),
        (ai, "(d) AI"),
        (diff_b, "(e) |c−GT|"),
        (diff_a, "(f) |d−GT|"),
    ]
    for ax, (img, title) in zip(axes.ravel(), panels):
        if title.startswith("(e") or title.startswith("(f"):
            ax.imshow(img, cmap="viridis", vmin=0, vmax=128, interpolation="nearest")
        else:
            ax.imshow(img, cmap="gray", vmin=0, vmax=255, interpolation="nearest")
        ax.set_title(title, fontproperties=font, fontsize=7, loc="left")
        ax.axis("off")
    ai_tag = {
        "zh": "AI 生成——不是测量",
        "en": "AI-generated — not a measurement",
    }[language]
    axes[1, 0].text(0.02, 0.05, ai_tag, transform=axes[1, 0].transAxes, color="red", fontproperties=font, fontsize=6)
    save_pair(fig, "ch08-07-ai-enhancement", language)
    plt.close(fig)
    return meta, True


def save_pair_placeholder07(language, gt, lr, bicubic, font):
    fig, axes = plt.subplots(1, 3, figsize=(7.0, 2.5))
    for ax, img, t in zip(
        axes,
        (gt, lr, bicubic),
        ("(a) GT", "(b) LR 4× down", "(c) bicubic"),
    ):
        ax.imshow(img, cmap="gray", vmin=0, vmax=255, interpolation="nearest")
        ax.set_title(t, fontproperties=font, fontsize=7)
        ax.axis("off")
    note = {
        "zh": "等待 Codex 生成式放大输出",
        "en": "Awaiting Codex generative upscale output",
    }[language]
    fig.suptitle(note, fontproperties=font, fontsize=9)
    save_pair(fig, "ch08-07-ai-enhancement", language)
    plt.close(fig)


def build_case_panels(hoechst, mito, final: bool) -> Tuple[dict, dict]:
    hn = linear_display_u8(hoechst, *HOECHST_RANGE)
    mn = linear_display_u8(mito, *MITO_RANGE)
    global FIG08_INSET_BOX
    if final:
        box = pick_median_cell_box(hoechst, mito)
        FIG08_INSET_BOX = box
        merge = merge_magenta_green(hn, mn)
        x0, y0, x1, y1 = box
        panels = {"a": hn, "b": mn, "c": merge, "d": None}
        meta = {
            "final": True,
            "inset_box": list(box),
            "hoechst_range": list(HOECHST_RANGE),
            "mito_range": list(MITO_RANGE),
            "scale_ac_um": 50,
            "scale_ac_px": 50 / UM_PER_PX_U2OS,
            "scale_d_um": 10,
            "scale_d_px": (10 / UM_PER_PX_U2OS) * 3,
            "saturated_mito_pixels": int((mito >= 4095).sum()),
        }
        crop_h = hoechst[y0:y1, x0:x1]
        crop_m = mito[y0:y1, x0:x1]
        ch = linear_display_u8(crop_h, *HOECHST_RANGE)
        cm = linear_display_u8(crop_m, *MITO_RANGE)
        panels["d"] = nearest_upscale(merge_magenta_green(ch, cm), 3)
        log = meta.copy()
        log["linear_no_gamma"] = True
        return panels, meta, log, None
    box = pick_brightest_cell(hoechst)
    h_min, h_max = int(hoechst.min()), int(hoechst.max())
    m_min, m_max = int(mito.min()), int(mito.max())
    hn_v = linear_display_u8(hoechst, h_min, h_max)
    mn_v = gamma_display_u8(mito, m_min, m_max, 0.6)
    merge = merge_red_green(hn_v, mn_v)
    x0, y0, x1, y1 = box
    crop = merge[y0:y1, x0:x1]
    up = np.array(Image.fromarray(crop).resize((crop.shape[1] * 4, crop.shape[0] * 4), Image.BICUBIC))
    panels = {"a": hn_v, "b": mn_v, "c": merge, "d": up}
    meta = {
        "final": False,
        "deliberate_error": True,
        "per_panel_autocontrast": True,
        "red_green_merge": True,
        "wrong_scale_px": 50,
        "wrong_scale_label_um": 20,
        "gamma_mito": 0.6,
        "inset_brightest_cell": list(box),
        "bicubic_x4": True,
    }
    return panels, meta, meta, None


def render_case_figure(language: str, panels: dict, meta: dict, font, stem: str) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(7.0, 5.5))
    letters = ["a", "b", "c", "d"]
    for ax, letter in zip(axes.ravel(), letters):
        img = panels[letter]
        if img.ndim == 2:
            ax.imshow(img, cmap="gray", vmin=0, vmax=255, interpolation="nearest")
        else:
            ax.imshow(img, interpolation="nearest")
        panel_letter(ax, letter, font)
        ax.axis("off")
        if letter in ("a", "b", "c") and meta.get("final"):
            draw_scale_bar(ax, 50 / UM_PER_PX_U2OS, UM_PER_PX_U2OS, 50.0)
        if letter == "d" and meta.get("final"):
            draw_scale_bar(ax, (10 / UM_PER_PX_U2OS) * 3, UM_PER_PX_U2OS, 10.0)
        if letter == "c" and meta.get("final") and meta.get("inset_box"):
            x0, y0, x1, y1 = meta["inset_box"]
            ax.add_patch(
                plt.Rectangle(
                    (x0, y0),
                    x1 - x0,
                    y1 - y0,
                    fill=False,
                    edgecolor="white",
                    linewidth=0.5,
                )
            )
        if not meta.get("final") and letter == "c":
            draw_scale_bar(ax, 50, UM_PER_PX_U2OS, 20.0)
    fig.subplots_adjust(hspace=0.08, wspace=0.05)
    save_pair(fig, stem, language)
    plt.close(fig)


def export_final_panels(panels: dict) -> None:
    out_dir = FIG / "work/panels"
    out_dir.mkdir(parents=True, exist_ok=True)
    for key in ("a", "b", "c", "d"):
        Image.fromarray(panels[key]).save(out_dir / f"panel-{key}.png")


def write_tikz_overlays() -> None:
    overlay_zh = r"""
\begin{tikzpicture}
  \node[circle,draw=BookRule,fill=BookPale!30,inner sep=1pt,font=\scriptsize] (n1) at (0.25,0.75) {1};
  \node[font=\scriptsize,align=center] at (0.25,0.68) {各自自动对比度};
  \node[circle,draw=BookRule,fill=BookPale!30,inner sep=1pt,font=\scriptsize] at (0.75,0.75) {2};
  \node[font=\scriptsize] at (0.75,0.68) {红/绿};
  \node[circle,draw=BookRule,fill=BookPale!30,inner sep=1pt,font=\scriptsize] at (0.92,0.55) {3};
  \node[font=\scriptsize,align=center] at (0.85,0.48) {比例尺无依据};
  \node[circle,draw=BookRule,fill=BookPale!30,inner sep=1pt,font=\scriptsize] at (0.75,0.25) {4};
  \node[font=\scriptsize,align=center] at (0.75,0.18) {最亮细胞+双三次};
  \node[circle,draw=BookRule,fill=BookPale!30,inner sep=1pt,font=\scriptsize] at (0.25,0.25) {5};
  \node[font=\scriptsize] at (0.25,0.18) {未披露 $\gamma=0.6$};
\end{tikzpicture}
""".strip()
    overlay_en = overlay_zh.replace("各自自动对比度", "auto-contrast per panel").replace(
        "红/绿", "red--green"
    ).replace("比例尺无依据", "unfounded scale bar").replace(
        "最亮细胞+双三次", "brightest cell + bicubic"
    ).replace("未披露 γ 0.6", "undisclosed γ 0.6")
    FIG.mkdir(parents=True, exist_ok=True)
    (FIG / "ch08-08-case-v1-overlay-zh.tex").write_text(overlay_zh + "\n", encoding="utf-8")
    (FIG / "ch08-08-case-v1-overlay-en.tex").write_text(overlay_en + "\n", encoding="utf-8")


def write_tikz_preview() -> None:
    tex = ROOT / "production/tikz-preview-ch08.tex"
    tex.write_text(
        r"""% Compile: xelatex -interaction=nonstopmode production/tikz-preview-ch08.tex
\documentclass[UTF8,fontset=fandol,10pt]{ctexart}
\usepackage{graphicx}
\input{shared/preamble}
\setlength{\parindent}{0pt}
\begin{document}
\section*{FIG ch08-08 v1 overlay (zh)}
\input{figures/ch08/ch08-08-case-v1-overlay-zh.tex}
\newpage
\section*{FIG ch08-08 v1 overlay (en)}
\input{figures/ch08/ch08-08-case-v1-overlay-en.tex}
\end{document}
"""
        + "\n",
        encoding="utf-8",
    )


def main() -> None:
    setup_rc()
    PROV.mkdir(parents=True, exist_ok=True)
    FIG.mkdir(parents=True, exist_ok=True)
    print("Fetching data…")
    bbbc = fetch_bbbc()
    sourced = fetch_sourced()
    write_sourced_md(sourced)
    write_case_catalog()
    hoechst_s1, _ = load_tiff("hoechst_s1")
    mito_s1, _ = load_tiff("mito_s1")
    mito_s2, _ = load_tiff("mito_s2")
    leaf = SOURCED / "Leaf_epidermis.jpg"
    fluo = SOURCED / "FluorescentCells.jpg"
    provenance: Dict[str, dict] = {}
    fig07_meta, gt, lr = prepare_fig07_input(leaf)
    provenance["fig07_input"] = fig07_meta
    for lang in ("zh", "en"):
        font = chinese_font() if lang == "zh" else None
        provenance.setdefault("ch08-01", {})[lang] = fig01(lang, hoechst_s1, font)
        provenance.setdefault("ch08-02", {})[lang] = fig02(lang, mito_s1, font)
        provenance.setdefault("ch08-03", {})[lang] = fig03(lang, mito_s1, mito_s2, font)
        provenance.setdefault("ch08-04", {})[lang] = fig04(lang, hoechst_s1, mito_s1, font)
        provenance.setdefault("ch08-05", {})[lang] = fig05(lang, leaf, font)
        provenance.setdefault("ch08-06", {})[lang] = fig06(lang, fluo, font)
        meta07, ok = fig07(lang, gt, lr, font)
        provenance.setdefault("ch08-07", {})[lang] = meta07
        panels_v1, meta_v1, _, _ = build_case_panels(hoechst_s1, mito_s1, final=False)
        render_case_figure(lang, panels_v1, meta_v1, font, "ch08-08-case-v1")
        panels_f, meta_f, log, _ = build_case_panels(hoechst_s1, mito_s1, final=True)
        render_case_figure(lang, panels_f, meta_f, font, "ch08-08-case-final")
        if lang == "zh":
            export_final_panels(panels_f)
            write_json(PROV / "processing-log.json", log)
            write_json(PROV / "ch08-08.json", {"v1": meta_v1, "final": meta_f})
    write_tikz_overlays()
    write_tikz_preview()
    data_check = {
        "chapter": "08",
        "generated_on": date.today().isoformat(),
        "bbbc_downloads": bbbc,
        "sourced_downloads": sourced,
        "bbbc_assertions": {
            "hoechst_s1_mean": float(hoechst_s1.mean()),
            "mito_s1_mean": float(mito_s1.mean()),
            "mito_s2_mean": float(mito_s2.mean()),
            "mito_s1_saturated": int((mito_s1 >= 4095).sum()),
        },
        "leaf_scale_px": measure_leaf_scale_px(np.array(Image.open(leaf).convert("L"))),
        "figure_provenance": provenance,
        "figures": {
            "python": [
                "ch08-01-raw-display-mapping",
                "ch08-02-linear-vs-gamma",
                "ch08-03-consistent-display",
                "ch08-04-pseudocolor-colorblind",
                "ch08-05-crop-inset-scalebar",
                "ch08-06-no-calibration",
                "ch08-07-ai-enhancement",
                "ch08-08-case-v1",
                "ch08-08-case-final",
            ],
            "tikz": ["ch08-08-case-v1-overlay"],
            "reuse": [],
            "sourced": ["FluorescentCells.jpg", "Leaf_epidermis.jpg", "BBBC022 TIFF×4"],
        },
        "fig07_codex_complete": provenance["ch08-07"]["zh"].get("complete", False),
    }
    write_json(PROV / "data-check.json", data_check)
    print(json.dumps(data_check["bbbc_assertions"], indent=2))


if __name__ == "__main__":
    main()
