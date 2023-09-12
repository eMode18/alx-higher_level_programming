#!/usr/bin/python3
"""Defines a function for appending text to a file."""

def append_write(filename="", text=""):
    """Append a string to the end of a UTF-8 encoded text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended to the fi_le.
    """
    with open(filename, "a", encoding="utf-8") as fi_le:
        return fi_le.write(text)
