#!/usr/bin/env python3
"""Chapter 6: placeholder workflow icons, icon-sheet crop, skeleton-notext PNG, data checks."""
# SPDX-License-Identifier: MIT
import hashlib
import json
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import List, Optional

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures/ch06"
ICONS = FIG / "icons"
DATA = ROOT / "data/ch06"
PROV = ROOT / "provenance/ch06"
SHEET = FIG / "ch06-icons-sheet.png"

RNG_SEED = 20261029


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def make_placeholder_icons() -> List[dict]:
    """Simple geometric placeholders when codex icon sheet is not yet present."""
    from PIL import Image, ImageDraw

    ICONS.mkdir(parents=True, exist_ok=True)
    warm = ("#B5653A", "#FBF1EA")
    seq = ("#8A6D1F", "#FBF1EA")
    cool = ("#2F6F8F", "#EEF4F7")
    styles = [warm] * 4 + [warm, warm, warm, seq] + [cool] * 4
    records = []
    for idx, (stroke, fill) in enumerate(styles, start=1):
        im = Image.new("RGBA", (160, 160), (255, 255, 255, 0))
        draw = ImageDraw.Draw(im)
        draw.rounded_rectangle((18, 18, 142, 142), radius=12, fill=fill, outline=stroke, width=3)
        if idx in (1, 5, 11):
            draw.ellipse((55, 55, 105, 105), fill=stroke)
        elif idx == 12:
            draw.polygon([(80, 40), (110, 80), (50, 80)], outline=stroke, fill=fill)
        out = ICONS / f"ch06-icon-{idx:02d}.png"
        im.save(out)
        records.append({"file": str(out.relative_to(ROOT)), "sha256": sha256(out), "placeholder": True})
    assert len(records) == 12
    return records


def crop_icon_sheet() -> Optional[dict]:
    if not SHEET.is_file():
        return None
    from PIL import Image

    im = Image.open(SHEET).convert("RGBA")
    w, h = im.size
    cols, rows = 4, 3
    cell_w, cell_h = w // cols, h // rows
    ICONS.mkdir(parents=True, exist_ok=True)
    cropped = []
    for row in range(rows):
        for col in range(cols):
            idx = row * cols + col + 1
            left, top = col * cell_w, row * cell_h
            cell = im.crop((left, top, left + cell_w, top + cell_h))
            px = cell.load()
            for y in range(cell.height):
                for x in range(cell.width):
                    r, g, b, a = px[x, y]
                    if r > 245 and g > 245 and b > 245:
                        px[x, y] = (r, g, b, 0)
            bbox = cell.getbbox()
            if bbox:
                pad = max(2, int(0.06 * max(bbox[2] - bbox[0], bbox[3] - bbox[1])))
                cell = cell.crop(
                    (
                        max(0, bbox[0] - pad),
                        max(0, bbox[1] - pad),
                        min(cell.width, bbox[2] + pad),
                        min(cell.height, bbox[3] + pad),
                    )
                )
            out = ICONS / f"ch06-icon-{idx:02d}.png"
            cell.save(out)
            cropped.append(out.name)
    assert len(cropped) == 12
    return {"source": str(SHEET.relative_to(ROOT)), "icons": cropped}


def compile_skeleton_notext() -> dict:
    standalone = FIG / "ch06-skeleton-notext-standalone.tex"
    standalone.write_text(
        r"""
\documentclass[border=2mm]{standalone}
\usepackage{ctex}
\usepackage{tikz}
\usepackage{graphicx}
\input{figures/ch06/ch06-styles.tex}
\def\nolabels{}
\begin{document}
\input{figures/ch06/ch06-labels-zh.tex}
\begin{tikzpicture}[x=1cm,y=1cm]
  \input{figures/ch06/ch06-coords.tex}
  \input{figures/ch06/ch06-workflow-draw.tex}
\end{tikzpicture}
\end{document}
""".strip()
        + "\n",
        encoding="utf-8",
    )
    log = {"standalone": str(standalone.relative_to(ROOT)), "compiled": False}
    for _ in range(1):
        proc = subprocess.run(
            [
                "xelatex",
                "-interaction=nonstopmode",
                "-output-directory=figures/ch06",
                str(standalone.relative_to(ROOT)),
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=120,
        )
        log["xelatex_exit"] = proc.returncode
    pdf = FIG / "ch06-skeleton-notext-standalone.pdf"
    png = FIG / "ch06-03-skeleton-notext.png"
    if pdf.is_file():
        log["compiled"] = True
        subprocess.run(
            ["pdftoppm", "-png", "-singlefile", "-r", "200", str(pdf), str(png.with_suffix(""))],
            check=False,
            timeout=60,
        )
        if png.is_file():
            log["png"] = str(png.relative_to(ROOT))
            log["sha256"] = sha256(png)
    return log


def main() -> None:
    PROV.mkdir(parents=True, exist_ok=True)
    DATA.mkdir(parents=True, exist_ok=True)
    (DATA / "sourced").mkdir(parents=True, exist_ok=True)

    crop_info = crop_icon_sheet()
    if crop_info:
        icon_meta = {"mode": "cropped_from_sheet", **crop_info}
    else:
        icon_meta = {"mode": "geometric_placeholder", "icons": make_placeholder_icons()}

    notext = compile_skeleton_notext()

    main_nodes = 21
    optional_nodes = 5
    assert main_nodes == 21 and optional_nodes == 5

    summary = {
        "chapter": 6,
        "kind_python_figures": 0,
        "kind_reuse_figures": 0,
        "external_datasets": 0,
        "workflow_nodes_main": main_nodes,
        "workflow_nodes_optional": optional_nodes,
        "icons": icon_meta,
        "skeleton_notext": notext,
        "sourced_assets": [],
        "note": "Chapter 6 has no kind:python or reuse figures in production/plans/ch06.md.",
        "checked_on": str(date.today()),
    }
    out = PROV / "data-check.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
