# Lesson 5 - For loops
# Solution to Practice Question 1

# Copyright 2022 Qi Tianshi and Tyros members. Licensed under GNU GPLv3.


# Write a programme to print the following number pattern using a loop.

# ```
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# ```


for i in range(1, 6):

    # Initialises a variable to which we will append the numbers in each line.
    result = ""

    # A nested for loop that prints every number from 0 up to i (inclusive)
    for j in range(1, i + 1):

        # Appends the new number along with a space.
        result += str(j) + " "

    print(result)


# The reason we had a `result` variable was because the print statement will,
# by default, add a newline to the end of everything printed. We could have
# simplified this code even further by telling the print() function to change
# the ending character to a space.

# Uncomment this code to see if for yourself.


# for i in range(1, 6):

#     for j in range(1, i + 1):

#         # By writing `end=" "`, we tell print() to change the ending character to a space instead of a newline.
#         print(j, end=" ")

#     # This prints a newline.
#     print("")
