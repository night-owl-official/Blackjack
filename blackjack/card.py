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
    def rank(self) -> str:
        """
        Gets the rank of a Card.

        Returns:
            The rank of a Card.
        """

        return self._rank

    @property
    def suit(self) -> str:
        """
        Gets the suit of a Card.

        Returns:
            The suit of a Card.
        """

        return self._suit

    def __str__(self) -> str:
        """
        String representation for a Card.

        Returns:
            A string displaying info about a Card.
        """

        return f"{self._rank} of {self._suit}"

    def __eq__(self, other) -> bool:
        """
        Permits two cards to be compared with each other for equality

        Parameters:
            other (Card): The other card to compare to

        Returns:
            True when the two cards are equal, false otherwise
        """

        return (self._rank == other._rank) and (self._suit == other._suit)
