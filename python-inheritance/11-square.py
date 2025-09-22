#!/usr/bin/python3
"""
Module defining geometric shapes with area calculation.
"""


class BaseGeometry:
    """Base class providing area and integer validation methods."""

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

    def __str__(self):
        """Return string representation of the rectangle."""
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__width, self.__height)

    def area(self):
        """Return the area of the rectangle."""
        return self.__height * self.__width


class Square(Rectangle):
    """Square class inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize square with a given size."""
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """Return string representation of the square."""
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__size, self.__size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
