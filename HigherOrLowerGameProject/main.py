import random
from game_data import data
from art import logo, vs


# Returns a random account from the dataset
def get_random_account():
    return random.choice(data)


# Determines whether the user's choice is correct
# Returns +1 for correct or tie, -1 for wrong answer
def answer_controller(user_input, selected_A, selected_B):

    if selected_A["follower_count"] > selected_B["follower_count"] and user_input == "a":
        return 1

    elif selected_A["follower_count"] < selected_B["follower_count"] and user_input == "b":
        return 1

    # Tie is intentionally treated as a neutral win
    elif selected_A["follower_count"] == selected_B["follower_count"]:
        return 1

    else:
        return -1


# Ensures only valid input is accepted
def get_user_input():
    while True:
        user_input = input(
            "Who has more followers. Type 'A', 'B' or prees 0 to exit: "
        ).lower()

        if user_input in ["a", "b", "0"]:
            return user_input
        else:
            print("Invalid input. Please try again.")


user_score = 0

while True:

    print(logo)

    selected_A = get_random_account()
    selected_B = get_random_account()

    # Prevent comparing the same account
    while selected_A == selected_B:
        selected_B = get_random_account()

    print(
        f"Compare A: {selected_A['name']}, "
        f"{selected_A['description']}, {selected_A['country']}"
    )

    print(vs)

    print(
        f"Compare B: {selected_B['name']}, "
        f"{selected_B['description']}, {selected_B['country']} \n"
    )

    user_input = get_user_input()

    # Exit condition
    if user_input == "0":
        print("Game closed.")
        break

    result = answer_controller(user_input, selected_A, selected_B)

    # Game ends on wrong answer
    if result == -1:
        print(f"Sorry, that's wrong. Final score: {user_score}")
        break
    else:
        user_score += result
        print(f"You are right! Current score: {user_score}")
