"""Test import from src folder"""


from src.sample import add


def test_add_num():
    """basic test"""
    assert add(1, 2) == 3


class TestSample:
    """Class test"""

    def test_add_num(self):
        """fn test"""
        assert add(1, 2) == 3
