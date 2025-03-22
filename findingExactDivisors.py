entered_number = int(input("Please enter an integer:"))

divisors = []

# Special case for zero
if entered_number == 0:
    print("The divisors of zero are undefined.")
else:

    number = 1
    while number <= entered_number:

        if entered_number % number == 0:
            divisors.append(number)
        number += 1


    print(divisors)
