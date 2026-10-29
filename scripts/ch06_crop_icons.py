#!/usr/bin/env python3
"""Crop ch06-icons-sheet.png into 12 transparent PNGs (see production/plans/ch06.md V3)."""
# SPDX-License-Identifier: MIT
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHEET = ROOT / "figures/ch06/ch06-icons-sheet.png"


def main() -> None:
    if not SHEET.is_file():
        raise SystemExit(f"Missing icon sheet: {SHEET}")
    subprocess.run([sys.executable, str(ROOT / "scripts/ch06_figures.py")], check=True, timeout=120)


if __name__ == "__main__":
    main()
