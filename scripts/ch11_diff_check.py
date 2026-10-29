#!/usr/bin/env python3
"""FIG ch11-05: pixel difference maps and object-count table (book-owned images only)."""
# SPDX-License-Identifier: MIT
import csv
import json
import subprocess
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures" / "ch11"
PROV = ROOT / "provenance" / "ch11"
DATA = ROOT / "data" / "ch11"

# Recorded in provenance/ch11/diff-params.json
BLUR_SIGMA_PX = 2.0
DIFF_THRESHOLD = 40  # on 0–255 grayscale absolute difference
MIN_REGION_AREA_PX = 180

PAIR_SPECS = [
    {
        "row_label_zh": "本章 V2 与 V3",
        "row_label_en": "This chapter: V2 vs V3",
        "left": FIG / "ch11-03-v2-brief.png",
        "right": FIG / "ch11-04-v3-collateral.png",
        "case": "ch11",
    },
    {
        "row_label_zh": "第 7 章 V2 与 V3 第 1 次",
        "row_label_en": "Chapter 7: V2 vs V3 attempt 1",
        "left": ROOT / "cases/ch07-insulin-glut4/images/v2-brief.png",
        "right": ROOT / "cases/ch07-insulin-glut4/images/v3-revised-alt1.png",
        "case": "ch07",
    },
]


def load_counts() -> dict[str, list[dict]]:
    path = DATA / "ch11-object-counts.csv"
    by_case: dict[str, list[dict]] = {"ch11": [], "ch07": []}
    with path.open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream):
            case = row["case"]
            by_case[case].append(row)
    assert len(by_case["ch11"]) == 6
    assert len(by_case["ch07"]) == 4
    ch07_phos = next(r for r in by_case["ch07"] if "phosphorylation" in r["object_label_en"])
    assert int(ch07_phos["v2_count"]) == 6 and int(ch07_phos["v3_count"]) == 0
    return by_case


def _to_gray_array(path: Path) -> np.ndarray:
    with Image.open(path) as im:
        im = im.convert("L")
        return np.asarray(im, dtype=np.float32)


def _align_pair(left: Path, right: Path) -> tuple[np.ndarray, np.ndarray, tuple[int, int]]:
    assert left.is_file(), f"missing image: {left}"
    assert right.is_file(), f"missing image: {right}"
    with Image.open(left) as im_l, Image.open(right) as im_r:
        size = (min(im_l.width, im_r.width), min(im_l.height, im_r.height))
        resample = Image.Resampling.LANCZOS
        g_l = np.asarray(im_l.convert("L").resize(size, resample), dtype=np.float32)
        g_r = np.asarray(im_r.convert("L").resize(size, resample), dtype=np.float32)
    return g_l, g_r, size


def _gaussian_blur(arr: np.ndarray, sigma: float) -> np.ndarray:
    pil = Image.fromarray(arr.astype(np.uint8))
    blurred = pil.filter(ImageFilter.GaussianBlur(radius=sigma))
    return np.asarray(blurred, dtype=np.float32)


def _label_regions(mask: np.ndarray, min_area: int) -> tuple[np.ndarray, list[tuple[int, int, int, int]]]:
    h, w = mask.shape
    labels = np.zeros((h, w), dtype=np.int32)
    current = 0
    boxes: list[tuple[int, int, int, int]] = []
    for y in range(h):
        for x in range(w):
            if not mask[y, x] or labels[y, x]:
                continue
            current += 1
            stack = [(y, x)]
            ys, xs = [], []
            while stack:
                cy, cx = stack.pop()
                if cy < 0 or cy >= h or cx < 0 or cx >= w:
                    continue
                if not mask[cy, cx] or labels[cy, cx]:
                    continue
                labels[cy, cx] = current
                ys.append(cy)
                xs.append(cx)
                stack.extend([(cy + 1, cx), (cy - 1, cx), (cy, cx + 1), (cy, cx - 1)])
            if len(xs) >= min_area:
                boxes.append((min(xs), min(ys), max(xs), max(ys)))
    return labels, boxes


def diff_pipeline(left: Path, right: Path) -> dict:
    g_l, g_r, size = _align_pair(left, right)
    diff = np.abs(g_l - g_r)
    diff_blur = _gaussian_blur(diff, BLUR_SIGMA_PX)
    mask = diff_blur > DIFF_THRESHOLD
    _, boxes = _label_regions(mask, MIN_REGION_AREA_PX)
    changed_fraction = float(mask.mean())
    return {
        "size": size,
        "gray_left": g_l,
        "gray_right": g_r,
        "diff_blur": diff_blur,
        "mask": mask,
        "boxes": boxes,
        "changed_fraction": changed_fraction,
        "mean_diff": float(diff_blur.mean()),
    }


def active_pair_specs() -> list[dict]:
    ready = [
        spec
        for spec in PAIR_SPECS
        if spec["left"].is_file() and spec["right"].is_file()
    ]
    return ready


