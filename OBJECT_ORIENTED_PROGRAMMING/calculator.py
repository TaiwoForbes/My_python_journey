import math
"""
    Write a class calculator capable of finding square,cube and squareroot of a number
"""

class Calculator:
    """
    This class calculate square,cube and sqaure root of a given number
    """

    def __init__(self, num):
        self.num = num
    def square(self):
        """ Calculates the square """
        return self.num * self.num
    def cube(self):
        """ Calculates the cube"""
        return self.num * self.num * self.num
    def square_root(self):
        """ Calculates the square root"""
        return math.sqrt(self.num)

calculation = Calculator(4)
print("The square of {} is {}".format(calculation.num, calculation.square()))
print("The cube of {} is {}".format(calculation.num, calculation.cube()))
print("The square_root of {} is {}".format(calculation.num, calculation.square_root()))