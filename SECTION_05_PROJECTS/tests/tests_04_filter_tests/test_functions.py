import pytest


# we will skip expensive tests in this example.
# there are may ways we can selct tests using marks but this example shows how we can filter selected tests.
# we can use CLI arguments with [pytest addopts --skip-expensive] if we add addopts in hooks


def test_fn_example1_pass():
    """Docstring 1"""
    # print("\n\nRunning test1\n")
    assert True


@pytest.mark.expensive
def test_fn_example2_pass_expensive():
    """Docstring 2"""
    # print("\n\ntest_example2_pass\n")
    assert True


def test_fn_example3_pass():
    """Docstring 3"""
    assert True


@pytest.mark.expensive
def test_fn_example4_pass_expensive():
    """Docstring 2"""
    # print("\n\ntest_example2_pass\n")
    assert True
