# Tip Calculator
# This program calculates how much each person should pay,
# including the tip, by taking the total bill, tip percentage,
# and number of people as input.

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $ \n"))
tip = int(input("What percentage tip would you like to give? (10, 12, 15): \n "))
people = int(input("How many people to split the bill? \n "))

tip_percentage = tip / 100
total_bill = bill * (1 + tip_percentage)
bill_per_person = round(total_bill / people, 2)

print(f"Each person should pay: ${bill_per_person}")