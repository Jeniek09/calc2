"""Testing the Calculator"""
from calculator.main import Calculator

def test_calculator_result():
    """testing calculator result is 0"""
    calc = Calculator()
    assert calc.result == 0

def test_calculator_get_result():
    """Testing the Get result method of the calculator"""
    calc = Calculator()
    assert calc.get_result() == 0

def test_calculator_add():
    """Testing the Add function of the calculator, adding to zero"""
    calc = Calculator()
    calc.add_number(4)
    assert calc.result == 4

def test_calculator_add_numbers():
    """ Testing addition of two numbers"""
    calc = Calculator()
    result  = calc.add_numbers(4,2)
    assert result == 6
