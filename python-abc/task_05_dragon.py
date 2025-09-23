#!/usr/bin/python3
"""
Module: dragon_mixin
Contains mixins for swimming and flying, and a Dragon class
combining these abilities.
"""


class SwimMixin:
    """Mixin adding swimming capability to a class."""
    def swim(self):
        """Displays that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Mixin adding flying capability to a class."""
    def fly(self):
        """Displays that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a dragon that can swim, fly, and roar."""
    def roar(self):
        """Makes the dragon roar."""
        print("The dragon roars!")
