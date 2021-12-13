"""testing division for the calculator"""
import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations

@pytest.fixture
def _clear_history():
    """clears history before test"""
    Calculations.clear_history()

def test_calculator_subtract(_clear_history):
    """testing the division function of the calculator"""
    assert Calculator.division(1,2) == 0.5
    assert Calculator.division(2,1) == 2
    assert Calculator.get_last_result_value() == 2
    assert Calculations.count_history() == 2

def test_zero_division():
    """testing for zero division error"""
    # pylint: disable=pointless-statement)
    with pytest.raises(ZeroDivisionError):
        1 / 0
