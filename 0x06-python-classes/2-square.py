#!/usr/bin/python3
""" Class Square defined """


class Square:
    """ Square class created """

    def __init__(self, size=0):
        """ Square initialized with
        Args:
             size (int): size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError ("size must be >= 0")
        self.__size = size
