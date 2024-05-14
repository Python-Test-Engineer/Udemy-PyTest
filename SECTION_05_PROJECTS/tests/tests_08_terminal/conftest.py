import os
import random
import pytest

from pyboxen import boxen

from rich.console import Console

console = Console()


# https://docs.pytest.org/en/latest/reference/reference.html#pytest.hookspec.pytest_report_teststatus
# This adds icons to test result.
# I can only get it to work with passed and failed but xfail should be possible.
@pytest.hookimpl
def pytest_report_teststatus(report, config):
    if report.when == "call" and report.passed:
        return report.outcome, "T", ("✅")
    if report.when == "call" and report.failed:
        return report.outcome, "E", ("❌")
    # Handle xfailed and xpassed
    if hasattr(report, "wasxfail"):
        if report.skipped:
            return "xfailed", "x", ("XFAIL ✅")
        elif report.passed:
            return "xpassed", "x", ("XPASS ❌")
        else:
            return "", "", ""
    if report.when in ("setup", "teardown", "call") and report.skipped:
        return report.outcome, "s", "SKIPPED 🙄 "


def pytest_report_header(config):
    if config.getoption("verbose") > 0:
        output = "📝 ✅ pytest_report_header ❌"
        print(
            boxen(
                output,
                title="[blue]We can add a report header[/] [black on cyan] here... [/]",
                subtitle="pytest_report_header",
                subtitle_alignment="left",
                color="green",
                padding=1,
            )
        )
        return [
            f"\n📝 This is in a hook with a random number {random.randint(10000, 99999)}",
            "🙋 pytest_report_header data\n",
        ]


def pytest_runtest_call(item):
    # Called to run the test for test item (the call phase).
    # https://docs.pytest.org/en/7.1.x/reference/reference.html?highlight=pytest%20item#pytest.Item.add_report_section
    item.add_report_section("call", "custom", "content")


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    reports = terminalreporter.getreports("")
    # this holds record_property custom data
    output = [report.user_properties for report in reports]
    output2 = [report.sections for report in reports]

    content = os.linesep.join(
        f"{key}: {value}" for report in reports for key, value in report.user_properties
    )

    # content = ("").join(str(output + output2))

    if content:
        # https://docs.pytest.org/en/7.1.x/reference/reference.html?highlight=record_property#std-fixture-record_property
        terminalreporter.ensure_newline()
        terminalreporter.section("record_property", sep="-", red=True, bold=True)
        terminalreporter.line(content)

        terminalreporter.ensure_newline()
        terminalreporter.section(
            "Tests took place in", sep="=", blue=True, bold=True, fullwidth=None
        )
        # print(f"\nROOTDIR: {config.rootdir}\n")
        print("\n")
        output = f"\n✅ ROOTDIR: {config.rootdir} 🆗\n"
        print(
            boxen(
                output,
                title="[blue]Tests were in directory:[/]",
                subtitle="END OF DEMO",
                subtitle_alignment="left",
                color="green",
                padding=1,
            )
        )
