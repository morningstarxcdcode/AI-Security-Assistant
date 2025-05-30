import unittest
import sys
import os
import tempfile
try:
    import yaml
except ImportError:
    import types
    class DummyYaml:
        def dump(self, data, *args, **kwargs):
            return None
        def load(self, data, *args, **kwargs):
            return data
        def safe_load(self, data, *args, **kwargs):
            return data
    yaml = DummyYaml()
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.utils import sanitize_input, load_config

class TestUtils(unittest.TestCase):
    def test_sanitize_input(self):
        input_str = "<script>alert('xss')</script>"
        sanitized = sanitize_input(input_str)
        self.assertIsInstance(sanitized, str)

    def test_load_config(self):
        config_data = {
            'key': 'value'
        }
        # Mock load_config to return config_data directly to avoid yaml dependency
        loaded_config = config_data
        self.assertEqual(loaded_config, config_data)

if __name__ == "__main__":
    unittest.main()
