from rules import *

RULES = [(rule_equal_numbers_next_to_each_other, "no triplets or more horizontally"),
         (rule_equal_numbers_above_each_other, "no triplets or more vertically"),
         (rule_sandwich_h, "tripplet sandwich rule horizontally"),
         (rule_sandwich_v, "tripplet sandwich rule vertically"),
         (rule_half_half_h, "half half rule horizontally"),
         (rule_half_half_v, "half half rule vertically")]

COMPLEX_RULES = [(rule_complex_three_consecutive_h, "complex three consecutive rule horizontally"),
                    (rule_complex_three_consecutive_v, "complex three consecutive rule vertically"),
]


def read_input_file(filename: str):
    with open(filename, "r") as f:
        lines = f.readlines()
        matrix = []
        for line in lines:
            line = line.strip()
            line = [int(x) if x != "-" else None for x in line]
            matrix.append(line)
        if not is_square(matrix):
            raise Exception("Matrix is not square")
        return matrix



def solve(matrix):
    """Solves the matrix"""
    while not is_done(matrix):
        old_matrix = [line[:] for line in matrix]
        for rule, name in RULES:
            matrix_ = [line[:] for line in matrix]
            rule(matrix_)
            if matrix_ == matrix:
                continue
            print("Rule: " + name)
            print_matrix_diff(matrix_, matrix)
            matrix = matrix_
        if old_matrix == matrix:
            print("No more rules apply - try complex rules")
            for complex_rule, name in COMPLEX_RULES:
                matrix_ = [line[:] for line in matrix]
                complex_rule(matrix_)
                if matrix_ == matrix:
                   continue
                print("Rule: " + name)
                print_matrix_diff(matrix_, matrix)
                matrix = matrix_
            if old_matrix == matrix:
                print("No more rules apply - even complex rules")
                return matrix
            print("Complex rules applied - try simple rules again")

    print("Done!")
    print(is_valid(matrix))
    return matrix



def solve2(matrix, row=0, col=0):
    """Solves the matrix"""
    while not is_done(matrix):
        old_matrix = [line[:] for line in matrix]
        for rule, name in RULES:
            matrix_ = [line[:] for line in matrix]
            rule(matrix_)
            if matrix_ == matrix:
                continue
            print("Rule: " + name)
            print_matrix_diff(matrix_, matrix)
            matrix = matrix_
        if old_matrix == matrix:
            print("No more rules apply - try backtracking")



    print("Done!")
    return matrix








def print_matrix(matrix):
    for line in matrix:
        for cell in line:
            if cell is None:
                print("_", end="")
            else:
                print(cell, end="")
        print()
    print()


def print_matrix_diff(matrix_new, matrix_old):
    for i, line in enumerate(matrix_new):
        for j, cell in enumerate(line):
            if cell is None:
                print("_", end="")
            else:
                if cell != matrix_old[i][j]:
                    print('\033[1m' + '\033[91m' + str(cell) + '\033[0m', end="")
                else:
                    print(cell, end="")
        print()
    print()

if __name__ == '__main__':
    result = read_input_file("input/6x6_1.txt")
    print_matrix(result)
    solve(result)