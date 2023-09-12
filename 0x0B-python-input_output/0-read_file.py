#!/usr/bin/python3
"""This module contains a function to read and display the contents of a text file."""

def read_file(filename=""):
    """Read the content of a UTF-8 encoded text file and print it to the standard output.

    Args:
        filename (str): The name of the text file to read.
    """
    with open(filename, encoding="utf-8") as fi_le:
        print(fi_le.read(), end="")
