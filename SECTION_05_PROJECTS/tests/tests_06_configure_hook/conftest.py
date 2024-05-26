import os

from rich.console import Console

console = Console()


print("\n\n")


def pytest_configure(config):

    config.my_global_value = "Shared Value"
    # This is available via the request built in fixture so can be accessed in tests
    # global_value = request.config.my_global_value

    # output1 = str(dir(config))
    # Get the path to the text file in the same directory as conftest.py
    current_directory = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_directory, "input.txt")

    # Read the content of the file and store it in the pytest config object
    with open(input_file_path, "r") as file:
        file_content = file.read()

    config.input_file_content = file_content
    # we can then access this to load into a fixture in test_config_hook.py

    # we can see contents of config and note how it is printed before
    # ====== test session starts =======
    console.print("Config", (dir(config)))
