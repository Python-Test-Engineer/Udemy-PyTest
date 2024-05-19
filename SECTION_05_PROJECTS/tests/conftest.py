import pytest
from datetime import datetime
from _pytest.nodes import Item
from _pytest.runner import CallInfo

# timestamp our ouput files
report_date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
FILENAME = f"report_{report_date}.csv"

print("\n\n")


@pytest.hookimpl(
    hookwrapper=True
)  # hookwrapper = True as it is a parent in the tree - see image
def pytest_runtest_makereport(item: Item, call: CallInfo):
    # item is a collection of tests so we may use for test in Item rather than for item in Item

    outcome = yield  # Run all other pytest_runtest_makereport non wrapped hooks
    # report = outcome.get_result() # for reference

    if call.when == "call":  # when can be setup, call or teardown
        outcome = call.excinfo
        try:
            # Access the test outcome (passed, failed, etc.)
            test_outcome = "^!!!FAILED!!!^" if outcome else "-PASSED-"
            # Access the test duration
            test_duration = call.duration
            # Access the test ID (nodeid)
            test_id = item.nodeid
            # markers and keywords - see KEYWORDS.md
            # we will get all the markers for a test
            list_markers = [
                str(getattr(item.own_markers[j], "name"))
                for j in range(len(item.own_markers))
            ]
            all_markers = ("-").join(list_markers)

            # we can customise the format and what we ouput to the file
            # test_id is the item.node.id and is full path to the test that we would use in CLI
            # e.g tests/tests_ex01_make_report/test_class.py::TestApp::test_class_01_marked_last
            # I prefer a pipe delimed CSV '|' as it is easier to read and avoid conflicts with any other delimiters

            with open(f"{FILENAME}", "a") as f:
                f.write(
                    f"{item.name}|{test_id}|{test_outcome}|{test_duration}|{all_markers}\n"
                )
        except Exception as e:
            print("\nERROR:", e)
