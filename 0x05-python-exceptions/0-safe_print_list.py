#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """elements (x) to print
    Args:
        my_list (list): list containg elements to be printed
        x (int): represents number of items to print
    Returns:
        x printed items
    """
    tally = 0
    for e in range(x):
        try:
            print("{}".format(my_list[e]), end="")
            tally ++
        except IndexError:
            break
    print("")
    return (tally)
