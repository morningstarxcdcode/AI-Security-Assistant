# AI Security Assistant

Welcome to the **AI Security Assistant**, a next-generation, AI-powered platform for automated vulnerability scanning, bug bounty hunting, and collaborative security research.

---

## 🚀 Unique Vision

AI Security Assistant is not just another scanner—it's a modular, explainable, and collaborative security orchestration platform. It combines conversational multi-agent workflows, explainable AI, and a live interactive dashboard to empower security professionals and teams.

---

## ✨ Advanced & Unique Features

- **Conversational Multi-Agent Orchestration:** Design custom agent workflows via the web UI, chaining plugins, AI analysis, and reporting in a drag-and-drop or scriptable interface.
- **Live Interactive Recon Dashboard:** Real-time visualization of scan progress, discovered assets, and vulnerabilities, with the ability to trigger deeper scans or AI analysis on-the-fly.
- **Explainable AI:** Every AI-driven finding includes a natural language explanation, code PoC, and a trace of the reasoning steps.
- **Auto-Remediation Suggestions:** For each finding, the AI suggests not just PoC but also code/config fixes, and can generate PR-ready patches for common frameworks.
- **Plugin Marketplace:** Browse, install, and update plugins from a curated marketplace directly in the web UI.
- **Security Knowledge Graph:** Visualize a knowledge graph of discovered assets, vulnerabilities, and relationships, powered by AI and NVD data.
- **Team Collaboration:** Multi-user support, with role-based access, scan scheduling, and shared dashboards.
- **Continuous Learning:** The system adapts and improves findings based on user feedback, integrating a feedback loop into the UI and backend.
- **Automated Reporting:** Generates detailed, visually rich PDF reports with vulnerability charts.
- **Integration with Popular Tools:** Leverages well-known security tools and the NVD vulnerability database.
- **Notification System:** Supports Telegram and Discord alerts.
- **Monitoring Mode:** Continuous, scheduled scanning of target URLs.

---

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd ai_security_assistant
   ```

2. **Set up the environment and install dependencies:**
   ```bash
   ./setup_venv_and_run_tests.sh
   ```

3. **Configure your API keys and settings in `config.yaml`.**

---

## ⚡ Usage

- **Web Interface:**  
  Start the web UI:
  ```bash
  python3 web_ui/app.py
  ```
  Then open your browser to [http://localhost:5001](http://localhost:5001)

- **Command Line:**  
  Run a scan:
  ```bash
  python3 main.py [TARGET_URLS] [--mode {regular,monitor}]
  ```

---

## 🧑‍💻 Development

- Core modules: `core/`
- AI modules: `ai_modules/`
- Plugins: `plugins/`
- Tests: `tests/`

Run tests anytime with:
```bash
pytest
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Please check the guidelines before submitting.

---

Thank you for exploring the AI Security Assistant — where explainable AI, automation, and collaboration meet security innovation.
