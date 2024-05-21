# Sort by test name

Let's see the test again...

We will collect all the tests (--collect-only flag does this in CLI), using the `pytest_collection_modifyitems` hook.

Let's run -collect-only:

`python -m pytest -vs .\tests\tests_03_sort_tests\tests_sort_by_testname\ --collect-only`

The hook then sorts the list of tests by getting the last part of the nodeid. We then sort by the last part of the path. The nodeid uses '::' as a separator.
```
if config.option.desc:
    items.sort(key=lambda item: item.nodeid.split("::")[-1], reverse=True)
    print(f"\n\n===> DESC:")
if config.option.asc:
    items.sort(key=lambda item: item.nodeid.split("::")[-1])
    print(f"\n\n===> ASC:")
```
We can then sort the list in any way we like and later we will see how we can seledt/deselect tests based on custom criteria.

For now we will sort by tst name alphabetically and we will learn how to pass in CLI arguments by adding `--desc` and `--asc` boolean flags. 

In fact, when we come to make our distributable plugin, we will use this local plugin or conftest.py as our plugin feature.

Hook order:

https://github.com/pytest-dev/pytest/discussions/11226