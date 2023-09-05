#!/usr/bin/python3


"""This function defines an addition method for two integers."""


def add_integer(a, b=98):
    """Return the addition result (int).
    Also, typecast floats to int before addition
    Raise:
        TypeError: If a or/and b is neither int or float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
