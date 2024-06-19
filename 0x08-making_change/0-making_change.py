#!/usr/bin/python3

"""makechange function"""


def makeChange(coins, total):
    """
    This function finds the minimun number of change given to a total
    Args:
        coins: This is a list of change/coin denominations available.
        total: This is the total amountn (int) for
        which change needs to be made.
    Returns:
        The function returns the minimum number of coins (int) needed to
        make change for the total or
        returns -1 if it's not possible to meet the total.
    """
    if (total <= 0):
        return 0
    # sort in a descending order. We are using greedy algorithm
    # making changes from highest coins first
    coins.sort(reverse=True)

    number_coins = 0  # total coins
    for coin in coins:
        if total == 0:
            break  # no more change can be given
        if coin <= total:
            count = round(total / coin)
            number_coins += count
            total -= coin * count
    # Total has reach 0 so no more change return the change now
    if (total == 0):
        return number_coins
    else:
        return -1
