import pytest


def test_fn_example1_pass():
    """Docstring 1"""
    assert True


@pytest.mark.skip
def test_fn_example2_pass():
    """Docstring 2"""
    assert True


@pytest.mark.xfail
def test_fn_example3_xfail():
    """Docstring 3"""
    assert False
