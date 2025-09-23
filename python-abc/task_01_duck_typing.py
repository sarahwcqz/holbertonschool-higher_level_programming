#!/usr/bin/python3
"""
Module: shapes
Defines abstract and concrete shape classes with area and perimeter methods.
"""


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        ...

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        ...


class Circle(Shape):
    """Class representing a circle."""

    def __init__(self, radius):
        """Initialize circle with a radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return "Area: {}".format(pi * self.radius ** 2)

    def perimeter(self):
        """Return the perimeter of the circle."""
        return "Perimeter: {}".format(2 * pi * self.radius)


class Rectangle(Shape):
    """Class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return "Area: {}".format(self.width * self.height)

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return "Perimeter: {}".format(2 * (self.width + self.height))


def shape_info(shape):
    """Print area and perimeter of a given shape."""
    print(shape.area())
    print(shape.perimeter())
