#!/usr/bin/python3
"""
Module rectangle
Defines a Rectangle class with width and height validation.
"""


class Rectangle:
    """
    Represents a rectangle with a given width and height.

    Attributes:
        __width (int): The private width of the rectangle.
        __height (int): The private height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): Width of the rectangle (default 0).
            height (int): Height of the rectangle (default 0).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is < 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for the rectangle width.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the rectangle width.

        Args:
            value (int): New width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value < 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the rectangle height.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the rectangle height.

        Args:
            value (int): New height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value < 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of a rectangle.

        Returns:
        The area of the rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """
        Calculates the perimeter of a rectangle.

        Returns:
        The perimeter of the rectangle
        """
        return 2 * (self.height + self.width)
