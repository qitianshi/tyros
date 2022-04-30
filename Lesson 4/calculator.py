# Lesson 4 - While loops
# Solution to Practice Question 3

# Copyright 2022 Qi Tianshi and Tyros members. Licensed under GNU GPLv3.


# I want to do math with Python! Help me make a calculator that is able to add,
# subtract, multiply and divide.

# Your programme should first display a menu that looks like this:

# ```
# 0: Quit
# 1: Add
# 2: Subtract
# 3: Multiply
# 4: Divide

# Choose an option:
# ```

# I will choose an option by typing its number. Your programme should include a
# check to make sure that the number I've typed in is a valid option. If it
# isn't, the programme should prompt me to try again.

# Then, your programme should ask me for two numbers. It will then perform the
# operation, and display the number.

# Afterwards, it should show me the original menu again, so I can make as many
# operations as I want.


while True:

    print("----------")

    print("0: Quit")
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")

    option = int(input("Choose an option: "))

    if option == 0:
        break

    elif option == 1:           # Add
        a = float(input("First number: "))
        b = float(input("Second number to add: "))
        result = a + b

    elif option == 2:           # Subtract
        a = float(input("First number: "))
        b = float(input("Second number to subtract: "))
        result = a - b

    elif option == 3:           # Multiply
        a = float(input("First number: "))
        b = float(input("Second number to multiply: "))
        result = a * b

    elif option == 4:           # Divide
        a = float(input("First number: "))
        b = float(input("Second number to divide: "))
        result = a / b

    else:
        print("Invalid option.")
        continue

    print("The result is", result)

    input("Press enter to continue.")       # Waits for the user to press enter.
