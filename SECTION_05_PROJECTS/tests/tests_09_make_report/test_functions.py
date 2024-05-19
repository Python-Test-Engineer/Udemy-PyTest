""" Tests to run in pytest_runtest_makereport hook.
We have registered many marks in pytest.ini. 
"""

import pytest


@pytest.mark.outer
@pytest.mark.sanity
def test_fn_example1_pass():
    """Docstring 1"""
    print("\n\nRunning test1\n")
    assert True


@pytest.mark.sanity
@pytest.mark.inner
def test_fn_example2_pass():
    """Docstring 2"""
    print("\n\nRunning test_example2_pass\n")
    assert True


@pytest.mark.setup
@pytest.mark.xfail  # built in marker so no need to register in pytest.ini
@pytest.mark.inner
def test_fn_example3_xfail():
    """Docstring 3"""
    print("n\nRunning test_example3_xfail\n")
    assert False


def test_fn_example4_fail():
    """Docstring 3"""
    print("n\nRunning test_example4_fail\n")
    assert False


@pytest.mark.skip
def test_fn_example5_skipped():
    """Docstring 3"""
    print("n\nRunning test_example5_skipped\n")
    assert False


@pytest.mark.xfail
def test_fn_example6_xfail_passes():
    """Docstring 3"""
    assert True
