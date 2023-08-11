#!/usr/bin/python3

if __name__ == "__main__":
    """Sum arguments"""
    import sys

    my_sum = 0
    for n in range(len(sys.argv) - 1):
        my_sum += int(sys.argv[n + 1])
    print("{}".format(my_sum))
