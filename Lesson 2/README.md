# Lesson 2 — Operators

## Introduction
In the previous lesson, we learnt about the basic building blocks of programs — variables. While they can be useful on their own, we need them to interact with each other in most cases. It is like getting from one place to another — you need a path! Operators serve as this "path" for us to manipulate variables. As they say, "the whole is greater than the sum of the parts".

## Mathematical operators
Mathematical operators are exactly what they sound like — math. There are your basic _`+` (addition)_, _`-` (subtraction)_, _`*` (multiplication)_ and _`/` (division)_ operators, and there are a few more less commonly seen ones as well.

#### `%` (modulus) and `//` (integer division)
We use `%` to find the remainder of a division problem, while we use `//` to find the quotient.

For example, we have a microwave that displays the time left to heat up food only in seconds, and we want to change it to display the time in both minutes and seconds.

```Python
total_seconds = 400    # time remaining in seconds
min = total_seconds // 60    # remember that 1 minute consists of 60 seconds
sec = total_seconds % 60
print("Time remaining:", min, "minutes and", sec, "seconds.")
```

```
> Time remaining: 6 minutes and 40 seconds.
```

#### `**` (exponentiation)
We use `**` when we want to multiply the same number by itself multiple times. For instance, we want to multiply 2 by itself 3 times. If we use the multiplication operator (`*`), we can write...

```Python
2 * 2 * 2
```

... which does not look too bad. However, what if we wanted to multiply 2 by itself 20 times? While we definitely can do this,

```Python
2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2
```

this takes too much time! (Did I miss out any `2`s?) Instead, we can use `**` to do the same thing. The number on the left is the _number_ to be multiplied, and the number on the right is the _number of times_ to multiply.

```Python
2 ** 20
```


## Comparison operators
Comparison operators are used to compare values. It returns either `True` or `False` according to what is being compared (the _condition_)

#### `==` (equal)
We use `==` to check if two items are equal to each other.

```Python
print(1 == 1)
print("Yes" == "No")
```

```
> True
> False
```

#### `!=` (not equal)
We use `==` to check if two items are not equal to each other.

```Python
print(1 != 1)
print("Yes" != "No)
```

```
> False
> True
```

#### `>` (greater than)
We use `>` to check if the first item is greater than the second item.

```Python
print(2 > 1)
print(5 > 10)
print(1 > 1)
```

```
> True
> False
> False
```

#### `<` (less than)
We use `<` to check if the first item is less than the second item.

```Python
print(2 < 1)
print(5 < 10)
print(1 < 1)
```

```
> False
> True
> False
```

#### `>=` (greater than or equal to)
We use `>=` to check if the first item is greater than or equal to the second item.

```Python
print(2 >= 1)
print(5 >= 10)
print(1 >= 1)
```

```
> True
> False
> True
```

#### `<=` (less than or equal to)
We use `<=` to check if the first item is less than or equal to the second item.

```Python
print(2 <= 1)
print(5 <= 10)
print(1 <= 1)
```

```
> False
> True
> True
```

## Logical Operators
There are three main logical operators: `and`, `or` and `not`. These logical operators allow us to craft checks for us to use!

#### `and`
We use the `and` operator tests two expressions for a test condition to see if it is true or false. If _both_ the tests give a result of `True`, then `and` gives a result of `True`. However, if _either_ of the tests give a result of `False`, then `and` gives a result of `False`.

To illustrate this concept, I will bring in a habit of mine! I like to go to the beach when the weather is sunny and when I am free on that day.

```Python
weather = "sunny"
free = True    # this means I am free

# I am cheating a little here, but we will learn about if-else statements next lesson!
if weather == "sunny" and free == True:
    print("I shall go to the beach!")

weather = "raining"
if weather == "sunny" and free == True:
    print("I shall go to the beach!")
else:
    print("I will not go to the beach...")
```

```
> I shall go to the beach!
> I will not go to the beach...
```

#### `or`
We can also use the `or` operator to test two expressions for a test condition! Difference is, if _either_ of the tests are `True`, then the result of `or` is `True`. Only if _both_ of the tests return a result of `False` will `or` give a result of `False`.

Now if we look at the same example, but we change the `and`s to `or`s:

```Python
weather = "sunny"
free = True    # this means I am free

# I am cheating a little here, but we will learn about if-else statements next lesson!
if weather == "sunny" or free == True:
    print("I shall go to the beach!")

weather = "raining"
if weather == "sunny" or free == True:
    print("I shall go to the beach!")
else:
    print("I will not go to the beach...")
```

```
> I shall go to the beach!
> I shall go to the beach!
```

Since I am still `free`, in this new world, I will go to the beach if I am free or if the weather is sunny! So, I will go to the beach even though it is raining.

#### `not`
We use `not` to test for negation.

```Python
free = False

if not free:
    print("I am not free")
else:
    print("I am free")
```

```
> I am not free
```

## Conclusion
In this lesson, you learnt about operators, specifically mathematical, comparison, and logical operators. Do make good use of them!

---

© 2022 Tew En Hao and Qi Tianshi. This file is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International license (CC BY-NC-SA 4.0) license](https://creativecommons.org/licenses/by-nc-sa/4.0/).
