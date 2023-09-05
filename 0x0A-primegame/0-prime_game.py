#!/usr/python3
"""
0-prime_game module
"""


def isWinner(x, nums):
    """
    Args:
        x: is the number of rounds.
        nums: is an array of integers representing
        the values of `n` for each round.
    
    Returns:
        the name of the player that won the most rounds,
        if the winner cannot be determined, None is returned.
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
