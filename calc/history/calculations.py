"""Calculation history Class"""
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division

class Calculations:
    """Calculations class manages the history of calculations"""
    history = []

    # @staticmethod
    # def readHistoryFromCSV():
    #     """Read the history from csv and put it into the history """
    # @staticmethod
    # def writeHistoryToCSV():
    #     """Write the history to csv file"""
    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """clear the history of calculations"""
        Calculations.history.clear()
        return True
    @staticmethod
    def count_history():
        """get number of items in history"""
        return len(Calculations.history)
    @staticmethod
    def get_last_calculation_object():
        """get last calculation"""
        return Calculations.history[-1]
    @staticmethod
    def get_last_calculation_result_value():
        """get last calculation"""
        calculation = Calculations.get_last_calculation_object()
        return calculation.get_result()
    @staticmethod
    def get_first_calculation():
        """get first calculation"""
        return Calculations.history[0]
    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]
    @staticmethod
    def add_calculation(calculation):
        """ get a generic calculation from history"""
        return Calculations.history.append(calculation)
    @staticmethod
    def add_addition_calculation_to_history(value_a,value_b):
        """create an addition and add object to history using factory method create"""
        Calculations.add_calculation(Addition.create(value_a,value_b))
        #Get the result of the calculation
        return True
    @staticmethod
    def add_subtraction_calculation_to_history(value_a,value_b):
        """create a subtraction object to history using factory method create"""
        Calculations.add_calculation(Subtraction.create(value_a,value_b))
        return True
    @staticmethod
    def add_multiplication_calculation_to_history(value_a,value_b):
        """Add a multiplication object to history using factory method create"""
        Calculations.add_calculation(Multiplication.create(value_a,value_b))
        return True
    @staticmethod
    def add_division_calculation_to_history(value_a,value_b):
        """Add a division object to history using factory method create"""
        Calculations.add_calculation(Division.create(value_a,value_b))
        return True
