#!/usr/bin/env python3
"""Initialize an auditable production-system compilation workspace.

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


LEGACY_DIRECTORIES = (
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

DIRECTORIES = (
    "00-intake",
    "01-evidence-plan",
    "02-corpus",
    "03-observations",
    "04-comparisons",
    "05-doctrine",
    "06-grammar",
    "07-decision-units",
    "08-toolchain",
    "09-evaluation-contract",
    "10-execution-graphs",
    "11-generated-system",
    "12-test-outputs",
    "13-evaluations",
    "14-failures",
)

TEMPLATE_TARGETS = {
    "capability-contract.yaml": "00-intake/capability-contract.yaml",
    "system-manifest.json": "00-intake/system-manifest.json",
    "evidence-plan.yaml": "01-evidence-plan/evidence-plan.yaml",
    "corpus-manifest.yaml": "02-corpus/corpus-manifest.yaml",
    "comparison-matrix.csv": "04-comparisons/comparison-matrix.csv",
    "transfer-test.yaml": "04-comparisons/transfer-test.yaml",
    "doctrine-hypothesis.md": "05-doctrine/doctrine-hypothesis.md",
    "grammar-pattern.md": "06-grammar/grammar-pattern.md",
    "decision-unit.json": "07-decision-units/decision-001.json",
    "tool-capability-registry.json": "08-toolchain/capability-registry.json",
    "evaluation-rubric.json": "09-evaluation-contract/evaluation-rubric.json",
    "system-evaluation-rubric.json": "09-evaluation-contract/system-evaluation-rubric.json",
    "execution-graph.json": "10-execution-graphs/execution-001.json",
    "skill-spec.yaml": "11-generated-system/skill-spec.yaml",
    "lifecycle-status.yaml": "11-generated-system/lifecycle-status.yaml",
    "evaluation-result.json": "13-evaluations/evaluation-result-template.json",
    "system-evaluation-result.json": "13-evaluations/system-evaluation-result-template.json",
    "failure-record.yaml": "14-failures/failure-record-template.yaml",
}


def replace_managed_values(path: Path, replacements: dict[str, str]) -> None:
    """Replace required scalar lines in a freshly copied managed template."""
    content = path.read_text(encoding="utf-8")
    for current, replacement in replacements.items():
        if current not in content:
            raise ValueError(f"managed template value not found in {path}: {current}")
        content = content.replace(current, replacement, 1)
    path.write_text(content, encoding="utf-8")


def validate_slug(value: str) -> str:
    """Validate and return a portable kebab-case project slug."""
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value):
        raise argparse.ArgumentTypeError(
            "project slug must use lowercase letters, digits, and single hyphens"
        )
    return value


def initialize_project(
    slug: str,
    output: Path,
    force: bool = False,
    profile: str = "procedural",
) -> Path:
    """Create a project workspace and return its root path.

    Args:
        slug: Kebab-case project identifier.
        output: Parent directory for the project.
        force: Allow an existing directory and overwrite only managed templates.
        profile: Procedural, creative, or hybrid compilation profile.

    Raises:
        FileExistsError: If the project exists and force is false.
        FileNotFoundError: If a required bundled template is missing.
    """
    if profile not in {"procedural", "creative", "hybrid"}:
        raise ValueError(f"unsupported system profile: {profile}")

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

    replace_managed_values(
        root / "00-intake/capability-contract.yaml",
        {
            'project_id: "replace-me"': f'project_id: "{slug}"',
            'system_profile: "procedural"': f'system_profile: "{profile}"',
            "  doctrine_required: false": (
                f"  doctrine_required: {str(profile in {'creative', 'hybrid'}).lower()}"
            ),
            "  grammar_required: false": (
                f"  grammar_required: {str(profile in {'creative', 'hybrid'}).lower()}"
            ),
            "  toolchain_required: false": (
                f"  toolchain_required: {str(profile == 'hybrid').lower()}"
            ),
        },
    )
    for relative in (
        "01-evidence-plan/evidence-plan.yaml",
        "02-corpus/corpus-manifest.yaml",
    ):
        replace_managed_values(
            root / relative,
            {'project_id: "replace-me"': f'project_id: "{slug}"'},
        )
    replace_managed_values(
        root / "11-generated-system/skill-spec.yaml",
        {'system_profile: "procedural"': f'system_profile: "{profile}"'},
    )
    replace_managed_values(
        root / "11-generated-system/lifecycle-status.yaml",
        {'skill: ""': f'skill: "{slug}"'},
    )

    manifest_path = root / "00-intake/system-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest.update(
        {
            "project_id": slug,
            "profile": profile,
            "requires_doctrine": profile in {"creative", "hybrid"},
            "requires_grammar": profile in {"creative", "hybrid"},
            "requires_toolchain": profile == "hybrid",
        }
    )
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    project_metadata = {
        "schema_version": "0.3",
        "project_id": slug,
        "profile": profile,
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
    parser.add_argument(
        "--profile",
        choices=("procedural", "creative", "hybrid"),
        default="procedural",
        help="production-system profile (default: procedural)",
    )
    return parser


def main() -> int:
    """Run the project initializer."""
    args = build_parser().parse_args()
    try:
        root = initialize_project(
            args.project_slug,
            args.output,
            args.force,
            args.profile,
        )
    except (FileExistsError, FileNotFoundError, OSError, ValueError) as exc:
        print(f"ERROR: {exc}")
        return 1
    print(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
