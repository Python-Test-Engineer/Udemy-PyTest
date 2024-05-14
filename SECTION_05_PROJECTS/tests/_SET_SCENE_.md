

Imagine we work in a company that has 400 tests, in many different folders, some class based others not.

We want the following:

A stylish informative console output with REPORT_HEADE AND CUSTOM_REPORT SECTIONS.

We want a CSV output of:

- testname
- testnode (full path of test, class, function)
- PASS/FAIL result
- test duration
- all markers for each test

We want to be able to manage our tests:

- sort by name, markers or keywords
- randomise the tests to ensure that tests are fully independent
- filter tests based on certain criteria

We want to be able to dynamically add markers to tests based on criteria and then run our tests making use of these markers.

Based on previous test runs, we want to add an 'expensive/slow' marker dynamically so that we don't run these tests. The criteria changes frequently.

At certain points we want to store some data that is created as part of the test and have this displayed in final report as well as outputed to file.

We want an email sent at various stages of the test run and at certain test points.

We want to to use extensive input test data that we have compiled to examine edge cases.
