#!/usr/bin/python3
""" square module """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class created """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
