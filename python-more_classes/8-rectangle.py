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
        number_of_instances (int): Counts the number of Rectangle instances
        created.
        print_symbol (int): Used as symbol for string representation, # by
        default.
    """

    number_of_instances = 0

    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the rectangle with the bigger or equal area.

        Args:
            rect_1 (Rectangle): First rectangle to compare.
            rect_2 (Rectangle): Second rectangle to compare.

        Returns:
            Rectangle: The rectangle with the greater or equal area.

        Raises:
            TypeError: If either rect_1 or rect_2 is not a Rectangle instance.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    def __str__(self):
        """
        Return a string representation of the rectangle using the # character.

        Returns:
            str: The string representation of the rectangle.
                If either `width` or `height` is 0, return an empty string.
        """
        if self.height == 0 or self.width == 0:
            return ("")
        else:
            return "\n".join("{}".format(self.print_symbol) * self.width
                             for i in range(self.height))

    def __repr__(self):
        """
        Return an official string representation of the rectangle.

        Returns:
            str: A string in the form 'Rectangle(width, height)'.
        """
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """
        Print a message when the rectangle instance is deleted.

        Returns:
            None
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
