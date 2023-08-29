from rules import *
import os
import sys

RULES = [(rule_equal_numbers_next_to_each_other, "no triplets or more horizontally"),
         (rule_equal_numbers_above_each_other, "no triplets or more vertically"),
         (rule_sandwich_h, "tripplet sandwich rule horizontally"),
         (rule_sandwich_v, "tripplet sandwich rule vertically"),
         (rule_half_half_h, "half half rule horizontally"),
         (rule_half_half_v, "half half rule vertically"),
         (rule_no_double_row, "no double row"),
         (rule_no_double_col, "no double col"),
         ]

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

def solve_backtracking(matrix, row = 0, col = 0):
    N = len(matrix)
    if row == N - 1 and col == N:
        return True

    if col == N:
        row += 1
        col = 0

    if matrix[row][col] is not None:
        return solve_backtracking(matrix, row, col + 1)

    for num in [0, 1]:
        matrix [row][col] = num
        if is_valid(matrix) and solve_backtracking(matrix, row, col+1):
            return True
        matrix[row][col] = None
    return False


def print_matrix(matrix):
    for line in matrix:
        for cell in line:
            char = "_" if cell is None else cell
            print(char, end="")
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

def test():
    for filename in os.listdir('solutions'):
        solution = read_input_file(f"solutions/{filename}")
        input = read_input_file(f"input/{filename}")

        solve_backtracking(input)
        if solution != input:
            print("ERROR")
            print_matrix_diff(input, solution)
            return False
    print("SUCCESS")
    return True


if __name__ == '__main__':

    if len(sys.argv) == 1:
        print("Error: no argument")
        exit(1)

    # Join multiple arguments into one filename
    filename = " ".join(sys.argv[1:])

    # read the input and print it
    matrix = read_input_file(f"input/{filename}")
    print("The input is:")
    print_matrix(matrix)

    # solve the input and if successful print it
    res = solve_backtracking(matrix, 0, 0)
    if res:
        print("The solution is:")
        print_matrix(matrix)
    else:
        print("Could not solve the puzzle")