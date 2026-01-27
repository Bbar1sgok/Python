# Treasure Island Game
# A text-based adventure game where the player makes choices
# to find the hidden treasure.
# This project was created to practice conditional statements,
# user input handling, and basic game logic in Python.


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
*******************************************************************************
''')

# Welcome messages
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# First choice: crossroads
choice1 = input(
    'You\'re at a crossroad. Where do you want to go? Type "left" or "right":\n'
).lower()

if choice1 == "left":
    # Second choice: lake
    choice2 = input(
        'You\'ve come to a lake. There is an island in the middle of the lake.\n'
        'Type "wait" to wait for a boat or "swim" to swim across:\n'
    ).lower()

    if choice2 == "wait":
        # Third choice: doors
        choice3 = input(
            "You arrive at the island unharmed.\n"
            "There is a house with 3 doors: one red, one yellow, and one blue.\n"
            "Which colour do you choose?\n"
        ).lower()

        if choice3 == "red":
            print("It's a room full of fire. Game over.")
        elif choice3 == "yellow":
            print("You found the treasure. You win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game over.")
        else:
            print("You chose a door that doesn't exist. Game over.")
    else:
        # Player chose to swim
        print("You were attacked while swimming. Game over.")
else:
    # Player chose the wrong path
    print("You fell into a hole. Game over.")
