import pytest
from datetime import datetime
from _pytest.nodes import Item
from _pytest.runner import CallInfo


report_date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
FILENAME = f"report_skip_tests_{report_date}.csv"

print("\n\n")


# A pytest hook to for modifying collected items
def pytest_collection_modifyitems(items, config):

    selected = []
    deselected = []
    for item in items:
        print(f"\ntest: {item.nodeid}")
        # Either add to deselected or selected lists

        list_markers = [
            str(getattr(item.own_markers[j], "name"))
            for j in range(len(item.own_markers))
        ]
        all_markers = ("-").join(list_markers)
        # expensive in test name
        if "expensive" in item.nodeid:
            deselected.append(item)
        # expensive in markers
        # we could use -m flag in CLI to skip expensive tests but we might have more compled
        # logic in test functions to skip tests and this may be useful
        elif "expensive" in all_markers:
            deselected.append(item)
        else:
            selected.append(item)

    # Update the deselected tests
    config.hook.pytest_deselected(items=deselected)

    # Update the selected tests
    items[:] = selected
    for item in items:
        print(f"\nSELECTED: {item.nodeid}")