#!/usr/bin/python3

"""Function to find the maximum integer in a list"""

def max_integer(list=[]):
    """This function searches for and returns the largest integer within a list of integers.
       In case of an empty list, the function returns None."""
    
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
