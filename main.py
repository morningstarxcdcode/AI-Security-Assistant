"""
Main entry point for the AI-assisted security assistant.
"""

from core.orchestrator import Orchestrator

def main():
    orchestrator = Orchestrator()
    target = "https://example.com"
    print(f"Starting scan on target: {target}")
    results = orchestrator.run_scan(target)
    print("Scan results:")
    print(results)

if __name__ == "__main__":
    main()