def render(
    language: str,
    by_case: dict[str, list[dict]],
    pair_specs: list[dict],
    rows: list[dict],
) -> None:
    labels = {
        "zh": ("像素差（0–255，灰度）", "对象计数（作者人工）", "V2", "V3"),
        "en": ("Pixel difference (0–255, grayscale)", "Object counts (author)", "V2", "V3"),
    }[language]
    font = None
    if language == "zh":
        font_path = subprocess.check_output(
            ["kpsewhich", "FandolHei-Regular.otf"], text=True
        ).strip()
        if not font_path:
            raise RuntimeError("FandolHei not found; install TeX Live Fandol fonts.")
        font = FontProperties(fname=font_path, family="sans-serif")

    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.size": 9,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )
    n_rows = len(pair_specs)
    fig_h = 3.2 + 1.8 * n_rows
    fig = plt.figure(figsize=(10.5, fig_h), facecolor="white")
    gs = fig.add_gridspec(
        n_rows + 1,
        4,
        height_ratios=[1] * n_rows + [0.55],
        width_ratios=[1, 1, 1, 0.06],
        hspace=0.28,
        wspace=0.06,
    )

    im = None
    for row_idx, spec in enumerate(pair_specs):
        data = rows[row_idx]
        title = spec["row_label_zh" if language == "zh" else "row_label_en"]
        for col, key in enumerate(("gray_left", "gray_right", "diff_blur")):
            ax = fig.add_subplot(gs[row_idx, col])
            if col < 2:
                ax.imshow(data[key], cmap="gray", vmin=0, vmax=255)
            else:
                ax.imshow(data["gray_left"], cmap="gray", vmin=0, vmax=255, alpha=0.55)
                im = ax.imshow(data["diff_blur"], cmap="Reds", vmin=0, vmax=255, alpha=0.85)
                for x0, y0, x1, y1 in data["boxes"]:
                    ax.plot(
                        [x0, x1, x1, x0, x0],
                        [y0, y0, y1, y1, y0],
                        color="#C0392B",
                        linewidth=1.2,
                    )
            ax.set_axis_off()
            if col == 0:
                ax.set_title(title, fontproperties=font, loc="left", fontsize=10, pad=6)
        cax = fig.add_subplot(gs[row_idx, 3])
        plt.colorbar(im, cax=cax, fraction=0.8)
        cax.set_ylabel(labels[0], fontproperties=font, fontsize=8)

    ax_tbl = fig.add_subplot(gs[n_rows, :3])
    ax_tbl.set_axis_off()
    table_rows = []
    for case_key in ("ch11", "ch07"):
        for row in by_case[case_key]:
            name = row["object_label_zh" if language == "zh" else "object_label_en"]
            table_rows.append([name, row["v2_count"], row["v3_count"]])
    col_labels = [
        labels[1],
        labels[2],
        labels[3],
    ]
    table = ax_tbl.table(
        cellText=table_rows,
        colLabels=col_labels,
        loc="center",
        cellLoc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1, 1.35)
    if font:
        for cell in table.get_celld().values():
            cell.get_text().set_fontproperties(font)

    fig.subplots_adjust(left=0.04, right=0.96, top=0.96, bottom=0.06)
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
                FIG / f"ch11-05-diff-and-count-{language}.{extension}",
                backend="pgf" if use_pgf else None,
                dpi=300,
                facecolor="white",
            )
    plt.close(fig)


def main() -> None:
    FIG.mkdir(parents=True, exist_ok=True)
    PROV.mkdir(parents=True, exist_ok=True)
    by_case = load_counts()
    pairs = active_pair_specs()
    pending = sorted(
        {
            str(spec["left"].relative_to(ROOT))
            for spec in PAIR_SPECS
            if not spec["left"].is_file()
        }
        | {
            str(spec["right"].relative_to(ROOT))
            for spec in PAIR_SPECS
            if not spec["right"].is_file()
        }
    )
    if not pairs:
        raise SystemExit("No image pairs ready: " + ", ".join(sorted(set(pending))))
    row_metrics = []
    for spec in pairs:
        metrics = diff_pipeline(spec["left"], spec["right"])
        row_metrics.append(metrics)
        print(
            f"{spec['case']}: size={metrics['size']} "
            f"changed_fraction={metrics['changed_fraction']:.4f} "
            f"regions={len(metrics['boxes'])}"
        )
    for language in ("zh", "en"):
        render(language, by_case, pairs, row_metrics)
    summary = {
        "blur_sigma_px": BLUR_SIGMA_PX,
        "diff_threshold": DIFF_THRESHOLD,
        "min_region_area_px": MIN_REGION_AREA_PX,
        "resize": "LANCZOS to smaller of pair",
        "pending_inputs": sorted(set(pending)),
        "object_count_rows_ch11": len(by_case["ch11"]),
        "object_count_rows_ch07": len(by_case["ch07"]),
    }
    for spec, metrics in zip(pairs, row_metrics):
        summary[f"{spec['case']}_changed_fraction"] = metrics["changed_fraction"]
        summary[f"{spec['case']}_regions"] = len(metrics["boxes"])
    (PROV / "diff-params.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    (PROV / "data-check.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
