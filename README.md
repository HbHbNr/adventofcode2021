[![Python 3.7](https://hbhbnr.github.io/badges/Python-3.7-blue-python-white.svg)](https://docs.python.org/3.7/whatsnew/changelog.html)
[![Python 3.8](https://hbhbnr.github.io/badges/Python-3.8-blue-python-white.svg)](https://docs.python.org/3.8/whatsnew/changelog.html)
[![Python 3.9](https://hbhbnr.github.io/badges/Python-3.9-blue-python-white.svg)](https://docs.python.org/3.9/whatsnew/changelog.html)
[![Python 3.10](https://hbhbnr.github.io/badges/Python-3.10-blue-python-white.svg)](https://docs.python.org/3.10/whatsnew/changelog.html)
[![Python 3.11](https://hbhbnr.github.io/badges/Python-3.11-blue-python-white.svg)](https://docs.python.org/3.11/whatsnew/changelog.html)
[![GitHub Workflow Status](https://github.com/HbHbNr/adventofcode2021/actions/workflows/codequality.yml/badge.svg)](https://github.com/HbHbNr/adventofcode2021/actions/workflows/codequality.yml)
[![Codecov coverage](https://img.shields.io/codecov/c/github/HbHbNr/adventofcode2021?logo=codecov&logoColor=white)](https://app.codecov.io/gh/HbHbNr/adventofcode2021)

# adventofcode2021
Solutions for https://adventofcode.com/2021/ in pure Python, with code quality measurements and unit testing.

# Solution status
| **Day**      | **1** | **2** | **3** | **4** | **5** | **6** | **7** | **8** | **9** | **10** | **11** | **12** | **13** |
|-------------:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:------:|:------:|:------:|:------:|
| **Part One** | ✓     | ✓     | ✓     | ✓     | ✓     | ✓     | ✓     | ✓     | ✓     | ✓      | ✓      | ✓      | ✓      |
| **Part Two** | ✓     | ✓     | ✓     | ✓     | ✓     | ✓     | ✓     | ✓      | ✓     | ✓      | ✓      | ✓      | ✓      |

| **Day**      | **14** | **15** | **16** | **17** | **18** | **19** | **20** | **21** | **22** | **23** | **24** | **25** |
|-------------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|
| **Part One** | ✓      | ✓      | ✓      |        | ✓      |        |         |        |        |        |        |        |
| **Part Two** | ✓      | ✓      | ✓      |        | ✓      |        |         |        |        |        |        |        |

# Requirements
* Python 3 (developed with Python 3.7; tested with 3.7-3.11)

Optional:
* Flake8 (for linting)
* Pylint (for linting)
* mypy (for static type checking)
* pytest (for unit testing)
* pytest-cov (for code coverage) 

# Code quality

Install the requirements for code quality checks:

    python -m pip install -r requirements.txt

## Linting

    ./lint_flake8.sh
    ./lint_pylint.sh

## Static type checking

    ./mypy.sh

## Testing (including code coverage)

    ./pytest.sh

The code coverage report can be found in ``coverage_html_report`` afterwards.

## All of the above

    ./cqall.sh
