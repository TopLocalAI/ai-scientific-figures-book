#!/usr/bin/env python3
"""Generate all chapter 12 python figures, reuse copies, and provenance."""
# SPDX-License-Identifier: MIT
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROV = ROOT / "provenance" / "ch12"
PY = ROOT / ".venv/bin/python"


def run(script: str, *extra: str, timeout: int = 600) -> None:
    cmd = [str(PY), str(ROOT / "scripts" / script), *extra]
    subprocess.run(cmd, check=True, cwd=ROOT, timeout=timeout)


def main() -> None:
    if not PY.is_file():
        raise SystemExit("Create .venv: python3 -m venv .venv && .venv/bin/pip install -r requirements.txt")
    PROV.mkdir(parents=True, exist_ok=True)
    run("sim_perovskite.py", timeout=120)
    run("ch12_reuse.py", timeout=120)
    run("ch12_visual_angle.py", timeout=300)
    run("ch12_slides.py", timeout=600)
    run("ch12_pasted_vs_rebuilt.py", timeout=300)
    run("ch12_poster.py", timeout=900)
    run("ch12_poster.py", "--draft", timeout=600)
    run("ch12_squint.py", timeout=300)

    sys.path.insert(0, str(ROOT / "scripts"))
    from ch12_plot_utils import assert_perovskite_metrics  # noqa: E402

    metrics_info = assert_perovskite_metrics()
    reuse = json.loads((PROV / "reuse-copies.json").read_text(encoding="utf-8"))
    check = {
        "date": date.today().isoformat(),
        "data_status": "simulated teaching data (scripts/sim_perovskite.py)",
        "control_PCE_percent": metrics_info["control_PCE"],
        "modified_PCE_percent": metrics_info["modified_PCE"],
        "control_T80_h": metrics_info["control_T80_h"],
        "control_retention_1000h": metrics_info["control_retention_1000h"],
        "modified_retention_1000h": metrics_info["modified_retention_1000h"],
        "visual_angle_checks": {"pt_1.5m": 33.75, "pt_D_over_H_6": 25.416},
        "external_downloads": [],
        "reuse_figures": reuse,
        "figure_status": {
            "ch12-01-three-viewing-conditions": "tikz (compile via tikz-preview-ch12.tex)",
            "ch12-02-visual-angle-text-size": "complete",
            "ch12-03-paper-figure-2": "reuse from ch09-07-assembly-final",
            "ch12-04-slide-sequence": "complete",
            "ch12-05a-pasted": "complete",
            "ch12-05b-rebuilt": "complete",
            "ch12-06-a0-poster-layout": "complete",
            "ch12-07-poster-hall-distances": "codex-image (not in scope; base PNG present)",
            "ch12-08a-dense-squint": "complete",
            "ch12-08b-focused-squint": "complete",
        },
    }
    (PROV / "data-check.json").write_text(json.dumps(check, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(check, indent=2))


if __name__ == "__main__":
    main()
