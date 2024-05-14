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

# We must create stash keys
been_there_key = pytest.StashKey[bool]()
done_that_key = pytest.StashKey[str]()
test_stash_key = pytest.StashKey[str]()


def pytest_runtest_setup(item: pytest.Item) -> None:
    item.stash[been_there_key] = True
    item.stash[done_that_key] = "no"
    item.stash[test_stash_key] = "$value from test_stash.py$"


def pytest_runtest_teardown(item: pytest.Item) -> None:
    item.stash[done_that_key] = "yes!"


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
            output1 = "I run for every test"
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
            list_markers = [
                str(getattr(item.own_markers[j], "name"))
                for j in range(len(item.own_markers))
            ]
            all_markers = ("-").join(list_markers)

            with open(FILENAME, "a") as f:  # we need 'a' as it adds each item
                f.write(
                    f"{item.name}|{test_id}|{test_outcome}|{test_duration}|{all_markers}|{ item.stash[test_stash_key]}\n"
                )

        except Exception as e:
            print("\nERROR:", e)
