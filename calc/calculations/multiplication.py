"""Multiplication Class"""
from calc.calculations.calculation import Calculation

class Multiplication(Calculation):
    """subtraction calculation object"""
    def get_result(self):
        """get the multiplication results"""
        # result = 1.0
        # for value in self.values:
        #     result = result * value
        return self.value_a * self.value_b
