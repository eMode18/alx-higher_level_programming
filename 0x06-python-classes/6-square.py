#!/usr/bin/python3
"""square class definition"""

class Square:
    """square representition"""

    def __init__(self, size=0, position=(0, 0)):
         """Init the square.

        Args:
            size: private integer that represents new square size
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """obtain the current area"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """obtain the current square pos"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(x, int) for x in value) or
                not all(x >= 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculate area and return the value"""
        return (self.__size * self.__size)

    def my_print(self):
        """use # to graphically represent the square"""
        if self.__size == 0:
            print("")
            return

        [print("") for dig in range(0, self.__position[1])]
        for dig in range(0, self.__size):
            [print(" ", end="") for val in range(0, self.__position[0])]
            [print("#", end="") for l in range(0, self.__size)]
            print("")

