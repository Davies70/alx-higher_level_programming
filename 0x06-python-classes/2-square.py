#!/usr/bin/python3
""" module doc """


class Square:
    """ Square class created """

    def __init__(self, size=0):
        """ square initialized with arg size, self """
        self.__size = size
        if isinstance(self.__size, int) == False:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError ("size must be >= 0")
