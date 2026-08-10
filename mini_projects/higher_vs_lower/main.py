from game_data import data
from art import logo, vs
import random

def format_data(account):
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_desc}, from {account_country}"


def check_answer(user_guess, a_answer, b_answer):
    if a_answer > b_answer:
        return user_guess == 'a'
    else:
        return user_guess == 'b'

print(logo)
score = 0
should_continue_game = True
account_b = random.choice(data)

while should_continue_game:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n"*20)
    print(logo)

    account_a_follower = account_a['follower_count']
    account_b_follower = account_b['follower_count']

    is_answer_correct = check_answer(guess, account_a_follower, account_b_follower)
    if is_answer_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, you are wrong! Current score: {score}.")
        should_continue_game = False
