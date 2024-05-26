import pytest


@pytest.fixture
def input_file_content(request):
    return request.config.input_file_content


def test_display_input(request, input_file_content):
    print("\n------------------------------------------------------------------------")
    print("\n01 Content from input file:")
    print(f"\t{input_file_content}")
    print("\n02 config.my_global_value:")
    print(f"\t{request.config.my_global_value}")
    
    print("\n03 config.input_file_content:")
    print(f"\t{request.config.input_file_content}")
    
    assert "<test_word>" in input_file_content
