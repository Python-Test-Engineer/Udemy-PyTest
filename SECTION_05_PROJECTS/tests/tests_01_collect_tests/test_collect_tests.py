# By having 'simple' and 'complex' keywords in the test name, we can check for this and then add custom markers in our hook.


def test_interface_simple():
    assert 1


def test_interface_complex():
    assert 1


def test_event_simple():
    assert 1


def test_something_else():
    assert 1
