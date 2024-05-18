python -m pytest -vs --tb=no .\tests\tests_01_make_report\


--tb=no supresses output if there is an error

https://stackoverflow.com/questions/77485901/pytest-how-to-find-the-test-result-after-a-test

xfail = rep.outcome == 'skipped' and hasattr(rep, 'wasxfail')