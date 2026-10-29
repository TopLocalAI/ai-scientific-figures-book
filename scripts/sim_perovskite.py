#!/usr/bin/env python3
"""Simulated perovskite J–V and stability curves (Ch 9/12/13 teaching data)."""
# SPDX-License-Identifier: MIT
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
VT = 0.025693  # V at 25 °C
PIN = 100.0  # mW/cm² AM1.5G

GROUPS = {
    "control": {
        "J_L_mA": 22.5,
        "V_oc_target": 1.10,
        "n": 1.6,
        "R_s": 2.5,
        "R_sh": 1500.0,
    },
    "modified": {
        "J_L_mA": 22.8,
        "V_oc_target": 1.14,
        "n": 1.5,
        "R_s": 2.0,
        "R_sh": 3000.0,
    },
}


def j0_from_voc(J_L: float, V_oc: float, n: float, R_sh: float) -> float:
    denom = pow(2.718281828459045, V_oc / (n * VT)) - 1.0
    return (J_L - V_oc / R_sh) / denom


def solve_j(voltage: float, J_L: float, J0: float, n: float, R_s: float, R_sh: float) -> float:
    lo, hi = -0.5, J_L * 1.05

    def residual(j: float) -> float:
        v_eff = voltage + j * R_s
        return (
            j
            - J_L
            + J0 * (pow(2.718281828459045, v_eff / (n * VT)) - 1.0)
            + v_eff / R_sh
        )

    if residual(lo) * residual(hi) > 0:
        raise RuntimeError(f"No bracket for V={voltage}")
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if residual(mid) * residual(lo) <= 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def metrics_from_curve(voltages, currents_mA):
    jsc = currents_mA[0]
    voc = voltages[0]
    for v, j in zip(voltages, currents_mA):
        if j <= 0:
            voc = v
            break
    else:
        voc = voltages[-1]
    power = [v * j for v, j in zip(voltages, currents_mA)]
    p_max = max(power)
    idx = power.index(p_max)
    vmp, jmp = voltages[idx], currents_mA[idx]
    ff = p_max / (jsc * voc) if jsc * voc else 0.0
    pce = p_max / PIN
    return {
        "Jsc": jsc,
        "Voc": voc,
        "FF": ff,
        "PCE": pce,
        "Vmp": vmp,
        "Jmp": jmp,
    }


def stability_curve(t_h: float, burn: float, tau_burn: float, tau_decay: float) -> float:
    return (1.0 - burn * (1.0 - pow(2.718281828459045, -t_h / tau_burn))) * pow(
        2.718281828459045, -t_h / tau_decay
    )


def write_jv():
    rows = []
    metrics_rows = []
    for group, params in GROUPS.items():
        J_L = params["J_L_mA"] / 1000.0
        J0 = j0_from_voc(J_L, params["V_oc_target"], params["n"], params["R_sh"])
        v = 0.0
        curve_v, curve_j = [], []
        while v <= 1.200001:
            j = solve_j(v, J_L, J0, params["n"], params["R_s"], params["R_sh"])
            if j < 0 and curve_j:
                break
            j_mA = j * 1000.0
            rows.append(
                {
                    "group": group,
                    "voltage_V": f"{v:.4f}",
                    "current_density_mA_cm2": f"{j_mA:.4f}",
                }
            )
            curve_v.append(v)
            curve_j.append(j_mA)
            v += 0.0005
        m = metrics_from_curve(curve_v, curve_j)
        metrics_rows.append(
            {
                "group": group,
                "Jsc": f"{m['Jsc']:.4f}",
                "Voc": f"{m['Voc']:.4f}",
                "FF": f"{m['FF']:.4f}",
                "PCE": f"{m['PCE'] * 100:.4f}",
                "Vmp": f"{m['Vmp']:.4f}",
                "Jmp": f"{m['Jmp']:.4f}",
            }
        )

    jv_path = DATA / "sim-perovskite-jv.csv"
    with jv_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(
            stream, fieldnames=["group", "voltage_V", "current_density_mA_cm2"]
        )
        writer.writeheader()
        writer.writerows(rows)

    metrics_path = DATA / "sim-perovskite-jv-metrics.csv"
    with metrics_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames=["group", "Jsc", "Voc", "FF", "PCE", "Vmp", "Jmp"],
        )
        writer.writeheader()
        for row in metrics_rows:
            writer.writerow(row)
    return metrics_rows


def write_stability():
    specs = {
        "control": (0.08, 20.0, 1500.0),
        "modified": (0.04, 20.0, 9000.0),
    }
    rows = []
    t80 = {}
    for group, (burn, tau_b, tau_d) in specs.items():
        t80_val = ">1000"
        for t in range(0, 1001, 10):
            y = stability_curve(float(t), burn, tau_b, tau_d)
            rows.append(
                {
                    "group": group,
                    "time_h": str(t),
                    "normalized_pce": f"{y:.6f}",
                }
            )
            if t80_val == ">1000" and y < 0.80:
                t80_val = str(t)
        t80[group] = t80_val

    path = DATA / "sim-perovskite-stability.csv"
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=["group", "time_h", "normalized_pce"])
        writer.writeheader()
        writer.writerows(rows)

    t80_path = DATA / "sim-perovskite-stability-t80.csv"
    with t80_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=["group", "T80_h"])
        writer.writeheader()
        for group in specs:
            writer.writerow({"group": group, "T80_h": t80[group]})
    return t80


def main():
    DATA.mkdir(parents=True, exist_ok=True)
    metrics = write_jv()
    t80 = write_stability()
    control = next(r for r in metrics if r["group"] == "control")
    modified = next(r for r in metrics if r["group"] == "modified")
    summary = {
        "script": "sim_perovskite.py",
        "data_status": "simulated teaching data",
        "jv_rows_per_group": 2401,
        "control_PCE_percent": float(control["PCE"]),
        "modified_PCE_percent": float(modified["PCE"]),
        "control_T80_h": t80["control"],
        "modified_T80_h": t80["modified"],
        "stability_1000h_control": stability_curve(1000, 0.08, 20, 1500),
        "stability_1000h_modified": stability_curve(1000, 0.04, 20, 9000),
    }
    # Assert key metrics (tolerances allow bisection / rounding)
    assert abs(float(control["Jsc"]) - 22.46) < 0.05
    assert abs(float(control["Voc"]) - 1.100) < 0.01
    assert abs(float(control["PCE"]) - 19.21) < 0.15
    assert abs(float(modified["Jsc"]) - 22.78) < 0.05
    assert abs(float(modified["Voc"]) - 1.140) < 0.01
    assert abs(float(modified["PCE"]) - 20.98) < 0.15
    assert t80["control"] != ">1000"
    assert abs(summary["stability_1000h_control"] - 0.47) < 0.03
    assert abs(summary["stability_1000h_modified"] - 0.86) < 0.03
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
