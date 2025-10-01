#!/usr/bin/python3

import json


def serialize_and_save_to_file(data, filename):
    with open(filename, mode="w", encoding="utf-8") as File:
        return json.dump(data, File)

def load_and_deserialize(filename):
    with open(filename, encoding="utf-8") as File:
        return json.load(File)
