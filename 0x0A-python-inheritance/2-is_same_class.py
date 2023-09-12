#!/usr/bin/python3
"""Defines a function to verify if an object matches a specific class."""


def is_same_class(obj, a_class):
    """Determine whether obj is an instance of a_class.

    Args:
        obj (any): The object to examine.
        a_class (type): The class for comparison with obj's type.
    Returns:
        True if obj is an instance of a_class, False otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
