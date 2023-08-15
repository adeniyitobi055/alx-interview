#!/usr/bin/python3
"""
rotate_2d_matrix module
"""


def rotate_2d_matrix(matrix):
    """
    rotates a 2d matrix 90 degrees clockwise

    Args:
        matrix: A 2d list of lists.
    
    Rotates the matrix in place
    """

    n = len(matrix)

    for layer in range(n // 2):
        first = layer
        last = n - layer - 1

        for i in range(first, last):
            temp = matrix[first][i]
            matrix[first][i] = matrix[last - i][first]
            matrix[last - i][first] = matrix[last][last - i]
            matrix[last][last - i] = matrix[i][last]
            matrix[i][last] = temp
            