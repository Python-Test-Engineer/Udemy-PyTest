import pytest


class TestApp:
    @pytest.mark.outer
    @pytest.mark.db
    @pytest.mark.db2
    @pytest.mark.sanity
    @pytest.mark.first
    @pytest.mark.inner
    def test_class_multiplication(self):

        assert True

    @pytest.mark.outer
    @pytest.mark.inner
    def test_class_division(self):

        assert True
