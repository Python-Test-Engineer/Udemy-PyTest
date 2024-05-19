from pyboxen import boxen

from rich.console import Console

console = Console()


# A pytest hook to for modifying collected items
def pytest_collection_modifyitems(items, config):

    selected = []
    deselected = []
    for test in items:
        # get a string of markers separated with '-'
        list_markers = [
            str(getattr(test.own_markers[j], "name"))
            for j in range(len(test.own_markers))
        ]
        all_markers = ("-").join(list_markers)
        print("markers: ", all_markers)
        print("-----------")
        # for educational purposes we will also get all the keywords. We could then filter based on kewyords - see KEYWORDS.md in this folder if you need refreshing.
        all_keywords = [str(x) for x in test.keywords]
        all_keywords = (" - ").join(all_keywords)
        output = f"\nKeywords: {all_keywords}"
        print(output)
        # keyword order is
        # test name - markers - module name - folder - parent folder/grandparent folder - root folder
        # expensive in test name
        if "expensive" in test.nodeid:
            deselected.append(test)
        # expensive in markers
        # we could use -m flag in CLI to skip expensive tests but we might have more compled
        # logic in test functions to skip tests and this may be useful
        elif "custom_expensive_marker" in all_markers:
            deselected.append(test)
        else:
            selected.append(test)

    # Update the deselected tests
    config.hook.pytest_deselected(items=deselected)

    # Update the selected tests
    items[:] = selected
