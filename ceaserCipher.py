alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1  

    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % len(alphabet)
            output_text += alphabet[new_position]
        else:
            output_text += letter  

    print(f"Here is the {encode_or_decode}d result: {output_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction not in ("encode", "decode"):
        print("Invalid direction. Please type 'encode' or 'decode'.")
        continue

    text = input("Type your message:\n").lower()

    try:
        shift = int(input("Type the shift number:\n"))
        shift = shift % len(alphabet)
    except ValueError:
        print("Invalid shift number. Please enter an integer.")
        continue

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()

    if restart == "no":
        should_continue = False
        print("Good bye!")
