#!/usr/bin/env python3
"""
Module that calculates the derivative of a polynomial
"""


def poly_derivative(poly):
    """
    Compute the derivative of a polynomial.

    Args:
        poly (list): coefficients of the polynomial where index
                     represents the power of x.

    Returns:
        list: coefficients of the derivative polynomial,
              [0] if derivative is zero,
              None if input is invalid.
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    result = [poly[i] * i for i in range(1, len(poly))]

    if len(result) == 0 or all(x == 0 for x in result):
        return [0]

    return result
