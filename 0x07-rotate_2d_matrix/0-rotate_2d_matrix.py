#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """
    This function otates a 2d matrix 90 degrees clockwise
    """
    length = len(matrix)

    # Transpose the matrix
    for row in range(length):
        for col in range(row, length):
            matrix[col][row], matrix[row][col] = matrix[row][col], \
                matrix[col][row]

    # Reverse each row
    for row in range(length):
        matrix[row] = matrix[row][::-1]
