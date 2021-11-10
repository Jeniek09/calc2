"""Testing the Calculator"""
from calculator.main import Calculator

def test_calculator_result():
    """testing calculator result is 0"""
    calc = Calculator()
    assert calc.result == 0

def test_calculator_add():
    """Testing the Add function of the calculator"""
    #Arrange by instantiating the calc class
    calc = Calculator()
    #Act by calling the method to be tested
    calc.add_number(4)
    #Assert that the results are correct
    assert calc.result == 4

def test_calculator_get_result():
    """Testing the Get result method of the calculator"""
    calc = Calculator()
    assert calc.get_result() == 0

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    calc = Calculator()
    calc.subtract_number(1)
    assert calc.get_result() == -1

def test_calculator_multiply():
    """ tests multiplication of two numbers"""
    calc = Calculator()
    result  = calc.multiply_numbers(1,2)
    assert result == 2

def test_calculator_divide():
    """tests division of two numbers"""
    calc = Calculator()
    result = calc.divide_numbers(2,2)
    assert result == 1

def test_calculator_add_numbers():
    """test addition of numbers example 2"""
    calc = Calculator()
    result = calc.add_numbers(4,5)
    assert result == 9

def test_calculator_subtract_numbers():
    """test subtraction of numbers example 2"""
    calc = Calculator()
    result = calc.subtract_numbers(6,3)
    assert result == 3
