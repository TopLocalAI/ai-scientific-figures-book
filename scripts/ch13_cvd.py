#!/usr/bin/env python3
"""FIG ch13-06: grayscale and colour-vision deficiency simulations."""
# SPDX-License-Identifier: MIT
# Machado matrix check (2026-10-29): colorspacious 1.1.2 cvd.py uses
# Machado, Oliveira & Fernandes (2009) matrices; deuteranomaly severity 1.0
# row0 ≈ [0.152286, 1.052583, -0.204868] matching author supplementary values
# within float tolerance (verified against cvd._machado_2009_matrices in site-packages).
import io
import sys
from pathlib import Path

import colorspacious
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from ch13_plot_utils import FIG, chinese_font, load_stability, save_figure, setup_rc  # noqa: E402

SCHEMES = [
    {"name": "rg_draft", "control": "#CC0000", "modified": "#2CA02C", "control_ls": "-", "modified_ls": "-", "labels": False},
    {"name": "ch12", "control": "#6E6E6E", "modified": "#1B7F86", "control_ls": "-", "modified_ls": "-", "labels": False},
    {"name": "fixed", "control": "#6E6E6E", "modified": "#1B7F86", "control_ls": "--", "modified_ls": "-", "labels": True},
]

CVD_TYPES = [
    ("orig", None),
    ("gray", "gray"),
    ("protan", "protanomaly"),
    ("deutan", "deuteranomaly"),
    ("tritan", "tritanomaly"),
]

COL_TITLES = {
    "zh": ["原图", "灰度 (L*)", "红色弱", "绿色弱", "蓝色弱"],
    "en": ["Original", "Grayscale (L*)", "Protan", "Deutan", "Tritan"],
}


def hex_to_rgb01(h: str):
    h = h.lstrip("#")
    return np.array([int(h[i : i + 2], 16) for i in (0, 2, 4)], dtype=float) / 255.0


def srgb_to_lstar(rgb):
    linear = colorspacious.cspace_convert(rgb, "sRGB1", "XYZ1")
    lab = colorspacious.cspace_convert(linear, "XYZ1", "CIELab")
    return lab[..., 0]


def apply_view(rgb: np.ndarray, view: str) -> np.ndarray:
    rgb = np.clip(rgb.astype(float), 0, 1)
    if view == "gray":
        lstar = srgb_to_lstar(rgb)
        lnorm = np.clip(lstar / 100.0, 0, 1)
        return np.stack([lnorm, lnorm, lnorm], axis=-1)
    if view in ("protanomaly", "deuteranomaly", "tritanomaly"):
        return np.clip(
            colorspacious.cspace_convert(
                rgb,
                {"name": "sRGB1+CVD", "cvd_type": view, "severity": 100},
                "sRGB1",
            ),
            0,
            1,
        )
    return rgb


from typing import Optional


def delta_e_line_pair(c1_hex, c2_hex, view: Optional[str]):
    c1 = hex_to_rgb01(c1_hex)
    c2 = hex_to_rgb01(c2_hex)
    if view == "gray":
        c1 = apply_view(c1.reshape(1, 1, 3), "gray").reshape(3)
        c2 = apply_view(c2.reshape(1, 1, 3), "gray").reshape(3)
    elif view in ("protanomaly", "deuteranomaly", "tritanomaly"):
        c1 = apply_view(c1.reshape(1, 1, 3), view).reshape(3)
        c2 = apply_view(c2.reshape(1, 1, 3), view).reshape(3)
    return float(colorspacious.deltaE(c1, c2))


def render_curve_rgb(scheme, language: str, size=(2.2, 1.6), dpi=120) -> np.ndarray:
    setup_rc(6)
    t_c, y_c = load_stability()["control"]
    t_m, y_m = load_stability()["modified"]
    fig, ax = plt.subplots(figsize=size, dpi=dpi)
    ax.plot(t_c, y_c, color=scheme["control"], linestyle=scheme["control_ls"], linewidth=1.0)
    ax.plot(t_m, y_m, color=scheme["modified"], linestyle=scheme["modified_ls"], linewidth=1.0)
    ax.set_xlim(0, 1000)
    ax.set_ylim(0.4, 1.05)
    ax.axis("off")
    if scheme["labels"]:
        font = chinese_font() if language == "zh" else None
        lbl_c, lbl_m = ("对照", "改性") if language == "zh" else ("Control", "Modified")
        ax.text(980, y_c[-1], lbl_c, fontproperties=font, fontsize=5, color=scheme["control"], ha="right", va="center")
        ax.text(980, y_m[-1], lbl_m, fontproperties=font, fontsize=5, color=scheme["modified"], ha="right", va="center")
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=dpi, facecolor="white", bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)
    buf.seek(0)
    from PIL import Image

    img = np.asarray(Image.open(buf).convert("RGB"), dtype=float) / 255.0
    return img


def build(language: str):
    font = chinese_font() if language == "zh" else None
    nrows, ncols = len(SCHEMES), len(CVD_TYPES)
    fig, axes = plt.subplots(
        nrows, ncols,
        figsize=(ncols * 1.35, nrows * 1.25),
        gridspec_kw={"wspace": 0.05, "hspace": 0.12},
    )
    delta_log = []
    for ri, scheme in enumerate(SCHEMES):
        base = render_curve_rgb(scheme, language)
        for ci, (col_key, cvd) in enumerate(CVD_TYPES):
            ax = axes[ri, ci]
            if cvd is None:
                shown = base
                de_view = None
            else:
                shown = apply_view(base, cvd)
                de_view = cvd if cvd != "gray" else "gray"
            de = delta_e_line_pair(scheme["control"], scheme["modified"], de_view)
            delta_log.append({"scheme": scheme["name"], "view": col_key, "deltaE": round(de, 2)})
            ax.imshow(np.clip(shown, 0, 1))
            ax.set_xticks([])
            ax.set_yticks([])
            if ri == 0:
                ax.set_title(COL_TITLES[language][ci], fontproperties=font, fontsize=7)
            ax.text(
                0.98, 0.92, f"ΔE={de:.1f}", transform=ax.transAxes,
                ha="right", va="top", fontsize=6, color="#23363E",
                bbox=dict(facecolor="white", alpha=0.75, edgecolor="none", pad=1),
            )
    save_figure(fig, FIG / "ch13-06-grayscale-and-cvd", language)
    return delta_log


def main():
    # L* spot checks for planning colors
    for hx in ("#6E6E6E", "#1B7F86", "#CC0000", "#2CA02C"):
        lstar = float(srgb_to_lstar(hex_to_rgb01(hx)))
        print(hx, "L*=", round(lstar, 1))
    logs = {}
    for language in ("zh", "en"):
        logs[language] = build(language)
    print("deltaE grid (en):", logs["en"][:5], "...")


if __name__ == "__main__":
    main()
