#!/usr/bin/env python3
"""Derive greyscale PNGs for FIG ch07-05 colour-restraint pair (Pillow only)."""
# SPDX-License-Identifier: MIT
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
PAIRS = (
    ("figures/ch07/ch07-05a-many-colours.png", "figures/ch07/ch07-05a-many-colours-gray.png"),
    ("figures/ch07/ch07-05b-v3-revised.png", "figures/ch07/ch07-05b-v3-revised-gray.png"),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    records = []
    for source_rel, target_rel in PAIRS:
        source = ROOT / source_rel
        target = ROOT / target_rel
        assert source.is_file(), f"missing source: {source_rel}"
        with Image.open(source) as image:
            width, height = image.size
            assert width > 0 and height > 0
            gray = ImageOps.grayscale(image)
            gray.save(target)
        src_hash = sha256(source)
        out_hash = sha256(target)
        assert target.is_file()
        records.append(
            {
                "source": source_rel,
                "target": target_rel,
                "width_px": width,
                "height_px": height,
                "source_sha256": src_hash,
                "output_sha256": out_hash,
                "transform": "PIL.ImageOps.grayscale only",
            }
        )
    summary = {
        "script": "scripts/ch07_grayscale.py",
        "figures": records,
        "note": "No external data; greyscale derivatives for teaching comparison.",
    }
    out_json = ROOT / "provenance/ch07/data-check.json"
    out_json.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
