![Static Badge](https://img.shields.io/badge/Python-3.7-blue)
![Static Badge](https://img.shields.io/badge/Python-3.8-blue)
![Static Badge](https://img.shields.io/badge/Python-3.9-blue)
![Static Badge](https://img.shields.io/badge/Python-3.10-blue)
![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/HbHbNr/adventofcode2021/codequality.yml?logo=github&logoColor=white)
![Codecov](https://img.shields.io/codecov/c/github/HbHbNr/adventofcode2021?logo=codecov&logoColor=white)

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
