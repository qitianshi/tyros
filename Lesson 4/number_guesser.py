# Lesson 4 - While loops
# Solution to Practice Question 2

# Copyright 2022 Qi Tianshi and Tyros members. Licensed under GNU GPLv3.


# Let's play a number guessing game. The user will think of a number between 1
# and 10. A Python programme will guess the number and ask if it's right or
# wrong. If the guess is wrong, the programme will guess again. If the guess is
# right, the game will finish, and the programme will display the number of
# rounds it's taken to guess the number correctly.


print("Think of a number between 1 and 10. I'll try and guess your number.")

current_guess = 1
number_of_guesses = 0

while current_guess <= 10:

    print("My guess is", current_guess)

    number_of_guesses += 1
    user_input = input("Am I correct? (y/n) ")
    guessed_correctly = user_input == "y"

    if guessed_correctly:
        break

    current_guess += 1

print("Guessed in", number_of_guesses, "tries.")


# Because we're only demonstrating while loops in this solution code, we didn't
# include checks for whether the user chose a valid option between "y" or "n",
# or what happens if the user replied "n" every single time. Try adding those
# yourself!
