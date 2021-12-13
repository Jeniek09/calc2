"""Division Class"""
from calc.calculations.calculation import Calculation

#This is how you extent the Division class with the calculation
class Division(Calculation):
    """The division class has one method to get the result of the calculation A and B come
    from the calculation parent class"""
    def get_result(self):
        """get the multiplication results"""
        return self.value_a / self.value_b
