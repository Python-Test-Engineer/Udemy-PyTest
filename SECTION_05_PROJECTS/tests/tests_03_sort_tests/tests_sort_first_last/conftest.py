import pytest
from datetime import datetime
from _pytest.nodes import Item
from _pytest.runner import CallInfo

report_date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
FILENAME = f"report_sort_first_last{report_date}.csv"

print("\n\n")


def pytest_configure(config):
    # we need to add these markers to avoid error if strict-markers is used.
    config.addinivalue_line("markers", "first: run these tests first")
    config.addinivalue_line("markers", "last: run these tests last")


# A pytest hook to for modifying collected items
def pytest_collection_modifyitems(items, config):
    first_tests = []
    last_tests = []
    remaining_tests = []
    # get all the markers for a test
    for test in items:
        list_markers = [
            str(getattr(test.own_markers[j], "name"))
            for j in range(len(test.own_markers))
        ]
        # add items to first_tests and last_tests if they have the first or last marker
        if "first" in list_markers:
            first_tests.append(test)
        elif "last" in list_markers:
            last_tests.append(test)
        else:
            remaining_tests.append(test)

    items[:] = first_tests + remaining_tests + last_tests


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item: Item, call: CallInfo):

#     outcome = yield  # Run all other pytest_runtest_makereport non wrapped hooks

#     if call.when == "call":
#         outcome = call.excinfo
#         try:
#             # Access the test outcome (passed, failed, etc.)
#             test_outcome = "^!!!FAILED!!!^" if outcome else "-PASSED-"
#             # Access the test duration
#             test_duration = call.duration
#             # Access the test ID (nodeid)
#             test_id = item.nodeid

#             list_markers = [
#                 str(getattr(item.own_markers[j], "name"))
#                 for j in range(len(item.own_markers))
#             ]
#             all_markers = ("-").join(list_markers)

#             with open(FILENAME, "a") as f:  # we need 'a' as it adds each item
#                 f.write(
#                     f"{item.name}|{test_id}|{test_outcome}|{test_duration}|{all_markers}\n"
#                 )

#         except Exception as e:
#             print("\nERROR:", e)
