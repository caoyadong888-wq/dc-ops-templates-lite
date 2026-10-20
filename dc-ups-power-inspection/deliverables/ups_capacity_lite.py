#!/usr/bin/env python3
"""Lite capacity check: load percent and N+1 headroom only.

The full pack adds 2N, a formula workbook, the inspection checklist,
and alert colouring. This script covers N and N+1.

usable kW for N   = module_count * module_kw
usable kW for N+1 = (module_count - 1) * module_kw
load ratio        = measured_kw / rated_kw
headroom ratio    = (usable_kw - measured_kw) / usable_kw

CRITICAL if load >= 0.80 or headroom < 0.15
WARN     if load >= 0.70 or headroom < 0.25
OK       otherwise
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


def evaluate(row: dict) -> dict:
    redundancy = row["redundancy"].strip()
    modules = int(row["module_count"])
    module_kw = float(row["module_kw"])
    rated = float(row["rated_kw"])
    measured = float(row["measured_kw"])
    if rated <= 0 or module_kw <= 0 or modules < 1 or measured < 0:
        raise ValueError(f"{row['asset_id']}: ratings must be positive")
    if redundancy == "N":
        usable = modules * module_kw
    elif redundancy == "N+1":
        if modules < 2:
            raise ValueError(f"{row['asset_id']}: N+1 needs 2 or more modules")
        usable = (modules - 1) * module_kw
    else:
        raise ValueError(f"{row['asset_id']}: lite script supports N and N+1 only")
    load = measured / rated
    headroom = (usable - measured) / usable
    if load >= 0.80 or headroom < 0.15:
        alert = "CRITICAL"
    elif load >= 0.70 or headroom < 0.25:
        alert = "WARN"
    else:
        alert = "OK"
    return {
        "asset_id": row["asset_id"].strip(),
        "redundancy": redundancy,
        "load": load,
        "usable": usable,
        "headroom_kw": usable - measured,
        "headroom": headroom,
        "alert": alert,
    }


def render(results: list[dict]) -> str:
    counts = {"CRITICAL": 0, "WARN": 0, "OK": 0}
    for item in results:
        counts[item["alert"]] += 1
    lines = [
        "UPS/PDU capacity report (lite)",
        f"assets={len(results)} critical={counts['CRITICAL']} warn={counts['WARN']} ok={counts['OK']}",
        f"{'asset_id':<12} {'mode':<6} {'load':>7} {'headroom':>9}  alert",
    ]
    for item in results:
        lines.append(
            f"{item['asset_id']:<12} {item['redundancy']:<6} "
            f"{item['load'] * 100:6.1f}% {item['headroom'] * 100:8.1f}%  {item['alert']}"
        )
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Lite N / N+1 capacity check.")
    parser.add_argument("--input", required=True, type=Path)
    args = parser.parse_args(argv)
    with args.input.open(newline="", encoding="utf-8") as handle:
        rows = [row for row in csv.DictReader(handle) if (row.get("asset_id") or "").strip()]
    if not rows:
        print("error: no asset rows", file=sys.stderr)
        return 2
    try:
        report = render([evaluate(row) for row in rows])
    except (ValueError, KeyError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    sys.stdout.write(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
