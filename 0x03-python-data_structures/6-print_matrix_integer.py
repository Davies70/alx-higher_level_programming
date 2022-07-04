#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    p = len(matrix[0])
    i = 0
    while i < p:
        print(*matrix[i])
        i += 1
