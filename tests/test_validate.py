"""Exercise distribution failures using isolated copies of the repository."""

import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest


REPO = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_package", REPO / "scripts" / "validate.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class PackageValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "package"
        shutil.copytree(REPO, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__", ".venv"))

    def test_distribution_is_valid(self):
        self.assertEqual(MODULE.validate(self.root), [])

    def test_missing_referenced_file_is_reported(self):
        (self.root / "skills/ui-art-director/references/visual-review.md").unlink()
        self.assertTrue(any("broken local link" in item for item in MODULE.validate(self.root)))

    def test_links_cannot_escape_distribution(self):
        with (self.root / "README.md").open("a", encoding="utf-8") as file:
            file.write("\n[Outside](../outside.md)\n")
        self.assertTrue(any("link leaves repository" in item for item in MODULE.validate(self.root)))

    def test_machine_local_links_are_reported(self):
        with (self.root / "README.md").open("a", encoding="utf-8") as file:
            file.write("\n[Local](C:/Users/example/private.md)\n")
        self.assertTrue(any("non-portable link" in item for item in MODULE.validate(self.root)))

    def test_copied_skill_retains_licence(self):
        (self.root / "skills/ui-art-director/LICENSE").unlink()
        self.assertTrue(any("bundled licence" in item for item in MODULE.validate(self.root)))

    def test_duplicate_evaluation_id_is_reported(self):
        path = self.root / "evals/cases.json"
        cases = json.loads(path.read_text(encoding="utf-8"))
        cases.append(cases[0])
        path.write_text(json.dumps(cases), encoding="utf-8")
        self.assertTrue(any("unique" in item for item in MODULE.validate(self.root)))


if __name__ == "__main__":
    unittest.main()
