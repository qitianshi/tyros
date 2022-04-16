# Lesson 2 - Operators
# Solution to Practise Question 1

# Copyright 2022 Qi Tianshi and Tyros members. Licensed under GNU GPLv3.


# Write a program that takes in a temperature in fahrenheit, converts it to
# celsius, then prints the result. (Hint: you'll need to search for the
# conversion formula.)


temperature_in_fahrenheit = int(input("Enter temperature in Fahrenheit: "))
temperature_in_celsius = (temperature_in_fahrenheit - 32) * 5/9
print("Temperature in celsius is", temperature_in_celsius)
