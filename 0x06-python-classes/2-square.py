#!/usr/bin/python3

"""square class definition"""

class Square:
    """class to represent a square"""

    def __init__(self, size=0):

         """square init

        Args:
            size: type int, new square size
        """


        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
