#!/usr/bin/python3
"""The square class definition"""


class Square:
    """an illustration of the square"""

    def __init__(self, size):
        """new square init
        Args:
            size (int): the new square dimentions
        """
        self.size = size

    @property
    def size(self):
        """obtain the current dimentions of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the product of size squared"""
        return (self.__size * self.__size)

    def my_print(self):
        """Use the # character to print the square"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
