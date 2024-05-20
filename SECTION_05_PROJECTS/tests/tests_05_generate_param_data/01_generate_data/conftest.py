# A pytest hook to dynamically parametrize tests
def pytest_generate_tests(metafunc):
    if "dataset" in metafunc.fixturenames:
        metafunc.parametrize("dataset", range(10))
    if "data_tuple" in metafunc.fixturenames:
        data = [(x, x + 1) for x in range(10)]
        metafunc.parametrize("data_tuple", data)
    if "list1" in metafunc.fixturenames:
        data = [1, 2, 3]
        metafunc.parametrize("list1", data)
    if "list2" in metafunc.fixturenames:
        data = [3, 6, 9]
        metafunc.parametrize("list2", data)
