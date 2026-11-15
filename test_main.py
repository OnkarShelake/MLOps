
from main import addition

def test_addition_positive():
    assert addition(10, 20) == 30

def test_addition_negative():
    assert addition(-5, -5) == -10

def test_addition_zero():
    assert addition(10, 0) == 10

def test_addition_decimal():
    assert addition(2.5, 3.5) == 6.0
