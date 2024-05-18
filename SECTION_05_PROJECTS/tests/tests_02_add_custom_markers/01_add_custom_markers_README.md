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

![--collect-only flag](./pytest-collect-only-flag.png "San Juan Mountains")
pytest-collect-only-flag.png 

## When might we want to add markers dynamically?

Imagine having hundreds of tests and we want to make a custom selection based on terms in the file name, (we discussed the way test names could be used not just for descriptions but also for filtering).


e.g. select tests for tests that have:

- db in test name
- duration > 10s (cross refernece to our output file of test results)
- only for the test folders (DB and API)
- create a marker 'db-api-slow'

Let's say we have test names that have one of 'model, integration or api' and we ant to be able to add markers with these names so that we can use the -m flag to select by markers.

We could examine the file name and based on the criteria add a custom marker to the test as well as add it to the 'in memory' pytest.ini list of markers to avoid getting warnings or errors in the case that --strict-markers is set in the pytest.ini file.

As we will see in the lesson on filtering, where we select tests based on their markers, (we can also filter by other criteria), we can create `super marker`, a marker that references a list of markers obtained by some selection query, rather than making complex -m marker selection. 

This will be better understood when we do the filtering lesson.

