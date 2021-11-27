""" This is the increment function"""
#first import the addition namespace from addition file
from calc.addition import Addition
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication

class Calculator:
    """ This is the Calculator class"""
#this is the calculator static property
    history = []

    @staticmethod
    def get_result_of_first_calculation_added_to_history():
        return Calculator.history[0].getresult()

    @staticmethod
    def clear_history():
            Calculator.history.clear()
            return True

    @staticmethod
    def history_count():
            return len(Calculator.history)

#to put it in the history static property
    @staticmethod
    def add_calculation_to_history(calculation):
        Calculator.history.append(calculation)
        return True

    @staticmethod
    def get_result_of_calculation_added_to_history():
        #-1 gets the last item added to the list automatically
        Calculator.history[-1].getresult()

    @staticmethod
    def add_number(value_a, value_b):
        """adds number to result"""
        #create an addition object
        addition = Addition.create(value_a, value_b)
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_result_of_calculation_added_to_history()

    @staticmethod
    def subtract_number(value_a, value_b):
        """subtract number to result"""
        #create an subtraction object
        subtraction = Subtraction.create(value_a, value_b)
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_result_of_calculation_added_to_history()

    @staticmethod
    def multiply_number(value_a, value_b):
        """multiply number to result"""
        #create an subtraction object
        multiplication = Multiplication.create(value_a, value_b)
        Calculator.add_calculation_to_history(multiplication)
        return Calculator.get_result_of_calculation_added_to_history()