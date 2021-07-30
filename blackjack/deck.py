"""
This module holds the Deck class.
"""
from blackjack.card import Card


class Deck:
    """
    This class allows you to instantiate a deck of cards
    as well as access its methods.
    """

    # All the card suits in the deck
    card_suits = ("Clubs",
                  "Diamonds",
                  "Hearts",
                  "Spades")
    # All the card ranks in the deck
    card_ranks = ("Two",
                  "Three",
                  "Four",
                  "Five",
                  "Six",
                  "Seven",
                  "Eight",
                  "Nine",
                  "Ten",
                  "Jack",
                  "Queen",
                  "King",
                  "Ace")
    # All the card values based on ranks
    # (Note that the dict keys must coincide with the values in the ranks tuple)
    card_values = {"Two": 2,
                   "Three": 3,
                   "Four": 4,
                   "Five": 5,
                   "Six": 6,
                   "Seven": 7,
                   "Eight": 8,
                   "Nine": 9,
                   "Ten": 10,
                   "Jack": 10,
                   "Queen": 10,
                   "King": 10,
                   "Ace": 11}

    def __init__(self):
        """
        Initializes an instance of a Deck object.
        """

        self._cards = []

    @staticmethod
    def change_ace_value_to_eleven():
        """
        Changes the value of the Ace in the dictionary to be 11.
        """

        Deck.card_values["Ace"] = 11

    @staticmethod
    def change_ace_value_to_one():
        """
        Changes the value of the Ace in the dictionary to be 1.
        """

        Deck.card_values["Ace"] = 1

    @property
    def cards(self) -> [Card]:
        """
        Gets the deck of cards.

         Returns:
             The deck of cards.
        """

        return self._cards
