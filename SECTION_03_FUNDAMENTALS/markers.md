We can 'tag' tests with markers -  @pytest.mark.first

We can filter tests using `python -m pytest -m 'first`

We can make more complex expressions - `python -m pytest -m 'inner or outer`, `python -m pytest -m 'inner and db2`

They do not need to be registered in pytest.ini. But best to as we will see why later.

Below is more for later when we create marker based plugins but worth mentioning now.

Can add a marker dynamically via hooks - we will do this later - and one can also register dynamically in hooks which we will also do later. They are registered in 'memory' as it were and not dynamically added to pytest.ini

One may have a plugin that allows a command line option to run a set of markers and if one's hook does not register them then errors will occur.

When the --strict-markers command-line flag is passed, any unknown marks applied with the @pytest.mark.name_of_the_mark decorator will trigger an error. You can enforce this validation in your project by adding --strict-markers to addopts:
https://docs.pytest.org/en/7.1.x/how-to/mark.html?highlight=strict

Alternatively, you can register new markers programmatically in a pytest_configure hook:
```
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "env(name): mark test to run only on named environment"
    )
```

One never know in organisations if --strict-markers is set or not so it is best to register markers regardless.