#!/usr/bin/python3
"""
0-making_change module
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins for each value from 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: zero coins needed to make zero total

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    if dp[total] == float('inf'):
        return -1  # Cannot make the total with the given coins
    else:
        return dp[total]
