#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    tally = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
            print("{:d}".format(my_list[i]), end="")
            tally += 1
        except (ValueError, TypeError):
            pass
    print()
    return
