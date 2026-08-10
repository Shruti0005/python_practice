import random
from mimetypes import guess_type

import art

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turn):
    if guess > answer:
        print("Too high")
        return turn - 1
    elif guess < answer:
        print("Too low")
        return turn - 1
    else:
        print(f"You got it! The answer was {answer}.")
        return 0

def difficulty():
    level_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level_choice == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer_num = random.randint(1, 100)

    turns = difficulty()

    guess_num = 0
    while guess_num != answer_num:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess_num = int(input("Make a guess: "))
        turns = check_answer(guess_num, answer_num, turns)

        if turns == 0:
            print("You've run out of guesses. Refresh the page to run again.")
            return
        elif guess_num != answer_num:
            print("Guess again.")

game()