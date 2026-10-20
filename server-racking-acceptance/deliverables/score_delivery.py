#!/usr/bin/env python3
"""Lite delivery scorer. The full pack adds racking, sign-off, and the workbook.

A row FAILs when serial != asn_serial, seal_intact is not yes, packaging is
not intact, or shock_indicator is not ok.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


def score(row: dict) -> tuple[str, list[str]]:
    reasons = []
    if row["serial"].strip() != row["asn_serial"].strip():
        reasons.append("serial does not match ASN")
    if row["seal_intact"].strip().lower() != "yes":
        reasons.append("seal not intact")
    if row["packaging"].strip().lower() != "intact":
        reasons.append("packaging not intact")
    if row["shock_indicator"].strip().lower() != "ok":
        reasons.append("shock or tilt indicator tripped")
    return ("FAIL", reasons) if reasons else ("PASS", [])


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Score a delivery acceptance CSV.")
    parser.add_argument("--input", required=True, type=Path)
    args = parser.parse_args(argv)
    with args.input.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        print("error: no rows", file=sys.stderr)
        return 2
    passed = 0
    failed = 0
    lines = ["Delivery acceptance (lite)", "hostname     status  reasons"]
    try:
        for row in rows:
            status, reasons = score(row)
            if status == "PASS":
                passed += 1
            else:
                failed += 1
            lines.append(
                f"{row['hostname'].strip():<12} {status:<6}  {'; '.join(reasons)}"
            )
    except KeyError as exc:
        print(f"error: missing column {exc}", file=sys.stderr)
        return 2
    lines.append(f"delivery_pass={passed} delivery_fail={failed}")
    sys.stdout.write("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
