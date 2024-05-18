# Sort by test name

We will collect all the tests (--collect-only flag does this in CLI), using the `pytest_collection_modifyitems` hook.

--collect-only:

`python -m pytest -vs .\tests\tests_03_sort_tests\tests_sort_by_testname\ --collect-only`

```
def pytest_collection_modifyitems(items, config):
    # we can sort order of items (tests) as needed
    # can ber used to sort by fixtures used if one is say expensive in time
    # items.sort(key=lambda item: "expensive" in item.fixturenames)
    if config.option.desc:
        items.sort(key=lambda item: item.nodeid.split("::")[-1], reverse=True)
        print(f"\n\n===> DESC: {config.option.desc}\n")
    else:
        items.sort(key=lambda item: item.nodeid.split("::")[-1])
```
We can then sort the list in any way we like and later we will see how we can seledt/deselect tests based on custom criteria.

For now we will sort by tst name alphabetically and we will learn how to pass in CLI arguments by adding a `--desc` boolean flag. If present, it will sort in reverse order.

In fact, when we come to make our distributable plugin, we will use this local plugin or conftest.py as our plugin feature.