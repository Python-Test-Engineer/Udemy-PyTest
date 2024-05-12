import pytest


class TestApp:

    @pytest.mark.first
    def test_class_first_only(self):

        assert True

    @pytest.mark.outer
    @pytest.mark.first
    @pytest.mark.inner
    def test_class_first_inner_outer(self):

        assert True

    @pytest.mark.first
    @pytest.mark.inner
    def test_class_first_inner(self):

        assert True
