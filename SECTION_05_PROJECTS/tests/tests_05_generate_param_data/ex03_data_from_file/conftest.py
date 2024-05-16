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
