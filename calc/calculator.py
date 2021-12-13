""" This is the increment function"""
from calc.history.calculations import Calculations

#the calculator class just contains the methods to calculate
class Calculator:
    """ This is the Calculator class"""
    #the calculator class just calls methods on Calculations class
    @staticmethod
    def get_last_result_value():
        """ This is the gets the result of the calculation"""
        # I made this method so that I don't have more than one action per function
        return Calculations.get_last_calculation_result_value()
    @staticmethod
    #tuple allows me to pass in as many values as a I want
    def addition(value_a,value_b):
        """ adds list of numbers"""
        Calculations.add_addition_calculation_to_history(value_a,value_b)
        # return True
        return Calculator.get_last_result_value()
    @staticmethod
    def subtraction(value_a,value_b):
        """ subtract a list of numbers from result"""
        Calculations.add_subtraction_calculation_to_history(value_a,value_b)
        # return True
        return Calculator.get_last_result_value()
    @staticmethod
    def multiplication(value_a,value_b):
        """ multiplication number from result"""
        Calculations.add_multiplication_calculation_to_history(value_a,value_b)
        # return True
        return Calculator.get_last_result_value()
    @staticmethod
    def division(value_a,value_b):
        """ multiplication number from result"""
        Calculations.add_division_calculation_to_history(value_a, value_b)
        # return True
        return Calculator.get_last_result_value()
    @staticmethod
    def get_history():
        """ Get history """
        return Calculations.history
    # @staticmethod
    # def getHistoryFromCSV():
    #     """ Get history """
    #     return Calculations.readHistoryFromCSV()
    # @staticmethod
    # def writeHistoryToCSV():
    #     """ Get history """
    #     return Calculations.writeHistoryToCSV()
