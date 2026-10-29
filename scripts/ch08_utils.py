#!/usr/bin/env python3
"""Shared helpers for chapter 8 image figures."""
# SPDX-License-Identifier: MIT
import hashlib
import json
import subprocess
from pathlib import Path
from typing import List, Optional, Tuple

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
from PIL import Image
from scipy.ndimage import label, rotate, shift

matplotlib.use("Agg")

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures" / "ch08"
DATA = ROOT / "data" / "ch08"
RAW = DATA / "raw"
PROV = ROOT / "provenance" / "ch08"
SOURCED = DATA / "sourced"

UM_PER_PX_U2OS = 0.656

BBBC_FILES = {
    "hoechst_s1": "IXMtest_A13_s1_w1B35C6D5D-DBF9-4779-990D-5E7AFB14D600.tif",
    "mito_s1": "IXMtest_A13_s1_w5B257EE32-37B0-4698-891B-11B1B3D3D0C1.tif",
    "hoechst_s2": "IXMtest_A13_s2_w1951890F6-3FBD-488D-A559-E437F411FE17.tif",
    "mito_s2": "IXMtest_A13_s2_w5E4FF8FF2-B6AC-4AC6-810D-535064B5C89C.tif",
}

BBBC_STATS = {
    "hoechst_s1": {"min": 121, "max": 1655, "mean": 238.4, "p01": 132, "p999": 1236, "sat4095": 0, "sha16": "4be40f814481002a"},
    "mito_s1": {"min": 185, "max": 4095, "mean": 373.2, "p01": 218, "p999": 1140, "sat4095": 12, "sha16": "c1c441e44e91481c"},
    "hoechst_s2": {"min": 122, "max": 1450, "mean": 227.1, "p01": 129, "p999": 1150, "sat4095": 0, "sha16": "800419706668d4de"},
    "mito_s2": {"min": 176, "max": 1655, "mean": 366.3, "p01": 196, "p999": 1078, "sat4095": 0, "sha16": "b3d11076696b2bf4"},
}

HOECHST_RANGE = (132, 1236)
MITO_RANGE = (218, 1140)

MACHADO_DEUTERANOPIA = np.array(
    [[0.62550137, 0.37449863, 0.0], [0.7, 0.3, 0.0], [0.0, 0.3, 0.7]]
)
MACHADO_PROTANOPIA = np.array(
    [[0.566667, 0.433333, 0.0], [0.558333, 0.441667, 0.0], [0.0, 0.241667, 0.758333]]
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def chinese_font() -> FontProperties:
    font_path = subprocess.check_output(
        ["kpsewhich", "FandolHei-Regular.otf"], text=True
    ).strip()
    if not font_path:
        raise RuntimeError("Install TeX Live Fandol fonts for Chinese PDF figures.")
    return FontProperties(fname=font_path, family="sans-serif")


def setup_rc() -> None:
    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.size": 8,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "axes.linewidth": 0.7,
        }
    )


def save_pair(fig: plt.Figure, stem: str, language: str) -> None:
    FIG.mkdir(parents=True, exist_ok=True)
    for extension in ("pdf", "png"):
        use_pgf = language == "zh" and extension == "pdf"
        dpi = 300 if extension == "png" else 220
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
                FIG / f"{stem}-{language}.{extension}",
                backend="pgf" if use_pgf else None,
                dpi=dpi,
                facecolor="white",
                bbox_inches="tight",
                metadata={"Creator": "ai-scientific-figures-book ch08"},
            )


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_tiff(key: str) -> Tuple[np.ndarray, Path]:
    name = BBBC_FILES[key]
    path = RAW / name
    assert path.is_file(), f"Missing {path}; run ch08_fetch first"
    arr = np.array(Image.open(path))
    assert arr.ndim == 2
    check_bbbc_array(key, arr, path)
    return arr, path


def check_bbbc_array(key: str, arr: np.ndarray, path: Path) -> None:
    exp = BBBC_STATS[key]
    assert sha256(path).startswith(exp["sha16"])
    assert arr.shape == (520, 696)
    assert int(arr.min()) == exp["min"]
    assert int(arr.max()) == exp["max"]
    assert abs(float(arr.mean()) - exp["mean"]) < 0.05
    p01, p999 = np.percentile(arr, [0.1, 99.9])
    assert abs(p01 - exp["p01"]) < 1.0
    assert abs(p999 - exp["p999"]) < 1.0
    assert int((arr >= 4095).sum()) == exp["sat4095"]


