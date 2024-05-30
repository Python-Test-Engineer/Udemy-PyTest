"""Some basic asserts"""
import pytest


def test_a1():
    """A test"""
    assert 4 != 3


def test_a2():
    """A test"""
    assert 1


@pytest.mark.setup
def test_a3():
    """A test"""
    assert "abcd" == "abcd"


def test_a4():
    """A test"""
    assert ((3 - 1) * 4 / 2) == 4.0


@pytest.mark.setup
def test_a5():
    """A test"""
    assert 1 in divmod(9, 5)
    assert "this" in "this is pytest"
    assert [1, 2, 4] == [1, 2, 4]
