#!/usr/bin/python3
"""square class definition"""

class Square:
    """square representation"""

    def __init__(self, size):
         """Init the square.

        Args:
            size: private integer that represents new square size
        """
        self.size = size

    @property
    def size(self)i:
        """obtain the current area"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculate the area and return the value"""
        return (self.__size * self.__size)

    def my_print(self):
        """use the character # to print the square"""
        for dig in range(0, self.__size):
            [print("#", end="") for val in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")

