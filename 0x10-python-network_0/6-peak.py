#!/usr/bin/python3
"""Module for Task 6: Finding a Peak"""


def find_peak(list_of_integers):
    """This function finds and returns a peak within an unsorted
    list of integers.
    """
    if list_of_integers == []:
        return None

    list_length = len(list_of_integers)
    if list_length == 1:
        return list_of_integers[0]
    elif list_length == 2:
        return max(list_of_integers)

    mid_value = int(list_length / 2)
    peak = list_of_integers[mid_value]
    if peak > list_of_integers[mid_value - 1]
    and peak > list_of_integers[mid_value + 1]:
        return peak
    elif peak < list_of_integers[mid_value - 1]:
        return find_peak(list_of_integers[:mid_value])
    else:
        return find_peak(list_of_integers[mid_value + 1:])
