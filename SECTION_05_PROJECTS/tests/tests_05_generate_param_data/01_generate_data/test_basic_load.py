import pytest


def add(a, b):
    return a + b


# we can load in from a file or a database
# we can make this a fixture in conftest.py
data = [
    (1, 2, 3),  # The first set of arguments
    (4, 5, 9),  # The second set of arguments
    (10, 20, 30),  # The third set of arguments
    (0, 0, 0),  # The fourth set of arguments
    (-1, 1, 0),  # The fifth set of arguments
]


# Define the test function and use the parametrize mark
@pytest.mark.parametrize("input1, input2, expected", data)
def test_add(input1, input2, expected):
    assert add(input1, input2) == expected
