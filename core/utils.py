"""
Utility functions for the AI Security Assistant project.
"""

def sanitize_input(data):
    """
    Sanitize input data to prevent injection or unsafe operations.
    Args:
        data (str): Input string data.
    Returns:
        str: Sanitized string.
    """
    # Placeholder for sanitization logic
    return data

try:
    import yaml
except ImportError:
    import types
    class DummyYaml:
        def dump(self, *args, **kwargs):
            return None
        def load(self, *args, **kwargs):
            return None
        def safe_load(self, *args, **kwargs):
            return None
    yaml = DummyYaml()

def load_config(config_path):
    """
    Load configuration from a YAML file.
    Args:
        config_path (str): Path to the config file.
    Returns:
        dict: Configuration dictionary.
    """
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)
