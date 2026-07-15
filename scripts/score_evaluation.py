#!/usr/bin/env python3
"""Calculate an evaluation decision from a JSON rubric and scored result."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    """Load a JSON object from disk."""
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected a JSON object: {path}")
    return value


def score_evaluation(rubric: dict[str, Any], result: dict[str, Any]) -> dict[str, Any]:
    """Validate scores, calculate weighted total, and return a pass decision."""
    dimensions = rubric.get("dimensions", [])
    scores = result.get("dimension_scores", {})
    if not isinstance(dimensions, list) or not dimensions:
        raise ValueError("rubric dimensions must be a non-empty list")
    if not isinstance(scores, dict):
        raise ValueError("result dimension_scores must be an object")

    weights = [dimension.get("weight") for dimension in dimensions]
    if any(not isinstance(weight, (int, float)) for weight in weights):
        raise ValueError("every rubric dimension must have a numeric weight")
    if sum(weights) != 100:
        raise ValueError(f"rubric weights must total 100, got {sum(weights)}")

    weighted_total = 0.0
    critical_failures: list[str] = []
    dimension_report: list[dict[str, Any]] = []
    contract = rubric.get("pass_contract", {})
    critical_minimum = contract.get("critical_dimension_minimum", 60)

    for dimension in dimensions:
        dimension_id = dimension.get("id")
        if dimension_id not in scores:
            raise ValueError(f"missing score for dimension: {dimension_id}")
        score_value = scores[dimension_id]
        score = (
            score_value.get("score") if isinstance(score_value, dict) else score_value
        )
        if not isinstance(score, (int, float)) or not 0 <= score <= 100:
            raise ValueError(f"score for {dimension_id} must be between 0 and 100")
        weighted = score * dimension["weight"] / 100
        weighted_total += weighted
        if dimension.get("critical") and score < critical_minimum:
            critical_failures.append(dimension_id)
        dimension_report.append(
            {
                "id": dimension_id,
                "score": score,
                "weight": dimension["weight"],
                "weighted_score": round(weighted, 2),
            }
        )

    gate_results = result.get("hard_gates", {})
    if not isinstance(gate_results, dict):
        raise ValueError("result hard_gates must be an object")
    failed_gates: list[str] = []
    for gate in rubric.get("hard_gates", []):
        gate_id = gate.get("id")
        value = gate_results.get(gate_id)
        status = value.get("status") if isinstance(value, dict) else value
        if status != "pass":
            failed_gates.append(gate_id)

    minimum_total = contract.get("total_score_minimum", 80)
    total = round(weighted_total, 2)
    passed = total >= minimum_total and not critical_failures and not failed_gates
    return {
        "total_score": total,
        "decision": "pass" if passed else "revise",
        "dimension_scores": dimension_report,
        "critical_failures": critical_failures,
        "failed_hard_gates": failed_gates,
        "pass_contract": contract,
    }


def main() -> int:
    """Run evaluation scoring and print JSON."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("rubric", type=Path)
    parser.add_argument("result", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        report = score_evaluation(load_json(args.rubric), load_json(args.result))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"ERROR: {exc}")
        return 1
    serialized = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(serialized, encoding="utf-8")
    else:
        print(serialized, end="")
    return 0 if report["decision"] == "pass" else 2


if __name__ == "__main__":
    raise SystemExit(main())
