from art import logo


# -------------------- ADDITION FUNCTION --------------------
def addition_function(*args):
    """
    Adds multiple numbers together.
    Uses *args to accept a variable number of inputs.
    """

    # If no numbers are provided, return 0
    if len(args) == 0:
        return 0

    # Start with the first number
    result = args[0]

    # Add the remaining numbers
    for arg in args[1:]:
        result += arg

    return result


# -------------------- SUBTRACTION FUNCTION --------------------
def subtraction_function(*args):
    """
    Subtracts multiple numbers sequentially.
    The first number is used as the base value.
    """

    # If no numbers are provided, return 0
    if len(args) == 0:
        return 0

    # Start with the first number
    result = args[0]

    # Subtract remaining numbers from the first
    for arg in args[1:]:
        result -= arg

    return result


# -------------------- MULTIPLICATION FUNCTION --------------------
def multiplication_function(*args):
    """
    Multiplies multiple numbers together.
    """

    # If no numbers are provided, return 0
    if len(args) == 0:
        return 0

    # Start with the first number
    result = args[0]

    # Multiply remaining numbers
    for arg in args[1:]:
        result *= arg

    return result


# -------------------- DIVISION FUNCTION --------------------
def division_function(num1, num2):
    """
    Divides num1 by num2.
    Returns None if division by zero is attempted.
    """

    # Check for division by zero
    if num2 == 0:
        result = None
    else:
        result = num1 / num2

    return result


# Print calculator logo
print(logo)


# -------------------- MAIN PROGRAM LOOP --------------------
while True:

    # Ask user to select an operation
    symbol = input(
        "Please choose an operation on your calculator "
        "(Addition '+', Subtraction '-', Multiplication '*', Division '/'): "
    )

    nums_list = []  # List to store numbers entered by the user

    # Check if the entered symbol is valid
    if symbol in ['+', '-', '*', '/']:

        # For addition, subtraction, and multiplication
        if symbol == "+" or symbol == "-" or symbol == "*":

            while True:
                try:
                    # Ask the user to enter a number
                    num = int(input("Please enter a number: "))
                    nums_list.append(num)

                    # Ask if the user wants to continue
                    user_input = input(
                        "Enter the next number. If there are no more numbers, press '0': "
                    )

                    # Warn the user if fewer than two numbers are entered
                    if len(nums_list) < 2:
                        print(
                            "You entered only one number; "
                            "the operation cannot be performed properly."
                        )

                    # Stop taking numbers if user enters '0'
                    if user_input == "0":
                        break

                except ValueError:
                    # Handle non-numeric input
                    print("Please enter a valid number.")
                    continue

        # Perform the selected operation
        if symbol == "+":
            print(addition_function(*nums_list))

        elif symbol == "-":
            print(subtraction_function(*nums_list))

        elif symbol == "*":
            print(multiplication_function(*nums_list))

        elif symbol == "/":
            try:
                user_divison_input_1 = int(
                    input("Please enter the number to be divided: ")
                )
            except ValueError:
                print("Please enter a valid number.")

            try:
                user_divison_input_2 = int(
                    input("Please enter the divisor: ")
                )
            except ValueError:
                print("Please enter a valid number.")

            result = division_function(
                user_divison_input_1,
                user_divison_input_2
            )

            # Check for division by zero
            if result is None:
                print("In division, the divisor cannot be zero.")
            else:
                print(result)

        # Ask user whether they want to continue
        control = input("Do you want to perform another operation? (Y/N): ").lower()

        if control == "n":
            break
        elif control != "y" and control != "n":
            print("Please enter either 'Y' or 'N'.")

    else:
        # Handle invalid operation input
        print("You entered an invalid operation.")
