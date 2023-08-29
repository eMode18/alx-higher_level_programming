#!/usr/bin/python3
"""class square defination"""
class Square:
    def __init__(self, size=0):

        """square init

        Args:
            size: type int, new square size
        """

        self.size = size

    @property
    def size(self):

        """get curr size of square"""

        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """find area"""
        return (self.__size * self.__size)
