#!/usr/bin/python3
"""Rectangle class definition"""


class Rectangle:
    """Declaration of the rectangle class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Rectangle class init

        Args:
            width (int): Represents the width of the rectangle.
            height (int): Represents the height of the rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self) -> int:
        """Calculate and return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self) -> int:
        """Calculate and return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Provide a printable version of the rectangle, displaying it using the '#' character"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectObj = []
        for h in range(self.__height):
            [rectObj.append(str(self.print_symbol)) for w in range(self.__width)]
            if h != self.__height - 1:
                rectObj.append("\n")
        return "".join(rectObj) + "\n"

    def __repr__(self):
        """String representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Display a delete message and decrement the instance count"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
