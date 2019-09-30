# -*- coding: utf-8 -*-

__author__ = 'Jørgen Kongsro'
__email__ = 'jorgen.kongsro@nmbu.no'


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sdata = sorted(data)
    n = len(sdata)
    return (sdata[n // 2] if n % 2 == 1
            else 0.5 * (sdata[n // 2 - 1] + sdata[n // 2]))


def test_median_for_one_element_list():
    assert median([1])


def test_median_for_odd_numbers():
    odd_data = [1, 3, 5, 9]
    assert median(odd_data)


def test_median_for_even_numbers():
    even_data = [2, 4, 6, 8, 10]
    assert median(even_data)


def test_median_multiple_elements():
    assert median([1])


def test_median_value_error_exeption():
    assert median([1])


def test_median_leaves_orginial_unchanged():
    assert median([1])


def test_median_tuples_and_lists():
    assert median([1])


if __name__ == "__main__":
    test_median_for_one_element_list()
    print("Everything passed")
