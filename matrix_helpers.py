def slice_iterator_h(matrix):
    """Iterates over the matrix horizontally including the index of the line"""
    for i, line in enumerate(matrix):
        yield i, line


def slice_iterator_v(matrix):
    """Iterates over the matrix vertically including the index of the line"""
    for i, line in enumerate(zip(*matrix)):
        yield i, line

def replace_line_h(matrix, index, new_line):
    """Set a line into the matrix horizontally"""
    matrix[index] = new_line

def replace_line_v(matrix, index, new_line):
    """Set a line into the matrix vertically"""
    for i, cell in enumerate(new_line):
        matrix[i][index] = cell

def set(matrix, row, col, value):
    matrix[row][col] = value

def is_done(matrix):
    """Checks if the matrix is done"""
    for line in matrix:
        for cell in line:
            if cell is None:
                return False
    return True


def is_square(matrix):
    """Checks if the matrix is a square"""
    return all(len(line) == len(matrix) for line in matrix)


def is_valid(matrix):

    # Check if more than two of the same number are next to each other
    for i in range(len(matrix)):
        for j in range(len(matrix) - 2):
            if (matrix[i][j] is not None and matrix[i][j] == matrix[i][j + 1] and matrix[i][j + 1] == matrix[i][j + 2]) or (
                    matrix[j][i] is not None and matrix[j][i] == matrix[j + 1][i] and matrix[j + 1][i] == matrix[j + 2][i]):
                return False

    # Check for each column if there are more than 50% 0s or 1s
    for i, line in slice_iterator_v(matrix):
        count_0 = line.count(0)
        count_1 = line.count(1)
        if line.count(0) > len(line)/2 or line.count(1) > len(line)/2:
            return False

    # Check for each row if there are more than 50% 0s or 1s
    for i, line in slice_iterator_h(matrix):
        if line.count(0) > len(line)/2 or line.count(1) > len(line)/2:
            return False

    # CHeck if rows or columns are duplicated
    matrix_t = list(zip(*matrix))

    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            # rows
            if matrix[i].count(None) == 0 and matrix[i] == matrix[j]:
                return False
            # columns
            if matrix_t[i].count(None) == 0 and matrix_t[i] == matrix_t[j]:
                return False

    return True