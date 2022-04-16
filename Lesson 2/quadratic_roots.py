# Lesson 2 - Operators
# Solution to Practise Question 2

# Copyright 2022 Qi Tianshi and Tyros members. Licensed under GNU GPLv3.


# A quadratic equation may be expressed in terms of `ax² + bx + c = 0`, where
# `a`, `b` and `c` are constants, and `a` is non-zero.

# Write a program that takes in the values of `a`, `b`, and `c`, and prints the
# two roots of the equation, assuming that the roots are real. (Hint: do you
# remember lower sec math?)


# We'll put the solution here in a while. Try it yourself first!


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

root1 = (-b + (b**2-(4*a*c))**0.5)/(2*a) 
root2 = (-b - (b**2-(4*a*c))**0.5)/(2*a)

print(f"{root1}\n{root2}")
