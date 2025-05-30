"""
Nmap security scanning plugin.
"""

import subprocess

metadata = {
    "name": "nmap_plugin",
    "description": "Performs nmap scan on the target."
}

def run(target):
    """
    Run nmap scan on the target.
    Args:
        target (str): Target IP or URL.
    Returns:
        dict: Scan results.
    """
    try:
        result = subprocess.run(['nmap', '-sV', target], capture_output=True, text=True, timeout=60)
        return {
            "plugin": "nmap_plugin",
            "target": target,
            "output": result.stdout,
            "returncode": result.returncode
        }
    except Exception as e:
        return {
            "plugin": "nmap_plugin",
            "target": target,
            "error": str(e)
        }
