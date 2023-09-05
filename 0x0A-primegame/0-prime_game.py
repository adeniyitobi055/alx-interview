#!/usr/bin/python3
"""
0-prime_game module
"""
count_prime = __import__('count_prime').count_prime


def isWinner(x, nums):
    """
    Returns the name of the player that won the most rounds,
    if the winner cannot be determined, None is returned.
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        num_primes = count_prime(n)
        if num_primes % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
