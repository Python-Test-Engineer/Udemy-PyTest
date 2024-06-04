


# Flit

flit build --format wheel or flit build --format=wheel

# Install .whl

pip install dist/pytest_sort-0.0.2-py2.py3-none-any.whl - your .whl file may have a different name so use that.

# Uninstall .whl file
pip uninstall dist/pytest_sort-0.0.2-py2.py3-none-any.whl

or

pip uninstall pytest-sort - or your plugin name

# Test sort functionality

python -m pytest -vs .\src\test_sort.py        => tests in order they are in file

python -m pytest -vs .\src\test_sort.py --desc => in descending order

python -m pytest -vs .\src\test_sort.py --asc  => in ascending order

we can get the --help
- python -m pytest -vs .\src\test_sort.py --help

# Pytester

We have four tests:

Test with -v --asc
- python -m pytest .\tests\test_plugin.py::test_sort_asc  

Test with -v --desc
- python -m pytest .\tests\test_plugin.py::test_sort_desc         

Test with --asc for limited console output
 - python -m pytest -vs .\tests\test_plugin.py::test_sort_asc_outcomes

Test --help
 - python -m pytest  -v .\tests\test_plugin.py::test_help
