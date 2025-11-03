# GitHub-Actions-DEMO

DEMO repository for testing GitHub Actions (CI/CD) with Allure Reports.

## Viewing Test Reports

This repository generates test reports in Allure format. You can view them locally as an interactive HTML dashboard.

### Prerequisites
Make sure the following tools are installed on your system:
- Java (for Allure CLI)
- Allure CLI

### Steps to View the Dashboard

1. Locate the generated test results folder (e.g., `allure-results`).
2. Generate the HTML report:
   ```bash
   allure generate <path-to-allure-results> --clean -o <path-to-html-report>
3. Open the dashboard in your browser:
   ```bash
   allure open <path-to-html-report>
