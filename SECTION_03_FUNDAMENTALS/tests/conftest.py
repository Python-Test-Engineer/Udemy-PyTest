import pytest

# https://docs.pytest.org/en/7.1.x/example/simple.html#how-to-change-command-line-options-defaults
# https://docs.python.org/3/howto/argparse.html


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")


#  we can pass in `--cmdopt type1` or `--cmdopt=type1`
