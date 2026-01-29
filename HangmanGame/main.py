import random
from hangman_words import word_list
from hangman_art import stages, logo

# Hangman Game
#
# This program implements a classic Hangman game.
# The goal is to guess the randomly selected word
# before running out of lives.
#
# Concepts used in this project:
# - Python lists
# - Loops (while, for)
# - Conditional statements (if / else)
# - Module imports
# - User input validation

lives = 6
game_over = False

correct_letters = []
wrong_letters = []

print(logo)

# Choose a random word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Current state of the word
display = ["_"] * word_length

while not game_over:

    print(f"\n{'*' * 15} {lives}/6 LIVES LEFT {'*' * 15}")

    if wrong_letters:
        print(f"Wrong guesses: {', '.join(wrong_letters)}")

    # Show current word state (always visible)
    print(f"Word: {' '.join(display)}")

    guess = input("Guess a letter: ").lower()

    # Basic input checks
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in correct_letters or guess in wrong_letters:
        print(f"You already tried '{guess}'.")
        continue

    # Check guess
    if guess in chosen_word:
        correct_letters.append(guess)
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        wrong_letters.append(guess)
        lives -= 1
        print(f"'{guess}' is not in the word.")

    print(stages[lives])

    # Win condition
    if "_" not in display:
        game_over = True
        print("\nYOU WIN!")

    # Lose condition
    if lives == 0:
        game_over = True
        print(f"\nYOU LOSE! The word was '{chosen_word}'")
