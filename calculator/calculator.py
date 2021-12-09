""" This is the increment function"""
class Calculator:
    """ This is the Calculator class"""
    result = 0
    history =[]
    def get_result(self):
        """ Get Result of Calculation"""
        return self.result

    @staticmethod
    def add_numbers(value_a, value_b):
        """ adds two numbers and store the result"""
        return value_a + value_b
