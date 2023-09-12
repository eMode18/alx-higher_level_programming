#!/usr/bin/python3
"""This module defines a Square class that is a subclass of Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square shape."""

    def __init__(self, size):
        """Init a new square instance.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
