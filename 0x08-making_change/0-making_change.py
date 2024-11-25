#!/usr/bin/python3

"""
 a function that determines the fewest coins needed to meet a given amount using a specified set of denominations
"""

def makeChange(coins, total):
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        if total <= 0:
            break
        count += total // coin
        total %= coin

    return count if total == 0 else -1

