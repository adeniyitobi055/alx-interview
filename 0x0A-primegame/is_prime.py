#!/usr/bin/python3
"""
is_prime helper function
"""


def is_prime(n):
        """
        checks if a given number `n` is prime
        """
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        
        i = 5
        while i * i <= 5:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True