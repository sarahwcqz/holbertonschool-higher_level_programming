#!/usr/bin/python3
"""Module for reading and printing the content of a text file."""


def read_file(filename=""):
    """Prints the full content of a file given its filename."""
    with open(filename, encoding="utf-8") as MyFile:
        print(MyFile.read(), end="")
