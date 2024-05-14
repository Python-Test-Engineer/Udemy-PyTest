import pytest
import random
from datetime import datetime
from _pytest.nodes import Item
from _pytest.runner import CallInfo
from pyboxen import boxen

from rich.console import Console

console = Console()


# https://rich.readthedocs.io/en/stable/appendix/colors.html

# Let's define our failures.txt as a constant as we will need it later

rnd = random.randint(100_000, 999_999)
report_date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
FILENAME = f"report_store_hook_results_{report_date}.csv"

print("\n\n")

# We can have a global key that will store the plugin/conftest name
# We must create stash keys and it is in a per test basis so need a hook with item
which_plugin = pytest.StashKey[str]()


def pytest_runtest_setup(item: pytest.Item) -> None:

    item.stash[which_plugin] = "$tests_07_store_hook_results$"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: Item, call: CallInfo):

    outcome = yield  # Run all other pytest_runtest_makereport non wrapped hooks
    report = outcome.get_result()

    if call.when == "call":
        outcome = call.excinfo
        try:
            # Access the test outcome (passed, failed, etc.)
            test_outcome = "^!!!FAILED!!!^" if outcome else "-PASSED-"
            # Access the test duration
            test_duration = call.duration
            # Access the test ID (nodeid)
            test_id = item.nodeid
            list_markers = [
                str(getattr(item.own_markers[j], "name"))
                for j in range(len(item.own_markers))
            ]
            all_markers = ("-").join(list_markers)
            if all_markers == "":
                all_markers = "NONE"
            output1 = f"I run for every test and my markers are:\n {all_markers}"

            print("\n")
            print(
                boxen(
                    output1,
                    title="pytest_runtest_makereport Item",
                    subtitle="pytest_runtest_makereport Item",
                    subtitle_alignment="left",
                    color="green",
                    padding=1,
                )
            )

            with open(FILENAME, "a") as f:  # we need 'a' as it adds each item
                f.write(
                    f"{item.name}|{test_id}|{test_outcome}|{test_duration}|{all_markers}|{ item.stash[which_plugin]}\n"
                )

        except Exception as e:
            print("\nERROR:", e)
