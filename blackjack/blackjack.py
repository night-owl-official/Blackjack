"""
This module contains all the functions necessary for the correct
functioning of the blackjack game.
"""
from blackjack.card import Card
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


def ask_hit_or_stay(hand: Hand, deck: Deck) -> str:
    """
    Asks the player whether they want to be hit or stay

    Parameters:
        hand (Hand): The player's hand
        deck (Deck): The deck of cards

    Returns:
        The player's choice (hit or stay)
    """

    # This loop will run until the user enters a valid choice
    while True:
        # Asks the user if they want to hit or stay,
        # showing them their hand to help decide
        print("This is your hand:")
        print(f"{hand}\n")
        p_choice = input("Hit or Stay? (h/s) ").lower()

        # The user wants to hit
        # The choice is turned into lowercase so there's
        # no need to check for abnormal versions of the word 'hit'
        if (p_choice == 'h') or (p_choice == "hit"):
            # The player is dealt a card from the deck
            # The card object could be set to None just in case
            # the deck has run out of cards
            new_card = deck.deal_card()

            if new_card:
                # Adds the card to the player's hand
                # and shows the user what card they drew
                # as well as their new hand
                # then returns the choice
                hand.hit(new_card)
                print(f"You got {new_card}!\n")
                print("This is your hand:")
                print(f"{hand}\n")
                return 'h'
            else:
                print("* The deck has no more cards left! *\n")
                break
        elif (p_choice == 's') or (p_choice == "stay"):
            # Prints a newline just for neater output
            # and returns the choice
            print()
            return 's'

        # The user entered some invalid input and is advised to enter the correct one
        print("* You need to enter one of the following: h/hit, s/stay *\n")
