#!/usr/bin/env python3
"""FIG ch10-07: graphical-abstract thumbnail legibility test (Pillow + Matplotlib)."""
# SPDX-License-Identifier: MIT
import hashlib
import json
import subprocess
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures/ch10"
DATA = ROOT / "data/ch10"
PROV = ROOT / "provenance/ch10"

CANVAS_W, CANVAS_H = 2000, 800
THUMB_H = 200
THUMB_W = int(CANVAS_W * THUMB_H / CANVAS_H)  # 500
STAGE_FONT_GOOD = 36
STAGE_FONT_BAD = 14
RNG_SEED = 20261029

BASE_CANDIDATES = (
    FIG / "ch10-06-final-base.png",
    DATA / "simulated/ch10-06-final-base-en.png",
)
FINAL_CANDIDATES = (FIG / "ch10-06-final-en.png",)
OVERCLAIM_CANDIDATES = (FIG / "ch10-05-overclaim-en.png",)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def draw_simulated_base() -> Image.Image:
    """Flat 5:2 schematic base art (no text); fixed layout for reproducibility."""
    img = Image.new("RGB", (CANVAS_W, CANVAS_H), "white")
    draw = ImageDraw.Draw(img)
    green, burn, bluegray, blue, ink, cloud = (
        "#A8C3A0",
        "#C8743C",
        "#8FA3B8",
        "#2F6DB5",
        "#3A3A3A",
        "#D5D5D5",
    )

    def rect(x0, y0, x1, y1, fill, outline=ink, width=2):
        draw.rectangle([x0, y0, x1, y1], fill=fill, outline=outline, width=width)

    y0, y1 = int(0.18 * CANVAS_H), int(0.72 * CANVAS_H)
    rect(int(0.04 * CANVAS_W), y0, int(0.14 * CANVAS_W), y1, green)
    rect(int(0.15 * CANVAS_W), y0, int(0.25 * CANVAS_W), y1, green)
    draw.polygon(
        [
            (int(0.16 * CANVAS_W), int(0.35 * CANVAS_H)),
            (int(0.22 * CANVAS_W), int(0.32 * CANVAS_H)),
            (int(0.24 * CANVAS_W), int(0.45 * CANVAS_H)),
            (int(0.17 * CANVAS_W), int(0.48 * CANVAS_H)),
        ],
        fill=burn,
    )
    rect(int(0.05 * CANVAS_W), y0 - 70, int(0.11 * CANVAS_W), y0 - 10, green)
    draw.ellipse(
        [int(0.06 * CANVAS_W), y0 - 85, int(0.12 * CANVAS_W), y0 - 25],
        fill=cloud,
        outline=ink,
        width=1,
    )
    cx = int(0.375 * CANVAS_W)
    for dx, w in [(-55, 90), (-25, 50), (5, 50), (35, 90)]:
        rect(cx + dx, y0 + 20, cx + dx + w, y1 - 20, bluegray)
    rect(int(0.50 * CANVAS_W), y0 - 20, int(0.73 * CANVAS_W), y1 + 20, "#ECECEC")
    draw.polygon(
        [
            (int(0.58 * CANVAS_W), int(0.40 * CANVAS_H)),
            (int(0.66 * CANVAS_W), int(0.35 * CANVAS_H)),
            (int(0.68 * CANVAS_W), int(0.52 * CANVAS_H)),
            (int(0.57 * CANVAS_W), int(0.55 * CANVAS_H)),
        ],
        fill=burn,
        outline=ink,
        width=2,
    )
    inset = (int(0.77 * CANVAS_W), y0, int(0.96 * CANVAS_W), y1)
    draw.rectangle(inset, fill="#F5F5F5", outline=ink, width=2)
    ix0, iy0, ix1, iy1 = inset
    mid_y = (iy0 + iy1) // 2
    draw.line([(ix0 + 15, mid_y), (ix1 - 15, mid_y)], fill=ink, width=4)
    draw.line([(ix0 + 15, mid_y), (ix1 - 15, mid_y)], fill=blue, width=3)
    for x in range(ix0 + 20, ix1 - 15, 18):
        draw.line([(x, mid_y - 25), (x + 8, mid_y + 30)], fill="#A0A0A0", width=2)
    arrow_y = (y0 + y1) // 2
    for x_start, x_end in [(int(0.25 * CANVAS_W), int(0.30 * CANVAS_W)), (int(0.46 * CANVAS_W), int(0.50 * CANVAS_W))]:
        draw.line([(x_start, arrow_y), (x_end, arrow_y)], fill=ink, width=5)
        draw.polygon(
            [(x_end, arrow_y), (x_end - 18, arrow_y - 10), (x_end - 18, arrow_y + 10)],
            fill=ink,
        )
    return img


