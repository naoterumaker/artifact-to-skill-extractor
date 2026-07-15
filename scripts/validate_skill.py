#!/usr/bin/env python3
"""Validate the deterministic structure of an Agent Skill directory.

This validator intentionally does not claim to judge semantic quality. It checks
frontmatter, naming, referenced local resources, placeholders, and Python syntax.
"""

from __future__ import annotations

import argparse
import json
import py_compile
import re
from pathlib import Path
from typing import Any


NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
RESOURCE_RE = re.compile(r"`((?:references|assets|scripts)/[^`\s]+)`")


def parse_frontmatter(content: str) -> tuple[dict[str, str], str]:
    """Parse name and description from simple YAML frontmatter."""
    if not content.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter")
    parts = content.split("---\n", 2)
    if len(parts) != 3:
        raise ValueError("SKILL.md frontmatter is not closed")
    block, body = parts[1], parts[2]
    metadata: dict[str, str] = {}
    current_key: str | None = None
    for line in block.splitlines():
        if not line.strip():
            continue
        if not line.startswith((" ", "\t")) and ":" in line:
            key, value = line.split(":", 1)
            current_key = key.strip()
            metadata[current_key] = value.strip().strip('"').strip("'")
        elif current_key and line.startswith((" ", "\t")):
            metadata[current_key] = f"{metadata[current_key]} {line.strip()}".strip()
    return metadata, body


def validate_skill(root: Path, strict: bool = False) -> dict[str, Any]:
    """Return a machine-readable structural validation report."""
    root = root.expanduser().resolve()
    errors: list[str] = []
    warnings: list[str] = []
    skill_path = root / "SKILL.md"

    if not skill_path.is_file():
        return {"valid": False, "errors": ["missing SKILL.md"], "warnings": []}

    content = skill_path.read_text(encoding="utf-8")
    try:
        metadata, body = parse_frontmatter(content)
    except ValueError as exc:
        return {"valid": False, "errors": [str(exc)], "warnings": []}

    name = metadata.get("name", "")
    description = metadata.get("description", "")
    if not NAME_RE.fullmatch(name):
        errors.append("frontmatter name must be non-empty kebab-case")
    if name and root.name != name:
        warnings.append(
            f"directory name '{root.name}' differs from skill name '{name}'"
        )
    if not description or description in {">", ">-", "|"}:
        errors.append("frontmatter description must be informative")
    elif len(description) > 1024:
        errors.append("frontmatter description exceeds 1024 characters")
    elif not description.lower().startswith("use when"):
        warnings.append("description should start with 'Use when' for trigger clarity")

    if "TODO" in content or "[TODO" in content:
        errors.append("skill contains TODO placeholders")
    if len(body.strip()) < 100:
        errors.append("SKILL.md body is too short to be actionable")

    for resource in sorted(set(RESOURCE_RE.findall(content))):
        clean = resource.rstrip(".,;:")
        if not (root / clean).exists():
            errors.append(f"referenced local resource does not exist: {clean}")

    for script in (
        sorted((root / "scripts").glob("*.py")) if (root / "scripts").is_dir() else []
    ):
        try:
            py_compile.compile(str(script), doraise=True)
        except py_compile.PyCompileError as exc:
            errors.append(
                f"Python syntax error in {script.relative_to(root)}: {exc.msg}"
            )

    lower_body = body.lower()
    for section, signal in {
        "workflow": "workflow",
        "boundaries or quality rules": "boundary",
        "evaluation or tests": "evaluat",
    }.items():
        if signal not in lower_body:
            warnings.append(f"no clear {section} signal found")

    if strict and warnings:
        errors.extend(f"strict: {warning}" for warning in warnings)

    return {"valid": not errors, "errors": errors, "warnings": warnings}


def main() -> int:
    """Run skill validation and print JSON."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill_path", type=Path)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    report = validate_skill(args.skill_path, args.strict)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
