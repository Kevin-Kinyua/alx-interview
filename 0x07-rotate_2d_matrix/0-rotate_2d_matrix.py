def rotate_2d_matrix(matrix):
    """
    function that rotates a 2D matrix
    """
    n = len(matrix)
    for layer in range(n // 2):
        left = layer
        right = n - 1 - layer
        for i in range(left, right):
            top, bottom = layer, n - 1 - layer
            topleft = matrix[top][i]
            matrix[top][i] = matrix[bottom - (i - left)][left]
            matrix[bottom - (i - left)][left] = matrix[bottom][right - (i - left)]
            matrix[bottom][right - (i - left)] = matrix[top + (i - left)][right]
            matrix[top + (i - left)][right] = topleft
