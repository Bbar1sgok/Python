import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nrLetters = int(input("How many letters would you like in your password?\n"))
nrSymbols = int(input("How many symbols would you like?\n"))
nrNumbers = int(input("How many numbers would you like?\n"))

# Check if the user has selected at least one character type
if nrLetters < 0 and nrSymbols < 0 and nrNumbers < 0:
    print("You need to select at least one letter, symbol, or number for your password!")
else:
    passwordList = []
    password = ""

    # Add letters to the password
    for char in range(nrLetters):
        passwordList.append(random.choice(letters))

    # Add symbols to the password
    for char in range(nrSymbols):
        passwordList.append(random.choice(symbols))

    # Add numbers to the password
    for char in range(nrNumbers):
        passwordList.append(random.choice(numbers))

    # Shuffle the list to randomize the order of characters
    random.shuffle(passwordList)

    # Combine the list into a final password string
    password = ''.join(passwordList)

    print(f"Your password is: {password}")
