#!/usr/bin/python3
""" This program converts json to object """
import json


def from_json_string(my_str):
    """ converts to object """

    return json.loads(my_str)
