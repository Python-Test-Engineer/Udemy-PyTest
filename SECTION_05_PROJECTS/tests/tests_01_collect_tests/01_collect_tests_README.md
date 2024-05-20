## Creating a CSV of all tests that will be run

If we run test with the --collect-only flag we get a list of all test that will be run:

![--collect-only flag](./pytest-collect-only-flag.png "San Juan Mountains")
pytest-collect-only-flag.png 

`pytest_collection_modifyitems` hook gathers all the tests prior to running tests. 

We can output this to a CSV along with infomation on keywords usedof the test.
`python -m pytest .\tests\tests_collect_tests\`

Use 09 to show that it does this in real time...
