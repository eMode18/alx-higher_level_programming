#!/usr/bin/python3
"""class square definition"""


class Square:
    """a represenation of our square"""

    def __init__(self, size=0):
        """new square init
        Args:
            size (int): The dimentions of our square
        """
        self.size = size

    @property
    def size(self):
        """obtain the current dimetions of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the product calculation of size"""
        return (self.__size * self.__size)
