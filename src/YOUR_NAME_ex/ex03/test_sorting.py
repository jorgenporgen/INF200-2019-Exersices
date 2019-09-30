# -*- coding: utf-8 -*-

__author__ = 'Jørgen Kongsro'
__email__ = 'jorgen.kongsro@nmbu.no'


def bubble_sort(iterable):
    """ Bubble sort is a simple sorting algorithm
    Returns
    -------
    data : list
    """
    data1 = list(iterable)
    sorting_length = len(data1) - 1
    for i in range(sorting_length):
        for j in range(sorting_length - i):
            if data1[j] > data1[j + 1]:
                data1[j], data1[j + 1] = data1[j + 1], data1[j]
    return data1


if __name__ == "__main__":
    for data in ((), (1,), (1, 3, 8, 12), (12, 8, 3, 1), (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))


def test_empty():
    """Test that the sorting function works for empty list"""
    assert bubble_sort([])


test_empty()


def test_single():
    """Test that the sorting function works for single-element list"""
    assert bubble_sort([1])


test_single()


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert data != sorted_data


test_sorted_is_not_original()


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert data == data


test_original_unchanged()


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert sorted_data == bubble_sort(data)


test_sort_sorted()


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    pass


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    pass


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    pass
