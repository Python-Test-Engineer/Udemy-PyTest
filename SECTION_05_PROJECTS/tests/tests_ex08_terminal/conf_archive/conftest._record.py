import os


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    reports = terminalreporter.getreports("")
    content = os.linesep.join(
        f"{key}: {value}" for report in reports for key, value in report.user_properties
    )
    if content:
        terminalreporter.ensure_newline()
        terminalreporter.section("My custom summary", sep="-", blue=True, bold=True)
        terminalreporter.line(content)
