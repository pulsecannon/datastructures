"""Defines spiral traversal."""

def spiral_traversal(matrix):
    if not matrix:
        return matrix
    min_row, max_row = 0, len(matrix) - 1
    min_col, max_col = 0, len(matrix[0]) - 1
    output = []
    while min_row <= max_row and min_col <= max_col:
        for c in range(min_col, max_col + 1):
            output.append(matrix[min_row][c])
        for r in range(min_row + 1, max_row + 1):
            output.append(matrix[r][max_col])
        if min_row < max_row and min_col < max_col:
            for c in range(max_col - 1, min_col - 1, -1):
                output.append(matrix[max_row][c])
            for r in range(max_row - 1, min_row, -1):
                output.append(matrix[r][min_col])
        min_col += 1
        min_row += 1
        max_row -= 1
        max_col -= 1
    return output
