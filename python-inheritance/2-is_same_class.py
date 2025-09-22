#!/usr/bin/python3
"""
Module defining a function to check if an object is exactly
an instance of a given class.
"""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class."""
    return type(obj) is a_class
