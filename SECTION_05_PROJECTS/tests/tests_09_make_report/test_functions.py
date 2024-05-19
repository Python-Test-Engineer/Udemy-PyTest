""" Tests to run in pytest_runtest_makereport hook.
We have registered many marks in pytest.ini. 
"""

import pytest


def test_01_pass():
    """Docstring 1"""
    assert True


@pytest.mark.xfail  # built in marker so no need to register in pytest.ini
def test_02_xfail():
    """Docstring 3"""
    assert False


def test_03_fail():
    """Docstring 3"""
    assert False


@pytest.mark.skip
def test_04_skip():

    print("n\nRunning test_example5_skipped\n")
    assert False


@pytest.mark.xfail
def test_05_xfail_passes():
    assert True
