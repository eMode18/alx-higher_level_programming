#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using the functionality provided by BaseGeometry."""

    def __init__(self, width, height):
        """Init a new Rectangle.

        Args:
            width (int): new Rectangle's width.
            height (int): new Rectangle's height.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
