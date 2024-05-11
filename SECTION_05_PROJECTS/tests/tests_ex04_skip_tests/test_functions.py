import pytest


# we will skip expensive tests in this example.
# there are may ways we can selct tests using marks but this example shows how we can filter selected tests.
# we can use CLI arguments with [pytest addopts --skip-expensive] if we add addopts in hooks
@pytest.mark.outer
@pytest.mark.sanity
def test_fn_example1_pass_expensive():
    """Docstring 1"""
    print("\n\nRunning test1\n")
    assert True


@pytest.mark.expensive
@pytest.mark.inner
def test_fn_example2_pass():
    """Docstring 2"""
    print("\n\ntest_example2_pass\n")
    assert True


@pytest.mark.setup
@pytest.mark.xfail
@pytest.mark.inner
def test_fn_example3_xfail():
    """Docstring 3"""
    print("n\nRunning test_example3_xfail\n")
    assert False
