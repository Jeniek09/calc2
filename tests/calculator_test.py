"""Testing the Calculator"""
from calculator.calculator import Calculator

def test_calculator_result():
    """testing calculator result is 0"""
    calc = Calculator()
    assert calc.result == 0

def test_calculator_get_result():
    """Testing the Get result method of the calculator"""
    assert Calculator.result == 0

def test_calculator_add_numbers():
    """ Testing addition of two numbers"""
    assert Calculator.add_numbers(2,4) == 6
