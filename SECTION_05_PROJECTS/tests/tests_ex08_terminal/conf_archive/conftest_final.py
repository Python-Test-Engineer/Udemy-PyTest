import os
import random


def pytest_runtest_call(item):
    item.add_report_section("call", "custom", " [ Run      ]  " + str(item))


def pytest_report_teststatus(report, config):
    # print(">>> outcome:", report.outcome)

    if report.when == "call":
        print(f"\n>>> Result of test {report.nodeid} is {report.outcome.upper()}")
        #   print(report.keywords.keys())

        all_keywords = [str(x) for x in report.keywords]
        print("KEYWORDS:", " - ".join(all_keywords))
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
        terminalreporter.section("", sep=" ", green=True, bold=True)
        terminalreporter.section(
            "CUSTOM SUMMARY", sep="= = ", green=True, bold=True, fullwidth=None
        )
        terminalreporter.line(content)

    print("\n")
    content = os.linesep.join(
        f"{key}: {value}" for report in reports for key, value in report.user_properties
    )
    if content:

        terminalreporter.ensure_newline()
        terminalreporter.section(
            "report.user_properties", sep="-", blue=True, bold=True
        )
        terminalreporter.line(content)
