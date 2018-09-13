# -*- coding: utf-8 -*-
"""
MITx: 6.00.1x
Exercise: Guess My Number
Miko Man

Specification:
Create a program that guesses a secret number.
The program works as follows: you (the user) thinks of an integer between 0 
(inclusive) and 100 (not inclusive). The computer makes guesses, and you give 
it input - is its guess too high or too low? Using bisection search, 
the computer will guess the user's secret number!
"""
low = 0
high = 100
guess = 50
print("Please think of a number between 0 and 100!")
userInput = ""
while userInput != 'c':
    print("Is your secret number " + str(guess) + "?")
    userInput = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if userInput != 'h' and userInput != 'l' and userInput != 'c':
        print("Sorry, I did not understand your input.")
    elif userInput == 'c':
        print("Game over. Your secret number was: " + str(guess))
    else:
        if userInput == 'h':
            high = guess
        else:
            low = guess
        guess = (high + low) // 2
        
        