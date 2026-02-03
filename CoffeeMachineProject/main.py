# Coffee Machine Menu Data
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Total profit earned by the machine
profit = 0.0

# Available resources in the coffee machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """
    Checks whether the machine has enough resources
    to prepare the selected drink.
    """
    for item, amount in order_ingredients.items():
        # Using .get() prevents KeyError and ensures safe access
        if resources.get(item, 0) < amount:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """
    Takes coin input from the user and calculates
    the total amount of money inserted.
    """
    print("Please insert coins.")
    try:
        quarters = int(input("how many quarters?: ")) * 0.25
        dimes = int(input("how many dimes?: ")) * 0.10
        nickles = int(input("how many nickles?: ")) * 0.05
        pennies = int(input("how many pennies?: ")) * 0.01

        if quarters >= 0 and dimes >= 0 and nickles >= 0 and pennies >= 0:
            return round(quarters + dimes + nickles + pennies, 2)
        else:
            print("Negative values are not allowed. Money refunded.")
            return 0.0  # Protect the system by returning 0 on a negative input.

    # Handles invalid numeric input gracefully
    except ValueError:
        print("Invalid input. Money refunded.")
        return 0.0


def is_transaction_successful(money_received, drink_cost):
    """
    Verifies if the user has inserted enough money.
    If successful, updates profit and returns True.
    """
    global profit

    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False

    change = round(money_received - drink_cost, 2)
    if change > 0:
        print(f"Here is ${change} in change.")

    profit += drink_cost
    return True


def make_coffee(drink_name, order_ingredients):
    """
    Deducts the required ingredients from resources
    and serves the selected drink.
    """
    for item, amount in order_ingredients.items():
        resources[item] -= amount

    print(f"Here is your {drink_name} ☕️. Enjoy!")


def print_report():
    """
    Displays the current status of machine resources and profit.
    """
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


# Main program loop
is_on = True

while is_on:
    choice = input(
        "What would you like? (espresso/latte/cappuccino)\n"
        "To generate a report, please enter 'report'.\n"
        "To close, type 'off': "
    ).lower()

    if choice == "off":
        is_on = False

    elif choice == "report":
        print_report()

    elif choice in MENU:
        drink = MENU[choice]

        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

    else:
        print("Invalid selection. Please choose espresso, latte or cappuccino.")
