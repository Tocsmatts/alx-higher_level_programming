#!/usr/bin/python3

""" This is the doc module """


class MyList(list):
    """ The class inherits the attribute of the class """
    def print_sorted(self):
        """ Method prints sorted lists """
        s = self.copy()
        s.sort()
        print(s)
