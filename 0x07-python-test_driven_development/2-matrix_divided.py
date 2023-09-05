#!/usr/bin/python3

"""A function that divides a matrix"""


def matrix_divided(matrix, div):
    """Function to divide through every matrix element
    Args:
        matrix (list): a list made of lists of floats or ints.
        div (int/float): value to divide by.
    Raises:
        TypeError: For non-numbers
        TypeError: For matrix with different row sizes
        TypeError: if div is neither float or int
        ZeroDivisionError: If div is 0.
    Returns:
        new matrix containing division results
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(val, int) or isinstance(val, float))
                    for val in [mat for row in matrix for mat in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")


    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")


    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")


    if div == 0:
        raise ZeroDivisionError("division by zero")


    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
