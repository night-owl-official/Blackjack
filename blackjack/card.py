"""
This module holds the Card class.
"""


class Card:
    """
    This class allows you to instantiate a card,
    access its fields and use its methods.
    """

    def __init__(self, rank: str, suit: str):
        """
        Initializes an instance of a card object.

        Parameters:
            rank (str): The rank for the card e.g. one, jack, ace etc.
            suit (str): The suit for the card e.g. hearts, diamonds etc.
        """

        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __str__(self) -> str:
        """
        String representation for a Card.

        Returns:
            A string displaying info about a Card.
        """

        return f"{self._rank} of {self._suit}"
