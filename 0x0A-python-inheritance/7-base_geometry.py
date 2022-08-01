#!/usr/bin/python3
""" BaseGeomentary module """


class BaseGeometry:
    """ class declaration """

    def area(self):
        """ area method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator method"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be an greater than 0".format(name))
