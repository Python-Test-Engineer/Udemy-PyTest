def test_generate_data_list(dataset):  #
    """The dataset fixture is a list of numbers from 0 to 9"""
    assert dataset < 8


def test_generate_data_tuple(data_tuple):
    """The data_tuple fixture is a set of tuples (n, n+1) as created
    in the conftest.py file.
    """
    assert data_tuple[0] == data_tuple[1] - 1


def test_generate_data_two_lists_are_triples(list1, list2):
    assert list1 * 3 == list2
