
https://docs.pytest.org/en/7.4.x/how-to/parametrize.html

## Passing test

`python -m pytest -s --stringinput="hello" --stringinput="world" .\tests\tests_05_generate_param_data\02_cli_options\`

## Failing test

`python -m pytest -s --tb=no --stringinput="!" .\tests\tests_05_generate_param_data\02_cli_options\`

## Skipped test

If you don’t specify a stringinput it will be SKIPPED because metafunc.parametrize() will be called with an empty parameter list:

`python -m pytest -vs  .\tests\tests_05_generate_param_data\02_cli_options\ --tb=no`

