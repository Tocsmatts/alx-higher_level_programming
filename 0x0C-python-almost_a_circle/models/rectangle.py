#!/usr/bin/python3
""" The module for rectangle """
from models.base import Base


class Rectangle(Base):
    """ class Rectangle inherites Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializing """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= than 0")
        self.__x = value

    @property
    def y(self):
        """ Getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= than 0")
        self.__y = value

    def area(self):
        """ Returns the area """
        return self.width * self.height

    def display(self):
        """ DIsplay a rectangle using # """
        ht = self.height
        while(ht > 0):
            print("#" * self.width, end='')
            print()
            ht -= 1

    def __str__(self):
        """ string """
        rec = "[Rectangle]"
        rec_id = " ({}) ".format(self.id)
        rec_xy = "{}/{} - ".format(self.x, self.y)
        rec_wh = "{}/{}".format(self.width, self.height)

        return rec + rec_id + rec_xy + rec_wh
