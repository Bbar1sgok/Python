import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Check if the user has selected at least one character type
if nr_letters == 0 and nr_symbols == 0 and nr_numbers == 0:
    print("You need to select at least one letter, symbol, or number for your password!")
else:
    password_list = []
    password = ""

    # Add letters to the password
    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    # Add symbols to the password
    for char in range(nr_symbols):
        password_list.append(random.choice(symbols))

    # Add numbers to the password
    for char in range(nr_numbers):
        password_list.append(random.choice(numbers))

    # Shuffle the list to randomize the order of characters
    random.shuffle(password_list)

    # Combine the list into a final password string
    password = ''.join(password_list)

    print(f"Your password is: {password}")