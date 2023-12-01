#!/usr/bin/python3
"""Module for Task 6: Finding a Peak"""


def find_peak(list_of_integers):
    """This function finds and returns a peak within an unsorted
    list of integers.
    """
    if not list_of_integers:
        return None
    list_left = 0
    list_right = len(list_of_integers) - 1
    while list_left < list_right:
        mid = (list_left + list_right) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            list_right = mid
        else:
            list_left = mid + 1
    return list_of_integers[list_left]
