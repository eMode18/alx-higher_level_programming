#!/usr/bin/python3
"""create a Rectangle class."""
from models.base import Base

class Rectangle(Base):
    """Represents a geometric rectangle shape."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
            id (int): The unique identifier for the rectangle.

        Raises:
            TypeError: If width, height, x, or y is not an integer.
            ValueError: If width, height, x, or y are not within valid ranges.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, new_width):
        if type(new_width) != int:
            raise TypeError("width must be an integer")
        if new_width <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_width

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, new_height):
        if type(new_height) != int:
            raise TypeError("height must be an integer")
        if new_height <= 0:
            raise ValueError("height must be > 0")
        self.__height = new_height

    @property
    def x(self):
        """Get or set the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, new_x):
        if type(new_x) != int:
            raise TypeError("x must be an integer")
        if new_x < 0:
            raise ValueError("x must be >= 0")
        self.__x = new_x

    @property
    def y(self):
        """Get or set the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, new_y):
        if type(new_y) != int:
            raise TypeError("y must be an integer")
        if new_y < 0:
            raise ValueError("y must be >= 0")
        self.__y = new_y

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Display the rectangle using the '#' character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for _ in range(self.y)]
        for _ in range(self.height):
            [print(" ", end="") for _ in range(self.x)]
            [print("#", end="") for _ in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the attributes of the rectangle.

        Args:
            *args (ints): New attribute values in the order: id, width, height, x, y.
            **kwargs (dict): New attribute key-value pairs.
        """
        if args and len(args) != 0:
            arg_index = 0
            for arg_value in args:
                if arg_index == 0:
                    if arg_value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg_value
                elif arg_index == 1:
                    self.width = arg_value
                elif arg_index == 2:
                    self.height = arg_value
                elif arg_index == 3:
                    self.x = arg_value
                elif arg_index == 4:
                    self.y = arg_value
                arg_index += 1

        elif kwargs and len(kwargs) != 0:
            for attr_name, new_value in kwargs.items():
                if attr_name == "id":
                    if new_value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = new_value
                elif attr_name == "width":
                    self.width = new_value
                elif attr_name == "height":
                    self.height = new_value
                elif attr_name == "x":
                    self.x = new_value
                elif attr_name == "y":
                    self.y = new_value

    def to_dictionary(self):
        """Convert the rectangle's attributes to a dictionary."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return a human-readable string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

