#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

""" Rectangle module """


class Rectangle(BaseGeometry):
    """ classs Rectangle inherits from class BG"""
    def __init__(self, width, height):
        """ attributes initiatlization """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
