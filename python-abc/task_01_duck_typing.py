#!/usr/bin/python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for shapes.
    """

    @abstractmethod
    def area(self):
        """
        Calculate and return the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate and return the perimeter of the shape.

        Returns:
            float: The perimeter of the shape.
        """
        pass


def shape_info(shape):
    """
    Print the area and perimeter of a given shape.

    Args:
        shape (Shape): The shape object to get information about.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


class Circle(Shape):
    """
    A class representing a circle.
    """

    def __init__(self, radius):
        """
        Initialize a Circle object.

        Args:
            radius (float, optional): The radius of the circle.
        """
        self.radius = abs(radius)

    def area(self):
        """
        Calculate and return the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius**2

    def perimeter(self):
        """
        Calculate and return the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    A class representing a rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle object.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return (self.__height + self.__width) * 2
