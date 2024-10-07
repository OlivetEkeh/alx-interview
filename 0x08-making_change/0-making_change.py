#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.
"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to make the given total.
    
    :param coins: List of integers representing the coin values.
    :param total: Integer representing the total amount.
    :return: Minimum number of coins needed to make the total, or -1 if it's not possible.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0.

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
