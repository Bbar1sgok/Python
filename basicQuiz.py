# Question 1
# Assign the 5th letter of the following string to a variable
import random

my_string = "Python"

character5 = my_string[4]

print(character5)

# Question 2
# Print all letters between the 5th and 8th characters of the following string (Including 5th and 8th character)

my_new_string = "MachineLearning"

print(my_new_string[4:8])

# Question 3
# Write the following string in reverse

my_last_string = "Google Chrome"

print(my_last_string[::-1])

# Question 4
# What data type will the result of the following operation be?

x = 4 + 12.2 + 48
# x type float
# We can use the type function to check
print(type(x))

# Question 5
# What is the result of the following operation?

y = 5 + 7 * 12
# y = 89
# Python recognizes mathematical priorities

# Question 6
# Take the following "b" in a single line

myList = [3.14, 4, [2, 3, "b"], True]
b = myList[2][2]
print(b)

# Question 7
# Take the following "a" in a single line

my_dictionary = {"key1":20.25,"key2":[40,{"k21":"a"}]}
print(my_dictionary["key2"][1]["k21"])

# Question 8
# What values will remain in the following list when it is converted to set?

my_list_to_be_set = [3, 4, 9, 3, 21, 22, 4, 3, 9, 10, 21, 22]

reply = {3, 4, 9, 10, 21, 22}

# Question 9
# What would be the output of the following code?

p = 5
q = 3
w = 6
#p > q and w > p
#reply = True

# Question 10
# What will be the output of the following code?

age = 20

if age < 18 :
    print("You are under 18")
elif age >= 18 and age < 30:
    print("You are between the ages of 18 and 30")
elif age >= 30 and age < 40:
    print("You are between 30 and 40 years old")
else:
    print("You are over 40 years old")

# reply = "You are between the ages of 18 and 30"

# Question 11
# In the following dictionary, create an if condition that indicates whether the letter c occurs in the values

my_dictionary1 = {"k1": 10, "k2": "a", "k3": 30, "k4": "c"}

#Reply 1
if my_dictionary1["k1"] == "c":
    print("c")
elif my_dictionary1["k2"] == "c":
    print("c")
elif my_dictionary1["k3"] == "c":
    print("c")
elif my_dictionary1["k4"] == "c":
    print("c")
else:
    print(" 'c' not found in my_dictionary1")

# Reply 2
if "c" in my_dictionary1.values():
    print("yes")

# Question 12
# In the dictionary below, write an if condition that indicates whether the letter "a" occurs in the key or not

my_other_dictionary = {"b": 203, "c": "a", "a": 400, "d": "f"}

if "a" in my_other_dictionary.keys():
    print("yes")

# Question 13
# Write a code that selects even numbers from the list below

my_numbers = [1, 2, 3, 4, 5, 6, 19, 20, 32, 21, 20, 1111, 23, 24]

for num in my_numbers:
    if num % 2 == 0:
        print(num)

# Question 14
# Create a new list containing the perimeter of all circles. Pi = 3
# The numbers in the list below give the radius of a circle.

r_list = [3, 2, 5, 8, 4, 6, 9, 12]
environment_list = []
for r in r_list:
    environment = 2*3*r
    environment_list.append(environment)

print(environment_list)

# Question 15
# Create a new, separate list that includes only ages.

age_name_list = [("Diyar",20),("Yusuf",20),("Kemalettin",20),("Barış",21)]
justNameList = []
for (names, ages) in age_name_list:
    justNameList.append(ages)

print(justNameList)

# Question 16
# Write a code that randomly prints one of the following music groups

metal_list = ["Metallica", "Iron Maiden", "Dream Theater", "Megateht", "AC/DC"]

print(random.choice(metal_list))
