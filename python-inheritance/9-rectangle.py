#!/usr/bin/python3
"""Module to import BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle, inheriting from BaseGeometry."""
    def __init__(self, width, height):
        """
        Initialize a new Rectangle.

        Args: width , height
        """

        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the current rectangle area
        """
        return self.__height * self.__width

    def __str__(self):
        """
        Return a string representation of the rectangle.
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
