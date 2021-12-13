"""testing the history component of the calculator"""
import pytest
from calc.history.calculations import Calculations
from calc.calculations.addition import Addition

@pytest.fixture
def _clear_history_fixture():
    """define a clear function that is passed it to the test"""
    Calculations.clear_history()

@pytest.fixture
def _addition_fixture():
    """defines an addition fixture to be passed to the test"""
    addition = Addition(1,2)
    Calculations.add_calculation(addition)

def test_add_calculation_to_history_count(_clear_history_fixture, _addition_fixture):
    """testing addition of a calculation and then count"""
    assert Calculations.count_history() == 1

def test_clear_calculation_history(_clear_history_fixture, _addition_fixture):
    """testing clearing history"""
    assert Calculations.count_history() == 1
    Calculations.clear_history()
    assert Calculations.count_history() == 0
    assert Calculations.clear_history()

def test_get_first_calculation(_clear_history_fixture, _addition_fixture):
    """testing out get_result for first result"""
    assert Calculations.get_first_calculation().get_result() == 3

def test_get_last_calculation(_clear_history_fixture, _addition_fixture):
    """testing out get_result for last result"""
    addition = Addition(5, 2)
    Calculations.add_calculation(addition)
    assert Calculations.get_last_calculation_result_value() == 7
    assert Calculations.count_history() == 2

def test_get_n_calculation(_clear_history_fixture, _addition_fixture):
    """testing out get_result for a specific calculation in history"""
    assert Calculations.get_calculation(0).get_result() == 3
