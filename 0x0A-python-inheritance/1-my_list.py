#!/usr/bin/python3
"""Defines MyList - inherited class"""


class MyList(list):
    """use sorted printing via the inherited built-in class"""

    def print_sorted(self):
        """Print a sorted list"""
        print(sorted(self))
