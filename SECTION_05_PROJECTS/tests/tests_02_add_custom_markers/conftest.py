"""
In this example we have commented out pytest_runtest_makereport and use the root level configtest.py implementation of from django.conf import settings"
"""

import pytest


from pyboxen import boxen

print("\n\n")


# ensure ; addopts = --strict-markers not used or add via config hook otherwise following error cocurs:
# INTERNALERROR> Failed: 'simple' not found in `markers` configuration option
def pytest_configure(config):
    # we register our markers in pytest.ini 'memory' so that we do not get warnings r
    # errors with regard to pytest.ini and --strict-markers
    config.addinivalue_line("markers", "simple_marker: mark simple test")
    config.addinivalue_line("markers", "complex_marker: mark complex test")


def pytest_collection_modifyitems(items):
    # using simple_marker rather than simple so that when we print keywords we can see that we are using simple_marker
    # other wise if just simple it is not clear if it is picking part of test name that has simple in it.
    # NOTE these markers are not on the pytest.ini file but are 'in memory' as it were
    for test in items:
        if "simple" in test.name:
            test.add_marker(pytest.mark.simple_marker)
        if "complex" in test.name:
            test.add_marker(pytest.mark.complex_marker)
    print("\n")
    for test in items:
        all_keywords = [str(x) for x in test.keywords]
        all_keywords = (" - ").join(all_keywords)

        output = f"Test: {test.nodeid} \nKeywords: {all_keywords}"
        # keyword order is
        # test name - markers - module name - folder - parent folder/grandparent folder - root folder
        print(
            boxen(
                output,
                title=f"keywords for {test.name}",
                subtitle="keywords",
                subtitle_alignment="left",
                color="blue",
                padding=1,
            )
        )
