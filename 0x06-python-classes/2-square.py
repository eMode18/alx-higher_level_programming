#!/usr/bin/python3
"""Square class definition"""


class Square:
    """illustrate the square"""

    def __init__(self, size=0):
        """constructor that init new square size
        Args:
            size (int): new square dimentions
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
