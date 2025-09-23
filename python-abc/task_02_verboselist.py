#!/usr/bin/python3
"""
Module: verbose_list
Defines a custom list subclass that logs operations like append,
extend, remove, and pop.
"""


class VerboseList(list):
    """List subclass that prints messages when modified."""

    def append(self, item):
        """Append an item and print a message."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        """Extend the list and print a message."""
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        """Remove an item and print a message, or print if not found."""
        if item not in self:
            print("Couldn't remove {} from list, not found.".format(item))
        else:
            super().remove(item)
            print("Removed [{}] from the list.".format(item))

    def pop(self, item=None):
        """Pop an item (last by default) and print a message."""
        if item is None:
            removed = super().pop()
            print("Popped [{}] from the list.".format(removed))
        else:
            removed = super().pop(item)
            print("Popped [{}] from the list.".format(removed))
