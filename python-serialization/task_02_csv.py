#!/usr/bin/python3
"""Module to learn how to convert cvs files into json"""


import json
import csv


def convert_csv_to_json(file_name):
    """reads from a csv file and serializes it to a json"""
    with open(file_name, mode="r", newline="", encoding="utf-8") as csvfile:
        data = list(csv.DictReader(csvfile))
    with open("data.json", mode="w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile, indent=4)
