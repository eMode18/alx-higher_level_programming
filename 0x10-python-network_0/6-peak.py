#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    Peak list item

    Args:
    - list_of_integers: Unsorted integer list.

    Returns:
    - If exists, peak list element, otherwise None.
    """

    # Check if the list is empty
    if not list_of_integers:
        return None

    # Initialize low and high indices for binary search
    low, high = 0, len(list_of_integers) - 1

    # Binary search to find a peak
    while low < high:
        mid = (low + high) // 2

        # If mid element is less than its adjacent element, search in the right half
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        # Otherwise, search in the left half
        else:
            high = mid

    # Return the found peak element
    return list_of_integers[low]

