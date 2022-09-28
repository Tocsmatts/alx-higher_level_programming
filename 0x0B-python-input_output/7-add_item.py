#!/usr/bin/python3
""" Script that adds all arguments to a Python list,
and then save them to a file
"""
import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

new_list = []
if os.path.exists("add_item.json"):
    new_list = load_from_json_file("add_item.json")

for ag in sys.argv[1:]:
    new_list.append(ag)

save_to_json_file(new_list, "add_item.json")
