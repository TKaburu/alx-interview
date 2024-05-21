#!/usr/bin/python3

"""
Minimum number of operations
"""


def minOperations(n):
    """
    This method calculates the the fewest number of operations
    needed
    """
    if n < 2:
        return 0

    prime_factor = 2
    operations = 0

    while n > 1:
        while n % prime_factor == 0:
            operations += prime_factor
            n /= prime_factor
        prime_factor += 1

    return operations
