#!/usr/bin/python3

""" Function checks inheritance """


def inherits_from(obj, a_class):
    """ FUnction checks inheritance """

    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
