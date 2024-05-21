import pytest


@pytest.mark.last
def test_01_marked_last():
    """Docstring 1"""
    assert True


@pytest.mark.first
def test_02_marked_first():
    """Docstring 1"""
    assert True


def test_03_not_marked_first_or_last():
    """Docstring 2"""
    assert True


@pytest.mark.last
def test_04_marked_last():
    """Docstring 3"""
    assert True


@pytest.mark.first
def test_05_marked_first():
    """Docstring 3"""

    assert True



def test_06_not_marked_first_or_last():
    """Docstring 3"""

    assert True
