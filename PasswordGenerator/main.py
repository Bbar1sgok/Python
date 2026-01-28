import random

# PyPassword Generator
# This program generates a random password based on the number of
# letters, numbers, and symbols chosen by the user.
# It was created to practice Python lists, loops, and the random module.


letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']


print("Welcome to the PyPassword Generator!")

# Get user preferences
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

# List to store password characters
password_list = []


for _ in range(nr_letters):
    password_list.append(random.choice(letters))


for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))


for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Shuffle to randomize character order
random.shuffle(password_list)

# Convert the list into a string
last_password = "".join(password_list)


print(f"Your password is: {last_password}")
