# What is the nodeid?

If we look at sample_nodeIds.csv we have a '|' delimeted output CSV file:

testname | test_result | nodeid

test.nodeid = tests/test_expensive.py::test_01
test.nodeid = tests/test_expensive.py::TestClass:test_01

full path from root of project with the filename and test name.

If we have folders in our tests folder then these will be included too:

test.nodeid = tests/subFolderA/subFolderB/test_expensive.py::test_01

We can split this string on '::' and the last item is the test name.

item.nodeid.split("::")[-1]

# Keywords
A name -> value dictionary containing all keywords and markers associated with a test invocation <https://docs.pytest.org/en/7.1.x/reference/reference.html?highlight=keywords#pytest.TestReport.keywords>

We will go through this code later but for now...

```
  for test in items:
        all_keywords = [str(x) for x in test.keywords]
        all_keywords = (" - ").join(all_keywords)

        output = f"Test: {test.nodeid} \nKeywords: {all_keywords}"
        # keyword order is
        # test name - markers - module name - folder - parent folder/grandparent folder - root folder
```

When we run the above we see that we get where I have used the pipe operator '|' as the delimeter but this is still a CSV file. We will see how to customise this in one of our projects:

items are: testname | markers| filename | folders->including root folder

MARKERS: inner - first - outer

We can thus order tests by any of these keywords if we want. We can split the node and get the chosen 'bit' and then do a sort based on that key.

https://docs.python.org/3/howto/sorting.html#key-functions