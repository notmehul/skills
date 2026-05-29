#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Scenario:
    name: str
    units: float
    addressable_pct: float
    adoption_pct: float
    price_per_unit_per_year: float


def tam(
    units: float,
    addressable_pct: float,
    adoption_pct: float,
    price_per_unit_per_year: float,
) -> float:
    return (
        units
        * (addressable_pct / 100.0)
        * (adoption_pct / 100.0)
        * price_per_unit_per_year
    )


def _fmt_money(x: float) -> str:
    return f"${x:,.0f}"


def as_markdown_table(rows: Iterable[tuple[str, float]]) -> str:
    lines: list[str] = []
    lines.append("| Scenario | TAM ($/yr) |")
    lines.append("|---|---:|")
    for name, value in rows:
        lines.append(f"| {name} | {_fmt_money(value)} |")
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Quick TAM sensitivity calculator")
    p.add_argument("--units", type=float, default=None)
    p.add_argument("--addressable", type=float, default=None, help="Percent (0-100)")
    p.add_argument("--adoption", type=float, default=None, help="Percent (0-100)")
    p.add_argument("--price", type=float, default=None, help="$ per unit per year")
    p.add_argument(
        "--csv",
        type=str,
        default=None,
        help="CSV with columns: scenario,units,addressable_pct,adoption_pct,price_per_unit_per_year",
    )
    p.add_argument(
        "--json", type=str, default=None, help="JSON array of scenario objects"
    )
    p.add_argument("--format", choices=["md", "json"], default="md")
    return p.parse_args()


def scenarios_from_csv(path: str) -> list[Scenario]:
    out: list[Scenario] = []
    with open(path, "r", newline="") as f:
        reader = csv.DictReader(f)
        required = {
            "scenario",
            "units",
            "addressable_pct",
            "adoption_pct",
            "price_per_unit_per_year",
        }
        missing = required - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"CSV missing columns: {', '.join(sorted(missing))}")
        for row in reader:
            out.append(
                Scenario(
                    name=str(row["scenario"]),
                    units=float(row["units"]),
                    addressable_pct=float(row["addressable_pct"]),
                    adoption_pct=float(row["adoption_pct"]),
                    price_per_unit_per_year=float(row["price_per_unit_per_year"]),
                )
            )
    return out


def scenarios_from_json(path: str) -> list[Scenario]:
    with open(path, "r") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("JSON must be an array")
    out: list[Scenario] = []
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("JSON array entries must be objects")
        out.append(
            Scenario(
                name=str(item["name"]),
                units=float(item["units"]),
                addressable_pct=float(item["addressable_pct"]),
                adoption_pct=float(item["adoption_pct"]),
                price_per_unit_per_year=float(item["price_per_unit_per_year"]),
            )
        )
    return out


def main() -> None:
    args = parse_args()

    scenarios: list[Scenario] = []
    if args.csv:
        scenarios = scenarios_from_csv(args.csv)
    elif args.json:
        scenarios = scenarios_from_json(args.json)
    else:
        required = [args.units, args.addressable, args.adoption, args.price]
        if any(v is None for v in required):
            raise SystemExit(
                "Provide either --csv/--json, or all of --units --addressable --adoption --price"
            )
        scenarios = [
            Scenario(
                name="base",
                units=float(args.units),
                addressable_pct=float(args.addressable),
                adoption_pct=float(args.adoption),
                price_per_unit_per_year=float(args.price),
            )
        ]

    rows: list[tuple[str, float]] = []
    for s in scenarios:
        rows.append(
            (
                s.name,
                tam(
                    s.units,
                    s.addressable_pct,
                    s.adoption_pct,
                    s.price_per_unit_per_year,
                ),
            )
        )

    if args.format == "json":
        payload = [{"scenario": name, "tam_per_year": value} for name, value in rows]
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print(as_markdown_table(rows))


if __name__ == "__main__":
    main()
