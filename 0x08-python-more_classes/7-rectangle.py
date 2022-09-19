#!/usr/bin/python3

""" This is the module doc """


class Rectangle:
    """Initializing rectagle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return int(self.__width) * int(self.__height)

    def perimeter(self):
        if int(self.__width) == 0 or int(self.__height) == 0:
            return 0
        else:
            return (2 * int(self.__width)) + (2 * int(self.__height))

    def __str__(self):
        rectangle_print = ""

        if int(self.__width) == 0 or int(self.__height) == 0:
            return rectangle_print
        for i in range(self.height):
            rectangle_print += ("#" * self.width) + '\n'

        return rectangle_print[:-1]

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
