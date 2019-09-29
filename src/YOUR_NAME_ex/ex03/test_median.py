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
     data = [12]
     assert median(data) == 12

