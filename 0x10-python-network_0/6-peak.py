#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    Peak list item

    Args:
    - list_of_integers: Unsorted integer list.

    Returns:
    - If exists, peak list element, otherwise None.
    """

    if list_of_integers is None or list_of_integers == []:
        return None
    least = 0
    is_peak = len(list_of_integers)
    mid = ((is_peak - least) // 2) + least
    mid = int(mid)
    if is_peak == 1:
        return list_of_integers[0]
    if is_peak == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
