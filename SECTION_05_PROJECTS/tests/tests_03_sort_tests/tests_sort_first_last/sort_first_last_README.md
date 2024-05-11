We have five functions test_fn_01, test_fn_02 etc listed in that order.

We dynamcially add two markers `first` and `last`.

We use `pytest_collection_modifyitems(items, config)` hook to loop through tests and put those with `first` marker in `first_tests` list, the same for `last` and the remaining in `remaining_list`.

We then do:
```
items[:] = first_tests + last_tests + remaining_tests
```

We can use this further to have dynamic markers for groups by using:
```
groupA
groupB
groupC
```
and then fultering tests into their appropriate lists `groupA_list` etc