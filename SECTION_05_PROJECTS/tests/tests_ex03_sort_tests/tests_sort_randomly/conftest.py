import random

from pyboxen import boxen

print("\n\n")


# A pytest hook to for modifying collected items
def pytest_collection_modifyitems(items, config):
    # we can sort order of items (tests) as needed
    # can ber used to sort by fixtures used if one is say expensive in time
    # items.sort(key=lambda item: "expensive" in item.fixturenames)
    random.shuffle(items)
    output = ""
    for test in items:
        # print(f"Item: {item.nodeid}")
        keywords = [str(x) for x in test.keywords]
        all_keywords = ("|").join(keywords)
        output += f"TEST: {test.nodeid} \n\tKEYWORDS: {all_keywords}\n"
    print(
        boxen(
            output,
            title="Sorted order of tests randomly",
            subtitle="Sorted order of tests randomly",
            subtitle_alignment="left",
            color="green",
            padding=1,
        )
    )
