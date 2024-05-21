
We can 'tag' tests with markers -  @pytest.mark.first

We can filter tests using `python -m pytest -vs -m 'first`

We can make more complex expressions - `python -m pytest -m 'inner or first`, `python -m pytest -m 'inner and first`

They need to be registered in pytest.ini or a warning will occur.

When the --strict-markers command-line flag is passed, any unknown marks applied with the @pytest.mark.name_of_the_mark decorator will trigger an error. You can enforce this validation in your project by adding --strict-markers to addopts:
https://docs.pytest.org/en/7.1.x/how-to/mark.html?highlight=strict

Since will be adding markers dynamically, it is best to work on the assumption that --strict-markers is set and we will need to register our markers.