import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ai_modules.code_generator import CodeGenerator

class TestCodeGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = CodeGenerator()

    def test_generate_code_returns_string(self):
        code = self.generator.generate_code("Test prompt")
        print(f"[DEBUG] generate_code output: {code}")
        self.assertIsInstance(code, str)
        self.assertIn("Generated code placeholder", code)

if __name__ == "__main__":
    unittest.main()
