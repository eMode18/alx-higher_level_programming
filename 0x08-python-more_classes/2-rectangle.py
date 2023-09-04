#!/usr/bin/python3
"""Rectangle class definition"""


class Rectangle:
    """Declaratin of the rectangle class"""

    def __init__(self, width=0, height=0):
        """rectangle class init

        Args:
            width (int): represents the width of the object rectangle
            height (int): represents the height of the object rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """init the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """init the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
	if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate and return the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """calculate and return the value of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
