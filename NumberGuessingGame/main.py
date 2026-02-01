from random import randint
from art import logo

# Number of attempts for each difficulty level
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def number_generator():
    """
    Generates and returns a random number between 1 and 100.
    """
    return randint(1, 100)


def check_answer(user_guess, actual_answer, turns):
    """
    Compares the user's guess with the actual answer.

    Parameters:
    user_guess (int): The number guessed by the user
    actual_answer (int): The correct number
    turns (int): Remaining attempts

    Returns:
    int: Updated number of remaining turns
    """
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        # If the guess is correct, return the same number of turns
        return turns


def set_difficulty():
    """
    Asks the user to choose a difficulty level
    and returns the corresponding number of attempts.
    """
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game_controller():
    """
    Controls whether the user wants to play the game again.
    """
    while True:
        again = input("Do you want to play again? (y/n): ").lower()

        if again != "y":
            break
        else:
            game()


def game():
    """
    Main game function that runs the number guessing game.
    """
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate the correct answer
    answer = number_generator()

    # Set difficulty and initial attempts
    turns = set_difficulty()

    guess = 0

    # Game loop: continues until the user guesses correctly
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please, enter a valid number.")
            continue

        # Update remaining turns based on the guess
        turns = check_answer(guess, answer, turns)

        if guess == answer:
            print(f"You got it! The answer was {answer}")
            game_controller()
            break

        if turns == 0:
            print("You've run out of guesses, you lose.")
            game_controller()
            break
        else:
            print("Guess again.")


# Start the game
game()
