#!/usr/bin/python3
"""Module for the creation of the Student class"""


class Student:
    """Class representing a student with first name, last name, and age."""
    def __init__(self, first_name, last_name, age):
        """Initialize a Student with given first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance"""
        if isinstance(attrs, list) and all(isinstance(attr_given, str)
                                           for attr_given in attrs):
            result = {}
            for attr_given in attrs:
                if hasattr(self, attr_given):
                    result[attr_given] = getattr(self, attr_given)
            return result
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
