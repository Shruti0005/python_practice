import random

from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

lives = 6

choosen_word = random.choice(word_list)

placeholder = ""
word_len = len(choosen_word)
for place in range(word_len):
    placeholder += "_"

print(placeholder)

game_over = False
correct_letter = []

while not game_over:
    
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ")[0].lower()
    
    if guess in correct_letter:
        print(f"You've already guessed a {guess}")
    
    display = ""
    for letters in choosen_word:
        if letters == guess:
            display += letters
            correct_letter.append(letters)
        elif letters in correct_letter:
            display += letters
        else:
            display += "_"
            
    print("Word to guess: " + display)
    if guess not in choosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        if lives == 0:
            game_over = True
            print(f"****************************IT'S WAS '{choosen_word}' YOU LOSE!****************************")
    
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN!****************************")
    
    print(stages[lives])