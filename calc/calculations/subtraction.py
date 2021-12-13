"""Subtraction Class"""
from calc.calculations.calculation import Calculation

class Subtraction(Calculation):
    """subtraction calculation object"""
    def get_result(self):
        """get the subtraction results"""
        # difference_of_values = 0.0
        # for value in self.values:
        #     difference_of_values =   difference_of_values - value
        #     pprint.pprint(value)
        return self.value_a - self.value_b
