from calculator import Calculator
calculator = Calculator()

def test_addition():
    assert calculator.addition(1, 2) == 3

def test_substraction():
    assert calculator.substraction(1, 2) == -1

def test_division():
    assert calculator.division(1, 2) == 0.5
