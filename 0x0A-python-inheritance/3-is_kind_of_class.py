#!/usr/bin/python3
"""Defines a function for checking if an object is an instance or inherited instance of a class."""


def is_kind_of_class(obj, a_class):
    """Determine whether obj is an instance of a_class or inherits from it.

    Args:
        obj (any): The object to examine.
        a_class (type): The class to compare the object's type to.
    Returns:
        True if obj is an instance or inherited instance of a_class, False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
