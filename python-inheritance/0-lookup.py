#!/usr/bin/python3
"""
Module defining a function to list available attributes and methods of an object.
"""

def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    return list(dir(obj))
