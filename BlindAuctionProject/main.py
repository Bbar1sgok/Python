import os
from art import logo

# Blind Auction
#  A console-based blind auction application built with Python.
#  Users submit hidden bids, and the program determines the highest bidder at the end.
#  Focuses on dictionaries, control flow, functions, and input validation.

def clear_screen():
    # Clears the terminal screen (Windows / Mac / Linux compatible)
    os.system('cls' if os.name == 'nt' else 'clear')


def find_highest_bidder(bidding_record):

    # Takes a dictionary of bids and prints the winner with the highest amount.

    highest_bid = 0
    winner = ""

    # Loop through all bidders to find the highest bid
    for bidder, bid_amount in bidding_record.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")


print(logo)

offers = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name?: ")

    try:
        bid = int(input("What is your bid?: $"))
    except ValueError:
        # Prevents the program from crashing on invalid input
        print("Invalid input. Please enter a number.")
        continue

    offers[name] = bid

    should_continue = input(
        "Are there any other bidders? Type 'yes' or 'no':\n"
    ).lower()

    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(offers)
    elif should_continue == "yes":
        # Clears screen to keep bids hidden from next bidder
        clear_screen()
