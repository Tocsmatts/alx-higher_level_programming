#!/usr/bin/python3
""" This program writes object to ffile in json representation """
import json


def save_to_json_file(my_obj, filename):
    """ function writes to file """

    with open(filename, 'w', encoding="utf=8") as x:
        json.dump(my_obj, x)
