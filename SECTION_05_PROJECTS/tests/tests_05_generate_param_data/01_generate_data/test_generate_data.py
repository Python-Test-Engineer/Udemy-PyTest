def test_generate_data_list(dataset):  #
    """The dataset fixture is a list of numbers from 0 to 9"""
    assert dataset < 8


def test_generate_data_tuple(data_tuple):
    """The data_tuple fixture is a set of tuples (n, n+1) as created
    in the conftest.py file.
    """
    assert data_tuple[0] == data_tuple[1] - 1


def test_generate_data_two_lists_are_triples(list1, list2):
    """
    This function is a test case that checks if the product of `list1` multiplied by 3 is equal to `list2`. 

    Parameters:
        list1 (list): The first list to be multiplied.
        list2 (list): The second list to be compared against the product of `list1`.

    Returns:
        None

    Raises:
        AssertionError: If the product of `list1` multiplied by 3 is not equal to `list2`.
    """
    assert list1 * 3 == list2
