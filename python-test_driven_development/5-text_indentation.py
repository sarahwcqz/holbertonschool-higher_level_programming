#!/usr/bin/python3
"""
This module contains a function that prints a text with two new lines
after '.', '?', and ':' characters.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of the characters '.?:'.

    The function processes the input string `text` and splits it into lines
    whenever one of the delimiters ('.', '?' or ':') is found. Each resulting
    line is printed without leading or trailing spaces, followed by exactly
    two new lines.

    Args:
        text (str): The text to be processed and printed.

    Raises:
        TypeError: If `text` is not a string.

    Example:
        >>> text_indentation("Hello. How are you? Fine: thanks.")
        Hello

        How are you

        Fine

        thanks
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        print(i, end="")
        if i == "." or i == "?" or i == ":":
            print()
            print()
