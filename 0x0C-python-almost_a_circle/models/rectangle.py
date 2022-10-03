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
        rec  = self.y * "\n"
        for a in range(self.height):
            rec += (" " * self.x)
            rec += ("#" * self.width) + "\n"

        print(rec, end='')

    def __str__(self):
        """ string """
        rec = "[Rectangle]"
        rec_id = " ({}) ".format(self.id)
        rec_xy = "{}/{} - ".format(self.x, self.y)
        rec_wh = "{}/{}".format(self.width, self.height)

        return rec + rec_id + rec_xy + rec_wh

    def update(self, *args, **kwargs):
        """ update """
        if len(args) != 0 and args is not None:
            list_atr = ['id', 'width', 'height', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns a dictionary """
        atr_list = ['id', 'width', 'height', 'x', 'y']
        new_dict = {}

        for key in atr_list:
            new_dict[key] = getattr(self, key)

        return new_dict
