#!/usr/bin/python3
"""
Module: flying_fish
Defines classes for Fish, Bird, and a FlyingFish that inherits from both.
"""


class Fish:
    """Class representing a fish."""
    def swim(self):
        """Displays that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Displays the habitat of the fish."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""
    def fly(self):
        """Displays that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Displays the habitat of the bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a flying fish, combining fish and bird abilities."""
    def fly(self):
        """Displays that the flying fish is soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Displays that the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Displays the habitat of the flying fish (water and sky)."""
        print("The flying fish lives both in water and the sky!")