def load_or_create_base() -> tuple[Image.Image, str]:
    for path in BASE_CANDIDATES:
        if path.is_file():
            with Image.open(path) as image:
                base = image.convert("RGB")
            assert base.size == (CANVAS_W, CANVAS_H), base.size
            return base.copy(), str(path.relative_to(ROOT))
    DATA.mkdir(parents=True, exist_ok=True)
    sim_dir = DATA / "simulated"
    sim_dir.mkdir(parents=True, exist_ok=True)
    out = sim_dir / "ch10-06-final-base-en.png"
    base = draw_simulated_base()
    base.save(out)
    return base, str(out.relative_to(ROOT))


def stage_labels(language: str) -> list[tuple[str, float]]:
    if language == "zh":
        return [
            ("火前 / 火后 Sentinel-2 影像对", 0.14),
            ("分割网络", 0.38),
            ("过火区图", 0.62),
            ("比 dNBR 阈值法更贴近参考边界", 0.86),
        ]
    return [
        ("Pre-/post-fire Sentinel-2 pair", 0.14),
        ("Segmentation network", 0.38),
        ("Burned-area map", 0.62),
        ("Closer to reference edges than dNBR threshold", 0.86),
    ]


def load_font(language: str, font_px: int):
    candidates = []
    if language == "zh":
        try:
            fandol = subprocess.check_output(
                ["kpsewhich", "FandolHei-Regular.otf"], text=True
            ).strip()
            if fandol:
                candidates.append(fandol)
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass
    candidates.append("/System/Library/Fonts/Supplemental/Arial.ttf")
    for path in candidates:
        try:
            return ImageFont.truetype(path, font_px)
        except OSError:
            continue
    return ImageFont.load_default()


def compose_with_stage_labels(
    base: Image.Image, language: str, font_px: int
) -> Image.Image:
    img = base.copy()
    draw = ImageDraw.Draw(img)
    font = load_font(language, font_px)
    y = int(0.80 * CANVAS_H)
    for text, x_frac in stage_labels(language):
        x = int(x_frac * CANVAS_W)
        bbox = draw.textbbox((0, 0), text, font=font)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        draw.text((x - tw // 2, y - th // 2), text, fill="#23363E", font=font)
    return img


def scaled_height_after_thumb(font_px: int) -> float:
    return font_px * (THUMB_H / CANVAS_H)


def build_panel(language: str) -> dict:
    base, base_source = load_or_create_base()
    good = compose_with_stage_labels(base, language, STAGE_FONT_GOOD)
    bad = compose_with_stage_labels(base, language, STAGE_FONT_BAD)
    assert good.size == bad.size == (CANVAS_W, CANVAS_H)

    thumb_good = good.resize((THUMB_W, THUMB_H), Image.Resampling.LANCZOS)
    thumb_bad = bad.resize((THUMB_W, THUMB_H), Image.Resampling.LANCZOS)

    scaled_good = scaled_height_after_thumb(STAGE_FONT_GOOD)
    scaled_bad = scaled_height_after_thumb(STAGE_FONT_BAD)
    assert abs(scaled_good - 9.0) < 0.01
    assert abs(scaled_bad - 3.5) < 0.01

    labels = {
        "en": {
            "row_good": f"Stage labels {STAGE_FONT_GOOD}px tall → {scaled_good:.1f}px after scale (legible)",
            "row_bad": f"Stage labels {STAGE_FONT_BAD}px → {scaled_bad:.1f}px after scale (not legible)",
            "orig": f"Original {CANVAS_W} × {CANVAS_H} px",
            "thumb": f"TOC size {THUMB_W} × {THUMB_H} px",
            "title": "Thumbnail test · simulated base if codex final missing",
        },
        "zh": {
            "row_good": f"阶段名约 {STAGE_FONT_GOOD}px 字高 → 缩后约 {scaled_good:.0f}px（可读）",
            "row_bad": f"阶段名 {STAGE_FONT_BAD}px → 缩后约 {scaled_bad:.1f}px（不可读）",
            "orig": f"原图 {CANVAS_W} × {CANVAS_H} px",
            "thumb": f"目录尺寸 {THUMB_W} × {THUMB_H} px",
            "title": "缩略图测试 · 若无 codex 终稿则使用模拟底图",
        },
    }[language]

    display_w = THUMB_W
    preview_good = good.resize((display_w, THUMB_H), Image.Resampling.LANCZOS)
    preview_bad = bad.resize((display_w, THUMB_H), Image.Resampling.LANCZOS)

    row_h = THUMB_H + 40
    col_w = display_w + 20
    grid_w = col_w * 2 + 30
    grid_h = row_h * 2 + 80
    canvas = Image.new("RGB", (grid_w, grid_h), "white")

    def paste_row(row: int, left: Image.Image, right: Image.Image) -> None:
        y = 50 + row * row_h
        canvas.paste(left, (10, y))
        canvas.paste(right, (col_w + 20, y))

    paste_row(0, preview_good, thumb_good)
    paste_row(1, preview_bad, thumb_bad)

    return {
        "grid": canvas,
        "grid_size": (grid_w, grid_h),
        "layout": {"row_h": row_h, "col_w": col_w},
        "labels": labels,
        "scaled_good_px": scaled_good,
        "scaled_bad_px": scaled_bad,
        "base_source": base_source,
        "base_sha256": sha256(Path(ROOT / base_source)) if (ROOT / base_source).is_file() else None,
    }


def render_matplotlib(language: str, panel: dict) -> None:
    grid = panel["grid"]
    w_px, h_px = panel["grid_size"]
    row_h = panel["layout"]["row_h"]
    col_w = panel["layout"]["col_w"]
    labels = panel["labels"]
    dpi = 100
    fig_w, fig_h = w_px / dpi, h_px / dpi
    font = None
    if language == "zh":
        font_path = subprocess.check_output(
            ["kpsewhich", "FandolHei-Regular.otf"], text=True
        ).strip()
        if not font_path:
            raise RuntimeError("FandolHei required for Chinese PDF export.")
        font = FontProperties(fname=font_path, family="sans-serif")

    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.size": 9,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )
    fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=dpi)
    ax.imshow(grid, interpolation="nearest")
    ax.axis("off")
    ax.set_xlim(0, w_px)
    ax.set_ylim(h_px, 0)

    def t(x, y, s, size=9, color="#23363E", weight=None):
        ax.text(
            x,
            y,
            s,
            fontproperties=font,
            fontsize=size,
            color=color,
            va="top",
            ha="left",
            fontweight=weight,
        )

    t(10, 8, labels["title"], size=10, color="#176C68", weight="bold")
    t(10, 50 - 4, labels["row_good"])
    t(10, 50 + row_h - 4, labels["row_bad"])
    t(10, h_px - 8, labels["orig"], size=8, color="#666666")
    t(col_w + 20, h_px - 8, labels["thumb"], size=8, color="#666666")

    fig.subplots_adjust(0, 0, 1, 1)

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
                FIG / f"ch10-07-thumbnail-test-{language}.{extension}",
                backend="pgf" if use_pgf else None,
                dpi=300,
                facecolor="white",
            )
    plt.close(fig)


