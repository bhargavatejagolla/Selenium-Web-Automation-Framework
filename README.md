# 🚀 NextGen Enterprise Web Automation Framework

[![CI - Selenium Automation Tests](https://github.com/bhargavatejagolla/Selenium-Web-Automation-Framework/actions/workflows/ci.yml/badge.svg)](https://github.com/bhargavatejagolla/Selenium-Web-Automation-Framework/actions)
[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![Next.js](https://img.shields.io/badge/Next.js-14-black)](https://nextjs.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-green)](https://www.selenium.dev/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue)](https://www.docker.com/)

An industry-grade, production-ready E2E Test Automation Framework built from scratch. This project demonstrates a complete QA engineering lifecycle, featuring a custom System Under Test (SUT) built in Next.js, orchestrated alongside a highly scalable Python/Selenium automation suite using Docker Compose.

---

## 🌟 Key Features

* **Custom Next.js SUT**: A fully functional authentication system (Register/Login/Dashboard) with SQLite & Prisma.
* **Page Object Model (POM)**: Clean, maintainable, and highly scalable architecture.
* **Dynamic Data-Driven Testing**: Zero hardcoded mock data. Uses the `Faker` library to generate real-world personas and injects them directly into the database for testing.
* **Cross-Browser Compatibility**: Run tests seamlessly across Chrome, Firefox, and Edge with a single CLI flag.
* **Advanced Diagnostics**:
  * Rich Terminal Dashboards (Color-coded summaries and pass-rate bars).
  * Auto-retries for flaky tests.
  * Embedded screenshots in HTML reports on failure.
  * Step-by-step masked logging.
* **100% Dockerized**: Multi-container orchestration linking the SUT and automation framework perfectly.
* **CI/CD Pipeline**: GitHub Actions workflow that executes the Dockerized test suite on every push.

---

## 📂 Project Architecture

```text
Selenium-Web-Automation-Framework/
│
├── app/                          # 🟢 Next.js SUT (System Under Test)
│   ├── Dockerfile                # Next.js Container
│   ├── src/                      # App source code
│   └── prisma/                   # Database schema
│
├── automation/                   # 🔵 Python Automation Framework
│   ├── pages/                    # Page Object Model classes
│   ├── tests/                    # Pytest test suites (Login, Register, E2E)
│   └── utils/                    # Data generators, screenshot utilities, driver factory
│
├── reports/                      # 📈 HTML Pytest Reports
├── screenshots/                  # 🖼️ Failure Screenshots
├── logs/                         # 📝 Execution Logs
│
├── .github/workflows/            # 🔄 CI/CD Pipelines
├── docker-compose.yml            # 🐳 Container Orchestration
├── Dockerfile                    # 🐍 Python Automation Container
└── pytest.ini                    # ⚙️ Pytest Configuration
```

---

## 🚀 Getting Started

You can run this project in two ways: using **Docker** (Recommended) or **Locally**.

### Method 1: The Docker Way (Recommended)
You don't need Node.js or Python installed. Just Docker!

1. Clone the repository:
   ```bash
   git clone https://github.com/bhargavatejagolla/Selenium-Web-Automation-Framework.git
   cd Selenium-Web-Automation-Framework
   ```
2. Spin up the entire ecosystem:
   ```bash
   docker-compose up --build
   ```
   *Watch as Docker builds the app, waits for health checks to pass, and executes the headless Selenium tests perfectly. Reports will be mapped back to your local `reports/` folder!*

### Method 2: Local Execution

**1. Start the Next.js Application:**
```bash
cd app
npm install
npx prisma generate
npm run dev
```

**2. Run the Automation Suite (in a new terminal):**
```bash
# Set up virtual environment
python -m venv venv
source venv/Scripts/activate # Windows: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Tests
pytest -v
```

---

## 💻 CLI Commands (Local)

Run tests on specific browsers:
```bash
pytest --browser=chrome
pytest --browser=firefox
pytest --browser=edge
```

Run specific test suites using Pytest markers:
```bash
pytest -m smoke          # Critical paths only
pytest -m regression     # Full test suite
```

Run the cross-browser automation script (Windows):
```bash
.\run_all_browsers.bat
```

---

## 📊 Reporting

Upon completion, an enterprise-grade HTML report is generated at `reports/report.html`. If any test fails, a screenshot of the browser at the exact moment of failure is automatically embedded inside the HTML report for instant debugging.

---

## 👨‍💻 Author

Built with passion and precision. Designed to demonstrate mastery of modern QA Engineering, CI/CD, and Full-Stack awareness.
