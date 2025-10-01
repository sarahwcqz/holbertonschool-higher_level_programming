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
        with open(filename, mode="wb") as File:
            pickle.dump(self, File)
    
    @classmethod
    def deserialize(cls, filename):
        """deserializes from a file using pickle"""
        with open(filename, "rb") as File:
            return pickle.load(File)
