#!/usr/bin/python3
"""
The minOperations(n) function calculates the fewest number of operations needed to create exactly n characters in a text file using only two operations
"""

def minOperations(n):
    if n <= 1:
        return 0

    operation = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operation += divisor
            n //= divisor
        divisor += 1

    return operation

