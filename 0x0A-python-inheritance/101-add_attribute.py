#!/usr/bin/python3
"""Defines a function for adding attributes to objects."""


def add_attribute(obj, att, value):
    """Attempt to add a new attribute to an object if possible.

    Args:
        obj (any): The object to which the attribute will be added.
        att (str): The name of the attribute to add.
        value (any): The value of the new attribute.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add a new attribute")
    setattr(obj, att, value)
