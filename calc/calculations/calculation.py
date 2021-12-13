"""Calculation Class"""
class Calculation:
    """ calculation abstract base class"""
    # pylint: disable=too-few-public-methods
    def __init__(self,value_a,value_b):
        """ constructor method"""
        self.value_a = value_a
        self.value_b = value_b
    @classmethod
    def create(cls,value_a,value_b):
        """ factory method"""
        return cls(value_a,value_b)
    # @staticmethod
    # def convert_args_to_tuple_of_float(values: tuple):
    #     """ standardize values to list of floats"""
    #     #lists can be modified and tuple cannot, tuple are faster.
    #     #We need to convert the tuple of potentially random data types (its raw data)
    #     #into a standard data format to keep things consistent so we convert it to float
    #     #then i make it a tuple again because i actually won't need to change the calculation values
    #     #I can also use it as a list and then i would be able to edit the calculation
    #     list_values_float = []
    #     for item in values:
    #         list_values_float.append(float(item))
    #     return tuple(list_values_float)
