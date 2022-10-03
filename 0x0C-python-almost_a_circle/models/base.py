#!/usr/bin/python3
""" This module contains the class Base """


class Base:
    """ In the base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializations """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
