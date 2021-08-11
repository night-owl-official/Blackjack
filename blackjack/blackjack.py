"""
This module contains all the functions necessary for the correct
functioning of the blackjack game.
"""
from blackjack.currency import Currency
from blackjack.deck import Deck
from blackjack.hand import Hand


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


def ask_hit_or_stay(hand: Hand, deck: Deck) -> bool:
    """
    Asks the player whether they want to be hit or stay

    Parameters:
        hand (Hand): The player's hand
        deck (Deck): The deck of cards

    Returns:
        The player's choice (hit/true or stay/false)
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
                return True
            else:
                print("* The deck has no more cards left! *\n")
                break
        elif (p_choice == 's') or (p_choice == "stay"):
            # Prints a newline just for neater output
            # and returns the choice
            print()
            return False

        # The user entered some invalid input and is advised to enter the correct one
        print("* You need to enter one of the following: h/hit, s/stay *\n")


def dealer_hit_or_stay(hand: Hand, deck: Deck):
    """
    Deals cards to the dealer until they reach a score of 17 or higher

    Parameters:
        hand (Hand): The hand of cards for the dealer
        deck (Deck): The deck of cards
    """

    # Counts the dealer's score before starting to deal cards to them
    current_total = count_points(hand)

    # The dealer can only deal cards to themselves if their score is less than 17
    while current_total < 17:
        # Deals a new card
        new_card = deck.deal_card()

        # Deck can be empty, a check is necessary
        if not new_card:
            break

        # Deck isn't empty, therefore hits the dealer's hand
        # and checks their score after the new card has been dealt
        hand.hit(new_card)
        current_total = count_points(hand)


def count_points(hand: Hand) -> int:
    """
    Counts how many points are in a hand

    Parameters:
        hand (Hand): The hand of cards to count

    Returns:
        The total points a hand of cards has
    """

    total_points = 0
    # Creates a list of all aces in the hand
    ace_list = [card for card in hand.cards if card.rank == "Ace"]

    # Adds up all the cards that are not aces
    for card in hand.cards:
        # Skips aces because they will be counted separately
        if card.rank == "Ace":
            continue

        total_points += Deck.card_values[card.rank]

    # There's only one ace in the hand
    if len(ace_list) == 1:
        # The total points in the hand without the ace is not more than 10
        if total_points <= 10:
            # Ace is valued at 11 points
            Deck.change_ace_value_to_eleven()
        else:
            # Ace is valued at 1 point because the total
            # already surpasses 10
            Deck.change_ace_value_to_one()

        # Adds the ace value to the total
        total_points += Deck.card_values["Ace"]
    elif len(ace_list) > 1:
        # There is more than one ace in the hand

        # # The total points in the hand without the aces is not more than 10
        if total_points <= 10:
            # First ace is valued at 11 points and added to the total
            Deck.change_ace_value_to_eleven()
            total_points += Deck.card_values["Ace"]

            # The remaining aces will all be valued at one
            # because there can only be one ace valued at 11
            Deck.change_ace_value_to_one()
            # Loop starts counting from the second ace
            # as the first ace has already been counted
            # and all the aces are added to the total
            for i in range(1, len(ace_list)):
                total_points += Deck.card_values["Ace"]
        else:
            # The total without aces surpasses 10
            # therefore all aces will be valued at one
            # and added to the total
            Deck.change_ace_value_to_one()
            for i in range(len(ace_list)):
                total_points += Deck.card_values["Ace"]

    return total_points
