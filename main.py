from blackjack import blackjack


if __name__ == "__main__":
    
    # Essential game components
    main_deck = blackjack.init_deck()
    tokens = blackjack.init_currency()
    p_hand = blackjack.init_hand(main_deck)
    d_hand = blackjack.init_hand(main_deck)
