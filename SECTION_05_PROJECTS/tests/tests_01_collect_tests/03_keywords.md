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

When we run the above we see that we get where I have used the pipe operator '|' as the delimeter but this is still a CSV file. We will see how to customise this in one of our projects:

test_class_01_marked_last|test_class_01_marked_last|last|pytestmark|TestApp|test_class.py|tests_01_collect_tests|tests|SECTION_05_PROJECTS|
test_class_02_marked_first|test_class_02_marked_first|first|pytestmark|TestApp|test_class.py|tests_01_collect_tests|tests|SECTION_05_PROJECTS|
test_class_03_not_marked_first_or_last|test_class_03_not_marked_first_or_last|TestApp|test_class.py|tests_01_collect_tests|tests|SECTION_05_PROJECTS|
test_interface_simple|test_interface_simple|expensive|pytestmark|test_collect_tests.py|tests_01_collect_tests|tests|SECTION_05_PROJECTS|
test_interface_complex|test_interface_complex|inner|outer|pytestmark|test_collect_tests.py|tests_01_collect_tests|tests|SECTION_05_PROJECTS|
test_event_simple|test_event_simple|first|pytestmark|test_collect_tests.py|tests_01_collect_tests|tests|SECTION_05_PROJECTS|
test_something_else|test_something_else|inner|first|outer|pytestmark|test_collect_tests.py|tests_01_collect_tests|tests|SECTION_05_PROJECTS|


nodeid: 
tests/tests_ex03_sort_tests/tests_sort_by_testname/test_class.py::TestApp::test_class_multiplication

keywords: 

test_class_multiplication - inner-sanity-db2-db-outer - test_class.py - tests_01_playground - tests - SANDBOX -  UDEMY-PYTEST

Thus we get:

test name:        test_class_multiplication
markers:          inner-sanity-db2-db-outer (our delimeter - added between)
file_name:        test_class.py
parent folder:    tests
next up folder:  SANDBOX etc...
root folder:      UDEMY-PYTEST

We can thus order tests by any of these keywords if we want. We can split the node and get the chosen   'bit' and then do a sort based on that key.

https://docs.python.org/3/howto/sorting.html#key-functions