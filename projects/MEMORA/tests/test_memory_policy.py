import importlib.util
from pathlib import Path
import unittest

MODULE = Path(__file__).parents[1] / "src" / "memory_policy.py"
spec = importlib.util.spec_from_file_location("memory_policy", MODULE)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class MemoryPolicyTests(unittest.TestCase):
    def test_relevance_prefers_overlap(self):
        self.assertGreater(m.relevance("python experiment", "python experiment seed"),
                           m.relevance("python experiment", "database migration"))

    def test_retrieve_respects_k(self):
        items = [m.MemoryItem("python", 1), m.MemoryItem("sql", 1)]
        self.assertEqual(len(m.retrieve("python", items, 1)), 1)


if __name__ == "__main__":
    unittest.main()
