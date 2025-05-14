# The guessing game

import random

def guess_number():
    mysterious_number = random.randint(1, 100)
    attempts = 0
    guess = False

    print("******************************************")
    print("\t\tWelcome to the guessing game")
    print("******************************************")
    print("I am a number between 1 and 100. What number am I?")

    while not guess:
        try:
            attempt = int(input("Enter your guess: "))
            attempts += 1

            if attempt < mysterious_number:
                print("The number is too small try again ")
            elif attempt > mysterious_number:
                print("The number is too big try again ")
            else:
                guess = True
                print("Congratulations!! You guessed right after", attempts," attempts")
        except:
            print("Please enter a valid number.") 

# Running the game
guess_number()  
