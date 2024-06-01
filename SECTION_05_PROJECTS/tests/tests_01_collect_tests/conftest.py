from datetime import datetime
import pytest

# timestamp our ouput files
report_date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
FILENAME = f"collect_tests_{report_date}.txt"
print("\n\n")


def pytest_collection_modifyitems(items):

    print("\n")
    for test in items:
        # keyword order is:
        # test name - markers - module name - folder - parent folder/grandparent folder - root folder
        # we have no markers in tests_01_collect_tests
        all_keywords = [str(x) for x in test.keywords]
        all_keywords = ("|").join(all_keywords)

        print(f"KEYWORDS: \n{all_keywords}\n")
        # we can produce a --collect-only type of report of all test that we are going to run
        list_markers = [
            str(getattr(test.own_markers[j], "name"))
            for j in range(len(test.own_markers))
        ]
        all_markers = ("-").join(list_markers)
        print(f"MARKERS: \n{all_markers}")
        print("-------------------------------")
        with open(f"{FILENAME}", "a") as f:
            f.write(f"{test.name}|{all_keywords}\n")
    # we don't want to run tests...
    pytest.exit("Collect finished", returncode=0)


print("\n\n")
