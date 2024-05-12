pytest --debug gives output of hooks

![Examples](./images/hook-tree.png "PyTest Hooks")

Some hooks are wrap@pytest.hookimpl(hookwrapper=True) as they wrap other hooks.

![Examples](./images/hook-tree-with-wrappers.png "PyTest Hooks")

When PyTest runs certain functions, it looks for similar named function with *similar arguments*. If there is a match it will then run our function at the same point in the run:

![Examples](./images/hooks-docs.png "PyTest Hooks")

This are hooks.

Under the hood, PyTest uses Pluggy to create a plugin based architecture: https://pluggy.readthedocs.io/en/stable/index.html

The challenging part is finding more information on how to access the methods and properties of these hooks.

The PyTest docs and source code help with this as well as looking at existing plugins.