[![Python 3.7](https://img.shields.io/badge/Python-3.7-blue?logo=python&logoColor=white)](https://docs.python.org/3.7/whatsnew/changelog.html)
[![Python 3.8](https://img.shields.io/badge/Python-3.8-blue?logo=python&logoColor=white)](https://docs.python.org/3.8/whatsnew/changelog.html)
[![Python 3.9](https://img.shields.io/badge/Python-3.9-blue?logo=python&logoColor=white)](https://docs.python.org/3.9/whatsnew/changelog.html)
[![Python 3.10](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)](https://docs.python.org/3.10/whatsnew/changelog.html)
[![GitHub Workflow Status](https://github.com/HbHbNr/adventofcode2021/actions/workflows/codequality.yml/badge.svg)](https://github.com/HbHbNr/adventofcode2021/actions/workflows/codequality.yml)
[![Codecov coverage](https://img.shields.io/codecov/c/github/HbHbNr/adventofcode2021?logo=codecov&logoColor=white)](https://app.codecov.io/gh/HbHbNr/adventofcode2021)

# adventofcode2021
Solutions of https://adventofcode.com/2021/

# Requirements
* Python 3 (developed with Python 3.7; tested with 3.7-3.10)
* Flake8 (optional, for linting)
* pytest (optional, for testing)
* pytest-cov (optional, for coverage) 
* mypy (optional, for static type checking)

# Code quality
## Linting

    ./lint_flake8.sh
    ./lint_pylint.sh

## Static type checking

    ./mypy.sh

## Testing (including coverage)

    ./pytest.sh

## All of the above

    ./cqall.sh
