import importlib.util
from pathlib import Path
import unittest

MODULE = Path(__file__).parents[1] / "src" / "router.py"
spec = importlib.util.spec_from_file_location("router", MODULE)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class RouterTests(unittest.TestCase):
    def test_low_risk_task_uses_small_model(self):
        self.assertEqual(m.route(m.TaskSignal(0.1, 0.1, 0.1)), "small_model")

    def test_high_risk_task_escalates(self):
        self.assertEqual(m.route(m.TaskSignal(0.7, 0.7, 1.0)), "large_model")


if __name__ == "__main__":
    unittest.main()
