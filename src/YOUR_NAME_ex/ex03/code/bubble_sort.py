# -*- coding: utf-8 -*-

__author__ = "Jørgen Kongsro"
__email__ = "jorgen.kongsro@nmbu.no"


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
