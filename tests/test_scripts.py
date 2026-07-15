from __future__ import annotations

import json
import struct
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from init_project import initialize_project  # noqa: E402
from estimate_extraction import estimate  # noqa: E402
from run_test_prompts import normalize_fixture, score_observations  # noqa: E402
from score_evaluation import score_evaluation  # noqa: E402
from validate_project import validate_project  # noqa: E402
from validate_skill import validate_skill  # noqa: E402


class ProjectScriptTests(unittest.TestCase):
    def test_initialized_project_passes_structural_validation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = initialize_project(
                "example-skill-project", Path(temporary_directory)
            )
            report = validate_project(root)

        self.assertTrue(report["valid"], report)
        self.assertEqual(report["errors"], [])

    def test_invalid_rubric_weight_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = initialize_project("bad-rubric", Path(temporary_directory))
            rubric_path = root / "05-rubric/evaluation-rubric.json"
            rubric = json.loads(rubric_path.read_text(encoding="utf-8"))
            rubric["dimensions"][0]["weight"] = 19
            rubric_path.write_text(json.dumps(rubric), encoding="utf-8")
            report = validate_project(root)

        self.assertFalse(report["valid"])
        self.assertIn("rubric dimension weights must total 100", report["errors"][0])

    def test_extraction_estimator_reports_text_and_media_separately(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "notes.md").write_text("evidence " * 100, encoding="utf-8")
            (root / "reference.png").write_bytes(b"\x89PNG\r\n\x1a\n" + b"0" * 100)
            report = estimate([root])

        self.assertEqual(report["categories"], {"image": 1, "text": 1})
        self.assertGreater(report["estimated_text_tokens"]["high"], 0)
        self.assertEqual(report["media_files_requiring_native_estimation"], 1)
        self.assertEqual(report["recommended_depth"], "minimal")


class SkillValidatorTests(unittest.TestCase):
    def test_repository_skill_passes_strict_validation(self) -> None:
        report = validate_skill(ROOT, strict=True)
        self.assertTrue(report["valid"], report)
        self.assertEqual(report["warnings"], [])

    def test_generated_example_skills_pass_strict_validation(self) -> None:
        skill_paths = (
            ROOT / "assets/examples/x-article/source-grounded-x-article",
            ROOT / "assets/examples/image/destination-poster-recomposer",
        )
        for skill_path in skill_paths:
            with self.subTest(skill=skill_path.name):
                report = validate_skill(skill_path, strict=True)
                self.assertTrue(report["valid"], report)


class EvaluationScoringTests(unittest.TestCase):
    def setUp(self) -> None:
        self.rubric = json.loads(
            (ROOT / "assets/templates/evaluation-rubric.json").read_text(
                encoding="utf-8"
            )
        )

    def result(self, score: int, anti_clone: str = "pass") -> dict:
        return {
            "hard_gates": {
                "required-output": "pass",
                "rights-and-safety": "pass",
                "anti-clone": anti_clone,
            },
            "dimension_scores": {
                dimension["id"]: score for dimension in self.rubric["dimensions"]
            },
        }

    def test_passing_result(self) -> None:
        report = score_evaluation(self.rubric, self.result(84))
        self.assertEqual(report["decision"], "pass")
        self.assertEqual(report["total_score"], 84)

    def test_failed_gate_forces_revision(self) -> None:
        report = score_evaluation(self.rubric, self.result(92, anti_clone="fail"))
        self.assertEqual(report["decision"], "revise")
        self.assertEqual(report["failed_hard_gates"], ["anti-clone"])

    def test_low_critical_dimension_forces_revision(self) -> None:
        result = self.result(90)
        result["dimension_scores"]["evidence-grounding"] = 55
        report = score_evaluation(self.rubric, result)
        self.assertEqual(report["decision"], "revise")
        self.assertEqual(report["critical_failures"], ["evidence-grounding"])

    def test_worked_example_rounds_revise_then_pass(self) -> None:
        for example, expected_final in (
            ("x-article", 87.9),
            ("image", 88.2),
            ("self-extraction", 88.2),
        ):
            root = ROOT / "assets/examples" / example
            rubric = json.loads(
                (root / "evaluation-rubric.json").read_text(encoding="utf-8")
            )
            round_one = json.loads(
                (root / "evaluation-round-1.json").read_text(encoding="utf-8")
            )
            round_two = json.loads(
                (root / "evaluation-round-2.json").read_text(encoding="utf-8")
            )
            with self.subTest(example=example):
                first_report = score_evaluation(rubric, round_one)
                final_report = score_evaluation(rubric, round_two)
                self.assertEqual(first_report["decision"], "revise")
                self.assertEqual(final_report["decision"], "pass")
                self.assertEqual(final_report["total_score"], expected_final)


class WorkedExampleFixtureTests(unittest.TestCase):
    def test_lifecycle_status_matches_current_evidence(self) -> None:
        status = (ROOT / "references/lifecycle-status.yaml").read_text(encoding="utf-8")
        self.assertIn("version: 0.2.0", status)
        self.assertIn("status: experimental", status)
        self.assertIn("x-article-forward-test", status)
        self.assertIn("image-forward-test", status)

    def test_prompt_fixture_counts(self) -> None:
        paths = (
            ROOT
            / "assets/examples/x-article/source-grounded-x-article/test-prompts.json",
            ROOT
            / "assets/examples/image/destination-poster-recomposer/test-prompts.json",
        )
        for path in paths:
            prompts = json.loads(path.read_text(encoding="utf-8"))
            with self.subTest(fixture=path.parent.name):
                self.assertGreaterEqual(len(prompts["should_trigger"]), 5)
                self.assertGreaterEqual(len(prompts["should_not_trigger"]), 5)
                self.assertGreaterEqual(len(prompts["boundary"]), 3)
                self.assertGreaterEqual(len(prompts["functional"]), 3)

    def test_prompt_runner_normalizes_and_scores_observations(self) -> None:
        fixture = json.loads(
            (ROOT / "assets/test-prompts-template.json").read_text(encoding="utf-8")
        )
        cases = normalize_fixture(fixture)
        observations = {
            "results": [
                {"case_id": case["case_id"], "status": "pass", "evidence": "reviewed"}
                for case in cases
            ]
        }
        report = score_observations(cases, observations, minimum_pass_rate=1.0)

        self.assertEqual(len(cases), 16)
        self.assertEqual(report["decision"], "pass")
        self.assertEqual(report["pass_rate"], 1.0)

        observations["results"][0]["status"] = "fail"
        threshold_report = score_observations(
            cases, observations, minimum_pass_rate=0.9
        )
        self.assertEqual(threshold_report["decision"], "pass")
        self.assertEqual(threshold_report["failed"], 1)

    def test_image_renders_have_expected_dimensions(self) -> None:
        expected = {
            "source-vintage-travel-poster-paris.png": (512, 702),
            "poster-round-1.png": (800, 1000),
            "poster-round-2.png": (800, 1000),
            "poster-round-2-thumbnail.png": (192, 240),
        }
        image_root = ROOT / "assets/examples/image"
        for filename, dimensions in expected.items():
            path = image_root / filename
            data = path.read_bytes()
            with self.subTest(image=filename):
                self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n")
                self.assertEqual(struct.unpack(">II", data[16:24]), dimensions)
                self.assertGreater(len(data), 5_000)


if __name__ == "__main__":
    unittest.main()
