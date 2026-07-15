#!/usr/bin/env python3
"""Validate decision units, tool capabilities, and execution graphs for v0.3."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


DECISION_FIELDS = {
    "id",
    "status",
    "intent",
    "context",
    "preconditions",
    "evidence_needed",
    "decision_rule",
    "action",
    "parameters",
    "invariants",
    "verifier",
    "fallback",
    "failure_modes",
    "provenance",
    "confidence",
    "agency",
}
TOOL_FIELDS = {
    "id",
    "name",
    "version",
    "verified_at",
    "interfaces",
    "modalities",
    "operation_granularity",
    "source_of_truth",
    "state_readable",
    "partial_editable",
    "reproducibility",
    "parameterization",
    "batch_support",
    "preview",
    "evaluation_support",
    "human_round_trip",
    "constraints",
    "license",
    "failure_recovery",
}
NODE_FIELDS = {
    "id",
    "capability",
    "judgment_owner",
    "executor",
    "approval_owner",
    "state_owner",
    "inputs",
    "outputs",
    "verifier",
    "retry_policy",
    "fallback",
    "provenance",
}


def load_object(path: Path, errors: list[str]) -> dict[str, Any] | None:
    """Load a JSON object and append errors rather than raising."""
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid JSON {path}: {exc}")
        return None
    if not isinstance(value, dict):
        errors.append(f"expected JSON object: {path}")
        return None
    return value


def missing_fields(value: dict[str, Any], required: set[str]) -> list[str]:
    """Return sorted missing required fields."""
    return sorted(required - set(value))


def validate_decision_unit(
    unit: dict[str, Any],
    label: str,
    errors: list[str],
    complete: bool,
) -> None:
    """Validate a decision-unit object."""
    missing = missing_fields(unit, DECISION_FIELDS)
    if missing:
        errors.append(f"{label} missing decision fields: {', '.join(missing)}")
        return
    if unit.get("schema_version") != "0.3":
        errors.append(f"{label} schema_version must be 0.3")
    if unit.get("status") not in {"hypothesis", "experimental", "verified", "rejected"}:
        errors.append(f"{label} has invalid status")
    if not isinstance(unit.get("context"), dict):
        errors.append(f"{label} context must be an object")
    for field in (
        "preconditions",
        "evidence_needed",
        "parameters",
        "invariants",
        "failure_modes",
        "provenance",
    ):
        if not isinstance(unit.get(field), list):
            errors.append(f"{label} {field} must be a list")
    confidence = unit.get("confidence")
    if not isinstance(confidence, dict) or confidence.get("level") not in {
        "low",
        "medium",
        "high",
        "verified",
    }:
        errors.append(f"{label} confidence.level is invalid")
    for field in ("decision_rule", "action", "verifier", "fallback", "agency"):
        if not isinstance(unit.get(field), dict):
            errors.append(f"{label} {field} must be an object")

    agency = unit.get("agency")
    if isinstance(agency, dict):
        agency_missing = missing_fields(
            agency, {"judgment_owner", "executor", "approval_owner"}
        )
        if agency_missing:
            errors.append(f"{label} agency missing fields: {', '.join(agency_missing)}")

    if complete:
        for field in ("id", "intent"):
            if not isinstance(unit.get(field), str) or not unit[field].strip():
                errors.append(f"{label} {field} must be non-empty")
        if not unit.get("evidence_needed"):
            errors.append(f"{label} needs evidence_needed entries")
        if not unit.get("invariants"):
            errors.append(f"{label} needs invariants")
        if not unit.get("provenance"):
            errors.append(f"{label} needs provenance")
        verifier = unit.get("verifier", {})
        if not verifier.get("checks") or not verifier.get("pass_condition"):
            errors.append(f"{label} needs verifier checks and pass_condition")
        decision_rule = unit.get("decision_rule", {})
        if not decision_rule.get("when") or not decision_rule.get("choose"):
            errors.append(f"{label} needs decision conditions and a selection")
        action = unit.get("action", {})
        if not action.get("operation") or not action.get("output"):
            errors.append(f"{label} needs an executable action and output")
        fallback = unit.get("fallback", {})
        if not fallback.get("action"):
            errors.append(f"{label} needs a fallback action")
        confidence = unit.get("confidence", {})
        if confidence.get("basis") in {"", "template", None}:
            errors.append(f"{label} confidence needs an evidence basis")


def validate_registry(
    registry: dict[str, Any],
    label: str,
    errors: list[str],
    complete: bool,
    requires_toolchain: bool,
) -> set[str]:
    """Validate a tool-capability registry and return tool ids."""
    if registry.get("schema_version") != "0.3":
        errors.append(f"{label} schema_version must be 0.3")
    required_capabilities = registry.get("required_capabilities")
    tools = registry.get("tools")
    assignments = registry.get("assignments")
    manual_fallbacks = registry.get("manual_fallbacks")
    unsupported = registry.get("unsupported_capabilities")
    for field, value in {
        "required_capabilities": required_capabilities,
        "tools": tools,
        "assignments": assignments,
        "manual_fallbacks": manual_fallbacks,
        "unsupported_capabilities": unsupported,
    }.items():
        if not isinstance(value, list):
            errors.append(f"{label} {field} must be a list")
    if not isinstance(tools, list):
        return set()

    tool_ids: set[str] = set()
    for index, tool in enumerate(tools, start=1):
        tool_label = f"{label} tool[{index}]"
        if not isinstance(tool, dict):
            errors.append(f"{tool_label} must be an object")
            continue
        missing = missing_fields(tool, TOOL_FIELDS)
        if missing:
            errors.append(f"{tool_label} missing fields: {', '.join(missing)}")
            continue
        tool_id = tool.get("id")
        if not isinstance(tool_id, str) or not tool_id:
            errors.append(f"{tool_label} id must be non-empty")
        elif tool_id in tool_ids:
            errors.append(f"{label} duplicate tool id: {tool_id}")
        else:
            tool_ids.add(tool_id)
        if complete:
            for field in (
                "name",
                "version",
                "verified_at",
                "source_of_truth",
                "reproducibility",
                "failure_recovery",
            ):
                if not isinstance(tool.get(field), str) or not tool[field].strip():
                    errors.append(f"{tool_label} {field} must be non-empty")
            for field in ("state_readable", "partial_editable", "batch_support"):
                if not isinstance(tool.get(field), bool):
                    errors.append(f"{tool_label} {field} must be boolean")

    if isinstance(assignments, list):
        for index, assignment in enumerate(assignments, start=1):
            assignment_label = f"{label} assignment[{index}]"
            if not isinstance(assignment, dict):
                errors.append(f"{assignment_label} must be an object")
                continue
            capability = assignment.get("capability")
            primary_tool = assignment.get("primary_tool")
            if capability not in (required_capabilities or []):
                errors.append(f"{assignment_label} references unknown capability")
            if primary_tool not in tool_ids:
                errors.append(f"{assignment_label} references unknown primary_tool")
            if not assignment.get("fallback"):
                errors.append(f"{assignment_label} needs a fallback")

    fallback_capabilities: set[str] = set()
    if isinstance(manual_fallbacks, list):
        for index, fallback in enumerate(manual_fallbacks, start=1):
            fallback_label = f"{label} manual_fallback[{index}]"
            if not isinstance(fallback, dict):
                errors.append(f"{fallback_label} must be an object")
                continue
            capability = fallback.get("capability")
            if capability not in (required_capabilities or []):
                errors.append(f"{fallback_label} references unknown capability")
            elif capability in fallback_capabilities:
                errors.append(f"{label} duplicate manual fallback: {capability}")
            else:
                fallback_capabilities.add(capability)
            if not fallback.get("owner") or not fallback.get("procedure"):
                errors.append(f"{fallback_label} needs owner and procedure")

    if complete and requires_toolchain:
        if not required_capabilities:
            errors.append(f"{label} requires at least one capability")
        if not tools:
            errors.append(f"{label} requires at least one tool")
        assigned = {
            item.get("capability")
            for item in (assignments or [])
            if isinstance(item, dict)
        }
        covered = assigned | fallback_capabilities
        missing_capabilities = set(required_capabilities or []) - covered
        if missing_capabilities:
            errors.append(
                f"{label} unassigned capabilities: {', '.join(sorted(missing_capabilities))}"
            )
        unsupported_required = set(required_capabilities or []) & set(unsupported or [])
        if unsupported_required:
            errors.append(
                f"{label} required capabilities are unsupported: "
                f"{', '.join(sorted(unsupported_required))}"
            )
        if not registry.get("last_verified_at"):
            errors.append(f"{label} requires last_verified_at")
    return tool_ids


def has_cycle(node_ids: set[str], edges: list[dict[str, Any]]) -> bool:
    """Return true when non-iteration edges contain a directed cycle."""
    graph = {node_id: [] for node_id in node_ids}
    for edge in edges:
        if edge.get("type") == "iteration":
            continue
        source = edge.get("from")
        target = edge.get("to")
        if source in graph and target in graph:
            graph[source].append(target)

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node_id: str) -> bool:
        if node_id in visiting:
            return True
        if node_id in visited:
            return False
        visiting.add(node_id)
        if any(visit(neighbor) for neighbor in graph[node_id]):
            return True
        visiting.remove(node_id)
        visited.add(node_id)
        return False

    return any(visit(node_id) for node_id in node_ids)


def validate_graph(
    graph: dict[str, Any],
    label: str,
    errors: list[str],
    complete: bool,
    tool_ids: set[str],
) -> None:
    """Validate an execution graph."""
    if graph.get("schema_version") != "0.3":
        errors.append(f"{label} schema_version must be 0.3")
    nodes = graph.get("nodes")
    edges = graph.get("edges")
    if not isinstance(nodes, list):
        errors.append(f"{label} nodes must be a list")
        return
    if not isinstance(edges, list):
        errors.append(f"{label} edges must be a list")
        return
    node_ids: set[str] = set()
    for index, node in enumerate(nodes, start=1):
        node_label = f"{label} node[{index}]"
        if not isinstance(node, dict):
            errors.append(f"{node_label} must be an object")
            continue
        missing = missing_fields(node, NODE_FIELDS)
        if missing:
            errors.append(f"{node_label} missing fields: {', '.join(missing)}")
            continue
        node_id = node.get("id")
        if not isinstance(node_id, str) or not node_id:
            errors.append(f"{node_label} id must be non-empty")
        elif node_id in node_ids:
            errors.append(f"{label} duplicate node id: {node_id}")
        else:
            node_ids.add(node_id)
        tool_id = node.get("tool_id")
        if tool_id is not None and tool_id not in tool_ids:
            errors.append(f"{node_label} references unknown tool_id: {tool_id}")
        for field in ("inputs", "outputs", "provenance"):
            if not isinstance(node.get(field), list):
                errors.append(f"{node_label} {field} must be a list")
        retry_policy = node.get("retry_policy")
        if not isinstance(retry_policy, dict):
            errors.append(f"{node_label} retry_policy must be an object")
        elif not isinstance(retry_policy.get("maximum_attempts"), int):
            errors.append(f"{node_label} retry_policy needs maximum_attempts")
        if complete:
            for field in (
                "id",
                "capability",
                "judgment_owner",
                "executor",
                "state_owner",
                "verifier",
                "fallback",
            ):
                if not isinstance(node.get(field), str) or not node[field].strip():
                    errors.append(f"{node_label} {field} must be non-empty")
            if not node.get("outputs"):
                errors.append(f"{node_label} needs outputs")
            if not node.get("provenance"):
                errors.append(f"{node_label} needs provenance")

    for index, edge in enumerate(edges, start=1):
        edge_label = f"{label} edge[{index}]"
        if not isinstance(edge, dict):
            errors.append(f"{edge_label} must be an object")
            continue
        if edge.get("from") not in node_ids or edge.get("to") not in node_ids:
            errors.append(f"{edge_label} references unknown node")
        if edge.get("type") == "iteration" and (
            not isinstance(edge.get("maximum_rounds"), int)
            or edge.get("maximum_rounds", 0) < 1
            or not edge.get("stop_condition")
        ):
            errors.append(
                f"{edge_label} iteration needs maximum_rounds and stop_condition"
            )
    if has_cycle(node_ids, [edge for edge in edges if isinstance(edge, dict)]):
        errors.append(f"{label} contains an unbounded cycle")
    if complete:
        if not nodes:
            errors.append(f"{label} requires at least one node")
        if not graph.get("source_of_truth"):
            errors.append(f"{label} requires source_of_truth")
        iteration_policy = graph.get("iteration_policy")
        if not isinstance(iteration_policy, dict):
            errors.append(f"{label} requires iteration_policy")
        elif (
            not isinstance(iteration_policy.get("maximum_rounds"), int)
            or iteration_policy.get("maximum_rounds", 0) < 1
            or not iteration_policy.get("stop_condition")
        ):
            errors.append(f"{label} iteration_policy is incomplete")


def validate_system_ir(root: Path, complete: bool = False) -> dict[str, Any]:
    """Validate v0.3 intermediate representations under a project root."""
    root = root.expanduser().resolve()
    errors: list[str] = []
    warnings: list[str] = []
    manifest_path = root / "00-intake/system-manifest.json"
    manifest = load_object(manifest_path, errors)
    if manifest is None:
        return {"valid": False, "errors": errors, "warnings": warnings}
    profile = manifest.get("profile")
    if manifest.get("schema_version") != "0.3":
        errors.append("manifest schema_version must be 0.3")
    if profile not in {"procedural", "creative", "hybrid"}:
        errors.append("manifest profile must be procedural, creative, or hybrid")
    expected_flags = {
        "requires_doctrine": profile in {"creative", "hybrid"},
        "requires_grammar": profile in {"creative", "hybrid"},
        "requires_toolchain": profile == "hybrid",
    }
    for field, expected in expected_flags.items():
        if manifest.get(field) is not expected:
            errors.append(f"manifest {field} must be {str(expected).lower()}")
    if complete:
        target = manifest.get("target_system")
        if not isinstance(target, dict):
            errors.append("manifest target_system must be an object")
        else:
            required_target_fields = [
                "capability",
                "future_user",
                "execution_environment",
                "source_of_truth",
            ]
            if profile in {"creative", "hybrid"}:
                required_target_fields.append("distribution_context")
            for field in required_target_fields:
                if not isinstance(target.get(field), str) or not target[field].strip():
                    errors.append(f"manifest target_system.{field} must be non-empty")

    decision_paths = sorted((root / "07-decision-units").glob("*.json"))
    if not decision_paths:
        errors.append("no decision-unit JSON files found")
    for path in decision_paths:
        unit = load_object(path, errors)
        if unit is not None:
            validate_decision_unit(unit, str(path.relative_to(root)), errors, complete)

    registry_path = root / "08-toolchain/capability-registry.json"
    registry = load_object(registry_path, errors)
    tool_ids: set[str] = set()
    if registry is not None:
        tool_ids = validate_registry(
            registry,
            str(registry_path.relative_to(root)),
            errors,
            complete,
            bool(manifest.get("requires_toolchain")),
        )

    graph_paths = sorted((root / "10-execution-graphs").glob("*.json"))
    if not graph_paths:
        errors.append("no execution-graph JSON files found")
    for path in graph_paths:
        graph = load_object(path, errors)
        if graph is not None:
            validate_graph(
                graph, str(path.relative_to(root)), errors, complete, tool_ids
            )

    if complete and profile in {"creative", "hybrid"}:
        for relative in (
            "05-doctrine/doctrine-hypothesis.md",
            "06-grammar/grammar-pattern.md",
        ):
            path = root / relative
            content = path.read_text(encoding="utf-8") if path.is_file() else ""
            if not content.strip() or "<" in content:
                errors.append(f"incomplete creative-system document: {relative}")

    if not complete:
        warnings.append(
            "structural IR validation only; use --complete before promotion"
        )
    return {"valid": not errors, "errors": errors, "warnings": warnings}


def main() -> int:
    """Run IR validation and print JSON."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_path", type=Path)
    parser.add_argument("--complete", action="store_true")
    args = parser.parse_args()
    report = validate_system_ir(args.project_path, args.complete)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
