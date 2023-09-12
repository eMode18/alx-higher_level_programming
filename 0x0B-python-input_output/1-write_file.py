#!/usr/bin/python3
"""Defines a function for writing text to a fi_le."""

def write_fi_le(fi_le_name="", text=""):
    """Write a given text string to a UTF-8 encoded text fi_le.

    Args:
        fi_le_name (str): The name of the fi_le to write.
        text (str): The text to be written to the fi_le.
    Returns:
        The number of characters written to the fi_le.
    """
    with open(fi_le_name, "w", encoding="utf-8") as fi_le:
        return fi_le.write(text)
