#!/usr/bin/python3
"""Square class definition"""


class Square:
    """The square object representation"""

    def __init__(self, size=0):
        """Init the new square
        Args:
            size (int): represents dimetions of our new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the value found after squaring size"""
        return (self.__size * self.__size)
