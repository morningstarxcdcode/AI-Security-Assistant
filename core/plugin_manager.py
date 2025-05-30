"""
Plugin manager for loading and managing security scanning plugins with enhanced features.
"""

import importlib
import os
import sys

class PluginManager:
    def __init__(self, plugin_folder='plugins'):
        self.plugin_folder = plugin_folder
        self.plugins = {}

    def load_plugins(self):
        """
        Load all plugins from the plugin folder dynamically.
        Plugins must have a 'run' function and optional 'metadata' dict.
        """
        sys.path.insert(0, self.plugin_folder)
        for filename in os.listdir(self.plugin_folder):
            if filename.endswith('.py') and filename != '__init__.py':
                plugin_name = filename[:-3]
                try:
                    module = importlib.import_module(plugin_name)
                    if hasattr(module, 'run'):
                        metadata = getattr(module, 'metadata', {})
                        self.plugins[plugin_name] = {
                            'module': module,
                            'metadata': metadata
                        }
                except Exception as e:
                    print(f"Failed to load plugin {plugin_name}: {e}")
        sys.path.pop(0)

    def unload_plugin(self, plugin_name):
        """
        Unload a plugin by name.
        """
        if plugin_name in self.plugins:
            del self.plugins[plugin_name]

    def run_all(self, target):
        """
        Run all loaded plugins on the target.
        Args:
            target (str): Target URL or IP.
        Returns:
            dict: Aggregated results from all plugins.
        """
        results = {}
        for name, plugin_info in self.plugins.items():
            plugin = plugin_info['module']
            try:
                results[name] = plugin.run(target)
            except Exception as e:
                results[name] = {'error': str(e)}
        return results
