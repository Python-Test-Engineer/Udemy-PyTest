# PyTest_00_MINIMAL

<div>
   <img src="./_images/pytest.svg" width="75" height="75">
</div>

# PyTest_00_MINIMAL

<!-- - This is the foundation test suite that contains templates for PyTest and Playwright.  -->
- The **src** folder is where devs place their code.
- The **tests** folder is where devs place their tests and contains templates.
- The **pytest.ini** folder is the first configuration file where test_suite options can be stored.
- Custom logger format etc in pytest.ini

- Acknowledgements and links to YT videos and other resources are cited.

## Set up and rund

- create virtual env (python -m venv venv then activate .\venv\Scripts\activate for Windows).
- `python -m pip install -r requirements.txt`
- `python -m pytest -vs` - this will ensure all tests are found if *pytest* itself does not work.
- `pytest-sugar` is installed to create prettier console output. `pip uninstall pytest-sugar` to remove this feature.

