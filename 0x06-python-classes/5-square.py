#!/usr/bin/python3
""" creating a Square class """


class Square:
    """ a class with private instance attribute size """

    def __init__(self, size=0):
        """ init method """

        self.__size = size

    @property
    def size(self):
        """ getter method that returns size """

        return self.__size

    @size.setter
    def size(self, value):
        """ setter method """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ public instance method to return area of square """

        return self.__size ** 2

    def my_print(self):
        """ public intance method that prints square """

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
