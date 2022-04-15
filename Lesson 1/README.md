# Lesson 1 — the `print` statement, comments, and variables

## An introduction
Computer science is about using computers to solve problems.

To tell them what to do, we need to give them instructions. If I were to tell you to do something, I'd speak to you in a language, like English. Computers don't understand English though, so we must speak to them with *programming languages*. Python is an example of a programming language, and it's what we'll be learning!

Now that you've written your instructions in Python, your computer will perform your instructions step by step, line by line. Imagine you're baking a cake. You might see something like this:

```
1. Mix flour, eggs, sugar, and butter in a bowl.
2. Pour the mixture into a tin and bake.
3. Decorate your cake with icing.
```

If the instructions are wrong or their order is messed up, you wouldn't get a delicious cake! Writing programs is like writing a recipe. You must write exactly the correct instructions, and in the right order, to make your computer do what you want.

## `print()`
We can use `print()` to output something.

Anything between the brackets is printed. Remember to add quotation marks if you're printing text.

```Python
print("Hello, world!")
```

## Comments
Comments are useful for documenting and explaining our code. Everything that follows a `#` sign is a comment.

```Python
# This is a comment
print("Hello, world!")       # This is also a comment.
```

## Variables
Variables store values. You can imagine them like labelled boxes that contain different objects. The object inside the box is the value of the variable. The label on the box is the name of the variable.

In this example, we created a variable called "myVar" and gave it the value of "Hello".

```Python
greeting = "Hello"
```

We can use the names of variables to refer to the value they contain.

```Python
print(greeting)
```

```
> Hello
```

Variables can have any name you like, as long as they only contain letters, numbers, and underscores, and they can't begin with numbers. `var`, `firstVar`, `my_fav_variable`, `VARIABLE`, and `value1` are allowed, but `1number` and `my-var` aren't.

### Data types
Data comes in different types. The four main ones are *strings*, *integers*, *floats*, and *bools*.

Strings are for text, like letters, words, punctuation, and even sentences. All strings have quotation marks `"` around them.

```Python
stringType = "I'm a string!"
```

Integers are for positive or negative whole numbers.

```Python
integerType = 20
```

Floats are for any non-whole number. In Python, if a number has a decimal place, it's a float.

```Python
floatType = 1.5
```

Finally, bools can have two values, `True` or `False`. They represent 1s and 0s in our computers.

```Python
boolType = True
```

### Operations on variables
We can use math operators like `+-*/` to manipulate variables and data.

```Python
thisYear = 2022
birthYear = 1990
myAge = thisYear - birthYear                # Doing math with variables
print("This year I am", myAge, "years old!")
```

```
> This year I am 32 years old!
```

We can also use the `+` operator to join strings.

```Python
firstName = "Puja"
lastName = "Soni"
fullName = firstName + " " + lastName       # Using + to join strings
print("My full name is", fullName)
```

```
> My full name is Puja Soni
```

We'll learn more about operators next week!

### Modifying variables
Variables can be modified! We can assign them new values, and they'll forget their old values.

```Python
gst = 7
print("The GST is", gst)

gst = 9
print("The GST has changed to", gst)
```

```
> The GST is 7
> The GST has changed to 9
```

## Thinking time!
What happens if you try to run this code?

```Python
print(Hello world)
```

You'll get an error! If we want to print a string, we must put quotation marks `"` around them. Otherwise, Python will try to look for variables called "Hello" and "world"!

---

Why do the two `print` statements not print the same result?

```Python
var = 5

print(var)
print("var")
```

```
> 5
> var
```

In the first one, we didn't use quotation marks. Python sees `var` as a variable name, and prints the value of the `var` variable, which is `5`. In the second, we put quotation marks around it, so now `"var"` is recognized as a string. It will literally print "var"!

---

What do you think the output of this code will be?

```Python
var = 5
var = "Hi!"

print(var)
```

It just prints `Hi!`. When a new value is assigned, the variable forgets its old value.

## Conclusion
In this lesson you learned about how to get output from your Python code using the `print` statement, how to write notes in your code with comments, and how to create, modify, and print variables. In the next lesson you'll learn more about what we can do with these simple tools!

---
© 2022 Qi Tianshi. This file is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International license (CC BY-NC-SA 4.0) license](https://creativecommons.org/licenses/by-nc-sa/4.0/).
