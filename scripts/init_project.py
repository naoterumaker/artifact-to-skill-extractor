#!/usr/bin/env python3
"""Initialize an auditable artifact-to-skill project workspace.

The script creates the stable stage directories and copies only reusable
templates. It never deletes an existing project or user artifacts.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path


DIRECTORIES = (
    "00-intake",
    "01-evidence-plan",
    "02-corpus",
    "03-observations",
    "04-patterns",
    "05-rubric",
    "06-generated-skill",
    "07-test-outputs",
    "08-evaluations",
    "09-failures",
)

TEMPLATE_TARGETS = {
    "capability-contract.yaml": "00-intake/capability-contract.yaml",
    "evidence-plan.yaml": "01-evidence-plan/evidence-plan.yaml",
    "corpus-manifest.yaml": "02-corpus/corpus-manifest.yaml",
    "evaluation-rubric.json": "05-rubric/evaluation-rubric.json",
    "skill-spec.yaml": "06-generated-skill/skill-spec.yaml",
    "lifecycle-status.yaml": "06-generated-skill/lifecycle-status.yaml",
    "transfer-test.yaml": "04-patterns/transfer-test.yaml",
    "failure-record.yaml": "09-failures/failure-record-template.yaml",
}


def validate_slug(value: str) -> str:
    """Validate and return a portable kebab-case project slug."""
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value):
        raise argparse.ArgumentTypeError(
            "project slug must use lowercase letters, digits, and single hyphens"
        )
    return value


def initialize_project(slug: str, output: Path, force: bool = False) -> Path:
    """Create a project workspace and return its root path.

    Args:
        slug: Kebab-case project identifier.
        output: Parent directory for the project.
        force: Allow an existing directory and overwrite only managed templates.

    Raises:
        FileExistsError: If the project exists and force is false.
        FileNotFoundError: If a required bundled template is missing.
    """
    root = output.expanduser().resolve() / slug
    if root.exists() and any(root.iterdir()) and not force:
        raise FileExistsError(f"project already exists and is not empty: {root}")

    root.mkdir(parents=True, exist_ok=True)
    for directory in DIRECTORIES:
        (root / directory).mkdir(exist_ok=True)

    skill_root = Path(__file__).resolve().parents[1]
    templates = skill_root / "assets" / "templates"
    for source_name, target_name in TEMPLATE_TARGETS.items():
        source = templates / source_name
        if not source.is_file():
            raise FileNotFoundError(f"missing bundled template: {source}")
        target = root / target_name
        if force or not target.exists():
            shutil.copy2(source, target)

    project_metadata = {
        "schema_version": "0.2",
        "project_id": slug,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "stages": list(DIRECTORIES),
    }
    metadata_path = root / "project.json"
    if force or not metadata_path.exists():
        metadata_path.write_text(
            json.dumps(project_metadata, indent=2) + "\n", encoding="utf-8"
        )
    return root


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_slug", type=validate_slug)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path.cwd(),
        help="parent output directory (default: current directory)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="reuse an existing project without deleting unrecognized files",
    )
    return parser


def main() -> int:
    """Run the project initializer."""
    args = build_parser().parse_args()
    try:
        root = initialize_project(args.project_slug, args.output, args.force)
    except (FileExistsError, FileNotFoundError, OSError) as exc:
        print(f"ERROR: {exc}")
        return 1
    print(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
