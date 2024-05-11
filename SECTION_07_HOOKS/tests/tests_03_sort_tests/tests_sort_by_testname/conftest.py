from pyboxen import boxen

print("\n\n")


# A pytest hook to for modifying collected items
def pytest_collection_modifyitems(items, config):
    # we can sort order of items (tests) as needed
    # can be used to sort by fixtures used if one is say expensive in time
    # items.sort(key=lambda item: "expensive" in item.fixturenames)
    items.sort(key=lambda item: item.nodeid.split("::")[-1])
    output = ""
    for test in items:
        keywords = [str(x) for x in test.keywords]
        all_keywords = ("|").join(keywords)
        output += f"TEST: {test.nodeid} \n\tKEYWORDS: {all_keywords}\n"

    print(
        boxen(
            output,
            title="pytest_collection_modifyitems SORTED",
            subtitle="pytest_collection_modifyitems SORTED",
            subtitle_alignment="left",
            color="green",
            padding=1,
        )
    )
