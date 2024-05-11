import pytest
import time
from pyboxen import boxen
import os
import random


def pytest_addoption(parser):
    group = parser.getgroup("email")
    group.addoption(
        "--euname",
        action="store",
        dest="euname",
        default=None,
        help="Email id (for auth)",
    )
    group.addoption(
        "--epwd", action="store", dest="epwd", default=None, help="Email password"
    )
    group.addoption(
        "--efrom",
        action="store",
        dest="efrom",
        default=None,
        help="Email sender (if missing will use euname)",
    )
    group.addoption(
        "--eto", action="store", dest="eto", default=None, help="Email recipients"
    )

    group.addoption(
        "--esend",
        action="store",
        dest="esend",
        default="False",
        help="Sends email when --esend is True",
    )

    group.addoption(
        "--esubject",
        action="store",
        dest="esubject",
        default="Pytes Execution Result",
        help="Subject of email",
    )

    group.addoption(
        "--eorg",
        action="store",
        dest="eorg",
        default="Pytest Email",
        help="Your organization name",
    )

    group.addoption(
        "--esmtp",
        action="store",
        dest="esmtp",
        default="smtp.gmail.com:587",
        help="Email server smtp",
    )

    group.addoption("--eanon", action="store_true", help="Do not use SMTP AUTH")


# @pytest.fixture
# def base_url(request):
# #     return request.config.getoption("--base-url")
# @pytest.fixture
# def command_line_args(request):
#     args = {}
#     args["base_url"] = request.config.getoption("--base-url")
#     args["username"] = request.config.getoption("--username")
#     args["password"] = request.config.getoption("--password")
#     return args


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

    # print(str(dir(terminalreporter)))

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

    # print("showfspath: " + str(terminalreporter.showfspath))
    print("\nconfig.option.eanon: " + str(config.option.eanon) + "\n")
    print(
        boxen(
            str(config.option.eanon),
            title="config.option.eanon",
            subtitle="config.option.eanon",
            subtitle_alignment="center",
            color="blue",
            padding=1,
        )
    )

    reports = terminalreporter.getreports("")
    content = os.linesep.join(
        text for report in reports for secname, text in report.sections
    )
    if content:
        terminalreporter.ensure_newline()
        terminalreporter.section("My custom section", sep="-", blue=True, bold=True)
        terminalreporter.line(content)


def pytest_report_teststatus(report, config):
    messages = (
        "Egg and bacon",
        "Egg, sausage and bacon",
        "Egg and Spam",
        "Egg, bacon and Spam",
    )

    if report.when == "teardown":
        line = f'{report.nodeid} says:\t"{random.choice(messages)}"'
        report.sections.append(("My custom section", line))
