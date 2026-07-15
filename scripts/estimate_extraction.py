#!/usr/bin/env python3
"""Estimate artifact volume and recommend an extraction depth.

The estimate is intentionally conservative. Text token ranges are planning
proxies, while binary media is reported as separate workload rather than
converted into misleading token precision.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


TEXT_EXTENSIONS = {
    ".c",
    ".cc",
    ".cpp",
    ".css",
    ".csv",
    ".go",
    ".h",
    ".html",
    ".java",
    ".js",
    ".json",
    ".jsx",
    ".log",
    ".md",
    ".php",
    ".py",
    ".rb",
    ".rs",
    ".sql",
    ".svg",
    ".toml",
    ".ts",
    ".tsx",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}
IMAGE_EXTENSIONS = {".avif", ".gif", ".heic", ".jpeg", ".jpg", ".png", ".webp"}
VIDEO_EXTENSIONS = {".avi", ".m4v", ".mkv", ".mov", ".mp4", ".webm"}
AUDIO_EXTENSIONS = {".aac", ".flac", ".m4a", ".mp3", ".ogg", ".wav"}
DOCUMENT_EXTENSIONS = {
    ".doc",
    ".docx",
    ".epub",
    ".pdf",
    ".ppt",
    ".pptx",
    ".xls",
    ".xlsx",
}
SKIP_DIRECTORIES = {".git", ".hg", ".svn", "__pycache__", "node_modules"}


def classify(path: Path) -> str:
    """Classify a file into a planning category."""
    extension = path.suffix.lower()
    if extension in TEXT_EXTENSIONS or not extension:
        return "text"
    if extension in IMAGE_EXTENSIONS:
        return "image"
    if extension in VIDEO_EXTENSIONS:
        return "video"
    if extension in AUDIO_EXTENSIONS:
        return "audio"
    if extension in DOCUMENT_EXTENSIONS:
        return "document"
    return "binary-other"


def iter_files(paths: Iterable[Path]) -> Iterable[Path]:
    """Yield unique files while skipping dependency and VCS directories."""
    seen: set[Path] = set()
    for supplied in paths:
        path = supplied.expanduser().resolve()
        candidates = (
            (path,) if path.is_file() else path.rglob("*") if path.is_dir() else ()
        )
        for candidate in candidates:
            if not candidate.is_file():
                continue
            if any(part in SKIP_DIRECTORIES for part in candidate.parts):
                continue
            if candidate not in seen:
                seen.add(candidate)
                yield candidate


def recommend_depth(
    files_total: int,
    text_tokens_high: int,
    media_total: int,
    binary_bytes: int,
) -> tuple[str, list[str]]:
    """Return a depth recommendation and its deterministic reasons."""
    reasons: list[str] = []
    if files_total <= 10 and text_tokens_high <= 20_000 and media_total <= 3:
        depth = "minimal"
        reasons.append("Corpus fits an inventory plus focused full read.")
    elif (
        files_total <= 100
        and text_tokens_high <= 200_000
        and media_total <= 20
        and binary_bytes <= 500_000_000
    ):
        depth = "standard"
        reasons.append("Corpus supports representative reading and one forward test.")
    else:
        depth = "deep"
        reasons.append(
            "Corpus size warrants staged sampling and explicit coverage tracking."
        )
    if media_total:
        reasons.append(
            "Binary media requires modality-specific duration, frame, OCR, or contact-sheet estimates."
        )
    return depth, reasons


def estimate(paths: Iterable[Path], include_files: bool = False) -> dict[str, Any]:
    """Calculate a machine-readable extraction estimate."""
    files = list(iter_files(paths))
    categories: Counter[str] = Counter()
    bytes_by_category: Counter[str] = Counter()
    text_characters = 0
    file_rows: list[dict[str, Any]] = []
    warnings: list[str] = []

    for path in files:
        category = classify(path)
        size = path.stat().st_size
        categories[category] += 1
        bytes_by_category[category] += size
        characters: int | None = None
        if category == "text":
            try:
                characters = len(path.read_text(encoding="utf-8", errors="replace"))
                text_characters += characters
            except OSError as exc:
                warnings.append(f"could not read {path}: {exc}")
        if include_files:
            file_rows.append(
                {
                    "path": str(path),
                    "category": category,
                    "bytes": size,
                    "characters": characters,
                }
            )

    text_tokens_low = math.ceil(text_characters / 4) if text_characters else 0
    text_tokens_high = math.ceil(text_characters / 1.5) if text_characters else 0
    media_categories = {"image", "video", "audio", "document"}
    media_total = sum(categories[category] for category in media_categories)
    binary_bytes = sum(
        size for category, size in bytes_by_category.items() if category != "text"
    )
    depth, reasons = recommend_depth(
        len(files), text_tokens_high, media_total, binary_bytes
    )

    report: dict[str, Any] = {
        "schema_version": "0.2",
        "files_total": len(files),
        "bytes_total": sum(bytes_by_category.values()),
        "categories": dict(sorted(categories.items())),
        "bytes_by_category": dict(sorted(bytes_by_category.items())),
        "text_characters": text_characters,
        "estimated_text_tokens": {
            "low": text_tokens_low,
            "high": text_tokens_high,
            "method": "characters/4 to characters/1.5; planning range only",
        },
        "media_files_requiring_native_estimation": media_total,
        "recommended_depth": depth,
        "reasons": reasons,
        "warnings": warnings,
    }
    if include_files:
        report["files"] = file_rows
    return report


def main() -> int:
    """Run the estimator and print or write JSON."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", type=Path, nargs="+")
    parser.add_argument("--include-files", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    missing = [str(path) for path in args.paths if not path.expanduser().exists()]
    if missing:
        print(f"ERROR: missing input path(s): {', '.join(missing)}")
        return 1

    report = estimate(args.paths, args.include_files)
    serialized = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(serialized, encoding="utf-8")
    else:
        print(serialized, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
