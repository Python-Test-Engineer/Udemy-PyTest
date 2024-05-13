import os
import random
import pytest

from pyboxen import boxen

from rich.console import Console

console = Console()


def pytest_configure(config):
    # we need to add these markers to avoid error if strict-markers is used.
    config.addinivalue_line("markers", "first: run these tests first")
    config.addinivalue_line("markers", "last: run these tests last")

    config.input_file_content = "input_file_content no leading _"
    config.my_global_value = "Shared Value"
    # This is available via the request built in fixture so can be accessed in tests
    # global_value = request.config.my_global_value

    output1 = str(dir(config))
    # Get the path to the text file in the same directory as conftest.py
    current_directory = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_directory, "./data/input.txt")

    # Read the content of the file and store it in the pytest config object
    with open(input_file_path, "r") as file:
        file_content = file.read()

    # _input_file_content seems to be special in that in can be a fixture.abs
    # underscore does not work with my_global_value
    config._input_file_content = file_content


# A pytest hook to for modifying collected items
def pytest_collection_modifyitems(items, config):
    first_tests = []
    last_tests = []
    remaining_tests = []
    # get all the markers for a test
    for test in items:
        list_markers = [
            str(getattr(test.own_markers[j], "name"))
            for j in range(len(test.own_markers))
        ]
        # add items to first_tests and last_tests if they have the first or last marker
        if "first" in list_markers:
            first_tests.append(test)
        elif "last" in list_markers:
            last_tests.append(test)
        else:
            remaining_tests.append(test)

    items[:] = first_tests + remaining_tests + last_tests


def pytest_generate_tests(metafunc):
    if "dataset" in metafunc.fixturenames:
        metafunc.parametrize("dataset", range(10))
    if "data_tuple" in metafunc.fixturenames:
        data = [(x, x + 1) for x in range(10)]
        metafunc.parametrize("data_tuple", data)
    if "list1" in metafunc.fixturenames:
        data = [1, 2, 3]
        metafunc.parametrize("list1", data)
    if "list2" in metafunc.fixturenames:
        data = [3, 6, 9]
        metafunc.parametrize("list2", data)


# https://docs.pytest.org/en/latest/reference/reference.html#pytest.hookspec.pytest_report_teststatus
# This adds icons to test result.
# I can only get it to work with passed and failed but xfail should be possible.
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

        output = f"✅ ROOTDIR: {config.rootdir} 🆗"
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