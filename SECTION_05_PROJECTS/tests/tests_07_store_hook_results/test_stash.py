import pytest


@pytest.mark.first
@pytest.mark.inner
def test_fn_stash():
    """Docstring 2"""
    assert True
