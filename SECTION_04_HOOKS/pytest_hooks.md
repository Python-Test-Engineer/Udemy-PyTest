# PyTest_08_HOOKS

This is an isolated test suite to demonstrate variables etc accessible during a PyTest run.

## Hooks

PyTest has many hooks that we can tap into such as 'seesion_start'. 'make_report'

We can use conftest.py as a central location to add our own implementations when these hooks run.

In PyTest_07_HOOKS, we use these hooks to create a number of mini-plugins. Remember, hooks are the basis for plugins and if ina file, particulalry conftest.py, then the are 'local' plugins. If we make them distributale via PyPi or GitHub then the are 'pluigns'

![Examples](./images/list_hooks.png "PyTest Hooks")

In the conftest.py, we add hooks for:

- pytest_configure
- pytest_sessionstart
- pytest_sessionfinish
- pytest_collection_modifyitems - this gathers tests it will do and can display without running tests. One can sort by property as well as add markers dynamically
- pytest_generate_tests - this enables us to customise tests. The example we look it is how we can dynamically create params for the `@pytest.mark.paremetrize` feature. This is a Hypothesis Lite as it werem where can create datasets that push the boundaries of values.
- pytest_runtest_makereport - we get test results and export to CSV, (see below). This can be used to create simple summary reports.



There are many more. A useful article on hooks: https://paragkamble.medium.com/understanding-hooks-in-pytest-892e91edbdb7


## Install 

- move to `PyTest_08_HOOKS` 
- create virtual environment as you wish
- run `pip install requirements.txt`

## Run Tests

- run `python -m pytest -vs`.
- you will se output of accessible variables in PyBoxen, (a console formatter based on Rich).
- some more verbose information has been commented out.
- Test results are exported to an output pipe delimited CSV file that is timestamped Y-M-D-H-M-S `report_2024-05-04-12-55-53.csv` in the `pytest_runtest_makereport` hook. It is `|` pipe delimited. One can read and extract relevant infomation of test that will be run. It has all the markers including xfail included.
```
test_division|tests/ex01/test_class.py::TestApp::test_division|PASSED|0.00011979998089373112|inner-db2-outer
test_example1_pass|tests/ex01/test_functions.py::test_example1_pass|PASSED|0.0009691999293863773|sanity-outer
test_example2_pass|tests/ex01/test_functions.py::test_example2_pass|PASSED|0.0006700998637825251|inner-sanity
test_example3_xfail|tests/ex01/test_functions.py::test_example3_xfail|FAILED|0.000541699817404151|inner-xfail-setup
test_multiplication|tests/ex01/test_class.py::TestApp::test_multiplication|PASSED|8.490006439387798e-05|inner-sanity-db2-db-outer

```

`tests/ex01/test_class.py::TestApp::test_division` is the node of the test and has the full 'path' to the test that we might use in the CLI. The test duration in seconds is included too.

We can detect xfail either via markers or if we include it in our test name,
##  - create CSV report

##  -  add custom markers

##  -  sort tests

##  -  skip tests

We can use -k and -m but if we have more complex logic then `pytest_collection_modifyitems` can help.

##  -  dynamic param data

##  -  config hook

##  -  stash hook data



