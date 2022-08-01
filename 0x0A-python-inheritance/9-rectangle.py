#!/usr/bin/python3

"""
A module for BaseGeometry class.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class."""

    def __init__(self, width, height):
        """Initialize the rectangle class."""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
