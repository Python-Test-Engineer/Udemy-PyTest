import pytest
from datetime import datetime
from _pytest.nodes import Item
from _pytest.runner import CallInfo

report_date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
FILENAME = f"report_generate_from_file_{report_date}.csv"

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
