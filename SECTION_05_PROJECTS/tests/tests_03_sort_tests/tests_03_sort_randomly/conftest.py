import random
from datetime import datetime
import pytest
from _pytest.nodes import Item
from _pytest.runner import CallInfo

print("\n\n")

report_date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
FILENAME = f"report_sort_randomly_{report_date}.csv"


# A pytest hook to for modifying collected items
def pytest_collection_modifyitems(items, config):
    # we can sort order of items (tests) as needed
    # can ber used to sort by fixtures used if one is say expensive in time
    # items.sort(key=lambda item: "expensive" in item.fixturenames)
    random.shuffle(items)


@pytest.hookimpl(
    hookwrapper=True
)  # hookwrapper = True as it is a parent in the tree - see image
def pytest_runtest_makereport(item: Item, call: CallInfo):
    # item is a collection of tests so we may use for test in Item rather than for item in Item

    outcome = yield  # Run all other pytest_runtest_makereport non wrapped hooks
    # report = outcome.get_result() # for reference

    if call.when == "call":  # when can be setup, call or teardown
        # outcome = call.excinfo
        try:
            with open(
                FILENAME, "a"
            ) as f:  # we need 'a' as it adds each item an 'w' would overwrite
                f.write(f"{item.name}\n")

        except Exception as e:
            print("\nERROR:", e)
