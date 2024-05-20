""" Tests to run in pytest_runtest_makereport hook.
We have registered many marks in pytest.ini. 
"""

import pytest
from time import sleep


def test_01_pass():
    """Docstring 1"""
    sleep(2)
    assert True


@pytest.mark.xfail  # built in marker so no need to register in pytest.ini
def test_02_xfail_fails():
    """Docstring 3"""
    sleep(5)
    assert False


def test_03_fail():
    """Docstring 3"""
    sleep(5)
    assert False


@pytest.mark.skip
def test_04_skip():
    sleep(3)
    print("n\nRunning test_example5_skipped\n")
    assert False


@pytest.mark.xfail
def test_05_xfail_passes():
    sleep(3)
    assert True
