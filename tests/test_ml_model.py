import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.ml_model import MLModel

class TestMLModel(unittest.TestCase):
    def setUp(self):
        self.model = MLModel()

    def test_predict_returns_none(self):
        result = self.model.predict("dummy_input")
        self.assertIsNone(result)

    def test_fine_tune_runs_without_error(self):
        try:
            self.model.fine_tune([])
        except Exception as e:
            self.fail(f"fine_tune raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()
