"""This is our calculation base class/Abstract class"""
#Calculation class can't do any calculation of it's own and needs a child class,these type of base classes are called Abstract class

class Calculation:
    #this below is called a constructor and it is the first function called when an object of the class is instantiated (created)
    def __init__(self, value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b
#class Factory Method
    @classmethod
    def create(cls, value_a, value_b):
        return cls(value_a,value_b)
