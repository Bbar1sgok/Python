import random
from art import logo

# 🃏 Blackjack Game (Python)

# A simple terminal-based Blackjack (21) game implemented in Python.

## 🎯 Features
# - Real Blackjack rules
# - Automatic dealer logic (hits until 17)
# - Ace (11/1) handling
# - Blackjack detection



import random
from art import logo


def deal_card():
    # Represents the deck of cards (11 stands for Ace)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # Return a random card from the deck
    return random.choice(cards)


def calculate_score(cards):
    # Check for a Blackjack (21 with two cards)
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # If the hand contains an Ace and the score is over 21,
    # convert Ace from 11 to 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    # Return the total score
    return sum(cards)


def compare(user_score, computer_score):
    # Compare the final scores and determine the result
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    # Display the game logo
    print(logo)

    # Initialize card lists for user and computer
    user_cards = []
    computer_cards = []

    user_score = -1
    computer_score = -1
    is_game_over = False

    # Deal two cards to both player and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # User's turn
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # End game if Blackjack or user goes over 21
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: "
            ).lower()

            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer's turn (dealer must hit until score is at least 17)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Show final hands and scores
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    # Print the game result
    print(compare(user_score, computer_score))


# Restart the game if the user wants to play again
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)
    play_game()








