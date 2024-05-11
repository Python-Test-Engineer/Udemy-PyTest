"""
Plugin code
"""

__version__ = "0.0.1"

# ===============================================================================
# Paste contents of the conftest.py file here with any imports as needed


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mark test as slow to run")


# A pytest hook to for modifying collected items
def pytest_collection_modifyitems(items, config):
    # we can sort order of items (tests) as needed
    # can ber used to sort by fixtures used if one is say expensive in time
    # items.sort(key=lambda item: "expensive" in item.fixturenames)
    items.sort(key=lambda item: item.nodeid.split("::")[-1])
    output = ""
    print("\n")
    for test in items:
        # print(f"Item: {item.nodeid}")
        keywords = [str(x) for x in test.keywords]
        all_keywords = ("|").join(keywords)
        output += f"TEST: {test.nodeid} \n\tKEYWORDS: {all_keywords}\n"
        print(output)
