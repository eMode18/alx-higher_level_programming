#!/usr/bin/python3

"""A function to print a square."""

def print_square(size):
    """Use the chr # to print a square
    Args:
        size (int): Dimentions of the square.
    Raises:
        TypeError: if size is not of type int.
        ValueError: If size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")


    for l in range(size):
        [print("#", end="") for h in range(size)]
        print("")
