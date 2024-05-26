The data folder is the location of data file data.txt with contents:

```
Apples
Bananas
Cherries
Lemons
Oranges
```

We use:

```
pytest_generate_tests(metafunc)
```
to dynamically add parameters.

In our test we use a fixture `initial_value` as we used `metafunc.parametrize("initial_value", data):` in our .

```
def test_read_from_file(initial_value):
    # get value from file
    result = initial_value
    assert result == initial_value


We can change source of data to reading a CSV file or geting data from the database.
```
 python -m pytest -s .\tests\tests_05_generate_param_data\03_data_from_file\ --input_file=.\tests\tests_05_generate_param_data\03_data_from_file\data\data.txt

```