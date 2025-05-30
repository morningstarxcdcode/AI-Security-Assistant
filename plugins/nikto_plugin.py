"""
Nikto security scanning plugin.
"""

import subprocess

metadata = {
    "name": "nikto_plugin",
    "description": "Performs nikto scan on the target."
}

def run(target):
    """
    Run nikto scan on the target.
    Args:
        target (str): Target URL.
    Returns:
        dict: Scan results.
    """
    try:
        result = subprocess.run(['nikto', '-h', target], capture_output=True, text=True, timeout=120)
        return {
            "plugin": "nikto_plugin",
            "target": target,
            "output": result.stdout,
            "returncode": result.returncode
        }
    except Exception as e:
        return {
            "plugin": "nikto_plugin",
            "target": target,
            "error": str(e)
        }
