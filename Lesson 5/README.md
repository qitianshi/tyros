# Lesson 5 - For loops

## Introduction
[In the previous lesson](https://github.com/qitianshi/tyros-resources/tree/main/Lesson%204), we learnt about how to use while loops to repeat a particular set of steps.

However, while loops are not the only type of loops available at our disposal! Sometimes, we do want computers to repeatedly do things over and over again, but we want them to stop after some number of times! We are actually able to achieve this by usin what we will be looking at in today's lesson: for loops.

## The `for` loop
If you recall from our previous lesson, a while loop repeats a set of instructions for as long as a condition is true. However, a for loop is different! A for loop repeats a set of instructions a specified number of times!

This is what a basic for loop looks like. Just like with previous concepts we have learnt (like the while loop), the indentation is especially important.

```python
for SOME_VARIABLE in range(START, END, STEP):
    print("Looped")
```

A question we have to first ask ourselves is: is there a condition here? The answer is: yes! There actually is a condition. It is just presented to us as the `range` function. (More on that later...) So long as this condition is fulfilled, the contents of the loop (`print("Looped")`) will be performed. You might also notice that we introduce `SOME_VARIABLE` here. The purpose of that is because when we use the `range()` function, we actually assign a value to `SOME_VARIABLE`. Without it, our for loop would not work!

Before we dive into the specifics, let us first look at an example of how the for loop is used!

Do you remember the game show *The Price is Right* from last time?

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

Well, one contestant figured out a loophole, and guessed 1, 2, 3... all the way until the actual price. And our poor game show master could not do anything. It wasn't against the rules!

Now, instead of guessing until they reach the actual price, we give them a fixed number of guesses. Let's try writinsome code that accepts guesses for a fixed number of times, say 10 times.

```python
actual_price = 50

for i in range(0, 10):
    guess = float(input("What's your guess? "))
    
    if guess == actual_price:
        print("You got it!)
        break    # terminate loop after correct guess
        
    elif guess < actual_price:
        print("Too low...)
    
    else:
        print("Too high...")
```

Try running this code and type in different guesses! You'll see that if you keep getting wrong guesses, you will only get ten tries in total. (But if you get the correct guess, then you wouldn't need the additional tries either, so you just... finish.)

### `range()`
You might have guessed that we control the number of times we repeat the for loop above using the `range()` function, and you are right! 
