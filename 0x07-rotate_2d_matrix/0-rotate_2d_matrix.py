#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """
    function that rotates a 2D matrix
    """
    left = 0
    right = len(matrix) - 1
    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            topleft = matrix[top][left + i]
            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = topleft
        left += 1
        right -= 1