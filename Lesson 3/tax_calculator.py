# Lesson 3 - If/else statements
# Solution to Practice Question 2

# Copyright 2022 Qi Tianshi and Tyros members. Licensed under GNU GPLv3.


# In Singapore, individual income taxes are calculated based on a progressive
# tax model. Using the information on the IRAS website
# (https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-residency-and-tax-rates/individual-income-tax-rates),
# write an income tax calculator for a tax resident for 2022.


income = int(input("What's your income this year? "))

if income < 20000:
    tax_payable = 0
elif income <= 30000:
    tax_payable = (income - 20000) * 0.02
elif income <= 40000:
    tax_payable = (income - 30000) * 0.035 + 200
elif income <= 80000:
    tax_payable = (income - 40000) * 0.07 + 550
elif income <= 120000:
    tax_payable = (income - 80000) * 0.115 + 3350
elif income <= 160000:
    tax_payable = (income - 120000) * 0.15 + 7950
elif income <= 200000:
    tax_payable = (income - 160000) * 0.18 + 13950
elif income <= 240000:
    tax_payable = (income - 200000) * 0.19 + 21150
elif income <= 280000:
    tax_payable = (income - 240000) * 0.195 + 28750
elif income <= 320000:
    tax_payable = (income - 280000) * 0.20 + 36550
else:
    tax_payable = (income - 320000) * 0.22 + 44550

print("Your personal income tax is:", tax_payable)


# This code might be considered badly writen because it contains a lot of
# repetition, and its data is all over the place. If one of the tax bracekts
# were to change, we'd have to manually recalculate everything! We wrote our
# solution code like this because so far we've only learned if/else. If you're
# feeling adventurous, research for loops and lists and try using them to
# improve this code!
