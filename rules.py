from matrix_helpers import *

def rule_equal_numbers_next_to_each_other(matrix):

    for i, line in slice_iterator_h(matrix):
        line = line[:]
        for j, cell in enumerate(line):
            if cell is None:
                continue
            if j == 0:
                continue
            if line[j-1] == cell:
                if j+1 < len(line):
                    if line[j+1] is None:
                        line[j+1] = 1 if cell == 0 else 0
                if j-2 >= 0:
                    if line[j-2] is None:
                        line[j-2] = 1 if cell == 0 else 0
        replace_line_h(matrix, i, line)


def rule_equal_numbers_above_each_other(matrix):

    for i, line in slice_iterator_v(matrix):
        line = list(line)
        for j, cell in enumerate(line):
            if cell is None:
                continue
            if j == 0:
                continue
            if line[j-1] == cell:
                if j+1 < len(line):
                    if line[j+1] is None:
                        line[j+1] = 1 if cell == 0 else 0
                if j-2 >= 0:
                    if line[j-2] is None:
                        line[j-2] = 1 if cell == 0 else 0
        replace_line_v(matrix, i, line)


def rule_sandwich_h(matrix):

    for i, line in slice_iterator_h(matrix):
        line = line[:]
        for j, cell in enumerate(line):
            if j == 0 or j == len(line)-1:
                continue
            if cell is None:
                if line[j-1] != None and line[j-1] == line[j+1]:
                    line[j] = 1 if line[j-1] == 0 else 0
        replace_line_h(matrix, i, line)

def rule_sandwich_v(matrix):

    for i, line in slice_iterator_v(matrix):
        line = list(line)
        for j, cell in enumerate(line):
            if j == 0 or j == len(line)-1:
                continue
            if cell is None:
                if line [j-1] != None and line[j-1] == line[j+1]:
                    line[j] = 1 if line[j-1] == 0 else 0
        replace_line_v(matrix, i, line)

def rule_half_half_h(matrix):

    for i, line in slice_iterator_h(matrix):
        line = line[:]
        if line.count(0) == len(line)/2:
            for j, cell in enumerate(line):
                if cell is None:
                    line[j] = 1
        if line.count(1) == len(line)/2:
            for j, cell in enumerate(line):
                if cell is None:
                    line[j] = 0
        replace_line_h(matrix, i, line)

def rule_half_half_v(matrix):

    for i, line in slice_iterator_v(matrix):
        line = list(line)
        if line.count(0) == len(line)/2:
            for j, cell in enumerate(line):
                if cell is None:
                    line[j] = 1
        if line.count(1) == len(line)/2:
            for j, cell in enumerate(line):
                if cell is None:
                    line[j] = 0
        replace_line_v(matrix, i, line)

def rule_no_double_row(matrix):
    for i, line in slice_iterator_h(matrix):
        line = line[:]
        if line.count(0) == (len(line)/2)-1 and line.count(0) == line.count(1):
            for x, line_x in slice_iterator_h(matrix):
                if i == x: continue
                if helper_is_same(line, line_x):
                    for j in range(len(line)):
                        if line[j] == None:
                            if line_x[j] == 0: line[j] = 1
                            if line_x[j] == 1: line[j] = 0
                    replace_line_h(matrix, i, line)

def rule_no_double_col(matrix):
    for i, line in slice_iterator_v(matrix):
        line = list(line)
        if line.count(0) == (len(line)/2)-1 and line.count(0) == line.count(1):
            for x, line_x in slice_iterator_v(matrix):
                if i == x: continue
                if helper_is_same(line, line_x):
                    for j in range(len(line)):
                        if line[j] == None:
                            if line_x[j] == 0: line[j] = 1
                            if line_x[j] == 1: line[j] = 0
                    replace_line_v(matrix, i, line)

def helper_is_same(row1, row2):
    # row1 is row to be filled:
    if row2.count(None) != 0: return False
    for j in range(len(row1)):
        if row1[j] == None: continue
        if row1[j] != row2[j]: return False

    return True


def rule_complex_three_consecutive_h(matrix):

    for i, line in slice_iterator_h(matrix):
        line = line[:]
        if line.count(None) != 3:
            continue
        for j, cell in enumerate(line):
            if j == 0 or j == 1 or j == len(line)-2 or j == len(line)-1:
                continue
            if cell is None:
                if line[j-1] == None and line[j+1] == None:
                    if line.count(1) > line.count(0):
                        if j-2 >= 0 and line[j-2] == 0:
                            line[j+1] = 0
                        elif j+2 < len(line) and line[j+2] == 0:
                            line[j-1] = 0
                    elif line.count(0) > line.count(1):
                        if j-2 >= 0 and line[j-2] == 1:
                            line[j+1] = 1
                        elif j+2 < len(line) and line[j+2] == 1:
                            line[j-1] = 1

        replace_line_h(matrix, i, line)


def rule_complex_three_consecutive_v(matrix):

    for i, line in slice_iterator_v(matrix):
        line = list(line)
        if line.count(None) != 3:
            continue
        for j, cell in enumerate(line):
            if j == 0 or j == 1 or j == len(line)-2 or j == len(line)-1:
                continue
            if cell is None:
                if line[j-1] == None and line[j+1] == None:
                    if line.count(1) > line.count(0):
                        if j-2 >= 0 and line[j-2] == 0:
                            line[j+1] = 0
                        elif j+2 < len(line) and line[j+2] == 0:
                            line[j-1] = 0
                    elif line.count(0) > line.count(1):
                        if j-2 >= 0 and line[j-2] == 1:
                            line[j+1] = 1
                        elif j+2 < len(line) and line[j+2] == 1:
                            line[j-1] = 1

        replace_line_v(matrix, i, line)