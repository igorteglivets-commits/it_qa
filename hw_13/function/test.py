import pytest
from function import sum_of_num, divide_num, mult_num
from function import minus_num


def test_sum_of_num():
    assert sum_of_num(2, 3) == 5
    assert sum_of_num(-1, 1) == 0
    assert sum_of_num(0, 0) == 0
    assert sum_of_num(100, 200) == 300


@pytest.mark.parametrize("a, b, expected", [(2, 3, 5),
                                            (-1, 1, 0),
                                            (0, 0, 0),
                                            (100, 200, 300)])
def test_sum_of_num(a, b, expected):
    assert sum_of_num(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (0, 0, 0),
    (-1, -1, 0),
    (10, 20, -10)
])
def test_minus_num(a, b, expected):
    assert minus_num(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),
    (10, 2, 5),
    (5, 2, 2.5),
])
def test_divide_num(a, b, expected):
    assert divide_num(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide_num(5, 0)


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-1, 5, -5),
    (0, 10, 0),
    (10, 20, 200)
])
def test_mult_num(a, b, expected):
    assert mult_num(a, b) == expected
