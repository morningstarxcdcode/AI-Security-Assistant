"""
Monitoring module for continuous scanning of target URLs.
"""

import threading
import time

class Monitor:
    def __init__(self, orchestrator, interval=3600, targets=None):
        """
        Args:
            orchestrator (Orchestrator): The orchestrator instance to run scans.
            interval (int): Time interval between scans in seconds.
            targets (list): List of target URLs to scan.
        """
        self.orchestrator = orchestrator
        self.interval = interval
        self.targets = targets if targets is not None else []
        self._stop_event = threading.Event()
        self._thread = threading.Thread(target=self._monitor_loop)

    def start(self):
        """Start the monitoring thread."""
        self._stop_event.clear()
        self._thread.start()

    def stop(self):
        """Stop the monitoring thread."""
        self._stop_event.set()
        self._thread.join()

    def _monitor_loop(self):
        while not self._stop_event.is_set():
            for target in self.targets:
                self.orchestrator.run_scan(target)
            time.sleep(self.interval)
