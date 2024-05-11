import pytest
from pyboxen import boxen
import os
import random


def pytest_report_teststatus(report, config):
    messages = (
        "Egg and bacon",
        "Egg, sausage and bacon",
        "Egg and Spam",
        "Egg, bacon and Spam",
    )

    if report.when == "teardown":
        line = f'{report.nodeid} says:\t"{random.choice(messages)}"'
        report.sections.append(("My custom section\n", line))


@pytest.hookimpl(hookwrapper=True)
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    # duration = time.time() - terminalreporter._sessionstarttime
    yield

    passed_tests = len(terminalreporter.stats.get("passed", ""))
    failed_tests = len(terminalreporter.stats.get("failed", ""))
    skipped_tests = len(terminalreporter.stats.get("skipped", ""))
    error_tests = len(terminalreporter.stats.get("error", ""))
    xfailed_tests = len(terminalreporter.stats.get("xfailed", ""))
    xpassed_tests = len(terminalreporter.stats.get("xpassed", ""))

    total_tests = (
        passed_tests
        + failed_tests
        + skipped_tests
        + error_tests
        + xfailed_tests
        + xpassed_tests
    )

    pass_percentage = (
        0 if total_tests == 0 else round(passed_tests * 100.0 / total_tests, 2)
    )
    print(f"Total Tests: {total_tests}")  # total_tests,
    print(
        passed_tests,
        failed_tests,
        skipped_tests,
        error_tests,
        xfailed_tests,
        xpassed_tests,
        f"\nPercentage of tests: {pass_percentage}%",  #  pass_percentage,
    )

    reports = terminalreporter.getreports("")
    for report in reports:
        print(report.sections)
    content = os.linesep.join(
        text for report in reports for secname, text in report.sections
    )
    if content:
        terminalreporter.ensure_newline()
        terminalreporter.section("My custom section", sep="-", blue=True, bold=True)
        terminalreporter.line(content)
