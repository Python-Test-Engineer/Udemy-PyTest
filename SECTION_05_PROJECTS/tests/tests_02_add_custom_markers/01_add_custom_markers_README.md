## Intro

- make_report hook now not included in this conftest but project one.
- pytest.ini has our registered markers and --strict-markers option set True

## What we are doing in this project:

- Based on the test name, we determine if it contains 'simple' or complex.
- We then add markers dynamically called 'simple-marker' or 'complex-marker'
- for just these ones.
- This is a simple example but we might have a far more complex selection requirement that spans many folders etc.

`pytest_collection_modifyitems` hook gathers all the tests in the same way --collect-only in the CLI just gives a list of tests PyTest has discovered based on our CLI command.

`python -m pytest .\tests\tests_02_add_custom_markers\ --collect-only`

![--collect-only flag](./pytest-collect-only-flag.png "collect only")
pytest-collect-only-flag.png 

## When might we want to add markers dynamically?

Imagine having hundreds of tests and we want to make a custom selection based on terms in the file name, (we discussed the way test names could be used not just for descriptions but also for filtering).

We want to run this set of tests using a custom marker, say q1, so that we can use `python -m pytest -m 'db-api-slow'`.

`db-api-slow` might select tests that have:

- db in test name
- duration > 10s (cross refernece to our output file of test results)
- only for the test folders (DB and API)
- create a marker 'db-api-slow'
