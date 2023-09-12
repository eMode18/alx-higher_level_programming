#!/usr/bin/python3
"""This module defines a Rectangle class that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle and leverages the functionality provided by BaseGeometry."""

    def __init__(self, width, height):
        """Init a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Provide a string representation of the Rectangle for print() and str() methods."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
