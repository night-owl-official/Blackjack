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


def init_hand(deck: Deck) -> Hand:
    """
    Initializes a hand of cards

    Parameters:
        deck (Deck): The deck of cards

    Returns:
        The hand of cards
    """

    return Hand([deck.deal_card(), deck.deal_card()])


def init_currency(starting_tokens=1000) -> Currency:
    """
    Initialized the player's tokens to the given amount

    Parameters:
        starting_tokens (int): The initial amount of tokens the player has

    Returns:
        The player's tokens
    """

    return Currency(starting_tokens)


def ask_bet(currency: Currency):
    """
    Asks the player how much they want to bet

    Parameters:
        currency (Currency): The player's tokens to bet
    """

    # This loop will run until the user enters a number
    while True:
        # Asks the user to enter their bet, showing them
        # the tokens they currently own
        print(f"You have {currency.total_tokens} tokens left!")
        p_choice = input("What's your bet? ")

        # Checks the user's choice to make sure it's a number
        # and if it's not then asks them to enter their bet again
        if not p_choice.isdigit():
            print("* You need to enter a number! *\n")
            continue

        # Places the bet as integer, displaying the bet to the console
        # and ends the loop
        currency.bet(int(p_choice))
        print(f"You bet {currency.tokens_bet} tokens!\n")
        break
