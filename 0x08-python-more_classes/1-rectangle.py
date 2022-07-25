#!/usr/bin/python3
""" module created """


class Rectangle:
    """ innit method created with arg width, height """

    def __init__(self, width=0, height=0):
        """ innit method for instance """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        else:
            self.__width = value

    @property
    def height(self):
        """ getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ getter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
