# pytest-sort

We use a whl builder like flit to create pyproject.toml

in [project] section, change this to pytest-sort notpytest_sort as PyPi prefers dashes:

[project]
name = "pytest-sort" 

Copy conftest.py local to pytest_sort.py as this is the plugin with rest of template.

We use `flit build --format=wheel` to build a whl file which we then need to install so that our plugin is active:

`pip install .\dist\pytest_sort-0.0.1-py3-none-any.whl` (--force if already one there)

To test src code before and after installation of our plugin:

`python -m pytest -vs .\src\test_sort.py`.

Before plugin with `pip install .\dist\pytest_sort-0.0.1-py3-none-any.whl`, we get no sorting:
```
src/test_sort.py::test_s PASSED
src/test_sort.py::test_z PASSED
src/test_sort.py::test_a PASSED
src/test_sort.py::test_y PASSED
src/test_sort.py::test_x PASSED
src/test_sort.py::test_r PASSED
```

Once we install our plugin, we get test sorted alphabetically

```
src/test_sort.py::test_a PASSED
src/test_sort.py::test_r PASSED
src/test_sort.py::test_s PASSED
src/test_sort.py::test_x PASSED
src/test_sort.py::test_y PASSED
```

We then need to `python -m pytest -vs .\tests\test_plugin.py`. We don't want to run any other test files.

We will see that the tests are sorted alphabetically and KEYWORDS are displayed.

This is manual test so we need to do an assert on PASSED=6 as well as content displayed:

```
    result = pytester.runpytest("-v")
    # adjust if number of tests are different
    result.assert_outcomes(passed=6) 
    # search the console output for expected prhases
    # note we use * wild cards * for text fragments
    result.stdout.fnmatch_lines(
        [
            "*test_sort.py::test_z PASSED*",
        ]
    )
    result.stdout.fnmatch_lines(
        [
            "*test_sort.py::test_s PASSED*",
        ]
    )
    result.stdout.fnmatch_lines(
        [
            "*test_sort.py::test_a PASSED*",
        ]
    )
    result.stdout.fnmatch_lines(
        [
            "*==== 6 passed in*", # this is in the summary line
        ]
    )
 
 
```

as we see in test_result.png, we have 3 passed which is verified with `result.assert_outcomes(passed=3)` and we can also search the -v output for items using the wildcard `result.stdout.fnmatch_lines()` with `"*==== 3 passed in*"` for example.