def linear_display_u8(arr: np.ndarray, vmin: float, vmax: float) -> np.ndarray:
    scaled = (arr.astype(np.float64) - vmin) / (vmax - vmin)
    scaled = np.clip(scaled, 0.0, 1.0)
    return (scaled * 255.0).astype(np.uint8)


def fraction_mapped_white(arr: np.ndarray, vmin: float, vmax: float) -> float:
    return float((arr > vmax).mean())


def gamma_display_u8(arr: np.ndarray, vmin: float, vmax: float, gamma: float) -> np.ndarray:
    norm = np.clip((arr.astype(np.float64) - vmin) / (vmax - vmin), 0.0, 1.0)
    return (np.power(norm, gamma) * 255.0).astype(np.uint8)


def srgb_to_linear(rgb: np.ndarray) -> np.ndarray:
    c = rgb.astype(np.float64)
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def linear_to_srgb(linear: np.ndarray) -> np.ndarray:
    c = np.clip(linear, 0.0, 1.0)
    return np.where(c <= 0.0031308, 12.92 * c, 1.055 * (c ** (1.0 / 2.4)) - 0.055)


def simulate_cvd(rgb_u8: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    rgb = np.clip(rgb_u8.astype(np.float64) / 255.0, 0.0, 1.0)
    lin = srgb_to_linear(rgb)
    flat = np.nan_to_num(lin.reshape(-1, 3))
    out = np.clip(flat @ matrix.T, 0.0, 1.0)
    out = out.reshape(lin.shape)
    return np.clip(linear_to_srgb(out) * 255.0, 0, 255).astype(np.uint8)


def merge_red_green(nuc_u8: np.ndarray, mito_u8: np.ndarray) -> np.ndarray:
    h, w = nuc_u8.shape
    rgb = np.zeros((h, w, 3), dtype=np.uint8)
    rgb[..., 0] = nuc_u8
    rgb[..., 1] = mito_u8
    return rgb


def merge_magenta_green(nuc_u8: np.ndarray, mito_u8: np.ndarray) -> np.ndarray:
    h, w = nuc_u8.shape
    rgb = np.zeros((h, w, 3), dtype=np.uint8)
    rgb[..., 0] = nuc_u8
    rgb[..., 1] = mito_u8
    rgb[..., 2] = nuc_u8
    return rgb


def nearest_upscale(arr: np.ndarray, factor: int) -> np.ndarray:
    return np.repeat(np.repeat(arr, factor, axis=0), factor, axis=1)


def draw_scale_bar(
    ax,
    length_px: float,
    um_per_px: float,
    bar_um: float,
    y_frac: float = 0.04,
    color: str = "white",
) -> dict:
    """Draw horizontal scale bar near bottom-right; returns pixel length used."""
    bar_px = bar_um / um_per_px
    x0, x1 = ax.get_xlim()
    y0, y1 = ax.get_ylim()
    width = x1 - x0
    height = y1 - y0
    x_start = x1 - 0.08 * width - bar_px
    y_line = y0 + y_frac * height
    ax.plot(
        [x_start, x_start + bar_px],
        [y_line, y_line],
        color="black",
        linewidth=3,
        solid_capstyle="butt",
    )
    ax.plot(
        [x_start, x_start + bar_px],
        [y_line, y_line],
        color=color,
        linewidth=1.5,
        solid_capstyle="butt",
    )
    return {"bar_um": bar_um, "bar_px": bar_px, "y_data": y_line}


def panel_letter(ax, text: str, font: Optional[FontProperties]) -> None:
    ax.text(
        0.02,
        0.98,
        text,
        transform=ax.transAxes,
        va="top",
        ha="left",
        fontproperties=font,
        fontsize=9,
        fontweight="bold",
        color="white",
    )


def style_spines(ax) -> None:
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(axis="both", length=3)


def rgb_png_to_gray_u8(path: Path) -> np.ndarray:
    """Convert RGB(A) PNG to 8-bit gray (ITU-R BT.601 weights)."""
    rgb = np.array(Image.open(path).convert("RGB"), dtype=np.float64)
    gray = 0.299 * rgb[..., 0] + 0.587 * rgb[..., 1] + 0.114 * rgb[..., 2]
    return np.clip(gray, 0, 255).astype(np.uint8)


def resize_gray_lanczos(arr: np.ndarray, size: Tuple[int, int]) -> np.ndarray:
    return np.array(Image.fromarray(arr).resize(size, Image.LANCZOS))


def phase_shift(fixed: np.ndarray, moving: np.ndarray) -> Tuple[float, float]:
    """Integer pixel shift (dy, dx) aligning moving to fixed via FFT cross-correlation."""
    f = fixed.astype(np.float64)
    m = moving.astype(np.float64)
    f -= f.mean()
    m -= m.mean()
    corr = np.fft.ifft2(np.fft.fft2(f) * np.conj(np.fft.fft2(m))).real
    peak = np.unravel_index(int(np.argmax(corr)), corr.shape)
    dy, dx = peak
    if dy > f.shape[0] // 2:
        dy -= f.shape[0]
    if dx > f.shape[1] // 2:
        dx -= f.shape[1]
    return float(dy), float(dx)


def register_rigid_to_gt(
    gt: np.ndarray, ai: np.ndarray, angle_step: float = 0.5, angle_max: float = 2.0
) -> Tuple[np.ndarray, dict]:
    """Rigid registration (rotation + translation) of ai to gt; returns uint8 ai aligned."""
    gt_f = gt.astype(np.float64)
    ai_f = ai.astype(np.float64)
    best_mae = float("inf")
    best_img = ai
    best_meta: dict = {"method": "rotation_grid_plus_phase_shift", "angle_deg": 0.0, "shift_dy": 0.0, "shift_dx": 0.0}
    angles = np.arange(-angle_max, angle_max + angle_step * 0.5, angle_step)
    for angle in angles:
        rotated = rotate(ai_f, float(angle), reshape=False, order=1, mode="nearest")
        dy, dx = phase_shift(gt_f, rotated)
        warped = shift(rotated, shift=(dy, dx), order=1, mode="nearest")
        mae = float(np.abs(warped - gt_f).mean())
        if mae < best_mae:
            best_mae = mae
            best_img = np.clip(warped, 0, 255).astype(np.uint8)
            best_meta = {
                "method": "rotation_grid_plus_phase_shift",
                "angle_deg": float(angle),
                "shift_dy": float(dy),
                "shift_dx": float(dx),
                "mae_after_register": mae,
            }
    return best_img, best_meta


def find_fabricated_structure_circles(
    gt: np.ndarray,
    bicubic: np.ndarray,
    ai: np.ndarray,
    count: int = 3,
    min_area: int = 40,
    max_area: int = 8000,
) -> Tuple[List[dict], dict]:
    """
    Pick 2–3 regions where |ai−gt| exceeds |bicubic−gt| (connected components on excess map).
    Returns circle specs {cx, cy, radius_px} in image coordinates.
    """
    diff_b = np.abs(bicubic.astype(np.int16) - gt.astype(np.int16))
    diff_a = np.abs(ai.astype(np.int16) - gt.astype(np.int16))
    excess = np.maximum(diff_a.astype(np.int32) - diff_b.astype(np.int32), 0)
    positive = excess[excess > 0]
    if positive.size == 0:
        return [], {"threshold": None, "components_found": 0}
    threshold = float(np.percentile(positive, 85))
    mask = excess >= threshold
    labeled, n_comp = label(mask)
    candidates = []
    for comp_id in range(1, n_comp + 1):
        ys, xs = np.where(labeled == comp_id)
        area = int(ys.size)
        if area < min_area or area > max_area:
            continue
        score = float(excess[ys, xs].sum())
        cy = float(ys.mean())
        cx = float(xs.mean())
        radius = float(max(np.sqrt(area / np.pi) * 1.15, 12.0))
        candidates.append(
            {
                "cx": cx,
                "cy": cy,
                "radius_px": radius,
                "area_px": area,
                "excess_sum": score,
            }
        )
    candidates.sort(key=lambda item: item["excess_sum"], reverse=True)
    chosen = candidates[:count]
    meta = {
        "threshold_excess": threshold,
        "components_found": n_comp,
        "candidates_ranked": len(candidates),
        "selection": "top excess_sum after size filter",
    }
    return chosen, meta
