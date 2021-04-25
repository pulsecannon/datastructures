"""To check if sudoku is valid."""


def get_3by3_index(row, col):
    return 3 * (row // 3) + col // 3


def is_valid_sudoku(matrix):
    row_set = [set() for _ in range(9)]
    col_set = [set() for _ in range(9)]
    grid_set = [set() for _ in range(9)]
    for row in range(9):
        for col in range(9):
            val = matrix[row][col]
            if val == '.':
                continue
            if val in row_set[row]:
                return False
            else:
                row_set[row].add(val)

            if val in col_set[col]:
                return False
            else:
                col_set[col].add(val)

            grid_idx = get_3by3_index(row, col)
            if val in grid_set[grid_idx]:
                return False
            else:
                grid_set[grid_idx].add(val)
    return True
