"""Some assert examples"""
import pytest


@pytest.mark.sanity
def test_case01():
    """A test"""
    print("---> Sanity Marker", end=" ")
    with pytest.raises(ZeroDivisionError):
        assert 1 / 0
        # assert 3 > 3


def func1():
    """A test"""
    raise ValueError("EXPECTED IndexError func1 raised")
