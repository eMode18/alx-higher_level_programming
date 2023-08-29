#!/usr/bin/python3
"""Square class definition"""


class Square:
    """square representation"""

    def __init__(self, size=0):
         """Init the square.

        Args:
            size: private integer that represents new square size
        """
        self.size = size

    @property
    def size(self):
        """obtain the current size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calcuate the square and return the value"""
        return (self.__size * self.__size)

