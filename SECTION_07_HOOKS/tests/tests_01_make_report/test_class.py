""" Tests to run in pytest_runtest_makereport hook

We have registered many marks in pytest.ini. We will be able to report what marks were used in what tests in the report file we will be producing


"""

import pytest


class TestApp:

    @pytest.mark.last
    def test_class_01_marked_last(self):

        assert True

    @pytest.mark.first
    def test_class_02_marked_first(self):

        assert True

    def test_class_03_not_first_or_last(self):

        assert True
