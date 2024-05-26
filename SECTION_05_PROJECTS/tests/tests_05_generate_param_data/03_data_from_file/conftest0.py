import pytest
from datetime import datetime
from _pytest.nodes import Item
from _pytest.runner import CallInfo


print("\n\n")
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


# A pytest hook to dynamically parametrize tests
def pytest_generate_tests(metafunc):
    # Check if the num fixture is used
    if "initial_value" in metafunc.fixturenames:
        # Get the command line option
        input_file = metafunc.config.getoption("--input_file")
        pring("input_file: ", input_file)
        # Read the data from the input file (if specified)
        # We can load data from any external source that Python supports
        data = ["Apples", "Bananas", "Cherries"]
        # if input_file:
        #     with open(input_file, "r") as f:
        #         lines = f.readlines()
        #     data = [line.strip() for line in lines]

        # Parametrize the test
        metafunc.parametrize("initial_value", data)
