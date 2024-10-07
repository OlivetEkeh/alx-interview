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

    # Initialize the dp array to store the minimum number of coins for each amount.
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # It takes 0 coins to make a total of 0.

    # Loop through each coin and each amount to update the dp array.
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means we couldn't form the amount.
    return dp[total] if dp[total] != float('inf') else -1
