#!/usr/bin/python3
"""Module to import Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class Square that inherits from Rectangle.
    """
    def __init__(self, size):
        """
        Initialize a new Square.

        Args: size.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the current square area.
        """
        return self.__size * self.__size
