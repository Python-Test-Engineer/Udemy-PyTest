import pytest


# we don't need to create a fixture. we can use pytester.copy_example("src/test_sort.py") in the test_sort_asc an test_sort_desc tests but this makes it reuseable.
@pytest.fixture()
def examples(pytester):
    pytester.copy_example("src/test_sort.py")


def test_sort_asc(pytester, examples):
    result = pytester.runpytest("-v", "--asc")

    result.stdout.fnmatch_lines(
        [
            "*test_sort.py::test_1 PASSED*",
            "*test_sort.py::test_2 PASSED*",
            "*test_sort.py::test_3 PASSED*",
            "*test_sort.py::test_4 PASSED*",
            "*test_sort.py::test_5 PASSED*",
            "*test_sort.py::test_6 PASSED*",
        ]
    )

    # etc for all tests
    result.stdout.fnmatch_lines(
        [
            "*==== 6 passed in*",
        ]
    )

    result.assert_outcomes(passed=6)


def test_sort_desc(pytester, examples):
    result = pytester.runpytest("-v", "--desc")
    result.stdout.fnmatch_lines(
        [
            "*===> DESC:*",
        ]
    )
    result.stdout.fnmatch_lines(
        [
            "*test_sort.py::test_6 PASSED*",
            "*test_sort.py::test_5 PASSED*",
            "*test_sort.py::test_4 PASSED*",
            "*test_sort.py::test_3 PASSED*",
            "*test_sort.py::test_2 PASSED*",
            "*test_sort.py::test_1 PASSED*",
        ]
    )
    result.assert_outcomes(passed=6)


def test_sort_asc_outcomes(pytester, examples):
    result = pytester.runpytest("--asc")

    result.assert_outcomes(passed=6)


def test_help(pytester):
    result = pytester.runpytest("--help")
    result.stdout.fnmatch_lines(["* --desc*  sort descending*"])
    result.stdout.fnmatch_lines(["* --asc*  sort ascending*"])
