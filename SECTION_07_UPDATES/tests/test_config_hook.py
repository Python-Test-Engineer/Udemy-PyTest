import pytest

from pyboxen import boxen

from rich.console import Console

console = Console()


@pytest.fixture
def input_file_content(request):
    return request.config._input_file_content


def test_display_input(request, input_file_content):

    assert "<test_word>" in input_file_content
    output = "\n"
    output += "\n01 Content from input file:"
    output += f"\t{input_file_content}"
    output += "\n02 config.my_global_value:"
    output += f"\t{request.config.my_global_value}"
    output += "\n03 config._input_file_content:"
    output += f"\t{request.config._input_file_content}"
    output += "\n04 config.input_file_content:"
    output += f"\t{request.config.input_file_content}"
    output += "\n"

    console.print(output, style="green")
