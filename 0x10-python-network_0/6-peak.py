#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    Peak list item

    Args:
    - list_of_integers: Unsorted integer list.

    Returns:
    - If exists, peak list element, otherwise None.
    """
    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    smallest = 0
    is_peak = len(list_of_integers)

    while smallest <= is_peak:
        mid_value = (smallest + is_peak) // 2

        if (mid_value == 0 or list_of_integers[mid_value]
            >= list_of_integers[mid_value - 1]) and \
           (mid_value == len(list_of_integers) - 1 or
                list_of_integers[mid_value] >= list_of_integers[mid_value
                                                                + 1]):
            return list_of_integers[mid_value]

        if mid_value < len(list_of_integers) - 1 and
        list_of_integers[mid_value] < list_of_integers[mid_value + 1]:
            smallest = mid_value + 1
        else:
            is_peak = mid_value - 1

    return None
