#!/usr/bin/python3
"""Create a class named square"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Represents a geometric square shape."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): The unique identifier for the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get or set the size of the Square."""
        return self.width

    @size.setter
    def size(self, new_size):
        self.width = new_size
        self.height = new_size

    def update(self, *args, **kwargs):
        """Update the attributes of the square.

        Args:
            *args (ints): New attribute values in the order: id, size, x, y.
            **kwargs (dict): New attribute key-value pairs.
        """
        if args and len(args) != 0:
            arg_index = 0
            for arg_value in args:
                if arg_index == 0:
                    if arg_value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg_value
                elif arg_index == 1:
                    self.size = arg_value
                elif arg_index == 2:
                    self.x = arg_value
                elif arg_index == 3:
                    self.y = arg_value
                arg_index += 1

        elif kwargs and len(kwargs) != 0:
            for attr_name, new_value in kwargs.items():
                if attr_name == "id":
                    if new_value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = new_value
                elif attr_name == "size":
                    self.size = new_value
                elif attr_name == "x":
                    self.x = new_value
                elif attr_name == "y":
                    self.y = new_value

    def to_dictionary(self):
        """Convert the square's attributes to a dictionary."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return a human-readable string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

