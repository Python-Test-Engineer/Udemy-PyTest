
# Sort tests in a random order

There are some very powerful randomiser plugins:

- https://pypi.org/project/pytest-randomly/
- https://pypi.org/project/pytest-random-order/

We can create are own simple versions by getting the list of tests from  the  `pytest_collection_modifyitems(items, config)` hook and use `random.shuffle(items)`.

We can also use the technique from `tests_sort_first_last` where we split tests uisng some criteria and then adding these list together.

In fact, once split by some criteria, we can shuffle these lists.

If we use add-options to send in CLI options, we can create hooks/plugins that can have options in how these files are split/randomised.