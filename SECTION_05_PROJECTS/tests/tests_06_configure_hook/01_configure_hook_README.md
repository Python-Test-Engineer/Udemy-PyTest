We have used the pytest_configure hook to set up markers dynamically. 

We can use the pytest_configure hook to load data before we start the PyTest run.

We will look at this in this project: we pass in a value for an input file, load the data into it and then set up a fixture which is used in a test.