def main() -> None:
    FIG.mkdir(parents=True, exist_ok=True)
    PROV.mkdir(parents=True, exist_ok=True)

    missing_inputs = [
        str(p.relative_to(ROOT))
        for p in FINAL_CANDIDATES + OVERCLAIM_CANDIDATES
        if not p.is_file()
    ]

    summaries = []
    for language in ("en", "zh"):
        panel = build_panel(language)
        render_matplotlib(language, panel)
        for ext in ("png", "pdf"):
            out = FIG / f"ch10-07-thumbnail-test-{language}.{ext}"
            assert out.is_file(), out
        png = FIG / f"ch10-07-thumbnail-test-{language}.png"
        with Image.open(png) as im:
            w, h = im.size
        summaries.append(
            {
                "language": language,
                "output_png": str(png.relative_to(ROOT)),
                "output_png_px": [w, h],
                "output_sha256": sha256(png),
                "stage_font_good_px": STAGE_FONT_GOOD,
                "stage_font_bad_px": STAGE_FONT_BAD,
                "scaled_stage_height_good_px": panel["scaled_good_px"],
                "scaled_stage_height_bad_px": panel["scaled_bad_px"],
                "thumb_height_px": THUMB_H,
                "resize_filter": "PIL.Image.Resampling.LANCZOS",
                "base_art_source": panel["base_source"],
                "simulated_base": "simulated" in panel["base_source"],
            }
        )
        print(f"[{language}] scaled good={panel['scaled_good_px']:.1f}px bad={panel['scaled_bad_px']:.1f}px base={panel['base_source']}")

    check = {
        "figure": "ch10-07-thumbnail-test",
        "script": "scripts/ch10_thumbnail_test.py",
        "canvas_px": [CANVAS_W, CANVAS_H],
        "toc_thumb_px": [THUMB_W, THUMB_H],
        "random_seed": RNG_SEED,
        "missing_codex_inputs": missing_inputs,
        "assertions": {
            "scaled_good_px": 9.0,
            "scaled_bad_px": 3.5,
            "thumb_width_px": THUMB_W,
        },
        "runs": summaries,
        "note": "Good/bad rows differ only in stage-label font size on the same base pixels.",
    }
    out_json = PROV / "data-check.json"
    out_json.write_text(json.dumps(check, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(check, indent=2))


if __name__ == "__main__":
    main()
