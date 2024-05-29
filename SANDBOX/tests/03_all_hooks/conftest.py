import os
import random
import pytest
from datetime import datetime
from _pytest.nodes import Item
from _pytest.runner import CallInfo

from pyboxen import boxen

from rich.console import Console

console = Console()
report_date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
FILENAME = f"report_{report_date}.csv"

# We must create stash keys
been_there_key = pytest.StashKey[bool]()
done_that_key = pytest.StashKey[str]()
test_stash_key = pytest.StashKey[str]()
doneloaded_in_config_hook_from_filethat_key = pytest.StashKey[str]()


def pytest_configure(config):

    output1 = str(dir(config))
    # Get the path to the text file in the same directory as conftest.py
    current_directory = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_directory, "config.txt")

    # Read the content of the file and store it in the pytest config object
    with open(input_file_path, "r") as file:
        file_content = file.read()
    config._input_file_content = (
        file_content  # Store the file content in the pytest config object
    )

    # print(
    #     boxen(
    #         output1,
    #         title="Config contents",
    #         subtitle="Config contents",
    #         subtitle_alignment="left",
    #         color="purple4",
    #         padding=1,
    #     )
    # )


def pytest_runtest_setup(item: pytest.Item) -> None:
    item.stash[been_there_key] = True
    item.stash[done_that_key] = "no"
    item.stash[test_stash_key] = "$value from test_stash.py$"


# https://docs.pytest.org/en/latest/reference/reference.html#pytest.hookspec.pytest_report_teststatus
@pytest.hookimpl
def pytest_report_teststatus(report, config):
    if report.when == "call" and report.passed:
        return report.outcome, "T", ("✅")
    if report.when == "call" and report.failed:
        return report.outcome, "E", ("❌")


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
