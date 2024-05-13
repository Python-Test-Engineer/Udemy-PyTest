import pytest
from datetime import datetime
from _pytest.nodes import Item
from _pytest.runner import CallInfo

# we will get two reports as there is the hook here for educational purposes but also in the root of our projects

# timesamp our output files
report_date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
FILENAME = f"report_make_report_{report_date}.csv"

print("\n\n")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: Item, call: CallInfo):
    # item is actuall a test so we may use for test in Item rather than for item in Item
    # call is an event that is one of setup - call - teardown

    # item is a collection of tests so we may use for test in Item rather than for item in Item
    # https://docs.pytest.org/en/7.1.x/reference/reference.html?highlight=call#item

    # Run all other pytest_runtest_makereport non wrapped hooks
    outcome = yield
    # report = outcome.get_result() # for reference

    # when can be setup, call or teardown
    if call.when == "call":

        # outcomes can be passed, failed, skipped
        outcome = call.excinfo

        try:
            # Access the test outcome (passed, failed, etc.)
            test_outcome = "^!!!FAILED!!!^" if outcome else "-PASSED-"
            # Access the test duration
            test_duration = call.duration
            # Access the test ID (nodeid)
            test_id = item.nodeid

            # markers and keywords - see KEYWORDS.md
            # we will get all the markers for each test
            list_markers = [
                str(getattr(item.own_markers[j], "name"))
                for j in range(len(item.own_markers))
            ]
            all_markers = ("-").join(list_markers)

            # we can customise the format and what we ouput to the file
            # test_id is the item.node.id and is full path to the test that we would use in CLI
            # e.g tests/tests_ex01_make_report/test_class.py::TestApp::test_class_01_marked_last
            # I prefer a pipe delimed CSV '|' as it is easier to read and avoid conflicts with any other delimiters

            # we need 'a' as it adds each item an 'w' would overwrite
            with open(FILENAME, "a") as f:
                f.write(
                    f"{item.name}|{test_id}|{test_outcome}|{test_duration}|{all_markers}\n"
                )

        except Exception as e:
            print("\nERROR:", e)
