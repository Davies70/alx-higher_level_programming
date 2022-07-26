#!/usr/bin/python3
""" creating module """


class Rectangle:
    """ class created """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ init method """

        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        w = self.__width
        h = self.__height
        return (((str(self.print_symbol) * w) + "\n") * h)[:-1]

    def __repr__(self):
        """ repr string """
        return 'Rectangle(' + str(self.width) + ', ' + str(self.height) + ')'

    def __del__(self):
        """destructor """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2
        if rect_1.area() == rect_2.area():
            return rect_1

    @classmethod
    def square(cls, size=0):
        cls.__width = size
        cls.__height = size
        new_instance = Rectangle(cls.__width, cls.__height)
        return new_instance
