#!/usr/bin/python3
"""Defines a class named BaseGeometry."""


class BaseGeometry:
    """Represents fundamental geometric operations."""

    def area(self):
        """Raises an unimplemented exception for calculating area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer parameter.

        Args:
            name (str): The parameter name.
            value (int): The value to be validated.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is non-positive.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
