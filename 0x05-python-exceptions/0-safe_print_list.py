#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    tally = 0
    for e in range(x):
        try:
            print(my_list[e], end="")
        tally += 1
        except IndexError:
            break
    print("")
    return
