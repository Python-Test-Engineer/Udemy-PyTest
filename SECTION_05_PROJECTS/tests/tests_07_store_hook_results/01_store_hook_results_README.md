We can store test properties.

We will make use of this in the next section where we see how it can be outputed in the final terminal report.

```
def test_foo(record_property):
    # records a key-value pair
    record_property("hello", "world")


def test_bar(record_property):
    record_property("spam", "eggs")

```
PS
I am using a report with more details now.