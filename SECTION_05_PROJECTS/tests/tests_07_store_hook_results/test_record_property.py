content01 = "our info we added in test_foo 📝 "
content02 = "our info we added in test_bar 📝 "

# https://docs.pytest.org/en/7.1.x/reference/reference.html?highlight=record_property#std-fixture-record_property


def test_foo(record_property, request):
    # records a key-value pair
    record_property("recorded in test_bar-> data01", content01)


def test_bar(record_property):
    record_property("recorded in test_bar-> data02", content02)
