
# Ordering our tests by markers first, all non-last, then last.

We have five functions test_fn_01, test_fn_02 etc listed in that order.

They have markers of 'first', 'last' or none of these.

We use `pytest_collection_modifyitems(items, config)` hook to loop through tests and put those with `first` marker in `first_tests` list, the same for `last` and the remaining in `remaining_list`.

We then do:
```
items[:] = first_tests  + remaining_tests + last_tests
```
We can use this further to have dynamic markers for groups by using:
```
groupA
groupB
groupC
```
and then fultering tests into their appropriate lists `groupA_list` etc

We dynamcially add two markers `first` and `last` based on criteria of keywords as we saw in a previous lesson.