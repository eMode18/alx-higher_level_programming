#!/usr/bin/python3
"""program defines a class named square"""


class Square:
    """This class will represent a square"""

    def __init__(self, size=0):
        """Init the square.

        Args:
            size: private integer that represents new square size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
