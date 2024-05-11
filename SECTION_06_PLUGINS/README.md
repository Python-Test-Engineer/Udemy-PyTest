# pytest-sort

We use a whl builder like flit to create pyproject.toml

It will need some changes so best to use a ready made template.

If you do use flit init, in [project] section, change this to pytest-sort notpytest_sort as PyPi prefers dashes:

[project]
name = "pytest-sort" 

Copy conftest.py local to pytest_sort.py as this is the plugin with rest of template. 

Remember, a plugin is just the hook code. `conftest.py` is a plugin but a local one. 

We need to test that the plugin does sort and we use the src to test this.

1. Copy conftest.py inot pytest_sort.py and add `__version__ = "0.0.1"`

To test src code before and after installation of our plugin:

`python -m pytest -vs .\src\test_sort.py`.

We get no sorting:
```
src/test_sort.py::test_s PASSED
src/test_sort.py::test_z PASSED
src/test_sort.py::test_a PASSED
src/test_sort.py::test_y PASSED
src/test_sort.py::test_x PASSED
src/test_sort.py::test_r PASSED
```
2. We need to build a `.whl` file as this is distributable and is what is on PyPi when we use `pip install <plugin>`.


We use `flit build --format=wheel` to build a whl file which we then need to install so that our plugin is active:

`pip install .\dist\pytest_sort-0.0.1-py3-none-any.whl` (--force if already one there)

Once we install our plugin, we get test sorted alphabetically

```
src/test_sort.py::test_a PASSED
src/test_sort.py::test_r PASSED
src/test_sort.py::test_s PASSED
src/test_sort.py::test_x PASSED
src/test_sort.py::test_y PASSED
src/test_sort.py::test_zPASSED
```
and with the --desc flag get the reverse:

```
src/test_sort.py::test_z PASSED
src/test_sort.py::test_y PASSED
src/test_sort.py::test_x PASSED
src/test_sort.py::test_s PASSED
src/test_sort.py::test_r PASSED
src/test_sort.py::test_a PASSED
```

as well as 
```
===> DESC: True
```

We can confirm our plugin works in terms of sorting.

Our end user will install our plugin and then run their tests, getting tests sorted alphabetically in either asc or desc order depending on whether the --desc flag is supplied.

We need to test this funcionality and we do this wwith Pytester which is built to test plugins.

Thus we have a tests folder to test the plugin operation.

3. Create a conftest.py file in tests and add
```
pytest_plugins = ["pytester"]
```

We now can run tests.

We need to test what happens if once installed we run our tests with no flag and with the flag.

`test_plugin.py` has two tests:
One to run tests and we add th `-v` flag so we can see results.
Another to test with the flag `-v --desc `. We pass them in as separate arguments - see file.


We then run two tests from test_plugin.py to test the plugin itself not the src code. The end user will just run their test files with --desc or not. The plugin will then sort one way or the other.

It is the same as we saw in the project.

```
result = pytester.runpytest("-v")
```
and we test that the output is ascending

```
result = pytester.runpytest("-v","--desc")
```

We get:


```
src/test_sort.py::test_a PASSED
src/test_sort.py::test_r PASSED
src/test_sort.py::test_s PASSED
src/test_sort.py::test_x PASSED
src/test_sort.py::test_y PASSED
src/test_sort.py::test_zPASSED
```
and with the --desc flag get the reverse:

```
src/test_sort.py::test_z PASSED
src/test_sort.py::test_y PASSED
src/test_sort.py::test_x PASSED
src/test_sort.py::test_s PASSED
src/test_sort.py::test_r PASSED
src/test_sort.py::test_a PASSED
```

as well as 
```
===> DESC: True
```
and we see the reverse order and the presence of `===> DESC: `. We don't need to check for True as the presence of this indicates the flag was set.

We also get 6 tests passed.

These are then the tests. Do we get 6 lines of tests and is the total passed == 6.

```    result.stdout.fnmatch_lines(
        [
            "*test_sort.py::test_a PASSED*",
            "*test_sort.py::test_r PASSED*",
            "*test_sort.py::test_s PASSED*",
            "*test_sort.py::test_x PASSED*",
            "*test_sort.py::test_y PASSED*",
            "*test_sort.py::test_z PASSED*",
        ]
    )
```
fnmatch_lines is a way of seein if the supplied string is present and we use * wildcards either side.

```
result.assert_outcomes(passed=6)
```
tests if we do in fact have 6 passed tests.

If these tests pass then we can feel assured that our plugin works satisfactorily as a plugin and we have also tested the functionality of the plugin code.

If you change the plugin_sort.py or any other plugin file, uninstall the plugin, delete the dist folder and then rebuild and install.

To uninstall the plugin:

`pip uninstall .\dist\pytest_sort-0.0.1-py3-none-any.whl`