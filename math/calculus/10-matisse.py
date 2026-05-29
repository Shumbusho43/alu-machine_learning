#!/usr/bin/env python3
"""
Calculates the derivative of a polynomial
"""

def poly_derivative(poly):
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    # derivative terms: i * a[i], starting from power 1
    result = []
    for i in range(1, len(poly)):
        result.append(poly[i] * i)

    # If derivative is empty or all zeros → return [0]
    if len(result) == 0 or all(x == 0 for x in result):
        return [0]

    return result
