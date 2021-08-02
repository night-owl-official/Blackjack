"""
This module holds the Hand class
"""
from collections import Sequence

from blackjack.card import Card


class Hand:
    """
    This class allows you to instantiate a hand of cards,
    which is what the players and the dealer use to play blackjack.
    """
    
    def __init__(self, cards: Sequence[Card]):
        """
        Initializes an instance of the Hand class.
        """

        self._cards = cards

    @property
    def cards(self) -> Sequence[Card]:
        """
        Gets all the cards in the hand

        Returns:
            The list of cards in hand
        """

        return self._cards
