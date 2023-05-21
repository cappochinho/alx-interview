#!/usr/bin/python3
"""Task 0 module"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix
    """

    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i] = matrix[i][::-1]
