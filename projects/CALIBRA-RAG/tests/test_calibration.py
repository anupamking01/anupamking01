import importlib.util
from pathlib import Path
import unittest

MODULE = Path(__file__).parents[1] / "src" / "calibration.py"
spec = importlib.util.spec_from_file_location("calibration", MODULE)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class CalibrationTests(unittest.TestCase):
    def test_contradiction_reduces_confidence(self):
        clean = [m.Evidence(0.9, True)]
        conflict = [m.Evidence(0.9, True, True)]
        self.assertGreater(m.confidence(clean), m.confidence(conflict))

    def test_empty_evidence_abstains(self):
        self.assertEqual(m.decision([]), "abstain")


if __name__ == "__main__":
    unittest.main()
