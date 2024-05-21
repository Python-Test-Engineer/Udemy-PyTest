# By having 'simple' and 'complex' keywords in the test name, we can check for this and then add custom markers in our hook.
# we can filter tests using pytest -k simple or pytest -k complex but for more complex criteria we may find value in having a 'super marker' so that users can just run pytest -m supermarker


def test_interface_simple():
    assert 1


def test_interface_complex():
    assert 1


def test_event_simple():
    assert 1


def test_something_else():
    assert 1
