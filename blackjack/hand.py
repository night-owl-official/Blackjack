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

        self._cards = list(cards)

    @property
    def cards(self) -> Sequence[Card]:
        """
        Gets all the cards in the hand

        Returns:
            The list of cards in hand
        """

        return self._cards

    def __str__(self) -> str:
        """
        Allows to print out a hand of cards

        Returns:
            The string displaying all the cards in hand
        """

        hand_string = "=================\n"
        hand_string += '\n'.join(str(card) for card in self._cards)
        hand_string += "\n================="
        return hand_string

    def hit(self, card: Card):
        """
        Adds a new card to the list of cards in the hand

        Parameters:
            card (Card): The card to add to the hand
        """

        self._cards.append(card)

    def clear(self):
        """
        Removes all cards from a hand
        """

        self._cards.clear()
