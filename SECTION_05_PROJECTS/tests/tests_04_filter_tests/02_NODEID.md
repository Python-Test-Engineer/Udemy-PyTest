# nodeid

For our test file test_expensive.py in:

SECTION_05_PROJECTS/tests/tests_04_filter_tests/test_expensive.py

the test test_01 will have a nodeid of:

tests/tests_04_filter_tests/test_expensive.py::test_01

If we are in SECTION_05_PROJECTS, then we get the full path to the file from within the folder along with the test name added on to the full path to the file using '::'.

We can thus get the test name by splitting on '::' and getting the last element in the list.

Getting the test name from a nodeid of a test is then:

        test.nodeid.split("::")[-1]


