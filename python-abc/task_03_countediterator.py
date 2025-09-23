#!/usr/bin/python3
"""
Module: counted_iterator
Defines an iterator that counts how many items have been retrieved.
"""


class CountedIterator:
    """Iterator wrapper that counts the number of items iterated."""

    def __init__(self, some_iterable):
        """Initialize with an iterable and set counter to zero."""
        self.iterator = iter(some_iterable)
        self.counter = 0

    def __iter__(self):
        """Return the iterator itself."""
        return self

    def __next__(self):
        """Return the next item and increment the counter."""
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """Return the number of items iterated so far."""
        return self.counter
