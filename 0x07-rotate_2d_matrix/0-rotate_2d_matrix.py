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

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
