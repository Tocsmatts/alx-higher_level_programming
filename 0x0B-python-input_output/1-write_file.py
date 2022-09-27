#!/usr/bin/python3
""" Program that writes to a file """


def write_file(filename="", text=""):
    """ function writes to a file and counts the characters written """

    line_no = 0

    with open(filename, "w", encoding="utf-8") as myFile:
        myFile.write(text)

    with open(filename, encoding="utf-8") as myFile:
        mFile = myFile.read()

    for x in mFile:
        line_no += 1

    return line_no
