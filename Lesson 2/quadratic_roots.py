# Lesson 2 - Operators
# Solution to Practice Question 3

# Copyright 2022 Qi Tianshi and Tyros members. Licensed under GNU GPLv3.


# A quadratic equation may be expressed in terms of `ax² + bx + c = 0`, where
# `a`, `b` and `c` are constants, and `a` is non-zero.

# Write a program that takes in the values of `a`, `b`, and `c`, and prints the
# two roots of the equation, assuming that the roots are real. (Hint: do you
# remember lower sec math?)


a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# This part uses the quadratic formula: https://en.wikipedia.org/wiki/Quadratic_formula
# For the square root, recall that √x = x^0.5
root1 = (-b + (b ** 2 - (4 * a * c)) ** 0.5) / (2 * a)
root2 = (-b - (b ** 2 - (4 * a * c)) ** 0.5) / (2 * a)

print("The roots are", root1, "and", root2)
