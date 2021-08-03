"""
This module holds the Currency class
"""


class Currency:
    """
    This class allows you to represent a currency that the player
    can use to bet as well as win or lose
    """

    def __init__(self, initial_amount: int):
        """
        Initializes an instance of Currency

        Parameters:
            initial_amount (int): The amount of the currency the player has
            when the game starts
        """

        self._total_tokens = initial_amount
        self._tokens_bet = 0

    @property
    def total_tokens(self) -> int:
        """
        Gets the amount of tokens currently owned

        Returns:
             The total amount of held tokens
        """

        return self._total_tokens

    @property
    def tokens_bet(self) -> int:
        """
        Gets the amount of tokens the player bet

        Returns:
             The total amount of bet tokens
        """

        return self._tokens_bet

    def __str__(self) -> str:
        """
        Allows you to print out a player's currency

        Returns:
            A string with info on a player's currency
        """

        return f"You have {self._total_tokens} tokens left.\nYour current bet is {self._tokens_bet} tokens."

    def bet(self, bet_amount: int):
        """
        Sets the current bet amount of tokens

        Parameters:
            bet_amount (int): The amount of tokens to bet
        """

        # If the player bets more than they have available
        # they will go all in, however, they can only bet as much as they own
        self._tokens_bet = bet_amount if (bet_amount < self._total_tokens) else self._total_tokens

    def reset_bet(self):
        """
        Resets the tokens bet to zero
        """

        self._tokens_bet = 0

    def cash_in(self):
        """
        Adds to the total tokens based on the player's bet
        """

        self._total_tokens += self._tokens_bet
        self.reset_bet()
