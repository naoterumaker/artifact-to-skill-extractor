#!/usr/bin/env python3
"""Validate prompt-test coverage and score externally observed test results.

This script does not pretend to infer model behavior. A model or human runs the
prompts, records pass/fail evidence, and this script checks coverage and computes
the deterministic decision.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


SUITE_MINIMUMS = {
    "should_trigger": 5,
    "should_not_trigger": 5,
    "boundary": 3,
    "functional": 3,
}


def load_object(path: Path) -> dict[str, Any]:
    """Load a JSON object."""
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected a JSON object: {path}")
    return value


def normalize_fixture(fixture: dict[str, Any]) -> list[dict[str, str]]:
    """Validate suite coverage and return normalized test cases."""
    cases: list[dict[str, str]] = []
    identifiers: set[str] = set()
    for suite, minimum in SUITE_MINIMUMS.items():
        entries = fixture.get(suite)
        if not isinstance(entries, list):
            raise ValueError(f"fixture suite must be a list: {suite}")
        if len(entries) < minimum:
            raise ValueError(
                f"fixture suite {suite} needs at least {minimum} cases, got {len(entries)}"
            )
        for index, entry in enumerate(entries, start=1):
            if isinstance(entry, str):
                case_id = f"{suite}-{index:03d}"
                prompt = entry
            elif isinstance(entry, dict):
                case_id = str(entry.get("id") or f"{suite}-{index:03d}")
                prompt_value = entry.get("prompt") or entry.get("task")
                if not isinstance(prompt_value, str):
                    raise ValueError(f"case {case_id} is missing a string prompt")
                prompt = prompt_value
            else:
                raise ValueError(f"invalid case in {suite} at position {index}")
            if not prompt.strip():
                raise ValueError(f"case {case_id} has an empty prompt")
            if case_id in identifiers:
                raise ValueError(f"duplicate case id: {case_id}")
            identifiers.add(case_id)
            cases.append({"case_id": case_id, "suite": suite, "prompt": prompt})
    return cases


def score_observations(
    cases: list[dict[str, str]],
    observations: dict[str, Any],
    minimum_pass_rate: float,
) -> dict[str, Any]:
    """Join observed pass/fail records to cases and calculate a decision."""
    results = observations.get("results")
    if not isinstance(results, list):
        raise ValueError("observations must contain a results list")
    by_id: dict[str, dict[str, Any]] = {}
    for result in results:
        if not isinstance(result, dict) or not isinstance(result.get("case_id"), str):
            raise ValueError("every observation needs a string case_id")
        if result["case_id"] in by_id:
            raise ValueError(f"duplicate observation: {result['case_id']}")
        if result.get("status") not in {"pass", "fail"}:
            raise ValueError(
                f"observation {result['case_id']} status must be pass or fail"
            )
        by_id[result["case_id"]] = result

    known_ids = {case["case_id"] for case in cases}
    unknown_ids = sorted(set(by_id) - known_ids)
    if unknown_ids:
        raise ValueError(
            f"observations contain unknown case ids: {', '.join(unknown_ids)}"
        )

    rows: list[dict[str, Any]] = []
    passed = 0
    failed = 0
    pending = 0
    for case in cases:
        observed = by_id.get(case["case_id"])
        status = observed.get("status") if observed else "pending"
        evidence = observed.get("evidence", "") if observed else ""
        if status == "pass":
            passed += 1
        elif status == "fail":
            failed += 1
        else:
            pending += 1
        rows.append({**case, "status": status, "evidence": evidence})

    observed_total = passed + failed
    pass_rate = passed / observed_total if observed_total else 0.0
    decision = "pass" if pending == 0 and pass_rate >= minimum_pass_rate else "revise"
    return {
        "decision": decision,
        "cases_total": len(cases),
        "passed": passed,
        "failed": failed,
        "pending": pending,
        "pass_rate": round(pass_rate, 4),
        "minimum_pass_rate": minimum_pass_rate,
        "cases": rows,
    }


def main() -> int:
    """Validate a fixture or score supplied observations."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", type=Path)
    parser.add_argument("--observations", type=Path)
    parser.add_argument("--minimum-pass-rate", type=float, default=1.0)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if not 0 <= args.minimum_pass_rate <= 1:
        print("ERROR: --minimum-pass-rate must be between 0 and 1")
        return 1
    try:
        cases = normalize_fixture(load_object(args.fixture))
        if args.observations:
            report = score_observations(
                cases, load_object(args.observations), args.minimum_pass_rate
            )
        else:
            report = {
                "decision": "plan-valid",
                "cases_total": len(cases),
                "suite_counts": {
                    suite: sum(case["suite"] == suite for case in cases)
                    for suite in SUITE_MINIMUMS
                },
                "note": "Run these prompts with the target agent and supply observations for behavioral scoring.",
                "cases": cases,
            }
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"ERROR: {exc}")
        return 1

    serialized = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(serialized, encoding="utf-8")
    else:
        print(serialized, end="")
    return 0 if report["decision"] in {"pass", "plan-valid"} else 2


if __name__ == "__main__":
    raise SystemExit(main())
