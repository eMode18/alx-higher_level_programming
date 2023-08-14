#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for elmnt in row:
            print("{:d}".format(elmnt), end=" " if elmnt != row[-1] else "")
        print()
