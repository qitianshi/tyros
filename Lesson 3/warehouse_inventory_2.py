# Lesson 3 - If/else statements
# Solution to Practice Question 1

# Copyright 2022 Qi Tianshi and Tyros members. Licensed under GNU GPLv3.


# Do you remember the inventory manager problem from last week?

# > You're the inventory manager for a warehouse that supplies soft drinks. You
# > have a fixed number of cases of drinks in your stock. Each case costs $15.
# > To cover delivery costs, the minimum order amount must be at least $100.
# >
# > Write a program that helps you evaluate new orders. Your program should
# > take in the number of cases ordered, then decide if you should accept the
# > order using the conditions above, as well as consider if you have enough
# > cases to fufill the order. Print out: whether you're accepting the order,
# > the amount of money you should receive, and how much stock you'll have left
# > after fulfilling the order.

# Previously, because we hadn't learned if/else, our code was limited to
# printing "True" or "False", and we sometimes ended up with negative stocks!

# Using if/else statements, improve your code with more user-friendly messages.
# If the order is rejected, don't print the price of the order or the amount of
# stock left.


stock = 100
orders = int(input("Enter the number of cases: "))
# You need to use int() to convert the string input to an integer.

price = orders * 15

if stock - orders >= 0:
    if price > 100:
        print("I accept the order")
        print("Amount of money I should receive:", price)
        stock = stock - orders
        print("How much stock I'll have left after fulfilling the order:", stock)
    else:
        print("order is below minimum order requirement")

else:
   print("Out of stock sorry")
