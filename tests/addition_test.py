"""testing addition for the calculator"""
import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations

@pytest.fixture
def _clear_history():
    """clears history before test"""
    Calculations.clear_history()

def test_calculator_add(_clear_history):
    """testing the addition function of the Calculator"""
    assert Calculator.addition(1, 2) == 3
    assert Calculator.addition(2, 2) == 4
    assert Calculator.addition(3, 2) == 5
    assert Calculator.addition(4, 2) == 6
    assert Calculator.get_last_result_value() == 6
    assert Calculations.count_history() == 4
