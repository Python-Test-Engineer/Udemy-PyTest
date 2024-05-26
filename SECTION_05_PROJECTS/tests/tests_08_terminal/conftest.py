import os
import random
import pytest

from pyboxen import boxen

from rich.console import Console

console = Console()


def pytest_configure(config):

    config.my_global_value = "✅ MY GLOBLAL VALUE ✅"


# report is report for a single test
@pytest.hookimpl
def pytest_report_teststatus(report, config):
    # order seems to matter as the xpassed did not work when after passed
    # Handle xfailed and xpassed
    if hasattr(report, "wasxfail"):
        if report.skipped:
            # short desc, long desc
            return "xfailed", "x", ("XFAIL ✅")
        elif report.passed:
            return "xpassed", "❌", ("XPASS ✅❌")
        else:
            return "", "", ""
    if report.when in ("setup", "teardown", "call") and report.skipped:
        return report.outcome, "s", "SKIPPED 🙄 "
    if report.when == "call" and report.passed:
        # we can style the text in long formats. Just color and bold no italic
        # does not work for error?
        return report.outcome, "T", ("PASSED ✅", {"blue": True, "bold": True})
    if report.when == "call" and report.failed:
        return report.outcome, "E", ("ERROR ❌")


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
        # We can add another item the report header but it is useful to see that we get a return value that automatically gets added to the terminal report
        return [
            f"\n📝 This is in a pytest_report_header hook and it can access the config built in fixture: {config.my_global_value}"
        ]


def pytest_runtest_call(item):
    # Called to run the test for test item (the call phase).
    # https://docs.pytest.org/en/7.1.x/reference/reference.html?highlight=pytest%20item#pytest.Item.add_report_section
    item.add_report_section("call", "custom", "content")


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    reports = terminalreporter.getreports("")
    # this holds record_property custom data
    # output = [report.user_properties for report in reports]
    # output2 = [report.sections for report in reports]

    content = os.linesep.join(
        f"{key}: {value}" for report in reports for key, value in report.user_properties
    )

    if content:
        # https://docs.pytest.org/en/7.1.x/reference/reference.html?highlight=record_property#std-fixture-record_property
        terminalreporter.ensure_newline()
        terminalreporter.section("record_property", sep="-", red=True, bold=True)
        terminalreporter.line(content)
        print("\n")
        terminalreporter.ensure_newline()
        terminalreporter.section(
            f"Our custom test results section with exit status: {exitstatus}",
            sep="=",
            blue=True,
            bold=True,
            fullwidth=None,
        )

        print("\n")
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

        output = f"Total tests: {total_tests}\n"
        output += f"Passed: {passed_tests}\n"
        output += f"Failed: {failed_tests}\n"
        output += f"Skipped: {skipped_tests}\n"
        output += f"Error: {error_tests}\n"
        output += f"xfailed: {xfailed_tests}\n"
        output += f"xpassed: {xpassed_tests}\n"
        print(
            boxen(
                output,
                title="[blue]Test results:[/]",
                subtitle="END OF DEMO",
                subtitle_alignment="left",
                color="green",
                padding=1,
            )
        )
