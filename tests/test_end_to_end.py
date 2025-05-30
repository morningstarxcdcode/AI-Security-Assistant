import unittest
from core.orchestrator import Orchestrator

class TestEndToEnd(unittest.TestCase):
    def setUp(self):
        self.orchestrator = Orchestrator()

    def test_full_scan_workflow(self):
        target = "http://example.com"
        results = self.orchestrator.run_scan(target)
        self.assertIsInstance(results, dict)
        self.assertIn(target, results)
        self.assertIn("example_plugin", results[target])
        # Additional assertions can be added based on expected scan results

if __name__ == "__main__":
    unittest.main()
