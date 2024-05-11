import pytest


@pytest.fixture
def input_file_content(request):
    return request.config._input_file_content


def test_display_input(input_file_content):
    print("Content from input file:")
    print(input_file_content)
    assert " <test_word>" in input_file_content
