#!/usr/bin/python3
"""
Module: animals
Defines an abstract Animal class and concrete Dog and Cat subclasses.
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        ...


class Dog(Animal):
    """Class representing a dog."""

    def sound(self):
        """Return the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Class representing a cat."""

    def sound(self):
        """Return the sound of a cat."""
        return "Meow"
