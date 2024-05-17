import pytest


@pytest.fixture()
def examples(pytester):
    pytester.copy_example("src/test_sort.py")


def test_sort(pytester, examples):
    result = pytester.runpytest("-v")

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


# fails if order reversed so this shows they are in desc
