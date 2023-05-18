#!/usr/bin/python3
"""Module for Task 0: Making change
"""

def makeChange(coins, total):
    """Making change
    """

    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)

    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
