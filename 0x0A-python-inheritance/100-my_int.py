#!/usr/bin/python3
"""Defines a custom class MyInt, which inherits from int and modifies the behavior of == and != operators."""

class MyInt(int):
    """Reverses the behavior of int's == and != operators."""

    def __eq__(self, value):
        """Modify the == operator to behave like !=."""
        return self.real != value

    def __ne__(self, value):
        """modify the != operator to behave like ==."""
        return self.real == value
