#!/usr/bin/env python


def reverse_row(matrix, line):
    matrix[0].reverse()

    return matrix


def reverse_col(matrix, col):
    col_values = [r[col] for r in matrix]

    for i in range(0, len(matrix)):
        matrix[i][col] = col_values.pop()

    return matrix


def change(matrix):
    sums = [sum_result(matrix)]
    for i, r in enumerate(matrix):
        print(reverse_row(matrix, i))
        sums.append(sum_result(reverse_row(matrix, i)))
        for j, c in enumerate(r):
            print(reverse_col(matrix, j))
            sums.append(sum_result(reverse_col(matrix, j)))

    return max(sums)


def sum_result(matrix):
    line_1 = sum(matrix[0][:2])
    line_2 = sum(matrix[1][:2])

    return line_1 + line_2


if __name__ == '__main__':
    pass
