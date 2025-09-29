#!/usr/bin/python3
"""Module for the creation of the Student class"""


class Student:
    """Class representing a student with first name, last name, and age."""
    def __init__(self, first_name, last_name, age):
        """Initialize a Student with given first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation of a Student instance"""
        return self.__dict__
