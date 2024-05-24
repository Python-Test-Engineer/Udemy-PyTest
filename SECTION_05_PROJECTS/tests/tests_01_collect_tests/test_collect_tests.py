import pytest


@pytest.mark.outer
@pytest.mark.first
@pytest.mark.inner
def test_something_else():
    assert 1
