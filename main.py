from blackjack import blackjack

# Essential game components
main_deck = blackjack.init_deck()
tokens = blackjack.init_currency()
p_hand = blackjack.init_hand(main_deck)
d_hand = blackjack.init_hand(main_deck)

# Flag to decide whether to play another round after a loss
play_again = True

p_has_busted = False
p_has_blackjack = False
both_have_blackjack = False

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


def player_wins():
    """Earns the tokens and resets the hands
    """
    
    # Player cashes in the full bet
    tokens.cash_in()
    
    # Both hands are reset to start next turn
    blackjack.reset_turn([p_hand, d_hand], main_deck)


def handle_possible_blackjack_draw():
    """Holds the logic that checks for a blackjack
    in the current dealer's hand and if it finds it
    then it will be a blackjack draw
    """
    
    # Use module scoped flags
    global p_has_blackjack
    global both_have_blackjack
    
    # Flags player blackjack
    p_has_blackjack = True
    
    # Dealer can at least try to tie the score if they have a blackjack
    blackjack.dealer_hit_or_stay(d_hand, main_deck)
    
    # Dealer's blackjack?
    if check_for_blackjack(d_hand):
        # Flags dealer's blackjack
        both_have_blackjack = True
        
        # Prints message announcing it's a draw
        print("You and the dealer both have a blackjack!")
        print("It's a draw!\n")
        
        # Player cashes in half the bet
        tokens.cash_in_half()
        
        # Both hands are reset to start next turn
        blackjack.reset_turn([p_hand, d_hand], main_deck)
        
    else:
        # Dealer didn't have a blackjack, therefore player wins
        # Prints a message showing that
        print("You have a blackjack!")
        print("You won the turn!\n")
        
        # Cashes in the price and resets hands
        player_wins()


def reset_flags():
    """Resets all the game flags to default state
    """
    
    # Use the variables declared in the scope of the module
    global p_has_busted
    global p_has_blackjack
    global both_have_blackjack
    
    # Reset them
    p_has_busted = False
    p_has_blackjack = False
    both_have_blackjack = False


if __name__ == "__main__":    
    # The game keeps running until the user doesn't want to play anymore
    while play_again:
        # Asks the user how many tokens to bet     
        blackjack.ask_bet(tokens)
        
        # The player might have a blackjack in their first hand
        if check_for_blackjack(p_hand):
            # The dealer might also have a blackjack
            handle_possible_blackjack_draw()
            
            # Skips the remaining logic in the loop since the game has been decided already
            continue
        else:
            # Keeps asking the player if they want to get hit until they refuse
            while blackjack.ask_hit_or_stay(p_hand, main_deck):
                # Player might have a blackjack
                if check_for_blackjack(p_hand):
                    # The dealer might also have a blackjack
                    handle_possible_blackjack_draw()
                    
                    # Breaks out of the loop since somebody had a blackjack
                    # No need to keep asking the player if they want to get hit
                    break    
                elif check_for_bust(p_hand):
                    # Player might have busted
                    
                    # Flags the player has busted
                    p_has_busted = True
                    
                    # Prints a message showing that
                    print("You busted!\n")
                    
                    # Player loses their bet
                    tokens.cash_out()
                    
                    # Both hands are reset to start the next turn
                    blackjack.reset_turn([p_hand, d_hand], main_deck)
                    
                    # Breaks out of the loop since the player has busted
                    break
            
            # Dealer will hit their hand if no blackjack or bust occurred
            if not (p_has_blackjack or both_have_blackjack or p_has_busted):
                # Dealer hits their hand
                blackjack.dealer_hit_or_stay(d_hand, main_deck)
                
                # Dealer might have busted
                if check_for_bust(d_hand):
                    # Prints a message showing the dealer has busted
                    print("The dealer busted!")
                    print("You won the turn!\n")
                    
                    # Cashes in the price and resets the hands
                    player_wins()
                else:
                    # Get the player's and dealer's score
                    p_score = blackjack.count_points(p_hand)
                    d_score = blackjack.count_points(d_hand)
                    
                    # Compares player's and dealer's score
                    if p_score > d_score:
                        # Player has a higher score
                        print(f"You won {p_score} to {d_score}!\n")
                        
                        # Cashes in the price and resets hands
                        player_wins()
                    elif p_score < d_score:
                        # Player has a lower score
                        print(f"You lost {d_score} to {p_score}!\n")
                        
                        # Player loses their full bet
                        tokens.cash_out()
                        
                        # Both hands are reset to start next turn
                        blackjack.reset_turn([p_hand, d_hand], main_deck)
                    else:
                        # It's a draw
                        print(f"You tied {p_score} to {d_score}!\n")
                        
                        # Splits the bet
                        tokens.cash_in_half()
                        
                        # Both hands are reset to start next turn
                        blackjack.reset_turn([p_hand, d_hand], main_deck)
                        
            # Resets all flags
            reset_flags()
                        
            # No more tokens left means the player
            # has lost their game
            if tokens.total_tokens > 0:
                continue
            else:
                print("You're out of tokens!\n")
                
            # When the deck of cards is empty, it gets refilled
            if len(main_deck.cards) == 0:
                main_deck.init_deck()
                main_deck.shuffle()
                
        # Sets the flag to keep playing or not
        play_again = ask_play_again()
        
        # The user wants to play again
        if play_again:
            # All game flags are reset
            reset_flags()
            
            # The game is reset to initial state
            blackjack.reset_game(main_deck, [p_hand, d_hand], tokens)
            
            # Introduces the user to the game
            print("\n\n*** WELCOME TO BLACKJACK!! ***\n")
