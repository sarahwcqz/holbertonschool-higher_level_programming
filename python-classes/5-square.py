#!/usr/bin/python3

"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a Square instance.
        Attributes: size (int): The size of the square.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the current square area."""
        return (self.__size ** 2)

    @property
    def size(self):
        """Gets the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.
        Args: value (int): The new size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints the square with the character # to stdout.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
