#!/usr/bin/python3
"""Module for writing text to a file."""


def write_file(filename="", text=""):
    """Writes text to a file and returns the number of characters written."""
    with open(filename, mode="w", encoding="utf-8") as MyFile:
        MyFile.write(text)
    return (len(text))
