

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
    for i in range(len(matrix)):
        for j in range(len(matrix) - 2):
            if (matrix[i][j] == matrix[i][j + 1] and matrix[i][j + 1] == matrix[i][j + 2]) or (
                    matrix[j][i] == matrix[j + 1][i] and matrix[j + 1][i] == matrix[j + 2][i]):
                return False

    for line in slice_iterator_v(matrix):
        if line.count(0) > len(line)/2 or line.count(1) > len(line)/2:
            return False

    for line in slice_iterator_h(matrix):
        if line.count(0) > len(line)/2 or line.count(1) > len(line)/2:
            return False


    return True