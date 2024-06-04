# Make a plugin called pytest-sort

`pip install flit` - docs at https://flit.pypa.io/en/stable/

minimum files:
- plugin.py
- pyproject.toml - pyproject_minimal.toml has minimum needed. pyproject_base.toml has a fuller version.

Once a .whl file is used, it can be used `pip (un)install thewheel.whl` and it can also be uninstalled with `pip uninstall plugin-name`.


1. How do we make conftest.py distributable (and installable with pip install)?
2. Test it does sorting.
3. Test it for when user does `python -m pytest -vs --asc`.

We will use the plugin/conftest.py code of 'sort_by_testname' as our plugin. It has a CLI flags of --desc and --asc.

Out plugin will have the name pytest-sort as PyPi etc prefers '-' to '_' but it can be any name.

The conftest.py will be renamed to plugin_sort.py but we can have any name.
 and code so that you can see how to make changes for your own plugin.

  *Most of this is boiler plate code that we don't have to understand - we just need to know what is expected of us for plugin distribution to take place.*

We will use `flit` which is a lighter weight package manager as we want to make production of .whl files as easy as possible. .whl or wheel files will be explained a bit later...

What do we need to do to create and maintain a distributable plugin project/repo?

1. MANDATORY: We need to convert the conftest.py into a distributable version rather than asking users to put this file in their code.
2. OPTIONAL: We also need to manage our distributable plugin project.
3. OPTIONAL: We need to test that the plugin does what we want it to do, (sort by test name).
4. OPTIONAL: We also need to test that the plugin once installed by user sorts by test name and the --desc flag works. Once users have installed the plugin they will just use `python -m pytests` or `python -m pytest --desc or --asc`.


So we now have a plugin project to maintain.

## Building a .whl file.

To make some code distributable, we need to build a .whl file.

When we do `pip install pytest` for example, what this command is doing is downloading a .whl file and then behind the scenes doing `pip install the_dot_wheel.whl` file.

We will use a whl builder like flit to create this wheel file but whatever tool works best for you is fine.

Copy conftest.py local to pytest_sort.py as this is the plugin with rest of template. 

<!-- For Flit we need to add a version number in this file. (moved to pyproject.toml rather than dynamic). -->

Remember, a plugin is just the hook code. `conftest.py` is a plugin but a local one. 

Our plugin will be called pytest-sort, with a file called plugin_sort.py that has the code contents from the conftest.py file.

PyPi can accept plugin names with a '_' but prefers a '-' so that is why we have both pytest-sort and pytest_sort.

1. Copy conftest.py into pytest_sort.py.
2. Run `flit build --format wheel` or `flit build --format=wheel`.

This will give a .whl like `pytest_sort-0.0.2-py2.py3-none-any.whl` which can then be installed with `pip install pytest_sort-0.0.2-py2.py3-none-any.whl`


TESTING OUR PLUGIN:

To test src code before and after installation of our plugin we need to copy in our test we used previously. The plugin will still work regardless of testing as it is just the plugin_sort.py that does the work. However, it is good practice to have tests for mainatable plugins.

`python -m pytest -vs .\src\test_sort.py`.

This is just regular testing and is part of the plugin project.

We get no sorting:
```
src/test_sort.py::test_s PASSED
src/test_sort.py::test_z PASSED
src/test_sort.py::test_a PASSED
src/test_sort.py::test_y PASSED
src/test_sort.py::test_x PASSED
src/test_sort.py::test_r PASSED
```

Once we install our plugin, we get test sorted alphabetically

`python -m pytest -v --asc`


```
src/test_sort.py::test_1 PASSED      
src/test_sort.py::test_2 PASSED                     
src/test_sort.py::test_3 PASSED
src/test_sort.py::test_4 PASSED
src/test_sort.py::test_5 PASSED 
src/test_sort.py::test_6 PASSED 
```
and with the --desc flag ``python -m pytest -v --desc` we get the reverse:

```
src/test_sort.py::test_6 PASSED
src/test_sort.py::test_5 PASSED
src/test_sort.py::test_4 PASSED
src/test_sort.py::test_3 PASSED
src/test_sort.py::test_2 PASSED
src/test_sort.py::test_1 PASSED
```
as well as 
```
===> DESC: True
```
which we put in our test for illustrative purposes.

We can confirm our plugin works in terms of sorting with and without the --desc flag.

Our end user will install our plugin and then run their tests, getting tests sorted alphabetically in either asc or desc order depending on whether the --desc flag is supplied.

# Testing with Pyteser

We need to test this funcionality and we do this with Pytester which is built to test plugins. It comes with PyTest.

Thus we have a tests folder to test the plugin operation.

1. Create a conftest.py file in tests and add

```
pytest_plugins = ["pytester"]
```
so that we can use Pytester as it is disabled by default. We are testing the plugin as a unit now rather than its purpose of sorting by testname.

We now can run tests to very plugin useage by our user.

We need to test what happens if once installed we run our tests with no flag and with the flag.

`test_plugin.py` has two three:

One to run tests and we add the `-v --asc` flag so we can see test ouput.

Another to test with the flag `-v --desc `. We pass them in as separate arguments - see file.

Another test_sort_asc_outcomes using just `--asc` with less console ouput.

To test the plugin with pytester, we run:

`python -m pytest -vs .\tests\test_plugin.py`

We can also run `python -m pytest -vs .\tests\test_plugin.py::test_sort_asc_outcomes` which will not have output but just asserts if two tests pass.

We then run two individual tests from test_plugin.py to test the plugin itself not the src code. The end user will just run their test files with --desc or not. The plugin will then sort one way or the other.

It is the same as we saw in the project.

We do this:
```
result = pytester.runpytest("-v --asc")
```
and we test that the output is ascending

```
src/test_sort.py::test_1 PASSED
src/test_sort.py::test_2 PASSED
src/test_sort.py::test_3 PASSED
src/test_sort.py::test_4 PASSED
src/test_sort.py::test_5 PASSED
src/test_sort.py::test_6 PASSED
```
and with the --desc flag get the reverse:

```
src/test_sort.py::test_6 PASSED
src/test_sort.py::test_5 PASSED
src/test_sort.py::test_4 PASSED
src/test_sort.py::test_3 PASSED
src/test_sort.py::test_2 PASSED
src/test_sort.py::test_1 PASSED
```

as well as 
```
===> DESC: True
```
and we see the reverse order and the presence of `===> DESC: `. 

We also get 6 tests passed.

These are then the tests:

Do we get 6 lines of tests and is the total of `passed test == 6`.

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
fnmatch_lines is a way of seeing if the test ouput contains a line with certain text. We use * wild cards to focus on a what we need to see.

```
result.assert_outcomes(passed=6)
```
tests if we do in fact have 6 passed tests.
