import pytest
from datetime import datetime
from pyboxen import boxen

# interesting note - the main source code to see how PyTest works is in the dunder folders...
from _pytest.nodes import Item
from _pytest.runner import CallInfo

# we will get two reports as there is the hook here for educational purposes but also in the root of our projects.

# This conftest gives us a file report_make_report_2024-05-15-09-45-46.csv
# whereas the conftest for the whole project is just report_2024-05-15-09-have
# # we have the pytest_runtest_makereport hook in here as well.

# timesamp our output files
report_date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
FILENAME = f"report_09_{report_date}.csv"

print("\n\n")

# this hook will become a standard ouput report for other projects and will not be included in the project but in the root folder as a common hook.


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: Item, call: CallInfo):
    # item is actual a test.
    # call is an event that is one of setup - call - teardown
    # https://docs.pytest.org/en/7.1.x/reference/reference.html?highlight=call#item

    # this hook needs @pytest.hookimpl(hookwrapper=True) as it must run first and yield to other hooks and other hooks may occur inside it.
    # generally we just use the hook function name.

    # Run all other pytest_runtest_makereport non wrapped hooks and yield the outcome
    outcome = yield
    # report = outcome.get_result() # for reference

    # whe is a property that can be  one of setup, call or teardown.
    if call.when == "call":

        # outcomes can be passed, failed, skipped, xfail, xpass, deselected.AttributeError
        outcome = call.excinfo

        try:
            # Access the test outcome (passed, failed, etc.)

            # Access the test duration
            # test_duration = call.duration
            # Access the test ID (nodeid)
            # e.g tests/tests_01_make_report/test_class.py::TestApp::test_class_01_marked_last
            test_id = item.nodeid

            # markers and keywords - see KEYWORDS.md
            # we will get all the markers for each test
            list_markers = [
                str(getattr(item.own_markers[j], "name"))
                for j in range(len(item.own_markers))
            ]
            all_markers = ("-").join(list_markers)
            # print(all_markers)

            # we can customise the format and what we ouput to the file
            # test_id is the item.node.id and is full path to the test that we would use in CLI
            # e.g tests/tests_ex01_make_report/test_class.py::TestApp::test_class_01_marked_last
            # I prefer a pipe delimed CSV '|' as it is easier to read and avoid conflicts with any other delimiters

            # we need 'a' as it adds each item an 'w' would overwrite
            # we can log directly to a DB.
            # the output format can be customised - I use '|' (pipe) as it is easier to read

            # print(f"{item.name}|{test_id}|{outcome}|{test_duration}|{all_markers}")
            with open(FILENAME, "a") as f:
                if "xfail" in all_markers and outcome is None:
                    outcome = "X-PASSED"
                elif "xfail" in all_markers and outcome is not None:
                    outcome = "X-FAILED PASSED"
                elif outcome is None:
                    outcome = "PASSED"
                elif outcome is not None:
                    outcome = "FAILED"
                else:
                    outcome = outcome
                f.write(
                    # f"{item.name}|{test_id}|{outcome}|{test_duration}|{all_markers}\n"
                    f"{item.name}|{outcome}|{test_id}|{all_markers}\n"
                )

        except Exception as e:
            print("\nERROR:", e)
