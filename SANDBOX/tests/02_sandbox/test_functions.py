""" Tests to run in pytest_runtest_makereport hook

We have registered many marks in pytest.ini. We will be able to report what marks were used in what tests in the report file we will be producing


"""

import pytest


@pytest.mark.outer
@pytest.mark.sanity
def test_fn_example1_pass():
    """Docstring 1"""
    # print("\n\nRunning test1\n")
    assert True


@pytest.mark.sanity
@pytest.mark.inner
def test_fn_example2_pass():
    """Docstring 2"""
    print("\n\ntest_example2_pass\n")
    assert True


@pytest.mark.setup
@pytest.mark.xfail  # built in marker so no need to register in pytest.ini
@pytest.mark.inner
def test_fn_example3_xfail():
    """Docstring 3"""
    print("n\nRunning test_example3_xfail\n")
    assert False
