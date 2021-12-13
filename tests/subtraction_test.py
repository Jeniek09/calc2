"""testing subtraction for the calculator"""
import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations

@pytest.fixture
def _clear_history():
    """clears history before test"""
    Calculations.clear_history()

def test_calculator_subtract(_clear_history):
    """testing the subtraction function of the calculator"""
    assert Calculator.subtraction(1,2) == -1
    assert Calculator.subtraction(2,1) == 1
    assert Calculator.subtraction(4,0) == 4
    assert Calculator.subtraction(0,4) == -4
    assert Calculator.get_last_result_value() == -4
    assert Calculations.count_history() == 4
