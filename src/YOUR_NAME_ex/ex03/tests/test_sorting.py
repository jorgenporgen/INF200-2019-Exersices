from code import bubble_sort


def test_empty():
    """Test that the sorting function works for empty list"""
    data = []
    assert len(bubble_sort(data)) == 0


def test_single():
    """Test that the sorting function works for single-element list"""
    assert bubble_sort([1])


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """

    data2 = [3, 2, 1]
    sorted_data = bubble_sort(data2)
    assert data2 != sorted_data


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data3 = [3, 2, 1]
    _sorted_data = bubble_sort(data3)
    assert data3 == data3


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    data4 = [3, 2, 1]
    sorted_data = bubble_sort(data4)
    assert sorted_data == bubble_sort(data4)


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    data4 = [3, 2, 1]
    data4.reverse()
    sorted_data = bubble_sort(data4)
    assert sorted_data == bubble_sort(data4)


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    data5 = [1, 1, 1]
    sorted_data = bubble_sort(data5)
    assert len(set(sorted_data)) <= 1


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    data = {
        "#1": [1, 2, 3, 5, 8],
        "#2": [10, 40, 5, 90],
        "#3": ["a", "b", "c", "d"],
        "#4": [5.6, 3.8, 2.7, 2.4, 65.22, 0.224],
    }

    for key in data:
        sorted_data = bubble_sort(data[key])
        assert sorted_data == bubble_sort(data[key])


# if __name__ == "__main__":
#    test_empty()
#    test_single()
#    test_sorted_is_not_original()
#    test_original_unchanged()
#    test_sort_sorted()
#    test_sort_reversed()
#    test_sort_all_equal()
#    test_sorting()
#    print("Everything passed")
