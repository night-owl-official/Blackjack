from blackjack import blackjack


def ask_play_again() -> bool:
    """Asks the user whether they want to play another round

    Returns:
        bool: True if the user wants to play again, false otherwise
    """
    
    # Keeps looping until the user enters a valid choice
    while True:
        # Asks the user for a valid answer and turns the answer to lowercase
        # which will allow us to compare it without worrying for casing
        choice = input("Do you want to play again? (y/n) ").lower()
        
        # True when the user wants to play again, false otherwise
        if (choice == 'y') or (choice == "yes"):
            return True
        elif (choice == 'n') or (choice == "no"):
            print("\nThanks for playing! See you next time!")
            return False
        
        # This only gets here in case of the user entering an invalid choice
        # and gives them a suggestion regarding what to enter
        print("* You need to enter one of the following: y/yes, n/no *\n")
        

def check_for_blackjack(hand_of_cards) -> bool:
    """Checks if a hand has a blackjack or not

    Args:
        hand_of_cards (Hand): The hand of cards to check

    Returns:
        bool: True if there's a blackjack, false otherwise
    """
    
    return blackjack.count_points(hand_of_cards) == 21


def check_for_bust(hand_of_cards) -> bool:
    """Checks if a hand has busted or not

    Args:
        hand_of_cards (Hand): The hand of cards to check

    Returns:
        bool: True if busted, false otherwise
    """
    
    return blackjack.count_points(hand_of_cards) > 21


if __name__ == "__main__":
    
    # Essential game components
    main_deck = blackjack.init_deck()
    tokens = blackjack.init_currency()
    p_hand = blackjack.init_hand(main_deck)
    d_hand = blackjack.init_hand(main_deck)
    
    # Flag to decide whether to play another round after a loss
    play_again = True
    
    # The game keeps running until the user doesn't want to play anymore
    while play_again:
        # Introduces the user to the game
        print("\n\n*** WELCOME TO BLACKJACK!! ***\n")
        
        # Asks the user how many tokens to bet     
        blackjack.ask_bet(tokens)
        
        # Sets the flag to keep playing or not
        play_again = ask_play_again()
