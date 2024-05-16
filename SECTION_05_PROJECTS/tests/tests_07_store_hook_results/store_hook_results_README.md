
## Stash: A place where plugins can store information on the config for their own use.

https://docs.pytest.org/en/7.1.x/reference/reference.html?highlight=stash#pytest.Stash

```
def test_foo(record_property):
    # records a key-value pair
    record_property("hello", "world")


def test_bar(record_property):
    record_property("spam", "eggs")

```

We will see how we can ouput this in final report in  the next lesson.

which_plugin = pytest.StashKey[str]() is useful as it is on the test or item element in our hooks so we can identify which plugin was used in the test for debugging.

We can add this to our CSV report file and we would get:

```
test_fn_stash|tests/tests_07_store_hook_results/test_stash.py::test_fn_stash|-PASSED-|8.8099999629776e-05|inner-first|$tests_07_store_hook_results$
```
