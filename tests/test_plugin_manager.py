import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.plugin_manager import PluginManager

class TestPluginManager(unittest.TestCase):
    def setUp(self):
        self.manager = PluginManager()

    def test_load_plugins(self):
        self.manager.load_plugins()
        self.assertIn("example_plugin", self.manager.plugins)

    def test_run_all(self):
        self.manager.load_plugins()
        results = self.manager.run_all("http://example.com")
        self.assertIn("example_plugin", results)
        self.assertIsInstance(results["example_plugin"], dict)

if __name__ == "__main__":
    unittest.main()
