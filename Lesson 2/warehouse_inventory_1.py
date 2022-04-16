# Lesson 2 - Operators
# Solution to Practise Question 2

# Copyright 2022 Qi Tianshi and Tyros members. Licensed under GNU GPLv3.


# You're the inventory manager for a warehouse that supplies soft drinks. You
# have a fixed number of cases of drinks in your stock. Each case costs $15. To
# cover delivery costs, the minimum order amount must be at least $100.

# Write a program that helps you evaluate new orders. Your program should take
# in the number of cases ordered, then decide if you should accept the order
# using the conditions above. Print out: whether you're accepting the order,
# the amount of money you should receive, and how much stock you'll have left
# after fulfilling the order.


# We'll put the solution here in a while. Try it yourself first!

stock = 100
cases = int(input("Enter the number of cases: "))

print("Am I accepting the order?", cases * 15 >= 100 and cases <= stock)
print("Amount of money I should receive:", cases * 15)
print("How much stock I'll have left after fulfilling the order:", stock - cases)
