print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: \n").upper()  
pepperoni = input("Do you want pepperoni on your pizza? Y or N: \n").upper()  
extra_cheese = input("Do you want extra cheese? Y or N: \n").upper()  
# Initial prices are determined based on the pizza size
if size == "S":  
    bill = 15  
elif size == "M":
    bill = 20  
elif size == "L":
    bill = 25  
else:
    print("Invalid size entered.")  # Inform the user of invalid input
    bill = 0  # Set the bill to zero for invalid input

# Add cost for pepperoni topping
if pepperoni == "Y":  
    if size == "S":
        bill += 2 
    else:
        bill += 3 

# Add cost for extra cheese
if extra_cheese == "Y":  
    bill += 1 

# Display the final bill if valid size was entered
if bill > 0:  
    print(f"Your final bill is: ${bill}") 
