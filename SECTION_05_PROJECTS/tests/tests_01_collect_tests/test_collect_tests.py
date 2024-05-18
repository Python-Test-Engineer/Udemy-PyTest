import pytest


@pytest.mark.expensive
def test_interface_simple():
    assert 1


@pytest.mark.outer
@pytest.mark.inner
def test_interface_complex():
    assert 1


@pytest.mark.first
def test_event_simple():
    assert 1


@pytest.mark.outer
@pytest.mark.first
@pytest.mark.inner
def test_something_else():
    assert 1
