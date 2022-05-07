# Lesson 5 - For loops

## Introduction
[In the previous lesson](https://github.com/qitianshi/tyros-resources/tree/main/Lesson%204), we learnt about how to use while loops to repeat a particular set of steps.

As we mentioned last time, `while` is not the only type of loop at our disposal! Sometimes, we want our programme to loop over a sequence. Today we'll discover how we can do that using for loops.

## Iteration
Recall from our previous lesson that a while loop repeats a set of instructions for as long as a condition is true, however many times that may be. On the other hand, a for loop repeats a set of instructions _for_ every item in a sequence. This is called iteration.

We can illustrate the concept of iteration with a simple example. Imagine you have a box of chocolates, containing many pralines, and you want to note down which ones contain nuts and which don't. You would take the first chocolate, see if it has nuts, and write down the answer. Then, you'd repeat the same set of steps for each chocolate in the box.

Formally, we say that "_**for** each chocolate **in** the box, you check it for nuts_". That's where the for loop gets its name from.

You are _iterating_ over each chocolate in the box, and looping the same steps for each packet. The box can be thought of as a sequence of chocolates, because it contains an ordered list of items.

## For loops
A for loop repeats a set of instructions _for_ every item in a sequence.

Generally, a basic for loop looks like. Just as before, pay attention to the indentation.

```Python
for ITERATOR in SEQUENCE:
    print("Looped")
```

We can draw parallels between this syntax and the chocolate analogy from earlier:

> ***for*** each chocolate ***in*** the box, you check it for nuts

In both cases, we begin with the keyword `for`; this tells Python we're writing a for loop. `ITERATOR` is analogous to "each chocolate"; it refers to the individual item in the sequence we're currently looking at in this round of the loop. We then see another keyword, `in`; this is also essential. `SEQUENCE` would be analogous to "the box"; it refers to the sequence of items we're looking at. Finally, we see a some instructions: `print()` and "check it for nuts".

To recap, `for` and `in` are keywords that identify for loops in Python. `SEQUENCE` is the sequence of items we're iterating through. `ITERATOR` is a variable that refers to the current item in `SEQUENCE` we're looking at.

Before we dive into the specifics, let's first look at an example of how the for loop is used! Last week, we wrote some code using a while loop to emulate *The Price is Right*:

> On the game show *The Price is Right*, contestants guess the prices of various items. The winner is the one whose guess is the closest to the actual price, without going over. Let's try writing some code that continually accepts guesses, until one goes over.
>
> ```
> actual_price = 50
> guess = 0
>
> while guess <= actual_price:
>     guess = float(input("What's your guess? "))
>
> print("You've gone over!")
> ```

Well, one contestant figured out a loophole, and guessed 1, 2, 3... all the way until the actual price. Our poor game master couldn't do anything — it wasn't against the rules! They've decided to change the rules: instead of unlimited guesses, contestants can only guess 10 times. Let's try changing our code to fit the new rules.

```python
actual_price = 50

for i in range(0, 10):
    guess = float(input("What's your guess? "))

    if guess == actual_price:
        print("You got it!")
        break    # Terminat the  loop after a correct guess

    elif guess < actual_price:
        print("Too low...")

    else:
        print("Too high...")

print("Too many guesses.")
```

Try running this code and type in different guesses! You'll see that if you keep getting wrong guesses, you will only get ten tries in total.

`i` is conventionally used as the iterator variable. Here, `range()` provides us with a sequence of numbers between 0 (inclusive) and 5 (exclusive). More on that later.

You'll also notice that the `break` keyword we learned last lesson (in the context of while loops) works with for loops too! So does `continue`.

## `range()`
`range()` is a function that gives us a sequence of numbers. You've probably already spotted it in the example, but now let's get familiar with this function.

### A quick word about functions
"Functions" might be an alien term to you, but you're actually already using them all the time!

`print()` and `input()` are both examples of functions. Notice that every function has a set of brackets `()` afterward. Inside these brackets, we can write multiple parameters, separated by commas. You're probably used to seeing something like `print("My age is", age)`. This is a `print()` function in which we give two parameters: first, the string `"My age is"`; and second, the variable `age`.

The exact number, order, and type of parameters passed into any function is predefined, and we must follow this syntax exactly. You might have discovered that we can't run `input("How old are you in", year)`, and expect it to print something like `How old are you in 2022`, because the `input()` function only allows a singular string as its output parameter.

---

Back to the `range()` function. Its purpose is to give us a sequence of numbers, between a start and end point.

Depending on the number of parameters, `range()` behaves a little differently:

```Python
range(START, STOP, STEP)
range(START, STOP)
range(STOP)
```

`START` is the starting number (inclusive). `STOP` is the ending number (exclusive). `STEP` is the difference between adjacent numbers. If `STEP` is not provided (as in line 2), it defaults to `1`. If `START` is not provided, it defaults to `0`.

Try running this code:

```python
for i in range(6):
    print(i)
```

```
> 0
> 1
> 2
> 3
> 4
> 5
```

Notice how the value of `i` changes with each round of the loop. Go back to the earlier section if you're confused as to why.

We'll illustrate with a few examples.

| Range | Result |
| -- | -- |
| `range(0, 6, 1)` | 0, 1, 2, 3, 4, 5 |
| `range(5, 10, 1)` | 5, 6, 7, 8, 9 |
| `range(5, 10, 2)` | 5, 7, 9 |
| `range(12, 6, -1)` | 12, 11, 10, 9, 8, 7 |
| `range(0, 6)` | 0, 1, 2, 3, 4, 5 |
| `range(6)` | 0, 1, 2, 3, 4, 5 |

## More examples

Let's go through a few more examples of for loops!

Let's try coding a programme to accept a number from a user and calculate the sum of all numbers from 1 to that given number.

```python
total = 0
stop = int(input("Please enter a number: "))

for i in range(stop + 1):
    total = total + i    # or we can use total += i here

print("The sum is: " + str(total))
```

```
> Please enter a number: 10
> The sum is: 55
```

Remember that since we want to include the given number, we have to add `+1` to `stop`!

---

We can also have nested for loops, like this:

```python
for i in range(1, 6):
    for j in range(i):
        print(*, end = ' ')
```

```
> *
> * *
> * * *
> * * * *
> * * * * *
```

In each round of the outer for loop, the inner for loop will run in its entirety. Remember that since `i` and `j` are variables, we must have different variable names for the iterator.

## Let's practise

Write a programme to print the following number pattern using a loop.

```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

[**Solution**](https://github.com/qitianshi/tyros-resources/blob/main/Lesson%205/number_triangle.py)

---

Write a programme to print the following pattern using for loops. (Hint: Use two for loops for this! The first for loop is for the upper half, and the second for loop is for the lower half.)

```
   *
  * *
 * * *
* * * *
 * * *
  * *
   *
```

[**Solution**](https://github.com/qitianshi/tyros-resources/blob/main/Lesson%205/diamond.py)

---

You're depositing some money into a savings account, for which you earn 0.1% interest per annum. Write a programme that takes in the original amount deposited, and prints out the total amount of money in the account for each of the next 10 years.

[**Solution**](https://github.com/qitianshi/tyros-resources/blob/main/Lesson%205/compound_interest.py)

## Conclusion
In this lesson, we learnt about for loops, a type of loop that repeats for a specified number of times.

This is the last lesson for this iteration of our project. Read [our final lesson notes](https://github.com/qitianshi/tyros-resources/tree/main/Lesson%20X) to see how you can continue your learning journey, how you can apply Python in your everyday life, and our sign-off.

### Further reading
We've only touched on the absolute most basic type of for loop (`for i in range()`), but Python for loops are actually much more capable! `range()` isn't the only type of sequence you can iterate over. Check out these resources for more:

* [For loops](https://www.w3schools.com/python/python_for_loops.asp)
* [Lists](https://www.w3schools.com/python/python_lists.asp)
* [Functions](https://www.w3schools.com/python/python_functions.asp)

---

© 2022 Qi Tianshi and Tew En Hao. This file is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International license (CC BY-NC-SA 4.0) license](https://creativecommons.org/licenses/by-nc-sa/4.0/).
