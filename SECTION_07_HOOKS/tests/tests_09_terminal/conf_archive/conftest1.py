import os
import random


def pytest_runtest_call(item):
    item.add_report_section("call", "custom", " [ Run      ]  " + str(item))


def pytest_report_teststatus(report, config):
    # print(">>> outcome:", report.outcome)

    if report.when == "call":
        # line = f' [ Run      ]  {report.nodeid}'
        # report.sections.append(('ChrisZZ', line))
        if report.outcome == "failed":
            line = f" [   FAILED ]  {report.nodeid}"
            report.sections.append(("failed due to", line))

    if report.when == "teardown":
        if report.outcome == "passed":
            line = f" [       OK ]  {report.nodeid}"
            report.sections.append(("ChrisZZ", line))


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    reports = terminalreporter.getreports("")
    content = os.linesep.join(
        text for report in reports for secname, text in report.sections
    )
    if content:
        terminalreporter.ensure_newline()
        # terminalreporter.section('', sep=' ', green=True, bold=True)
        # terminalreporter.section('My custom section2', sep='------]', green=True, bold=True, fullwidth=None)
        terminalreporter.line(content)

    content = os.linesep.join(
        f"{key}: {value}" for report in reports for key, value in report.user_properties
    )
    if content:
        terminalreporter.ensure_newline()
        terminalreporter.section(
            "report.user_properties", sep="-", blue=True, bold=True
        )
        terminalreporter.line(content)
