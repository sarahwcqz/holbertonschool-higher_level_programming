#!/usr/bin/python3
"""
Module defining Rectangle class inheriting from BaseGeometry.
"""


class BaseGeometry:
    """Base class providing area method and integer validation."""

    def area(self):
        """Raise an exception; to be implemented by subclasses."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if not value > 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class with private width and height."""

    def __init__(self, width, height):
        """Initialize rectangle and validate dimensions."""
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height
