
## Passing test

python -m pytest -s --stringinput="hello" --stringinput="world" .\tests\tests_ex06_generate_param_data\ex02

## Failing test

python -m pytest -s --tb=no --stringinput="!"  .\tests\tests_ex06_generate_param_data\ex02

--tb-no is no traceback on failure

## Skipped test

If you don’t specify a stringinput it will be skipped because metafunc.parametrize() will be called with an empty parameter list:

python -m pytest -rs .\tests\tests_ex06_generate_param_data\ex02

