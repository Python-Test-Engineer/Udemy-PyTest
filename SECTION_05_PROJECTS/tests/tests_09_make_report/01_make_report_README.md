
python -m pytest -vs --tb=no .\tests\tests_09_make_report\

--tb=no does not display trace back.

https://docs.pytest.org/en/7.1.x/how-to/output.html

- pytest --showlocals # show local variables in tracebacks
- pytest --tb=auto    # (default) 'long' tracebacks for the first and last
- pytest -l           # show local variables (shortcut)
                   # entry, but 'short' style for the other entries
- pytest --tb=long    # exhaustive, informative traceback formatting
- pytest --tb=short   # shorter traceback format
- pytest --tb=line    # only one line per failure
- pytest --tb=native  # Python standard library formatting
- pytest --tb=no      # no traceback at all

https://docs.pytest.org/en/7.1.x/how-to/writing_hook_functions.html#:~:text=hookwrapper%3A%20executing%20around%20other%20hooks,function%20which%20yields%20exactly%20once.

hookwrapper: executing around other hooks

pytest plugins can implement hook wrappers which wrap the execution of other hook implementations. A hook wrapper is a generator function which yields exactly once. When pytest invokes hooks it first executes hook wrappers and passes the same arguments as to the regular hooks.

At the yield point of the hook wrapper pytest will execute the next hook implementations and return their result to the yield point in the form of a Result instance which encapsulates a result or exception info. The yield point itself will thus typically not raise exceptions (unless there are bugs).

Lets look at the images of hook order...

If we use one of the hook functions in our test files, PyTest will make not of these during setup and run run our hook.

By using certain hooks we can create custom effects.

The hook function can be anywhere but it is placed in conftest.py so that it is held in one place rather than having to have it in every test file.

This is a local plugin. We can reuse/share it and it will take precedence over conftest.py files higher up in the folder tree.

A distributable plugin is using the same code in the conftest.py file byt place in a module in a plugin package that can be built into a whl file to be and installable package. 

We will be doing this the building plugins section.

We can place conftest.py in root of tests and it will work.


