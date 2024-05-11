"""
Plugin code
"""

import pytest

__version__ = "0.0.1"


#
def pytest_addoption(parser):
    parser.addoption("--desc", action="store_true", default=False)
    parser.addoption("--runenv", action="store", default="local")


@pytest.fixture(scope="session")
def desc(request):
    if request.config.option.desc:
        print("\n--desc TRUE: ", request.config.option.desc)
        return True
    else:
        print("\n--desc FALSE: ", request.config.option.desc)
        return False


# A pytest hook to for modifying collected items
def pytest_collection_modifyitems(items, config, desc):
    # we can sort order of items (tests) as needed
    # can ber used to sort by fixtures used if one is say expensive in time
    # items.sort(key=lambda item: "expensive" in item.fixturenames)
    if desc:
        print(f"\n--desc TRUE: {config.option.desc}")
        items.sort(key=lambda item: item.nodeid.split("::")[-1], reverse=True)
    else:
        print(f"\n--desc FALSE: {config.option.desc}")
        items.sort(key=lambda item: item.nodeid.split("::")[-1])
