import pytest
from datetime import datetime
from _pytest.nodes import Item
from _pytest.runner import CallInfo


print("\n\n")


# A pytest hook for adding an option
def pytest_addoption(parser):
    parser.addoption(
        "--input_file", action="store", default="", help="Choose an input file!"
    )


# A pytest hook to dynamically parametrize tests
def pytest_generate_tests(metafunc):
    # Check if the num fixture is used
    if "initial_value" in metafunc.fixturenames:
        # Get the command line option
        input_file = metafunc.config.getoption("--input_file")

        # Read the data from the input file (if specified)
        # We can load data from any external source that Python supports
        data = []
        if input_file:
            with open(input_file, "r") as f:
                lines = f.readlines()
            data = [line.strip() for line in lines]

        # Parametrize the test
        metafunc.parametrize("initial_value", data)
