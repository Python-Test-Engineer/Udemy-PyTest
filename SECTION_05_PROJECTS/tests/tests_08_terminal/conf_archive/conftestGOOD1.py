import os
import random


def pytest_runtest_call(item):
    item.add_report_section("call", "custom", " [ Run      ]  " + str(item))


def pytest_report_teststatus(report, config):

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
            report.sections.append(("", line))


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    reports = terminalreporter.getreports("")
    content = os.linesep.join(
        text for report in reports for secname, text in report.sections
    )
    if content:
        terminalreporter.ensure_newline()
        terminalreporter.section(
            "Tests took place in", sep="=", green=True, bold=True, fullwidth=None
        )
        print(f"\nROOTDIR: {config.rootdir}\n")
        terminalreporter.section("", sep="=", green=True, bold=True, fullwidth=None)
        terminalreporter.section(
            "CUSTOM SECTION", sep=" X O ", blue=True, bold=True, fullwidth=None
        )
        terminalreporter.line(content)
