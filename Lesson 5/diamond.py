# Lesson 5 - For loops
# Solution to Practice Question 2

# Copyright 2022 Qi Tianshi and Tyros members. Licensed under GNU GPLv3.


# Write a programme to print the following pattern using for loops. (Hint: Use
# two for loops for this! The first for loop is for the upper half, and the
# second for loop is for the lower half.)

# ```
#    *
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#    *
# ```


# Notice that this shape is made of two triangles. In the top half, the number
# of asterisks is equal to the line number; the converse is true for the bottom
# half. The padding is done with spaces.

for i in range(1, 5):

    # This is to add the spaces at the beginning of each line.
    # Remember that the multiplication operator repeats strings.
    output = " " * (4 - i)

    # With each run of the loop, the number of asterisks decreases.
    output += "* " * i

    print(output)

# We've now printed the top half of the triangle. Now, we do the converse for
# the bottom half.

for i in range(1, 4):

    # We've combined the same code from the above step into a single line.
    output = (" " * i) + ("* " * (4 - i))

    print(output)


# Try challenging yourself by printing other shapes, like triangles,
# parallelograms, and circles. And get the user to input the size of the shape
# they want.
