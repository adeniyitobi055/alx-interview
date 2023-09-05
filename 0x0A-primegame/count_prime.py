#!/usr/bin/python3
"""
count_prime helper function
"""
is_prime = __import__('is_prime').is_prime


def count_prime(n):
    """
    count number from `2` to `n` to check if they are
    prime number using `is_prime` function
    """
    count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            count += 1
    return count
