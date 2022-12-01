# advent-of-code-2022

Advent of Code 2022 Solutions https://adventofcode.com/

## Setup

### Advent Of Code Data Setup
Get your session cookie to allow access to your user specific data

Instructions: https://github.com/wimglenn/advent-of-code-wim/issues/1

### Python Setup

You can utilize [pyenv](https://github.com/pyenv/pyenv) or [conda](https://docs.conda.io/en/latest/) for setting up your base python interpreter(s).

1. Install [Poetry](https://python-poetry.org/docs/master/#installing-with-the-official-installer) if you have not installed on your machine
2. Install project dependencies into poetry environment: `poetry install`
 
General Poetry usage:
Use your poetry environment defined by [pyproject.toml](pyproject.toml). How to: https://python-poetry.org/docs/master/basic-usage/#activating-the-virtual-environment

Adding Dependencies
https://python-poetry.org/docs/master/basic-usage/#specifying-dependencies

Adding development only dependencies (e.g. tools for testing, code coverage, etc.)
`poetry add $PACKAGE --dev`
This will change in Poetry 1.2 to use the groups syntax `poetry add $PACKAGE --group dev`
