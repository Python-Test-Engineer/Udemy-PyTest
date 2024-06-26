"""Some assert examples"""

import logging

import pytest

# uses config in pytest.ini
LOGGER = logging.getLogger(__name__)


def test_a1():
    """A test"""
    LOGGER.info("test_a1")
    assert 4 != 3


def test_a2():
    """A test"""
    LOGGER.info("test_a2")
    assert 1


@pytest.mark.sanity
def test_case01():
    """A test"""
    print("---> Sanity Marker", end=" ")
    with pytest.raises(ZeroDivisionError):
        assert 1 / 0
    LOGGER.info("API call done")


def func1():
    """A test"""
    LOGGER.error("func1 ValueError")
    raise ValueError("EXPECTED IndexError func1 raised")


@pytest.mark.sanity
@pytest.mark.xfail
def test_case03():
    """A test"""
    LOGGER.error("test_case03 xfail")
    with pytest.raises(Exception) as excinfo:
        # assert (1,2,3) == (1,2,4)
        func1()
    print(str(excinfo))
    assert (str(excinfo.value)) == "Exception func1 raised"
