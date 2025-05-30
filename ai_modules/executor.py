"""
Execution environment for ephemeral AI-generated scripts.
"""

import subprocess
import tempfile
import os

class Executor:
    def __init__(self):
        pass

    def execute_code(self, code, timeout=30):
        """
        Execute the given code safely and capture output.
        Args:
            code (str): Code to execute.
            timeout (int): Maximum execution time in seconds.
        Returns:
            dict: Execution result including stdout, stderr, and return code.
        """
        with tempfile.NamedTemporaryFile(delete=False, suffix='.py') as temp_file:
            temp_file.write(code.encode('utf-8'))
            temp_file_path = temp_file.name

        try:
            result = subprocess.run(
                ['python3', temp_file_path],
                capture_output=True,
                text=True,
                timeout=timeout
            )
            return {
                'stdout': result.stdout,
                'stderr': result.stderr,
                'returncode': result.returncode
            }
        except subprocess.TimeoutExpired:
            return {
                'stdout': '',
                'stderr': 'Execution timed out',
                'returncode': -1
            }
        finally:
            os.remove(temp_file_path)
