#!/usr/bin/python3
""" The module for class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializations """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str """
        sq = "[Square]"
        sq_id = " ({}) ".format(self.id)
        sq_xy = "{}/{} - ".format(self.x, self.y)
        sq_sz = "{}".format(self.width)

        return sq + sq_id + sq_xy + sq_sz

    @property
    def size(self):
        """ Getter """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter """
        self.width = value
        self.height = value
