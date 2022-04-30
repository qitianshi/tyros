# Lesson 4 - While loops
# Solution to Practice Question 1

# Copyright 2022 Qi Tianshi and Tyros members. Licensed under GNU GPLv3.


# In maths, the factorial of an integer is the product of that integer and all
# its preceding integers. It is denoted by the `!` mark. For example,
# `5! = 5 × 4 × 3 × 2 × 1 = 120`. Write a programme that takes in an integer,
# and calculates its factorial.


factorial_of = int(input("Find the factorial of: "))
result = 1

while factorial_of >= 1:
    result *= factorial_of
    factorial_of -= 1

print(result)


# There are, of course, other ways to approach this question. We'll look at
# another way next week, using the for loop.
