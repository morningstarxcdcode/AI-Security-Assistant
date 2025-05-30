"""
Web interface backend for AI Security Assistant using Flask.
"""

from flask import Flask, request, jsonify, render_template
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ai_modules.code_generator import CodeGenerator

app = Flask(__name__)
codegen = CodeGenerator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    # Compose a structured prompt for the code generator
    prompt = {
        "instructions": data.get("instructions", ""),
        "context": data.get("context", ""),
        "goals": data.get("goals", ""),
        "constraints": data.get("constraints", "")
    }
    # For now, pass the prompt as a string for compatibility
    output = codegen.generate_code(str(prompt))
    return jsonify({"output": output})

@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    targets = data.get('targets', [])
    # Placeholder: invoke orchestrator to run scans
    # For now, return dummy response
    return jsonify({"status": "scanning started", "targets": targets})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
