import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--desc", action="store_true", default=False, help="sort descending"
    )
    parser.addoption("--asc", action="store_true", default=False, help="sort ascending")


# A pytest hook to for modifying collected items
def pytest_collection_modifyitems(items, config):
    # We get the value of the flag passed in the command line. If both are supplied then we sort by the last flag which is --asc.

    # items is in fact 'tests' but not used as this would clash with the 'test' keyword.

    # We have seen that a test has a test nodeid which is a path to the test. We want to sort by the last part of the path, so we split and get the last part.

    # We then sort by the last part of the path. The nodeid uses '::' as a separator.

    # We print out DESC or ASC depending on the flag passed in the command line for illustration.

    # item.nodeid - this is test_2 in the example below
    # tests/tests_03_sort_tests/tests_01_sort_by_testname/test_sort_num.py::test_2

    if config.option.desc:
        items.sort(key=lambda item: item.nodeid.split("::")[-1], reverse=True)
        print(f"\n\n===> DESC:")
    if config.option.asc:
        items.sort(key=lambda item: item.nodeid.split("::")[-1])
        print(f"\n\n===> ASC:")
