#!/usr/bin/python3
"""Module for converting Python objects to JSON strings."""


import json


def to_json_string(my_obj):
    """Returns the JSON string representation of a Python object."""
    s_obj = json.dumps(my_obj)
    return s_obj
