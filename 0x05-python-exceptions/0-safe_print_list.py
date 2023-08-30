#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
     """x list elements to be printed

    Args:
        my_list (list): a list containing elements to print
        x (int): elements to print

    Returns:
        total elemnts to print
    """
    try:
        tally = 0
        for ele in my_list:
            if tally < x:
                print(ele, end=" ")
                tally += 1
        print() """print new line"""
        return tally
    except:
        return tally
