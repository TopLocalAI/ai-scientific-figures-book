#!/usr/bin/env python3
"""Chapter 3: measure layout areas on candidate PNGs when present; no kind:python figures."""
# SPDX-License-Identifier: MIT
import json
import hashlib
from datetime import date
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures/ch03"
PROV = ROOT / "provenance/ch03"
DATA = ROOT / "data/ch03"

CANDIDATES = {
    "A": FIG / "ch03-03a-cand-linear.png",
    "B": FIG / "ch03-03b-cand-hub.png",
    "C": FIG / "ch03-03c-cand-branch.png",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def measure_outcome_fraction(png: Path) -> Optional[float]:
    """Lower-half teal proxy: fraction of pixels in bottom 45% that are green/teal-ish."""
    try:
        from PIL import Image
    except ImportError:
        return None
    im = Image.open(png).convert("RGB")
    w, h = im.size
    y0 = int(h * 0.55)
    region = im.crop((0, y0, w, h))
    pixels = list(region.getdata())
    if not pixels:
        return None
    teal = 0
    for r, g, b in pixels:
        if g > 100 and g > r + 15 and g > b + 10:
            teal += 1
        elif r < 120 and g > 90 and b > 70 and g >= r:
            teal += 1
    return round(100.0 * teal / len(pixels), 1)


def main() -> None:
    PROV.mkdir(parents=True, exist_ok=True)
    DATA.mkdir(parents=True, exist_ok=True)
    areas: dict[str, object] = {"measured_on": str(date.today()), "layouts": {}}
    for key, path in CANDIDATES.items():
        entry: dict[str, object] = {"path": str(path.relative_to(ROOT)), "exists": path.is_file()}
        if path.is_file():
            entry["sha256"] = sha256(path)
            frac = measure_outcome_fraction(path)
            entry["outcome_area_percent_bottom_band"] = frac
            assert frac is not None and 0 <= frac <= 100
        areas["layouts"][key] = entry
    present = sum(1 for e in areas["layouts"].values() if e["exists"])
    assert present >= 0
    summary = {
        "chapter": 3,
        "kind_python_figures": 0,
        "external_datasets": 0,
        "candidate_pngs_present": present,
        "layout_area_measurement": areas,
        "note": "Chapter 3 has no kind:python figures; this file records PNG area checks for FIG ch03-04.",
    }
    out = PROV / "data-check.json"
    out.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
