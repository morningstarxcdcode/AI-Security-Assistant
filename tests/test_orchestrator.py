import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.orchestrator import Orchestrator

class TestOrchestrator(unittest.TestCase):
    def setUp(self):
        self.orchestrator = Orchestrator()

    def test_run_scan_empty(self):
        result = self.orchestrator.run_scan("http://example.com")
        self.assertIsInstance(result, dict)

if __name__ == "__main__":
    unittest.main()
