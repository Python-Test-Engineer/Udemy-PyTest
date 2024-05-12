import os
import random
import pytest

from pyboxen import boxen

from rich.console import Console

console = Console()


# https://docs.pytest.org/en/latest/reference/reference.html#pytest.hookspec.pytest_report_teststatus
@pytest.hookimpl
def pytest_report_teststatus(report, config):
    if report.when == "call" and report.passed:
        return report.outcome, "T", ("✅")
    if report.when == "call" and report.failed:
        return report.outcome, "E", ("❌")
    # if report.when == "call" and report.xfail:
    #     return report.outcome, ".", ("✅")


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


# 🆗
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
