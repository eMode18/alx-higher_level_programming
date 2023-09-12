#!/usr/bin/python3
"""Defines a function for checking if an object is an inherited instance of a class."""


def inherits_from(obj, a_class):
    """Verify if obj is an inherited instance of a_class.

    Args:
        obj (any): The object to examine.
        a_class (type): The class to compare the object's type to.
    Returns:
        True if obj is an inherited instance of a_class, False otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
