#!/usr/bin/python3
""" BaseGeomentary module """


class BaseGeometry:
    """ class declaration """

    def area(self):
        """ area method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator method"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


""" Rectangle module """


class Rectangle(BaseGeometry):
    """ classs Rectangle inherits from class BG"""

    def __init__(self, width, height):
        """ attributes initiatlization """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)
