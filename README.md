[![Python 3.7](https://hbhbnr.github.io/docs/badges/Python-3.7-blue-python-white.svg)](https://docs.python.org/3.7/whatsnew/changelog.html)
[![Python 3.8](https://hbhbnr.github.io/docs/badges/Python-3.8-blue-python-white.svg)](https://docs.python.org/3.8/whatsnew/changelog.html)
[![Python 3.9](https://hbhbnr.github.io/docs/badges/Python-3.9-blue-python-white.svg)](https://docs.python.org/3.9/whatsnew/changelog.html)
[![Python 3.10](https://hbhbnr.github.io/docs/badges/Python-3.10-blue-python-white.svg)](https://docs.python.org/3.10/whatsnew/changelog.html)
[![Python 3.11](https://hbhbnr.github.io/docs/badges/Python-3.11-blue-python-white.svg)](https://docs.python.org/3.11/whatsnew/changelog.html)
[![GitHub Workflow Status](https://github.com/HbHbNr/adventofcode2021/actions/workflows/codequality.yml/badge.svg)](https://github.com/HbHbNr/adventofcode2021/actions/workflows/codequality.yml)
[![Codecov coverage](https://img.shields.io/codecov/c/github/HbHbNr/adventofcode2021?logo=codecov&logoColor=white)](https://app.codecov.io/gh/HbHbNr/adventofcode2021)

# adventofcode2021
Solutions for https://adventofcode.com/2021/ in plain Python

# Requirements
* Python 3 (developed with Python 3.7; tested with 3.7-3.11)
* Flake8 (optional, for linting)
* Pylint (optional, for linting)
* mypy (optional, for static type checking)
* pytest (optional, for testing)
* pytest-cov (optional, for coverage) 

# Code quality
## Linting

    ./lint_flake8.sh
    ./lint_pylint.sh

## Static type checking

    ./mypy.sh

## Testing (including coverage)

    ./pytest.sh

Code coverage report can be found in ``coverage_html_report`` afterwards.

## All of the above

    ./cqall.sh
