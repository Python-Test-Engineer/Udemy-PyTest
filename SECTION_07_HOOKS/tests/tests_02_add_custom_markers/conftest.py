"""
In this example we have commented out pytest_runtest_makereport and use the root level configtest.py implementation of from django.conf import settings"
"""

import pytest

from datetime import datetime

# from _pytest.nodes import Item
# from _pytest.runner import CallInfo
from pyboxen import boxen


# https://rich.readthedocs.io/en/stable/appendix/colors.html

# Let's define our failures.txt as a constant as we will need it later


report_date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
FILENAME = f"report_add_custom_markers_{report_date}.csv"


print("\n\n")


def pytest_configure(config):
    config.addinivalue_line("markers", "simple_marker: mark simple test")
    config.addinivalue_line("markers", "complex_marker: mark complex test")


# !INFO
# ensure ; addopts = --strict-markers not used or add via config hook otherwise following error cocurs:
# INTERNALERROR> Failed: 'simple' not found in `markers` configuration option
def pytest_collection_modifyitems(items):
    # using simple_marker rather than simple so that when we print keywords we can see that we are using simple_marker
    # other wise if just simple it is not clear if it is picking part of test name that has simple in it.
    # NOTE these markers are not on the pytest.ini file but are 'in memory' as it were
    for test in items:
        if "simple" in test.name:
            test.add_marker(pytest.mark.simple_marker)
        if "complex" in test.name:
            test.add_marker(pytest.mark.complex_marker)
    print("\n")
    for test in items:
        all_keywords = [str(x) for x in test.keywords]
        all_keywords = (" - ").join(all_keywords)

        output = f"Test: {test.nodeid} \nKeywords: {all_keywords}"
        # keyword order is
        # test name - markers - module name - folder - parent folder/grandparent folder - root folder
        print(
            boxen(
                output,
                title=f"keywords for {test.name}",
                subtitle="keywords",
                subtitle_alignment="left",
                color="blue",
                padding=1,
            )
        )


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
