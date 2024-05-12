content01 = "world"
content02 = "eggs"


def test_foo(record_property):
    # records a key-value pair
    record_property("data01", content01)


def test_bar(record_property):
    record_property("data02", content02)
