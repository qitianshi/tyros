# Lesson 3 - If/else statements
# Solution to Practice Question 2

# Copyright 2022 Qi Tianshi and Tyros members. Licensed under GNU GPLv3.


# I need some help to decide how I should spend my time! I can do the following
# things depending on what is happening tomorrow:

# * Sleep early (if I have completed my homework or none of my friends are
#   online, and there is no school tomorrow)
# * Homework (if there is school tomorrow)
# * Play some games (if I have friends online and there is no school tomorrow)

# Write a program that allows me to input if I have school tomorrow, if I have
# completed my homework and if I have friends online, then print what I should
# do!


school_tomorrow = input("Do I have school tomorrow? (Yes/No) ")
completed_homework = input("Have I completed my homework? (Yes/No) ")
friends_online = input("Do I have friends online (Yes/No) ")

if (completed_homework == "Yes" or friends_online == "No") and school_tomorrow == "No":
    print("Sleep early")
if school_tomorrow == "Yes":
    print("Homework")
if friends_online == "Yes" and school_tomorrow == "No":
    print("Play some games")
