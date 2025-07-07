# 🧪 Test Coverage Visualizer

**Test Coverage Visualizer** is a Python-based proof-of-concept project that runs unit tests and displays code coverage metrics for a simple application. It's designed to demonstrate best practices in test automation, CI integration, and Python packaging using `pytest`, `pytest-cov`, and GitHub Actions.

---

## 🔍 Project Goals

- Showcase test automation skills
- Provide a reproducible CI pipeline with GitHub Actions
- Measure and visualize code coverage
- Serve as part of a professional QA/automation engineer GitHub portfolio

---

## 📦 Project Structure
```bash
test-coverage-visualizer/
├── src/
    └── test_coverage_visualizer/
        ├── init.py
        ├── app.py
└── example/
    ├── init.py
    └── math_utils.py
├── tests/
    └── test_math_utils.py
├── pyproject.toml
├── README.md
└── .github/
    └── workflows/
        └── ci.yml
```

---

## 🚀 How to Run Locally

### 1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install in editable mode with dev dependencies:
```bash
pip install -e .[dev]
```
3. Run tests and generate coverage report:
```bash
pytest --cov=src/test_coverage_visualizer --cov-report=term-missing
```

✅ Continuous Integration

GitHub Actions automatically run tests and coverage analysis on every push to the main branch.

CI checks include:

    Python environment setup

    Dependency installation

    Test execution

    Code coverage reporting

🛠 Tech Stack

    Python 3.12+

    pytest for unit testing

    coverage and pytest-cov for coverage reports

    GitHub Actions for CI

📈 Example Output

Sample output from pytest with coverage:
```bash
tests/test_math_utils.py ..                                                          [100%]

Name                                                 Stmts   Miss  Cover
------------------------------------------------------------------------
src/test_coverage_visualizer/app.py                     11     11     0%
src/test_coverage_visualizer/example/math_utils.py       4      0   100%
------------------------------------------------------------------------
TOTAL                                                   15     11    27%
```

👤 Author

David Cohn Lifshitz

Automation Test Engineer

📫 david.kon@gmail.com
