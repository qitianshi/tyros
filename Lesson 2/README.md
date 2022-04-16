# Lesson 2 — Operators

## Introduction
In the previous lesson, we learned about the basic building blocks of programs — variables. Variables are like labelled boxes that store values. We can mention the values contained in each box using their labels; more accurately, we refer to variables using their variable names. [Here are the notes from Lesson 1 if you need a refresh.](https://github.com/qitianshi/tyros-resources/tree/main/Lesson%201)

While variables can be useful on their own, they become so much more powerful when we manipulate them and make them interact with each other. We saw a brief example of this last week: using `+-*/` to add, subtract, multiply, and divide values. These are examples of operators — we use them to _operate_ on values. Today, you'll discover that there's so much more to operators than those four!

Python has three categories of operators: mathematical, comparison, and logic. Let's dive in!

## Mathematical operators
Mathematical operators are exactly what they sound like — math. Here are the ones we'll be looking at:

* `+`, `-`, `*`, `/`: addition, subtraction, multiplication, and division. You're already familiar with these.
* `//`: floor division, a special type of division that always gives you integers.
* `%`: modulo, which gives you the remainder after dividing.
* `**`: exponentiate, which lets you calculate powers.

We'll first understand what the three new operators (`//`, `%`, and `**`) do, then we'll look at some examples of how we can use them.

### `//` (floor division)
Let's try to evaluate `25 / 10`. The standard division operator, `/`, will give us a floating-point number (non-whole number): `2.5`. [(If you need a recap of data types...)](https://github.com/qitianshi/tyros-resources/tree/main/Lesson%201#data-types)

Sometimes, we want an integer result instead. This is where the floor division, `//`, operator comes in.

```Python
print(25 // 10)
print(39 // 10)
print(2 // 3)
```

```
> 2
> 3
> 0
```

Notice that `//` always rounds _down_ to the nearest integer.

### `%` (modulo)
In primary school, we learned that `7 ÷ 3` gives us a _quotient_ of `2` and a _remainder_ of `1`; i.e. `7 = 3 × 2 + 1`.

`%` doesn't have anything to do with percentages! In Python, it's the _modulo_ operator — it tells us the _remainder_ after a division.

```Python
print(7 % 3)
print(8 % 4)
```

```
> 1
> 0
```

### `**` (exponentiation)
What's the volume of a cube whose sides are 5m? In math, we'd calculate that with `5³`, which is `5 × 5 × 5`.

In Python, we'd represent `5³` with `5 ** 3`. `**` is the exponential operator!

```Python
print(5 ** 3)
print(0.5 ** 2)
```

```
> 125
> 0.25
```

### More examples with operators
Let's see how we can use operators to solve some real life problems!

We can use `+-*/` for simple operations. Let's use Python to help us run a hot chocolate stall.

```Python
cups_in_stock = 25        # I have 25 cups of hot chocolate left.
price_per_cup = 1.5       # Each cup costs $1.50

# A customer comes.
cups_bought = 4          # The customer asks for 4 cups of hot chocolate.

total_price = cups_bought * price_per_cup
cups_in_stock = cups_in_stock - cups_bought

print("For", cups_bought, "cups of hot chocolate, you need to pay", total_price, "dollars.")
print("I now have", cups_in_stock, "cups of hot chocolate left.")
```

```
> For 4 cups of hot chocolate, you need to pay 6.0 dollars.
> I now have 21 cups of hot chocolate left.
```

At our hot chocolate stall, we have a microwave to heat up our milk. But our microwave only displays seconds! Let's convert it to minutes and seconds.

```Python
total_seconds_remaining = 415    # Total time remaining in seconds

min = seconds_remaining // 60    # Remember that 1 minute is 60 seconds
sec = seconds_remaining % 60

print("Time remaining:", min, "minutes and", sec, "seconds.")
```

```
> Time remaining: 6 minutes and 55 seconds.
```

## Comparison operators
Comparison operators are used to compare two values. They give us either `True` or `False`.

Python comparison operators are just like math! Here's a handy table to help you remember:

| Math | Python | Description | Example |
| ---- | ------ | ----------- | ------- |
| =    | `==`   | equal to    | `1 + 2 == 3` |
| ≠    | `!=`   | not equal to | `2 - 1 != 5` |
| >    | `>`    | greater than | `5 > 2` |
| ≥    | `>=`   | greater than or equal to | `5 > 2`, `3 >= 3` |
| <    | `<`    | less than | `1 < 3` |
| ≤    | `<=`   | less than or equal to | `1 < 3`, `3 <= 3` |

Printing the result of a comparison will only give us one of two possible values, `True` or `False`.

```Python
print(5 > 2)
print(8 <= (16 / 2))
print(3 == 4)
print(3 != 4)
print(4 != 4)
```

```
> True
> True
> False
> True
> False
```

We can also use the `==` and `!=` operators to compare strings.

```Python
print("Hello" == "Hi")
print("One" != "Two")
```

```
> False
> True
```

**Important**: The comparison operator `==` and the assignment operator `=` are not the same. Can you explain their differences?

## Logical Operators
Logical operators help us evaluate combinations of boolean (`True` or `False`) values.

There are three main logical operators:
* `or` gives `True` only if either value is `True`.
* `and` gives `True` only if both values are `True`.
* `not` simply inverses the value — `True` becomes `False`, and `False` becomes `True`.

### `or`
The `or` operator tests two boolean values. If _either_ of the tests are `True`, then the result of `or` is `True`. Only if _both_ of the tests return a result of `False` will `or` give a result of `False`.

| Expression | Result |
| ---------- | ------ |
| `True or True` | `True` |
| `True or False` | `True` |
| `False or True` | `True` |
| `False or False` | `False` |

I like shopping online! If I need new shoes, I'll go and buy a pair online. But if I see a discount, I'll still buy a pair even if I don't need them. In other words, if I need new shoes, _or_ they're on discount, I'll buy them.

Let's write a Python program to help me decide if I'm buying new shoes!

```Python
need_new_shoes = False
on_discount = True

will_buy_shoes = need_new_shoes or on_discount
print("Will I buy new shoes?", will_buy_shoes)
```

```
> Will I buy new shoes? True
```

### `and`
If _both_ the tests are `True`, then `and` gives `True`. However, if _either_ of the tests are `False`, then `and` gives a result of `False`.

| Expression | Result |
| ---------- | ------ |
| `True and True` | `True` |
| `True and False` | `False` |
| `False and True` | `False` |
| `False and False` | `False` |

My parents have scolded me for my online shopping habits 🙁. Now, they say I can only buy new shoes if I need them _and_ they're also on discount! Let's change our previous Python program a little bit.

```Python
need_new_shoes = False
on_discount = True

will_buy_shoes = need_new_shoes and on_discount
print("Will I buy new shoes?", will_buy_shoes)
```

```
> Will I buy new shoes? False
```

### `not`
Unlike `and` and `or`, `not` acts only on a single boolean value. It simply inverses it — `True` becomes `False`, and `False` becomes `True`.

| Expression | Result |
| ---------- | ------ |
| `not True` | `False` |
| `not False` | `True` |

My parents have softened up a bit. Now they say that if I didn't buy any shoes, I can go and buy a jacket!

```Python
bought_shoes = False

will_buy_jacket = not bought_shoes
print("Will I buy a new jacket?", will_buy_jacket)
```

```
> Will I buy a new jacket? True
```

## More examples
Just like in math, we can use brackets to specify the order of operations.

```Python
price_of_drink = 1.2
price_of_burger = 4.5

number_of_sets_ordered = 5

total_price = (1.2 + 4.5) * 5
print("Total price is", total_price)
```

```
> Total price is 28.5
```

We even combine multiple operators together!

```Python
number_of_sets_ordered = 5
total_price = 28.5

money_in_wallet = 30
number_of_friends = 6

should_buy_meal = total_price <= money_in_wallet and number_of_friends == number_of_sets_ordered
print("Should I buy the meal?", should_buy_meal)
```

```
> Should I buy the meal? False
```

## Conclusion
Operators let us manipulate data and variables. There are three types of operators: mathematical, comparison, and logical.

In the next lesson, you'll see how we can further use these operators to make our code adapt to different scenarios!

---

© 2022 Qi Tianshi and Tew En Hao. This file is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International license (CC BY-NC-SA 4.0) license](https://creativecommons.org/licenses/by-nc-sa/4.0/).
