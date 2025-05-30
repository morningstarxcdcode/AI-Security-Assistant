import unittest
import sys
import os
from unittest.mock import MagicMock, patch
import threading
import time
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.monitor import Monitor

class TestMonitor(unittest.TestCase):
    def setUp(self):
        self.mock_orchestrator = MagicMock()
        self.monitor = Monitor(self.mock_orchestrator, interval=1)

    def test_monitor_loop_runs_once(self):
        # Override targets for testing
        self.monitor._stop_event.set()  # Stop immediately to avoid infinite loop
        self.monitor._monitor_loop()
        self.mock_orchestrator.run_scan.assert_not_called()  # No targets, so no scan

    def test_monitor_runs_scan(self):
        self.mock_orchestrator.run_scan.reset_mock()
        self.monitor.targets = ["http://example.com"]
        self.monitor.start()
        time.sleep(2)  # Let it run for 2 seconds
        self.monitor.stop()
        self.mock_orchestrator.run_scan.assert_called()

if __name__ == "__main__":
    unittest.main()
