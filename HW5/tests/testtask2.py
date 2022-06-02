from HW5.task2 import custom_sum
import pytest


@pytest.mark.parametrize("a, b, c, expected_result", [(1, 2, 3, 6),
                                                      (5, 9, 11, 25),
                                                      ([1, 2], [3, 4], [5, 6, 7], [1, 2, 3, 4, 5, 6, 7]),
                                                      ('hello,', ' dude', '!', 'hello, dude!')])
def test_custom_sum(a, b, c, expected_result):
    assert custom_sum(a, b, c) == expected_result


def test_custom_sum_name_attribute():
    assert custom_sum.__name__ == 'custom_sum'


def test_custom_sum_doc_attribute():
    assert custom_sum.__doc__ == 'This function can sum any objects which have __add___'


def test_custom_sum_orig_func_attribute():
    assert str(custom_sum.__original_func)[:23] == '<function custom_sum at'