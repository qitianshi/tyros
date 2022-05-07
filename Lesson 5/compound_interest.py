# Lesson 5 - For loops
# Solution to Practice Question 3

# Copyright 2022 Qi Tianshi and Tyros members. Licensed under GNU GPLv3.


# You're depositing some money into a savings account, for which you earn 0.1%
# interest per annum. Write a programme that takes in the original amount
# deposited, and prints out the total amount of money in the account for each
# of the next 10 years.


money = int(input("Original deposit amount: "))
this_year = 2022

for i in range(10):

    this_year += 1
    money *= 1.001

    print(this_year, money)


# Try adding functionality to your code to handle additional deposits and
# withdrawals every year, or to have the interest rate be changing.
