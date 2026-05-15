#!/usr/bin/env python3
'''
    def matrix_shape(matrix) calculates the shape of a matrix
'''


def matrix_shape(matrix):

    mat_shape = []
    while isinstance(matrix, list):
        mat_shape.append(len(matrix))
        matrix = matrix[0]
    return mat_shapie
