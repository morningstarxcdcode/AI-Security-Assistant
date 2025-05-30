"""
Central orchestrator module managing AI code generation, execution, and feedback loop with multi-agent parallel scanning.
"""

import threading
from core.plugin_manager import PluginManager

class Orchestrator:
    def __init__(self):
        self.plugin_manager = PluginManager()
        self.plugin_manager.load_plugins()

    def _run_scan_for_target(self, target, results):
        """
        Run scan for a single target and store results.
        """
        scan_result = self.plugin_manager.run_all(target)
        results[target] = scan_result

    def run_scan(self, targets):
        """
        Run security scans on multiple targets in parallel.
        Args:
            targets (list or str): List of target URLs or IPs, or a single target string.
        Returns:
            dict: Aggregated scan results keyed by target.
        """
        if isinstance(targets, str):
            targets = [targets]

        threads = []
        results = {}

        for target in targets:
            t = threading.Thread(target=self._run_scan_for_target, args=(target, results))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        return results
