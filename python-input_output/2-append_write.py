#!/usr/bin/python3
"""Module for appending text to a file."""


def append_write(filename="", text=""):
    """Appends text to a file and returns the number of characters added."""

    with open(filename, mode="a", encoding="utf-8") as MyFile:
        MyFile.write(text)
        return len(text)
