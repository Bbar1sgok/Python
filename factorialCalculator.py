print("""
*********************************
Factorial Calculation

Press "q" to exit.

*********************************
""")

while True:
    number = input("Number: ")

    if number.lower() == "q":
        print("Program is terminating")
        break

    try:
        number = int(number)
        factorial = 1

        if number >= 0:
            for i in range(2, number + 1):
                factorial *= i
            print(f"Factorial: {factorial}")

        else:
            print("Please enter a positive integer")

    except ValueError:
        print("Please enter an integer")
