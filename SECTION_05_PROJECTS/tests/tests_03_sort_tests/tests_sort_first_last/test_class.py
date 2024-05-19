import pytest


class TestApp:

    @pytest.mark.last
    def test_class_01_marked_last(self):

        assert True

    @pytest.mark.first
    def test_class_02_marked_first(self):

        assert True

    def test_class_03_not_marked_first_or_last(self):

        assert True
