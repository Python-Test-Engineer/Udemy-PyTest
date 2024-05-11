# pytest-sort

We use a whl builder like flit to create pyproject.toml

in [project] section, change this to pytest-sort notpytest_sort as PyPi prefers dashes:

[project]
name = "pytest-sort" 

Copy conftest.py local to pytest_sort.py as this is the plugin with rest of template. 

Remember, a plugin is just the hook code. `conftest.py` is a plugin but a local one. 

We need to test that the plugin does sort and we use the src to test this.

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

We use `flit build --format=wheel` to build a whl file which we then need to install so that our plugin is active:

`pip install .\dist\pytest_sort-0.0.1-py3-none-any.whl` (--force if already one there)

We then run two tests from test_plugin.py to test the plugin itself not the src code. The end user will just run their test files with --desc or not. The plugin will then sort one way or the other.

It is the same as we saw in the project.

```
result = pytester.runpytest("-v")
```
and we test that the output is ascending

```
result = pytester.runpytest("-v","--desc")
```
and we see the reverse order and the presence of `===> DESC: `. We don't need to check for True as the presence of this indicates the flag was set.

We also check 6 tests passed.

If you change the plugin_sort.py or any other plugin file, uninstall the plugin, delete the dist folder and then rebuild and install.

To uninstall the plugin:

`pip uninstall .\dist\pytest_sort-0.0.1-py3-none-any.whl`