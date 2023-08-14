#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for length in matrix:
        for height in length:
            print("{:n}".format(height), end=" " if height != length[-1] else "")
        print()
