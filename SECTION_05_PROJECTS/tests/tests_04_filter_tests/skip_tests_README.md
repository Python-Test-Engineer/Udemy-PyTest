# Filtering selection of tests

We have seen how we can collect all the tests and able to sort the sequence order.

We can also filter tests based on custom criteria.

We use the nodeid to see if the test name has 'expensive' in it,(see tes_functions.py) or if it already has an 'expensive' marker.

We then add these tests to the deselected list and put all the others in the selected list.

We can also use techniques used in add markers to either dyanamcially create markers based on test name and filter based on the test having a particalar marker of set of markers.

Selection can be more advanced than this.

Using the `pytest_collection_modifyitems` hook gathers all the tests and we have access to keywords:

```
  for test in items:
        all_keywords = [str(x) for x in test.keywords]
        all_keywords = (" - ").join(all_keywords)

        output = f"Test: {test.nodeid} \nKeywords: {all_keywords}"
        # keyword order is
        # test name - markers - module name - folder - parent folder/grandparent folder - root folder
```