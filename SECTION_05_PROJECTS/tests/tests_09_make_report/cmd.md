python -m pytest -v .\tests\tests_04_filter_tests\python -m pytest -vs --tb=no .\tests\tests_01_make_report\

python -m pytest -vs .\tests\tests_09_make_report\test_functions.py::test_fn_example6_xfail_passes --tb=no

--tb=no supresses output if there is an error

https://stackoverflow.com/questions/77485901/pytest-how-to-find-the-test-result-after-a-test

xfail = rep.outcome == 'skipped' and hasattr(rep, 'wasxfail')

    symbol_passed: str = "✓"
    symbol_skipped: str = "s"
    symbol_failed: str = "⨯"
    symbol_failed_not_call: str = "ₓ"
    symbol_xfailed_skipped: str = "x"
    symbol_xfailed_failed: str = "X"


def pytest_report_teststatus(report: BaseReport) -> Optional[Tuple[str, str, str]]:
    if not IS_SUGAR_ENABLED:
        return None

    if report.passed:
        letter = colored(THEME.symbol_passed, THEME.success)
    elif report.skipped:
        letter = colored(THEME.symbol_skipped, THEME.skipped)
    elif report.failed:
        letter = colored(THEME.symbol_failed, THEME.fail)
        if report.when != "call":
            letter = colored(THEME.symbol_failed_not_call, THEME.fail)
    elif report.outcome == "rerun":
        letter = colored(THEME.symbol_rerun, THEME.rerun)
    else:
        letter = colored(THEME.symbol_unknown, THEME.unknown)

    if hasattr(report, "wasxfail"):
        if report.skipped:
            return (
                "xfailed",
                colored(THEME.symbol_xfailed_skipped, THEME.xfailed),
                "xfail",
            )
        if report.passed:
            return (
                "xpassed",
                colored(THEME.symbol_xfailed_failed, THEME.xpassed),
                "XPASS",
            )

    return report.outcome, letter, report.outcome.upper()

