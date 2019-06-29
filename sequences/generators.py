import random
from itertools import product

ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
suits = ['H', 'D', 'C', 'S']


# Method 1
def cards1():
    """Returns a generator that yields playing cards"""
    for rank in ranks:
        for suit in suits:
            yield rank, suit


# Method 2
cards2 = ((rank, suit) for rank in ranks for suit in suits)

# Method 3
cards3 = product(ranks, suits)


def shuffle(deck):
    """Returns iterator over shuffled deck"""
    deck = list(deck)
    random.shuffle(deck)

    return iter(tuple(deck))


cards = shuffle(cards3)

print(next(cards))
