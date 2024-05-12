

## When might we want to add markers dynamically?

Imagine having hundreds of tests and we want to make a custom selection based on terms in the file name, (we discussed the way test names could be used not just for descriptions but also for filtering).

Let's say we have test names that have one of 'model, integration or api' and we ant to be able to add markers with these names so that we can use the -m flag to select by markers.

We could examine the file name and based on the criteria add a custom marker to the test as well as add it to the 'in memory' pytest.ini list of markers to avoid getting warnings or errors in the case that --strict-markers is set in the pytest.ini file.