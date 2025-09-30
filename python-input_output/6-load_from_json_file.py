#!/usr/bin/python3
"""Module to create an object from a .json"""


import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename, encoding="utf-8") as MyFile:
        return json.load(MyFile)
