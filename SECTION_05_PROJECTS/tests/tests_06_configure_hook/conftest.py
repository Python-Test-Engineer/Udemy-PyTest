import pytest
import os
import random
from datetime import datetime
from _pytest.nodes import Item
from _pytest.runner import CallInfo
from pyboxen import boxen

from rich.console import Console

console = Console()


# https://rich.readthedocs.io/en/stable/appendix/colors.html

# Let's define our failures.txt as a constant as we will need it later

rnd = random.randint(100_000, 999_999)
report_date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
FILENAME = f"report_configure_hook_{report_date}.csv"

print("\n\n")


def pytest_configure(config):

    config.input_file_content = "input_file_content no leading _"
    config.my_global_value = "Shared Value"
    # This is available via the request built in fixture so can be accessed in tests
    # global_value = request.config.my_global_value

    output1 = str(dir(config))
    # Get the path to the text file in the same directory as conftest.py
    current_directory = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_directory, "input.txt")

    # Read the content of the file and store it in the pytest config object
    with open(input_file_path, "r") as file:
        file_content = file.read()

    # _input_file_content seems to be special in that in can be a fixture.abs
    # underscore does not work with my_global_value
    config._input_file_content = file_content


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: Item, call: CallInfo):

    outcome = yield  # Run all other pytest_runtest_makereport non wrapped hooks

    if call.when == "call":
        outcome = call.excinfo
        try:
            # Access the test outcome (passed, failed, etc.)
            test_outcome = "^!!!FAILED!!!^" if outcome else "-PASSED-"
            # Access the test duration
            test_duration = call.duration
            # Access the test ID (nodeid)
            test_id = item.nodeid

            list_markers = [
                str(getattr(item.own_markers[j], "name"))
                for j in range(len(item.own_markers))
            ]
            all_markers = ("-").join(list_markers)

            with open(FILENAME, "a") as f:  # we need 'a' as it adds each item
                f.write(
                    f"{item.name}|{test_id}|{test_outcome}|{test_duration}|{all_markers}\n"
                )

        except Exception as e:
            print("\nERROR:", e)
