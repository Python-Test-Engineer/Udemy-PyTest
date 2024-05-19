import pytest


@pytest.mark.outer
@pytest.mark.sanity
def test_fn_03():
    """Docstring 1"""
    assert True


@pytest.mark.sanity
@pytest.mark.inner
def test_fn_04():
    """Docstring 2"""
    assert True


@pytest.mark.setup
@pytest.mark.xfail
@pytest.mark.inner
def test_fn_05():
    """Docstring 3"""
    assert False
