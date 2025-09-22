#!/usr/bin/python3
"""
Return attributes defined in an object's __dict__.
"""


def lookup(obj):
    """List attribute names of obj."""
    return list(obj.__dict__)
