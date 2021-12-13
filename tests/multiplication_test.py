"""testing multiplication for the calculator"""
import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations

@pytest.fixture
def _clear_history():
    """clears history before test"""
    Calculations.clear_history()

def test_calculator_subtract(_clear_history):
    """testing the multiplication function of the calculator"""
    assert Calculator.multiplication(1,2) == 2
    assert Calculator.multiplication(2,1) == 2
    assert Calculator.multiplication(4,0) == 0
    assert Calculator.multiplication(0,4) == 0
    assert Calculator.get_last_result_value() == 0
    assert Calculations.count_history() == 4
