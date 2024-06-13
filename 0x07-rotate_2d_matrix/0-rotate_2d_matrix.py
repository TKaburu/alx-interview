#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise.

    Args:
        matrix (list[list]): The 2D matrix to rotate.

    Returns:
        None
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
