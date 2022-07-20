#!/usr/bin/python3
""" class made for a square """


class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def size(self):
        self.__size
    def size(self, value):
        self.__size = value

    def area(self):
        return self.__size**2
