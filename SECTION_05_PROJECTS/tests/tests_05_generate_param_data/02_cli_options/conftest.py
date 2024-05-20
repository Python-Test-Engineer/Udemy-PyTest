import pytest
import random
from datetime import datetime
from _pytest.nodes import Item
from _pytest.runner import CallInfo
from pyboxen import boxen

from rich.console import Console

console = Console()


# https://rich.readthedocs.io/en/stable/appendix/colors.html

# Let's define our failures.txt as a constant as we will need it later


def pytest_addoption(parser):
    parser.addoption(
        "--stringinput",
        action="append",
        default=[],
        help="list of string inputs to pass to test functions",
    )


def pytest_generate_tests(metafunc):
    if "stringinput" in metafunc.fixturenames:
        metafunc.parametrize("stringinput", metafunc.config.getoption("stringinput"))
