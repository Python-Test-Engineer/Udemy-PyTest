import pytest


# we will skip expensive tests in this example.
# there are may ways we can selct tests using marks but this example shows how we can filter selected tests.
# we can use CLI arguments with [pytest addopts --skip-expensive] if we add addopts in hooks


def test_01():
    """Docstring 1"""
    # print("\n\nRunning test1\n")
    assert True


@pytest.mark.custom_expensive_marker
def test_02_mark_expensive():
    """Docstring 2"""
    assert True



def test_03():
    """Docstring 3"""
    assert True


@pytest.mark.custom_expensive_marker
def test_04_mark_expensive():
    """Docstring 2"""
    assert True


def test_05():
    """Docstring 2"""
    assert True


@pytest.mark.custom_expensive_marker
def test_06_mark_expensive():
    """Docstring 2"""
    assert True


def test_07():
    """Docstring 2"""
    assert True
