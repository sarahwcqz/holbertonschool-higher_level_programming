#!/usr/bin/python3
"""Module to learn how to serailize/deserialize with json"""


import json


def serialize_and_save_to_file(data, filename):
    """serializes using json"""
    with open(filename, mode="w", encoding="utf-8") as File:
        return json.dump(data, File)


def load_and_deserialize(filename):
    """deserializes using json"""
    with open(filename, encoding="utf-8") as File:
        return json.load(File)
