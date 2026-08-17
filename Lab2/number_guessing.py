# This program is a number guessing game with a maximum of 7 attempts.

import random

number = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("Guess the number between 1 and 100.")
print("You have 7 attempts.")

while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Correct!")
            print("You guessed it in", attempts, "attempts.")
            break

    except ValueError:
        print("Please enter a valid number.")

else:
    print("Game over!")
    print("The correct number was", number)
