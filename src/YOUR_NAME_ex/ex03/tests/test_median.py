import pytest
from code import median


def test_median_for_one_element_list():
    assert median([1])


def test_median_for_odd_numbers():
    odd_data = [1, 3, 5, 9]
    assert median(odd_data)


def test_median_for_even_numbers():
    even_data = [2, 4, 6, 8, 10]
    assert median(even_data)


def test_median_multiple_elements():
    data = {
        "#1": [1, 2, 3, 5, 8],
        "#2": [10, 40, 5, 90],
        "#3": [5.6, 3.8, 2.7, 2.4, 65.22, 0.224],
    }

    for key in data:
        multiple_data = median(data[key])
        print("Running case ", [key])
        assert multiple_data == median(data[key])


def test_median_raises_value_error_on_empty_list():
    with pytest.raises(ValueError):
        median([])


def test_median_leaves_orginial_unchanged():
    assert median([1])


def test_median_tuples_and_lists():
    assert median([1])


# if __name__ == "__main__":
#    test_median_for_one_element_list()
#    test_median_for_odd_numbers()
#    test_median_for_even_numbers()
#    test_median_multiple_elements()
#    test_median_raise_value_error_exeption()
#    test_median_leaves_orginial_unchanged()
#    test_median_tuples_and_lists()
#    print("Everything passed")
