#!/usr/bin/env python3
"""Perform deterministic structural validation of a skill project workspace."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from init_project import DIRECTORIES


REQUIRED_FILES = {
    "project.json": (),
    "00-intake/capability-contract.yaml": (
        "desired_capability:",
        "primary_archetype:",
        "quality_target:",
    ),
    "01-evidence-plan/evidence-plan.yaml": ("research_axes:", "approval:"),
    "02-corpus/corpus-manifest.yaml": ("sources:", "rights:"),
    "05-rubric/evaluation-rubric.json": (),
    "06-generated-skill/skill-spec.yaml": ("skill:", "tests:"),
    "06-generated-skill/lifecycle-status.yaml": ("version:", "status:"),
}


def validate_rubric(path: Path, errors: list[str]) -> None:
    """Validate rubric JSON shape and arithmetic invariants."""
    try:
        rubric = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid rubric JSON: {exc}")
        return

    dimensions = rubric.get("dimensions")
    if not isinstance(dimensions, list) or not dimensions:
        errors.append("rubric must define a non-empty dimensions list")
        return
    weights = [item.get("weight") for item in dimensions if isinstance(item, dict)]
    if any(not isinstance(weight, (int, float)) for weight in weights):
        errors.append("every rubric dimension must have a numeric weight")
    elif sum(weights) != 100:
        errors.append(f"rubric dimension weights must total 100, got {sum(weights)}")


def validate_project(root: Path) -> dict[str, Any]:
    """Return a machine-readable validation report for a project root."""
    root = root.expanduser().resolve()
    errors: list[str] = []
    warnings: list[str] = []

    if not root.is_dir():
        return {"valid": False, "errors": [f"not a directory: {root}"], "warnings": []}

    for directory in DIRECTORIES:
        if not (root / directory).is_dir():
            errors.append(f"missing stage directory: {directory}")

    for relative, markers in REQUIRED_FILES.items():
        path = root / relative
        if not path.is_file():
            errors.append(f"missing required file: {relative}")
            continue
        if path.stat().st_size == 0:
            errors.append(f"required file is empty: {relative}")
            continue
        if markers:
            content = path.read_text(encoding="utf-8")
            for marker in markers:
                if marker not in content:
                    errors.append(f"{relative} is missing marker: {marker}")

    metadata_path = root / "project.json"
    if metadata_path.is_file():
        try:
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            if metadata.get("schema_version") != "0.2":
                warnings.append("project schema_version is not 0.2")
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid project.json: {exc}")

    rubric_path = root / "05-rubric/evaluation-rubric.json"
    if rubric_path.is_file():
        validate_rubric(rubric_path, errors)

    return {"valid": not errors, "errors": errors, "warnings": warnings}


def main() -> int:
    """Run project validation and print JSON."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_path", type=Path)
    args = parser.parse_args()
    report = validate_project(args.project_path)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
