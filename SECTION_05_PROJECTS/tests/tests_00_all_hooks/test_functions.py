import pytest


@pytest.mark.outer
@pytest.mark.sanity
def test_fn_example1_pass():
    """Docstring 1"""
    assert True


@pytest.mark.sanity
@pytest.mark.inner
def test_fn_example2_pass():
    """Docstring 2"""

    assert True


@pytest.mark.setup
@pytest.mark.xfail
@pytest.mark.inner
def test_fn_example3_xfail():
    """Docstring 3"""

    assert False
