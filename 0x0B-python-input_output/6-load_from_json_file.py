#!/usr/bin/python3
""" progran converts json file to object """
import json


def load_from_json_file(filename):
    """ json file to object """

    with open(filename, 'r', encoding="utf-8") as x:
        return json.load(x)
