#!/usr/bin/env python3
"""Perform deterministic structural validation of a compiler project workspace."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from init_project import DIRECTORIES, LEGACY_DIRECTORIES


LEGACY_REQUIRED_FILES = {
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

REQUIRED_FILES = {
    "project.json": (),
    "00-intake/capability-contract.yaml": (
        "system_profile:",
        "desired_capability:",
        "intended_change:",
        "distribution_context:",
        "quality_target:",
    ),
    "00-intake/system-manifest.json": (),
    "01-evidence-plan/evidence-plan.yaml": ("research_axes:", "approval:"),
    "02-corpus/corpus-manifest.yaml": ("sources:", "rights:"),
    "04-comparisons/comparison-matrix.csv": ("case_id,source_id",),
    "05-doctrine/doctrine-hypothesis.md": ("# Doctrine Hypothesis",),
    "06-grammar/grammar-pattern.md": ("# Grammar Pattern",),
    "07-decision-units/decision-001.json": (),
    "08-toolchain/capability-registry.json": (),
    "09-evaluation-contract/evaluation-rubric.json": (),
    "09-evaluation-contract/system-evaluation-rubric.json": (),
    "10-execution-graphs/execution-001.json": (),
    "11-generated-system/skill-spec.yaml": ("skill:", "tests:"),
    "11-generated-system/lifecycle-status.yaml": ("version:", "status:"),
    "13-evaluations/evaluation-result-template.json": (),
    "13-evaluations/system-evaluation-result-template.json": (),
}


def load_json(path: Path, errors: list[str], label: str) -> dict[str, Any] | None:
    """Load a JSON object or append a validation error."""
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid {label}: {exc}")
        return None
    if not isinstance(value, dict):
        errors.append(f"{label} must contain a JSON object")
        return None
    return value


def validate_rubric(path: Path, errors: list[str]) -> None:
    """Validate rubric JSON shape and arithmetic invariants."""
    rubric = load_json(path, errors, "rubric JSON")
    if rubric is None:
        return

    dimensions = rubric.get("dimensions")
    if not isinstance(dimensions, list) or not dimensions:
        errors.append("rubric must define a non-empty dimensions list")
        return
    weights = [item.get("weight") for item in dimensions if isinstance(item, dict)]
    if len(weights) != len(dimensions) or any(
        not isinstance(weight, (int, float)) for weight in weights
    ):
        errors.append("every rubric dimension must have a numeric weight")
    elif sum(weights) != 100:
        errors.append(f"rubric dimension weights must total 100, got {sum(weights)}")
    if rubric.get("schema_version") != "0.3":
        return
    required_fields = {
        "id",
        "weight",
        "critical",
        "question",
        "anchors",
        "evidence_required",
    }
    for index, dimension in enumerate(dimensions, start=1):
        if not isinstance(dimension, dict):
            continue
        missing = sorted(required_fields - set(dimension))
        if missing:
            errors.append(
                f"rubric dimension {index} missing fields: {', '.join(missing)}"
            )
            continue
        anchors = dimension.get("anchors")
        if not isinstance(anchors, dict) or not {"0", "60", "80", "100"}.issubset(
            anchors
        ):
            errors.append(f"rubric dimension {index} needs 0/60/80/100 anchors")


def validate_manifest(
    root: Path,
    metadata: dict[str, Any],
    errors: list[str],
) -> None:
    """Validate the v0.3 system manifest."""
    path = root / "00-intake/system-manifest.json"
    if not path.is_file():
        return
    manifest = load_json(path, errors, "system manifest JSON")
    if manifest is None:
        return
    if manifest.get("schema_version") != "0.3":
        errors.append("system manifest schema_version must be 0.3")
    if manifest.get("project_id") != metadata.get("project_id"):
        errors.append("system manifest project_id must match project.json")
    profile = manifest.get("profile")
    if profile not in {"procedural", "creative", "hybrid"}:
        errors.append("system manifest profile must be procedural, creative, or hybrid")
    if metadata.get("profile") != profile:
        errors.append("system manifest profile must match project.json")
    expected_flags = {
        "requires_doctrine": profile in {"creative", "hybrid"},
        "requires_grammar": profile in {"creative", "hybrid"},
        "requires_toolchain": profile == "hybrid",
    }
    for field, expected in expected_flags.items():
        if manifest.get(field) is not expected:
            errors.append(f"system manifest {field} must be {str(expected).lower()}")

    contract_path = root / "00-intake/capability-contract.yaml"
    if contract_path.is_file():
        contract = contract_path.read_text(encoding="utf-8")
        expected_contract_lines = (
            f'system_profile: "{profile}"',
            f"  doctrine_required: {str(expected_flags['requires_doctrine']).lower()}",
            f"  grammar_required: {str(expected_flags['requires_grammar']).lower()}",
            f"  toolchain_required: {str(expected_flags['requires_toolchain']).lower()}",
        )
        for line in expected_contract_lines:
            if line not in contract:
                errors.append(f"capability contract does not match profile: {line}")

    skill_spec_path = root / "11-generated-system/skill-spec.yaml"
    if skill_spec_path.is_file():
        skill_spec = skill_spec_path.read_text(encoding="utf-8")
        expected_line = f'system_profile: "{profile}"'
        if expected_line not in skill_spec:
            errors.append(f"skill spec does not match profile: {expected_line}")


def validate_project(root: Path) -> dict[str, Any]:
    """Return a machine-readable structural validation report for a project root."""
    root = root.expanduser().resolve()
    errors: list[str] = []
    warnings: list[str] = []

    if not root.is_dir():
        return {"valid": False, "errors": [f"not a directory: {root}"], "warnings": []}

    metadata_path = root / "project.json"
    if not metadata_path.is_file():
        return {
            "valid": False,
            "errors": ["missing required file: project.json"],
            "warnings": [],
        }
    metadata = load_json(metadata_path, errors, "project.json")
    if metadata is None:
        return {"valid": False, "errors": errors, "warnings": warnings}

    schema_version = metadata.get("schema_version")
    if schema_version == "0.2":
        directories = LEGACY_DIRECTORIES
        required_files = LEGACY_REQUIRED_FILES
        rubric_relative = "05-rubric/evaluation-rubric.json"
        warnings.append("legacy project schema 0.2; migrate before adding v0.3 IR")
    elif schema_version == "0.3":
        directories = DIRECTORIES
        required_files = REQUIRED_FILES
        rubric_relative = "09-evaluation-contract/evaluation-rubric.json"
    else:
        return {
            "valid": False,
            "errors": [f"unsupported project schema_version: {schema_version}"],
            "warnings": [],
        }

    for directory in directories:
        if not (root / directory).is_dir():
            errors.append(f"missing stage directory: {directory}")

    for relative, markers in required_files.items():
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

    rubric_path = root / rubric_relative
    if rubric_path.is_file():
        validate_rubric(rubric_path, errors)

    if schema_version == "0.3":
        system_rubric_path = (
            root / "09-evaluation-contract/system-evaluation-rubric.json"
        )
        if system_rubric_path.is_file():
            validate_rubric(system_rubric_path, errors)
        validate_manifest(root, metadata, errors)

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
