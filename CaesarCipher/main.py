# Caesar Cipher (Encode / Decode)

# This project is a simple Caesar Cipher implementation written in Python.
# It allows the user to encrypt (encode) or decrypt (decode) a message by
# shifting letters in the alphabet by a given number.

# The project was created to practice:
# - Python functions
# - Loops
# - Conditional statements
# - Modulo arithmetic
# - User input validation

## Features
# - Encode and decode messages
# - Handles large and negative shift values using modulo
# - Preserves spaces and non-alphabet characters
# - Input validation for direction and shift
# - Loop-based program flow with safe exit option

## How It Works
# 1. The user chooses `encode` or `decode`
# 2. The user enters a message
# 3. The user enters a shift number
# 4. The program returns the transformed message

from art import logo

alphabet = ['a','b','c','d','e','f','g','h','i','j',
            'k','l','m','n','o','p','q','r','s','t',
            'u','v','w','x','y','z']


def encode_decode_function(direction, text, shift):
    """
        Encodes or decodes the given text using Caesar Cipher logic.

        :param direction: 'encode' or 'decode'
        :param text: input message
        :param shift: number of shifts
        :return: transformed text
        """

    result_text = ""

    # Reverse shift for decoding
    if direction == 'decode':
        shift *= -1

    for char in text:

        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index + shift) % 26
            result_text += alphabet[new_index]
        else:
            result_text += char  # Keeps spaces or symbols

    return result_text

print(logo)

while True:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt, to close '1':\n"
    ).lower()

    # Exit condition
    if direction == '1':
        print("Closed successfully ...")
        break

    # Direction validation
    if direction != 'encode' and direction != 'decode':
        print("Please enter either 'encode' or 'decode'.")
        continue

    text = input("Type your message:\n").lower()

    # Shift validation
    try:
        shift = int(input("Type the shift number:\n"))
    except ValueError:
        print("Please enter a valid number!")
        continue

    # Keep shift inside alphabet range
    shift = shift % 26

    result_text = encode_decode_function(direction, text, shift)
    print(result_text)




