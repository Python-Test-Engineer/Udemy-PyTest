import pytest


class TestApp:
    @pytest.mark.outer
    @pytest.mark.db
    @pytest.mark.db2
    @pytest.mark.sanity
    @pytest.mark.inner
    def test_class_01(self):

        assert True

    @pytest.mark.outer
    @pytest.mark.db2
    @pytest.mark.inner
    def test_class_02(self):

        assert True
