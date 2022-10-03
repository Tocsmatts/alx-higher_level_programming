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

    def update(self, *args, **kwargs):
        """ update method """
        if args is not None and len(args) != 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ returns a dictionary """
        atr_list = ['id', 'size', 'x', 'y']
        new_dict = {}

        for key in atr_list:
            new_dict[key] = getattr(self, key)

        return new_dict
