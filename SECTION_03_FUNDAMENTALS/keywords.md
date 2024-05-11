What does item.keywords give us?

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

test_class_multiplication|tests/tests_ex03_sort_tests/tests_sort_by_testname/test_class.py::TestApp::test_class_multiplication|-PASSED-|9.980006143450737e-05|inner-sanity-db2-db-outer  


nodeid = tests/tests_ex03_sort_tests/tests_sort_by_testname/test_class.py::TestApp::test_class_multiplication_FH8
Keywords: 

test_class_multiplication - inner-sanity-db2-db-outer - test_class.py - tests_01_playground - tests - SANDBOX -  UDEMY-PYTEST

This we get:

test name:        test_class_multiplication
markers:          inner-sanity-db2-db-outer (our delimeter)
file_name:        test_class.py
parent folder:    tests
gnext up folder:  SANDBOX
root folder:      UDEMY-PYTEST

We can thus order tests by any of these keywords if we want. We can split the node and get the chosed 'bit' and then do a sort based on that key.

https://docs.python.org/3/howto/sorting.html#key-functions