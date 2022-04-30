# Lesson 4 - While loops

## Introduction
[In the previous lesson](https://github.com/qitianshi/tyros-resources/tree/main/Lesson%203), we learnt about how to use if/else statements to make our code respond to different conditions. That was our first foray into control flow.

Another core concept in computer science is the loop. We often want computers to repeatedly do things over and over again. Think of traffic junctions that repeat the same pattern of lights, a login page where you're only allowed in after you write the correct password, or even your laptop screen refreshing 60 times a second.

Simply put, a loop repeats a set of steps. For our course, we'll be looking at the two most common types of loops. In this lesson, we'll explore the while loop.

## The `while` loop
A while loop repeats a set of instructions for as long as a [condition](https://github.com/qitianshi/tyros-resources/tree/main/Lesson%203#conditions) is true.

This is what a basic while loop looks like. Just like with if/else statements, the [indentation](https://github.com/qitianshi/tyros-resources/tree/main/Lesson%203#indentation) is important.

```Python
while SOME_CONDITION:
    print("Looped")
```

First, the condition (in this case, `SOME_CONDITION`) is checked. If it evaluates to `True`, the contents of the loop is performed once (`print("Looped")`). Afterward, it checks the condition again to see if it's still `True`, and if so, repeats the loop contents again. If at any point the condition evaluates to `False`, the loop exits. You can think of the while loop as a repeating if statement.

On the game show _The Price is Right_, contestants guess the prices of various items. The winner is the one whose guess is the closest to the actual price, without going over. Let's try writing some code that continually accepts guesses, until one goes over.

```Python
actual_price = 50
guess = 0

while guess <= actual_price:
    guess = float(input("What's your guess? "))

print("You've gone over!")
```

Try running this code and typing in different guesses. You'll see that as long as the condition is true (your guess being less than the actual price), the contents of the loop repeat indefinitely, over and over again. But, the moment your guess goes over, the condition will be false, the loop will exit, and the programme moves on to `print("You've gone over!")`.

Notice that we've had to _initialise_ the `guess` variable in line 2 by giving it a starting value (`0`, in this case). Try commenting out that line and see what happens. When the while loop goes to check the condition, the `guess` variable would be undefined, and we'd get an error. It's important to not only define our variables, but also to give them a meaningful starting value. In the example above, if our initial value had been greater than 50, the while loop would never have run!

### While loop conditions
Try running this.

```python
is_raining = False

while is_raining:
    print("It's raining.")

print("The loop's finished.")
```

When you run the code, it's as if the while loop weren't there at all. The while loop checks the condition, realises it's `False`, and then just moves on without ever running the contents of the loop. And so, the loop never runs!

Now, try changing the value of `is_raining` to `True`:

```python
is_raining = True

while is_raining:
    print("It's raining.")

print("The loop's finished.")
```

We know that while loops will run for as long as their condition is true. In this case, no part of our code ever changes the value of `is_raining`, so its value is forever `True`. We've just created an infinite loop! This while loop will run forever and never stop. Since we don't have an infinite amount of time on our hands, let's go ahead and interrupt the programme with the stop button.

You would've realised by now that, in practice, it's not very meaningful to have a while loop whose condition is an unchanging `True` or `False`. Most of the time, our code will somehow modify the condition so that the loop eventually ends. In our _Price is Right_ example, this happens when the user inputs different numbers.

Infinite loops are especially problematic. When a loop runs forever, our programme will be stuck in the loop, and never proceed to the next part. In the above example, our code will never get to `print("The loop's finished.")`. In fact, when you're using your phone and an app freezes, or a window on your laptop says "Not responding", an infinite loop might be the culprit! Somewhere under the hood, the code responsible for modifying or checking a condition is failing, and as a result, the app gets stuck in a loop that it never exits from, and you'll have to force quit the app or restart your device to forcibly exit the programme.

There are, however, exceptions to this rule, [which we'll be looking at later](#infinite-loops).

## `break`
Sometimes, we want our loop to exit even though the condition hasn't been met. That's where the simple `break` statement comes in.

Let's try writing a programme that checks a password. If our user enters the correct password, we'll let them in. Otherwise, as long as they enter an incorrect password, we'll get them to keep trying. However, to prevent hackers from getting into the account by brute-forcing (trying every single possible password), we'll limit the user to 5 attempts.

```Python
correct_password = "TallLamppost@6thAve"
password_entered = input("Enter your password: ")
number_of_attempts = 0
logged_in_successfully = False

while not logged_in_successfully:

    number_of_attempts = number_of_attempts + 1        # Alternatively, you could also write: number_of_attempts += 1

    if number_of_attempts > 4:                         # The number is 4 because we've already asked for the password once before the loop.
        print("Too many attempts.")
        break

    password_entered = input("Wrong password. Try again: ")

    if password_entered == correct_password:
        logged_in_successfully = True

if logged_in_successfully:
    print("You're logged in!")
else:
    print("Login failed.")
```

`break` is a control flow statement. It exits the loop, regardless of whether the condition is met, and moves on to the next part of the programme.

Typically, we only write `break` inside of an if/else, so the loop only breaks when a condition is met. Otherwise, the loop will always break when it reaches that line, making the loop redundant!

As always, there are many ways to approach any problem in programming. It's possible to change the above code so it doesn't use the `break` statement at all, and relies entirely on the while condition. (Try coding it yourself!) As you become more experienced with programming, you'll be able to tell which situations demand which approach.

Just as a quick aside, if you're using a password like "Password1", "12345678", or your birthday, or if you're using the same password for all your accounts, please take steps to strengthen your online security. Strong passwords needn't be complicated and difficult to remember — the one we used in our example is easily memorable ("tall lamppost at Sixth Ave") but still contains upper and lowercase letters, numbers, and symbols. If there's one thing you take away from this course, make it this. [How to choose better passwords.](https://www.popsci.com/how-to-choose-safe-passwords/)

## `continue`
`continue` is similar to `break`, but instead of exiting the loop entirely, it only skips the current iteration and moves on to the next round of the loop.

Say we want to write some code that prints all numbers from 1 to 20, but skipping multiples of 3. A possible way to do it would be like this:

```Python
number = 0

while number <= 20:

    number = number + 1     # Alternatively: number += 1

    if number % 3 == 0:
        continue

    print(number)

```

`continue` causes the loop to exit its current iteration, so it skips the rest of the code (in this case, the `print` function) and moves on to the next iteration.

Just like with the `break` statement, we usually only write `continue` inside an if/else, otherwise the loop would be meaningless.

## `while True` loops
We mentioned previously that infinite loops are usually to be avoided, because they cause our programme to never end. Sometimes, however, that's actually what we want.

Remember that while loops run as long as their condition evaluates to true. We can make an infinitely running loop by simply writing `while True:`.

A shopkeeper wants a programme that helps them keep track of total revenue. It makes sense for this programme to run indefinitely, until it's switched off manually.

```Python
running_total = 0.0

while True:

    print("--------")
    print("Current revenue:", running_total)
    added_amount = float(input("Add: "))
    running_total += added_amount
```

At a fundamental level, most computers, control systems, and robotics are continuously running some form of infinite loop. For instance, you'd want your laptop to work the same way today as it did yesterday. The operating system on your laptop is essentially running in an infinite loop, because it's forever taking in your input (like your mouse and keyboard) and responding to it.

At our level, we're not working so close to the metal (the most foundational levels of computers like CPUs and RAM). When _we_ use `while True` loops, it's typically because we want our programme to perform something indefinitely (as in the above example), or because we implement checks to exit the loop elsewhere, using `break` or `continue`. You'll explore these applications in the practice questions below.

## Let's practise
In maths, the factorial of an integer is the product of that integer and all its preceding integers. It is denoted by the `!` mark. For example, `5! = 5 × 4 × 3 × 2 × 1 = 120`. Write a programme that takes in an integer, and calculates its factorial.

---

Let's play a number guessing game. The user will think of a number between 1 and 10. A Python programme will guess the number and ask if it's right or wrong. If the guess is wrong, the programme will guess again. If the guess is right, the game will finish, and the programme will display the number of rounds it's taken to guess the number correctly.

---

I want to do math with Python! Help me make a calculator that is able to add, subtract, multiply and divide.

Your programme should first display a menu that looks like this:

```
0: Quit
1: Add
2: Subtract
3: Multiply
4: Divide

Choose an option:
```

I will choose an option by typing its number. Your programme should include a check to make sure that the number I've typed in is a valid option. If it isn't, the programme should prompt me to try again.

Then, your programme should ask me for two numbers. It will then perform the operation, and display the number.

Afterwards, it should show me the original menu again, so I can make as many operations as I want.

## Conclusion
Loops are essential devices in programming that let your programme repeat a set of steps. At the most fundamental level, almost all computers are running some sort of loop. In this lesson, we learned about the while loop, a type of loop that repeats for as long as a given condition is true.

In the next lesson, we'll learn about another type of loop: the for loop.

### Further reading
* [Python while loops](https://www.w3schools.com/python/python_while_loops.asp)
* [Control flow](https://en.wikipedia.org/wiki/Control_flow)
* [Control systems](https://en.wikipedia.org/wiki/Control_system)
