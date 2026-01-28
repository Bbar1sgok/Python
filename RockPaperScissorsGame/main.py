import random

# Rock Paper Scissors Game
# A simple Python game where the user plays against the computer.
# This project was created to practice lists, conditionals, and random module usage.

# ASCII art representations
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Store game images in a list
game_images = [rock, paper, scissors]

# Get user's choice
user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n")
)

# Validate user input
if user_choice < 0 or user_choice > 2:
    print("You typed an invalid number. You lose!")
else:

    print(game_images[user_choice])

    # Generate computer's choice
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    # Game logic
    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    else:
        print("You lose!")
