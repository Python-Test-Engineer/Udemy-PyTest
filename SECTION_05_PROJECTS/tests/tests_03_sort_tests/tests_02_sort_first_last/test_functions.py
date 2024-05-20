import pytest


@pytest.mark.last
def test_fn_01_marked_last():
    """Docstring 1"""
    assert True


@pytest.mark.first
def test_fn_02_marked_first():
    """Docstring 1"""
    assert True


def test_fn_03_not_marked_first_or_last():
    """Docstring 2"""
    assert True


@pytest.mark.last
def test_fn_04_marked_last():
    """Docstring 3"""
    assert True


@pytest.mark.first
def test_fn_05_marked_first():
    """Docstring 3"""
    print("n\nRunning test_05\n")
    assert True