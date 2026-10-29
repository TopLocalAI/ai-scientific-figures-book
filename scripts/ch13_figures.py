#!/usr/bin/env python3
"""Generate all chapter 13 python figures and provenance summaries."""
# SPDX-License-Identifier: MIT
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROV = ROOT / "provenance" / "ch13"
FIG = ROOT / "figures" / "ch13"


def run_script(name: str) -> None:
    subprocess.run(
        [str(ROOT / ".venv/bin/python"), str(ROOT / "scripts" / name)],
        check=True,
        cwd=ROOT,
        timeout=600,
    )


def main() -> None:
    PROV.mkdir(parents=True, exist_ok=True)
    FIG.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [str(ROOT / ".venv/bin/python"), str(ROOT / "scripts/sim_perovskite.py")],
        check=True,
        cwd=ROOT,
        timeout=120,
    )
    for script in (
        "ch13_upsampling.py",
        "ch13_text_final_width.py",
        "ch13_vector_container.py",
        "ch13_cvd.py",
    ):
        run_script(script)

    sys.path.insert(0, str(ROOT / "scripts"))
    import plot_paired  # noqa: E402
    from ch13_plot_utils import load_jv, load_metrics  # noqa: E402

    _, pairs = plot_paired.load_data()
    metrics = load_metrics()
    jv = load_jv()
    check = {
        "date": date.today().isoformat(),
        "data_status": "simulated teaching data",
        "paired_example": {
            "objects": 8,
            "SIM04_pair": pairs[3],
            "scaled_font_pt_at_85mm": round(10 * 85 / (7.3 * 25.4), 2),
        },
        "sim_perovskite_jv": {
            "control_points": len(jv["control"][0]),
            "modified_points": len(jv["modified"][0]),
            "control_PCE_percent": float(metrics["control"]["PCE"]),
            "modified_PCE_percent": float(metrics["modified"]["PCE"]),
        },
        "figures": [
            "ch13-02a-upsampled",
            "ch13-02b-native",
            "ch13-03-text-at-final-width",
            "ch13-05-vector-vs-container",
            "ch13-06-grayscale-and-cvd",
        ],
        "skipped": ["ch13-07-figure-checker-report (sourced screenshot per task note)"],
    }
    assert pairs[3] == (18.0, 17.0)
    assert abs(check["paired_example"]["scaled_font_pt_at_85mm"] - 4.58) < 0.05
    (PROV / "data-check.json").write_text(json.dumps(check, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(check, indent=2))


if __name__ == "__main__":
    main()
