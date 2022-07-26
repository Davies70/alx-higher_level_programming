#!/usr/bin/python3
""" creating module """


class Rectangle:
    """ class created """

    def __init__(self, width=0, height=0):
        """ init method """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ method return areas """
        return self.__height * self.__width

    def perimeter(self):
        """ method that returns perimeter """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """ string printer """
        if self.__width == 0 or self.__height == 0:
            return ""
        return ((("#" * self.width) + "\n") * self.height)[:-1]

    def __repr__(self):
        """ repr string """
        return 'Rectangle(' + str(self.width) + ', ' + str(self.height) + ')'
