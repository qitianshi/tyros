# Lesson 2 - Operators
# Solution to Practice Question 4

# Copyright 2022 Qi Tianshi and Tyros members. Licensed under GNU GPLv3.


# `xor` is another useful logical operator that gives `True` only if exactly
# one of the two boolean values are `True`, but not both.

# | Expression        | Result  |
# | ----------------- | ------- |
# | `True xor True`   | `False` |
# | `True xor False`  | `True`  |
# | `False xor True`  | `True`  |
# | `False xor False` | `False` |

# Unfortunately, Python doesn't have a built-in `xor` operator, so you can't
# simply type `True xor False` in Python.

# Write some code using the other logic operators(`and`, `or`, `not`) to get
# the same result as `xor` would give you. Test your code using the 4 examples
# in the table above.


a = True
b = False

print((a and not b) or (not a and b))


# Apart from NOT, AND, and OR, there are many other logical operators in
# computer science. Logic gates form the heart of our modern computers; they're
# essentially overgrown logical calculators! Research on NAND, NOR, XOR, and
# XNOR, and try coding them in Python using `not`, `and`, and `or`!
