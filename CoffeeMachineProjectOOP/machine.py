class Machine:
    def __init__(self):
        # Initial resources of the coffee machine
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        self.profit = 0.0

    def print_report(self):
        # Prints current machine status
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.profit}")

    def is_resource_sufficient(self, order_ingredients):
        # Checks if enough resources exist for the selected drink
        for item, amount in order_ingredients.items():
            if self.resources.get(item, 0) < amount:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        # Takes coin input from the user and calculates total amount
        print("Please insert coins.")
        try:
            quarters = int(input("how many quarters?: ")) * 0.25
            dimes = int(input("how many dimes?: ")) * 0.10
            nickles = int(input("how many nickles?: ")) * 0.05
            pennies = int(input("how many pennies?: ")) * 0.01

            return round(quarters + dimes + nickles + pennies, 2)
        except ValueError:
            # Handles invalid (non-integer) input
            return 0.0

    def is_transaction_successful(self, money_received, drink_cost):
        # Checks if the user inserted enough money
        if money_received < drink_cost:
            print("Sorry that's not enough money. Money refunded.")
            return False

        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")

        self.profit += drink_cost
        return True

    def make_coffee(self, drink_name, order_ingredients):
        # Deducts used resources and serves the coffee
        for item, amount in order_ingredients.items():
            self.resources[item] -= amount
        print(f"Here is your {drink_name} ☕️. Enjoy!")