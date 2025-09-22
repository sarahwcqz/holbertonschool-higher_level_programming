#!/usr/bin/python3
"""
Module defining MyList class that extends the built-in list.
"""


class MyList(list):
    """Custom list class with an additional method to print
    a sorted version."""

    def print_sorted(self):
        """Print the elements of the list in ascending order."""
        print(sorted(self))
