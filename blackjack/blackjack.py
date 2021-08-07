"""
This module contains all the functions necessary for the correct
functioning of the blackjack game.
"""
from blackjack.deck import Deck
from blackjack.hand import Hand
from blackjack.currency import Currency


def init_deck() -> Deck:
    """
    Initializes the deck

    Returns:
        The deck of cards initialized and shuffled
    """

    # Initializes deck and shuffles it
    d = Deck()
    d.shuffle()

    return d
