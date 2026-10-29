#!/usr/bin/env python3
"""Generate chapter 9 python figures, provenance, and optional assemblies."""
# SPDX-License-Identifier: MIT
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROV = ROOT / "provenance" / "ch09"
FIG = ROOT / "figures" / "ch09"
PY = ROOT / ".venv/bin/python"


def run(cmd, timeout=600):
    subprocess.run(cmd, check=True, cwd=ROOT, timeout=timeout)


def main() -> None:
    PROV.mkdir(parents=True, exist_ok=True)
    FIG.mkdir(parents=True, exist_ok=True)
    if not PY.is_file():
        raise SystemExit("Create .venv per task instructions.")

    run([str(PY), str(ROOT / "scripts/sim_perovskite.py")], timeout=120)
    run([str(PY), str(ROOT / "scripts/ch09_panels.py")], timeout=300)

    assembly_status = {}
    for version, langs in (("v1", ("zh", "en")), ("v2", ("zh", "en"))):
        for lang in langs:
            key = f"ch09-0{6 if version == 'v1' else 7}-{version}-{lang}"
            result = subprocess.run(
                [str(PY), str(ROOT / "scripts/ch09_assemble.py"), "--version", version, "--lang", lang],
                cwd=ROOT,
                timeout=300,
                capture_output=True,
                text=True,
            )
            if result.returncode == 0:
                assembly_status[key] = "complete"
            elif result.returncode == 2:
                assembly_status[key] = "skipped (codex panels a/b missing)"
            else:
                assembly_status[key] = f"failed: {result.stderr.strip()[:200]}"

    sys.path.insert(0, str(ROOT / "scripts"))
    from ch09_plot_utils import load_jv, load_metrics, load_t80  # noqa: E402

    jv = load_jv()
    metrics = load_metrics()
    t80 = load_t80()
    check = {
        "date": date.today().isoformat(),
        "data_status": "simulated teaching data (scripts/sim_perovskite.py)",
        "jv_rows_control": len(jv["control"][0]),
        "jv_rows_modified": len(jv["modified"][0]),
        "control_PCE_percent": float(metrics["control"]["PCE"]),
        "modified_PCE_percent": float(metrics["modified"]["PCE"]),
        "control_T80_h": t80["control"],
        "modified_T80_h": t80["modified"],
        "external_downloads": [],
        "figures_python": [
            "ch09-05-data-panels",
            "work/panel-c",
            "work/panel-d",
        ],
        "figures_assembly": assembly_status,
        "figures_tikz": [
            "ch09-01-panel-argument-map",
            "ch09-02-layout-wireframes",
            "ch09-08-legend-drafting",
        ],
        "codex_pending": [
            "ch09-03-device-structure",
            "ch09-04-sem-like-illustration",
        ],
    }
    assert len(jv["control"][0]) > 2000
    assert len(jv["modified"][0]) > 2000
    assert abs(check["control_PCE_percent"] - 19.21) < 0.15
    assert abs(check["modified_PCE_percent"] - 20.98) < 0.15
    assert check["control_T80_h"] == "210"

    (PROV / "data-check.json").write_text(json.dumps(check, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(check, indent=2))


if __name__ == "__main__":
    main()
