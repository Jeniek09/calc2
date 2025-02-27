"""Addition Class"""
from calc.calculations.calculation import Calculation

class Addition(Calculation):
    """ calculation addition class"""
    # pylint: disable=too-few-public-methods
    def get_result(self):
        """get the addition results"""
        # sum_of_values = 0.0
        # for value in self.values:
        #     sum_of_values = value + sum_of_values
        # return sum_of_values
        return self.value_a + self.value_b
