#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    An abstract base class representing an animal.

    This class serves as a template for creating specific animal classes.
    It defines an abstract method 'sound' that all subclasses must implement.
    """
    pass

    @abstractmethod
    def sound(self):
        """
        An abstract method to represent the sound made by the animal.

        This method should be implemented by all subclasses.

        Returns:
            str: The sound made by the animal.
        """
        pass


class Dog(Animal):
    """
    A class representing a dog, inheriting from the Animal class.
    """
    def sound(self):
        """
        Implements the sound method for a dog.

        Returns:
            str: The sound a dog makes ("Bark").
        """
        return ("Bark")


class Cat(Animal):
    """
    A class representing a cat, inheriting from the Animal class.
    """
    def sound(self):
        """
        Implements the sound method for a cat.

        Returns:
            str: The sound a cat makes ("Meow").
        """
        return ("Meow")
