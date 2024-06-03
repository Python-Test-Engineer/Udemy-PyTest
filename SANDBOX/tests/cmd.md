
python -m pytest -vs .\tests\01_check_setup\test_03_logging.py


python -m pytest -vs .\tests\02_sandbox\test_functions.py::test_fn_example1_pass
python -m pytest -vs .\tests\02_sandbox\test_functions.py::test_fn_example1_pass --debug

470, 750,

```
def pytest_runtest_logreport(report):
    if report.failed:
        print(f"\n[pytest_runtest_logreport]: {report}\n")
    print(f"\n[pytest_runtest_logreport]: {report}\n")
```
runs 3 times for setup, call, teardown

outputs:
```
tests/02_sandbox/test_functions.py::test_fn_example1_pass
[pytest_runtest_logreport]: <TestReport 'tests/02_sandbox/test_functions.py::test_fn_example1_pass' when='setup' outcome='passed'>

PASSED
[pytest_runtest_logreport]: <TestReport 'tests/02_sandbox/test_functions.py::test_fn_example1_pass' when='call' outcome='passed'>


[pytest_runtest_logreport]: <TestReport 'tests/02_sandbox/test_functions.py::test_fn_example1_pass' when='teardown' outcome='passed'>
```

```
def pytest_report_teststatus(report):
    if report.passed:
        print(f"\n[pytest_report_teststatus]: {report}\n")
    print(f"\n[pytest_report_teststatus]: {report}\n")
```
gives:

```
tests/02_sandbox/test_functions.py::test_fn_example1_pass
[pytest_report_teststatus]: <TestReport 'tests/02_sandbox/test_functions.py::test_fn_example1_pass' when='setup' outcome='passed'>


[pytest_report_teststatus]: <TestReport 'tests/02_sandbox/test_functions.py::test_fn_example1_pass' when='setup' outcome='passed'>


[pytest_report_teststatus]: <TestReport 'tests/02_sandbox/test_functions.py::test_fn_example1_pass' when='call' outcome='passed'>


[pytest_report_teststatus]: <TestReport 'tests/02_sandbox/test_functions.py::test_fn_example1_pass' when='call' outcome='passed'>

PASSED
[pytest_report_teststatus]: <TestReport 'tests/02_sandbox/test_functions.py::test_fn_example1_pass' when='teardown' outcome='passed'>


[pytest_report_teststatus]: <TestReport 'tests/02_sandbox/test_functions.py::test_fn_example1_pass' when='teardown' outcome='passed'>
```

```
def pytest_make_collect_report(collector):
    print(f"\n[pytest_make_collect_report]: {collector.parent}\n")
```

gives

```
collecting ... NB usually get collected 1
[pytest_make_collect_report]: <Dir tests>

[pytest_make_collect_report]: <Dir 02_sandbox>

collected 1 item                                                                                                     
tests/02_sandbox/test_functions.py::test_fn_example1_pass PASSED
```
