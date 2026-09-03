# AI-Assisted Web Test Automation Framework

A Python-based web automation framework built using Playwright and Pytest for functional, regression and end-to-end testing.

## 🚀 Features

- Page Object Model (POM)
- Python + Pytest automation
- Playwright browser automation
- Positive and negative test scenarios
- Parameterized testing
- End-to-end checkout testing
- Automatic screenshots on test failure
- HTML test reports
- Automation logging
- External JSON test data
- Environment-based configuration
- AI-assisted test case generation
- GitHub Actions CI/CD
- Headless browser execution in CI

## 🛠️ Tech Stack

- Python
- Playwright
- Pytest
- Pytest HTML
- Pytest Xdist
- JSON
- REST/API-ready architecture
- Git
- GitHub
- GitHub Actions

## 📁 Project Structure

```text
AI-Web-Test-Automation/
│
├── .github/
│   └── workflows/
│       └── qa-tests.yml
│
├── ai/
│   └── test_case_generator.py
│
├── pages/
│   ├── login_page.py
│   ├── products_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_products.py
│   └── test_checkout.py
│
├── test_data/
│   └── users.json
│
├── screenshots/
│
├── reports/
│
├── utils/
│   ├── config.py
│   └── logger.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
🧪 Test Coverage

The framework currently covers:

Valid login
Invalid username
Invalid password
Empty credentials
Locked user login
Product addition to cart
End-to-end checkout

Total automated tests: 8

▶️ Running the Tests

Create and activate the virtual environment:

python -m venv venv

Install dependencies:

pip install -r requirements.txt

Install Playwright:

playwright install

Run tests:

pytest

Generate HTML report:

pytest --html=reports/report.html --self-contained-html

Run tests in parallel:

pytest -n 2
🔄 CI/CD

GitHub Actions automatically:

Checks out the repository
Installs Python
Installs project dependencies
Installs Playwright
Executes the automated tests
Generates the HTML report
Uploads the report as a build artifact
🤖 AI-Assisted Testing

The project includes an AI-assisted test design component that converts application requirements into structured positive and negative test scenarios.

📌 Future Enhancements
REST API automation
Database validation
Cross-browser execution
Advanced AI-generated automation scripts
Test result dashboards