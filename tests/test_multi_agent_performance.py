import unittest
import time
from concurrent.futures import ThreadPoolExecutor
from core.plugin_manager import PluginManager

class TestMultiAgentPerformance(unittest.TestCase):
    def setUp(self):
        self.plugin_manager = PluginManager()
        self.plugin_manager.load_plugins()
        self.targets = [f"http://example{i}.com" for i in range(10)]

    def test_parallel_scanning_performance(self):
        start_time = time.time()
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(self.plugin_manager.run_all, target) for target in self.targets]
            results = [f.result() for f in futures]
        duration = time.time() - start_time
        print(f"Parallel scanning of {len(self.targets)} targets took {duration:.2f} seconds")
        self.assertTrue(duration < 10, "Parallel scanning took too long")

if __name__ == "__main__":
    unittest.main()
