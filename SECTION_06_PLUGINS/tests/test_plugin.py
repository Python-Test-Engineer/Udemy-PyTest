import pytest


@pytest.fixture()
def examples(pytester):
    pytester.copy_example("src/test_sort.py")


def test_sort(pytester, examples):
    result = pytester.runpytest("-v")
    result.stdout.fnmatch_lines(
        [
            "*test_sort.py::test_z PASSED*",
        ]
    )
    result.stdout.fnmatch_lines(
        [
            "*test_sort.py::test_s PASSED*",
        ]
    )
    result.stdout.fnmatch_lines(
        [
            "*test_sort.py::test_a PASSED*",
        ]
    )
    # etc for all tests
    result.stdout.fnmatch_lines(
        [
            "*==== 6 passed in*",
        ]
    )

    result.assert_outcomes(passed=6)
