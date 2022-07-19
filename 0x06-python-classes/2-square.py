#!/usr/bin/python3
""" create a class Square """



class Square:
    """ initialize instance variable """
    def __init__(self, size=0):
        """ instanstialize the variable size """
        self.__size = size
        if isinstance(self.__size, int) == False:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError ("size must be >= 0")
