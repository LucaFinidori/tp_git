from calculator import addition
from calculator import substraction
from calculator import division



def test_addition():
    assert addition(1, 2) == 3
def test_substraction():
    assert substraction(1, 2) == -1
def test_division():
    assert division(1, 2) == 0.5