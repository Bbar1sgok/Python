import random
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

user_choice = int(input("What do you do choose ? \nType 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

if user_choice == 0 and  computer_choice == 0:
    print(rock)
    print("Computer chose:")
    print(rock)
    print("You are in a draw.")
elif user_choice == 1 and computer_choice == 1:
    print(paper)
    print("Computer chose:")
    print(paper)
    print("You are in a draw")
elif user_choice == 2 and computer_choice == 2:
    print(scissors)
    print("Computer chose:")
    print(scissors)
    print("You are in a draw")
elif user_choice == 0 and computer_choice == 1:
    print(rock)
    print("Computer chose:")
    print(paper)
    print("You lose")
elif user_choice == 0 and computer_choice == 2:
    print(rock)
    print("Computer chose:")
    print(scissors)
    print("You win")
elif user_choice == 1 and computer_choice == 2:
    print(paper)
    print("Computer chose:")
    print(scissors)
    print("You lose")
elif user_choice == 1 and computer_choice == 0:
    print(paper)
    print("Computer chose:")
    print(rock)
    print("You win")
elif user_choice == 2 and computer_choice == 0:
    print(scissors)
    print("Computer chose:")
    print(rock)
    print("You lose")
elif user_choice == 2 and computer_choice == 1:
    print(scissors)
    print("Computer chose:")
    print(paper)
    print("You win")
else:
    print("Correct number not selected")
