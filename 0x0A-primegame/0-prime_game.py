#!/usr/bin/python3

""" The Prime Game """


def find_prime(n):
    """
    Finds the prime numbers between 1 and n
    Args:
    n : highest number in the list
    """
    num = 2  # This is the smallest prime number in the array list
    prime = []
    while num <= n:
        prime_num = True  # assuming the number is alread a prime number
        # if num has a divisor greater than the square root
        # it must be divisible by number smaller than the square root
        # thats why we are using square root
        for x in range(2, int(num ** 0.5) + 1):
            if num % x == 0:
                prime_num = False  # because it is not a prime number
                break
        # add the prime number to the list
        if prime_num:
            prime.append(num)
        num += 1  # on to the next number
    return prime


def isWinner(x, nums):
    """
    Determins the winner of a game depending on the strategic removal \
        of prime numbers and their multiples from a set of consecutive integers
    Args:
        x : The number of rounds to play
        nums : an array of n
    Return:
        The player that wins
    """
    # variables that hold each players wins
    bens_wins = 0
    marias_wins = 0

    # Play the game
    #  n is highest number in the list
    for n in nums:
        prime_nums = find_prime(n)
        #  maria wins if the len of the prime numbers is odd
        # since only odd nums have a reminder of 1 when divided by 2
        maria_wins_game = len(prime_nums) % 2 == 1
        # add winner of each round to the variables
        if maria_wins_game:
            marias_wins += 1
        else:
            bens_wins += 1

    # the winner is
    if bens_wins > marias_wins:
        return 'Ben'
    elif marias_wins > bens_wins:
        return 'Maria'
    else:
        return 'There is no winner'
