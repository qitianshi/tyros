# Lesson 4 - While Loops

## Introduction
In the previous lesson, we learnt about how to use if/else statements to make our code do different things in different situations. [Here are the notes from Lesson 3 if you need a refresh.](https://github.com/qitianshi/tyros-resources/tree/main/Lesson%203)

Everything that we have learnt so far allows us to execute specific things once! After our code finishes a particular step we tell it to execute, it moves on to the next one. But what if we need it to repeat a particular step multiple times? This is where we introduce loops!

## The `while` statement
Similar to its use in the English language, `while` hints to us that there needs to be a [condition](https://github.com/qitianshi/tyros-resources/tree/main/Lesson%203#conditions) in place for some things to happen.

I want to go to the beach! This would mean that I am (very anxiously) monitoring the weather. I see that it is raining right now, so let's set a variable `is_raining` to `True`:

```python
is_raining = True

while is_raining:
    print('it is still raining')
```

Now what happens if we run this snippet of code? The `while` loop will keep running so long as `is_raining` is `True`, so this will run forever! A key feature of the `while` loop is that so long as the condition *stays* fulfilled, the code within the loop (do you remember how to determine which lines are within the loop?) will be repeatedly executed.

## Preventing infinite loops
Now the question is, how do we stop a `while` loop? Not to worry, there are a few ways to do this!

### By modifying the conditional
Remember that the `while` loop checks for a condition before it decides whether to repeat the code within its body. As such, so long as we are able to modify the conditional within the loop, then the `while loop will be able to terminate and we can move on to other things in life.

```python
is_raining = True

while is_raining:
    print('it is still raining')
    
    # check if it is still raining
    weather_check = input('is it still raining? (Y/N): ')
    if weather_check == 'N':
        is_raining = False

print('it finally stopped raining')
```

Try running the above code! Here, by checking the condition of the weather using the `if` statement, we are able to modify the value of the conditional! This therefore allows us to control when we want to exit the loop.

This also works in situations when you are not asking for an input!

```python
tracker = 0

while tracker < 5:
    print(tracker)
    tracker += 1
print('tracker reached 5')
```

```
> 0
> 1
> 2
> 3
> 4
> tracker reached 5
```

### Using the `break` statement
The `break` statement forces our programmme to exit the loop.

```python
is_raining = True

while is_raining:
    print('it is still raining')
    
    # check if it is still raining
    weather_check = input('is it still raining? (Y/N): ')
    if weather_check == 'N':
        break

print('it finally stopped raining')
```

## Let's practise
