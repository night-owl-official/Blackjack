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


if __name__ == "__main__":
    
    # Essential game components
    main_deck = blackjack.init_deck()
    tokens = blackjack.init_currency()
    p_hand = blackjack.init_hand(main_deck)
    d_hand = blackjack.init_hand(main_deck)
