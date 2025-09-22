#!/usr/bin/python3
"""
Module defining BaseGeometry class with an abstract area method.
"""


class BaseGeometry:
    """Base class providing area method to be implemented by subclasses."""

    def area(self):
        """Raise an exception; to be implemented by subclasses."""
        raise Exception("area() is not implemented")
