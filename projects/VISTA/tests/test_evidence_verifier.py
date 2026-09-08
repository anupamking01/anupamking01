import importlib.util
from pathlib import Path
import unittest

MODULE = Path(__file__).parents[1] / "src" / "evidence_verifier.py"
spec = importlib.util.spec_from_file_location("evidence_verifier", MODULE)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class EvidenceVerifierTests(unittest.TestCase):
    def test_missing_reference_is_unsupported(self):
        claims = [m.Claim("x", ("missing",))]
        self.assertEqual(len(m.unsupported_claims(claims, [])), 1)

    def test_full_coverage(self):
        evidence = [m.EvidenceRegion("a", "value")]
        claims = [m.Claim("value", ("a",))]
        self.assertEqual(m.support_coverage(claims, evidence), 1.0)


if __name__ == "__main__":
    unittest.main()
