# Import random module, game_data and logos
from art import logo, vs
from game_data import data
import random


# Set score
score = 0
account_a = 0
account_b = 0
account_a_follower = 0
account_b_follower = 0


# Main function of the game
def higher_lower():
    # Printing logo
    print(logo)

    # Randomly generate first and Second options from the dictionary
    def generate_random_options():

        global account_a
        global account_b
        # Generating first option
        account_a = random.choice(data)
        print(f"Compare A: {account_a['name']}, {account_a['description']}, {account_a['country']}")

        will_continue = True
        while will_continue:
            # Printing 'vs' logo
            print(vs)
            # Generating_second_option
            account_b = random.choice(data)
            print(f"Against B: {account_b['name']}, {account_b['description']}, {account_b['country']}\n")

            # Check function to check the answer of users
            def check():
                global account_a_follower
                global account_b_follower
                global score
                # Asking user to choose one option from the above options
                guess = input("Who has more followers? Type 'A' or 'B'.\nEnter your answer: ").lower()
                account_a_follower = account_a['follower_count']
                account_b_follower = account_b['follower_count']
                if account_a_follower > account_b_follower:
                    return guess == "a"
                else:
                    return guess == "b"
            is_correct = check()
            global account_a_follower
            global account_b_follower
            global score
            if is_correct:
                print("You are right!")
                score += 1
                print(f"Your score is {score}")
                account_a = account_b
                account_a_follower = account_b_follower
                print(f"Compare A: {account_a['name']}, {account_a['description']}, {account_a['country']}")

            else:
                print("You are wrong!")
                print(f"Your final score is {score}")
                will_continue = False

        # Calling the generate_random_options function
    generate_random_options()


# Calling the main function
higher_lower()
