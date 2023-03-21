import pytest
from series import fibonacci
from series import lucas
from series import sum_series

def test_fibonacci():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_2():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_3():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_fibonacci_4():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected

def test_fibonacci_5():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_fibonacci_6():
    actual = fibonacci(6)
    expected = 8
    assert actual == expected

def test_fibonacci_10():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected

def test_fibonacci_19():
    actual = fibonacci(19)
    expected = 4181
    assert actual == expected




def test_lucas():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_0():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_1():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_2():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucas_3():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_lucas_7():
    actual = lucas(7)
    expected = 29
    assert actual == expected

def test_lucas_10():
    actual = lucas(10)
    expected = 123
    assert actual == expected


def test_sum_series3():
    actual = sum_series(3)
    expected = 2
    assert actual == expected

def test_sum_series10():
    actual = sum_series(10)
    expected = 55
    assert actual == expected

def test_sum_series7_2_1():
    actual = sum_series(7,2,1)
    expected = 29
    assert actual == expected

def test_sum_series10_2_1():
    actual = sum_series(10,2,1)
    expected = 123
    assert actual == expected