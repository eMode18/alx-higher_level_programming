#!/usr/bin/python3

if __name__ == "__main__":
    """Print list number and the corresponding arguments"""
    import sys

    tally = len(sys.argv) - 1
    if tally == 0:
        print("0 arguments.")
    elif tally == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(tally))
    for n in range(tally):
        print("{}: {}".format(n + 1, sys.argv[n + 1]))
