import pytest


@pytest.mark.outer
@pytest.mark.sanity
def test_fn_03():
    """Docstring 1"""
    print("\n\nRunning test03\n")
    assert True


@pytest.mark.sanity
@pytest.mark.inner
def test_fn_04():
    """Docstring 2"""
    print("\n\nRunning test_04\n")
    assert True


@pytest.mark.setup
@pytest.mark.xfail
@pytest.mark.inner
def test_fn_05():
    """Docstring 3"""
    print("n\nRunning test_05\n")
    assert False
