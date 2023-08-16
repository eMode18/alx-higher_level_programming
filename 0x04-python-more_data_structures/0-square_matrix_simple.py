#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for num in range(len(matrix)):
        new_matrix[num] = list(map(lambda n: n**2, matrix[i]))

    return (new_matrix)
