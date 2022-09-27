#!/usr/bin/python3
""" The program appends a file and returns the number of characters added """


def append_write(filename="", text=""):
    """ function appends to file """

    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)

    no = 0

    fx = text
    for x in fx:
        no += 1
    return no
