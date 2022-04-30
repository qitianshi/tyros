# Lesson 5 - For Loops

## Introduction
In the previous lesson, we learnt about using while loops to repeat parts of our programme. [Head here if you need a refresher on the previous lesson.](https://github.com/qitianshi/tyros-resources/tree/main/Lesson%204)

But what if we knew the number of times we wanted to repeat our code? This is where we introduce for loops!

## For Loops
A for loop is quite similar to a while loop - both allow for repetition. For our purposes, the main difference between the while loop and the for loop is that we are able to control the number of times the code within the loop repeats itself for the for loop!

Before we dive into any examples, we need to first look at the `range()` function.

### `range()`
The `range()` function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number. For instance, `range(6)` gives us the values from 0 to 5, *but not 6*.

We can also specify our own start and end points, as well as how large (or small) our increments are!
- `range(1, 6)` gives us values from 1 to 5
- `range(9, 82, 9)` gives us 9, 18, 27, 36, 45, 54, 63, 72, 81
- `range(10, 0, -1)` gives us 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

In general, the `range()` function follows this syntax:
