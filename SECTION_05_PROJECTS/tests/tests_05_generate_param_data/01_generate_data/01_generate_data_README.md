

https://docs.pytest.org/en/7.4.x/how-to/parametrize.html#pytest-generate-tests

A standard parametrize example:

python -m pytest -vs .\tests\tests_05_generate_param_data\01_generate_data\test_basic.py --tb=no

We can create parametrized fixture of data to avoid DRY.

In this example we create some lists and tuples to use as fixtures in our tests.


https://docs.pytest.org/en/latest/reference/reference.html#metafunc