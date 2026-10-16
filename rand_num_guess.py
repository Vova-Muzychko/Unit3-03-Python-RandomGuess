# Created by: Vova M
# Date: October 16, 2026
# This program is a random number guessing game.

import random

# Generate a random number from 0 to 9.
print("Username: Vova M")
correct_answer = random.randint(0, 9)

# Ask the user to guess the number.
guess = int(input("Guess a number between 0 and 9: "))

# Check if the guess is correct.
if guess == correct_answer:
    print("You guessed correctly!")
else:
    print("You guessed wrong. The correct answer was:", correct_answer)
