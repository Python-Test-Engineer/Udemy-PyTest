
## Passing test

`python -m pytest -s --stringinput="hello" --stringinput="world" .\tests\tests_05_generate_param_data\ex02_cli_options\`

## Failing test

`python -m pytest -s --stringinput="!" .\tests\tests_05_generate_param_data\ex02_cli_options\`

## Skipped test

If you don’t specify a stringinput it will be skipped because metafunc.parametrize() will be called with an empty parameter list:

python -m pytest -rs .\tests\tests_ex06_generate_param_data\ex02

