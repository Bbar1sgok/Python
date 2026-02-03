from machine import Machine
from menu import MENU

machine = Machine()
is_on = True

# Main application loop
while is_on:
    choice = input(
        "What would you like? (espresso/latte/cappuccino/report/off): "
    ).lower()

    if choice == "off":
        is_on = False

    elif choice == "report":
        machine.print_report()

    elif choice in MENU:
        drink = MENU[choice]

        if machine.is_resource_sufficient(drink["ingredients"]):
            payment = machine.process_coins()

            if machine.is_transaction_successful(payment, drink["cost"]):
                machine.make_coffee(choice, drink["ingredients"])

    else:
        print("Invalid selection.")