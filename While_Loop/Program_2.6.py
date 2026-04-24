# Guess the number game

import random

print("----- Guess the number game -----\n")

secret = random.randint(1, 10)

guess = 0

while guess != secret:
    guess = int(input("Guess a number (1-10) -_- "))
    print("\n")

    if guess < secret:
        print("Too low -_-")
    elif guess > secret:
        print("Too high -_-")

print("Correct! You guessed it -_-")
