#!/usr/bin/python3
"""Module to learn how to serialize/deserialize with pickle"""


import pickle


class CustomObject:
    """class containing a name, an age, and a bool to know if the person is a
    student"""

    def __init__(self, name, age, is_student):
        """initializes the object"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """prints a representation of the object"""
        print(
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Is Student: {self.is_student}"
            )

    def serialize(self, filename):
        """serializes to a file using pickle"""
        try:
            with open(filename, mode="wb") as File:
                pickle.dump(self, File)
        except PermissionError:
            print("Permission denied")
            return None
        except OSError:
            print("error with OS")
            return None

    @classmethod
    def deserialize(cls, filename):
        """deserializes from a file using pickle"""
        try:
            with open(filename, "rb") as File:
                return pickle.load(File)
        except FileNotFoundError:
            print("File not found.")
            return None
        except pickle.UnpicklingError:
            print("Corrupted or malformed file")
            return None
