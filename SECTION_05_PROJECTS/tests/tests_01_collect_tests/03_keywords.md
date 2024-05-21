What does item.keywords give us?

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

When we run the above we see that we get where I have used the pipe operator '|' as the delimeter but this is still a CSV file. We will see how to customise this in one of our projects: see console and report

KEYWORDS: test_something_else|inner|first|outer|pytestmark|test_collect_tests.py|tests_01_collect_tests|tests|SECTION_05_PROJECTS|
testname makers filename folders->including root folder

MARKERS: inner-first-outer

We can thus order tests by any of these keywords if we want. We can split the node and get the chosen 'bit' and then do a sort based on that key.

https://docs.python.org/3/howto/sorting.html#key-functions