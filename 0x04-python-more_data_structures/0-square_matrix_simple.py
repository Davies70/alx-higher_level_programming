#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_max = []
    for i in range(len(matrix)):
        squared = list(map(lambda a: a * a, matrix[i]))
        new_max.append(squared)

    return new_max
