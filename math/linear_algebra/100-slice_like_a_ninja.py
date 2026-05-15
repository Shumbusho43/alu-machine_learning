#!/usr/bin/env python3
'''
    Function def np_slice(matrix, axes):
    slices matrix along axes
'''


def np_slice(matrix, axes):
    '''
        Function def np_slice(matrix, axes):
        slices matrix along axes
    '''
    slices_matrix = [slice(None)] * len(matrix.shape)

    for axis, value in axes.items():
        slices_matrix[axis] = slice(*value)

    return matrix[tuple(slices_matrix)]
