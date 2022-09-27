#!/usr/bin/python3

""" The program that reads file """


def read_file(filename=""):
    """ function reads text file """

    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read())
