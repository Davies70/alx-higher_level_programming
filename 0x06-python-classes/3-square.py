#!/usr/bin/python3
""" Area of the square."""

class Square:
    """Creating the class."""

    def __init__(self, size=0):
        """Initialize object attribute.

        Args:
            self (obj): object name
            size (int): size of square

        Returns:
               Nothing

        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ method that returns area

        Args:
            self (obj): object name

        Returns:
               area
        """
        return self.__size**2


