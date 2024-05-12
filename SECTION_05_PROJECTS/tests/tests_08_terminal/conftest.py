import os
import random
import pytest


@pytest.hookimpl
def pytest_report_teststatus(report, config):
    if report.when == "call" and report.passed:
        return report.outcome, "T", ("😀", {"yellow": True})
    if report.when == "call" and report.failed:
        return report.outcome, "E", "😔"


def pytest_runtest_call(item):
    item.add_report_section("call", "custom", "content")


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    reports = terminalreporter.getreports("")
    content = os.linesep.join(
        f"{key}: {value}" for report in reports for key, value in report.user_properties
    )
    if content:
        terminalreporter.ensure_newline()
        terminalreporter.section("record_property", sep="-", red=True, bold=True)
        terminalreporter.line(content)
    content = os.linesep.join(
        text for report in reports for secname, text in report.sections
    )
    if content:
        terminalreporter.ensure_newline()
        terminalreporter.section(
            "Tests took place in", sep="=", blue=True, bold=True, fullwidth=None
        )
        print(f"\nROOTDIR: {config.rootdir}\n")
