# Filtering selection of tests

We can also filter tests based on custom criteria.

We can use the nodeid to see if the test name has 'expensive' in it.

We can also select by custom marker as is the case here with the custom marker 'custom_expensive_marker`.

We can get all the markers, either via:

```
        list_markers = [
            str(getattr(test.own_markers[j], "name"))
            for j in range(len(test.own_markers))
        ]
        all_markers = ("-").join(list_markers)
```
or we can get markers and full path location of test from the `keywords` of the test:

```
        all_keywords = [str(x) for x in test.keywords]
        all_keywords = (" - ").join(all_keywords)
        output = f"\nKeywords: {all_keywords}"
```

Based on our criteria, we can then select/deselect accordingly.

```
    # Update the deselected tests
    config.hook.pytest_deselected(items=deselected)

    # Update the selected tests
    items[:] = selected
```
We can add --flags so that when we run our tests, we need only pass in our chosen flag and the plugin code will select/deselct accordingly.

As you can see, once we have a list of all tests, we can combine CLI flags with custom filtering based on nodeid, markers, keywords or some combination of all three.

We can also add markers dynamically based on custom criteria so that user can use the -m 'selected_marker' option.