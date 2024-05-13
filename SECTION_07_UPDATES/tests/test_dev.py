import pytest

from pyboxen import boxen

from rich.console import Console

console = Console()


@pytest.mark.dev
def test_something_10():
    assert 1 + 1 == 2
