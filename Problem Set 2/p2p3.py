# -*- coding: utf-8 -*-
"""
MITx: 6.00.1x
Problem Set 2
Problem 3
Miko Man

Specification:
Write a program that uses these bounds and bisection search  to find the 
smallest monthly payment to the cent such that we can pay off the debt within 
a year.

Inputs:
    balance: the outstanding balance on a credit card
    annualInterestRate: annual interest rate as a decimal

Returns;
    Smallest monthly payment that will pay off all debt within a year
"""
# Initialize variables
monthlyInterestRate = annualInterestRate / 12.0
lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0
remainingBalance = balance

# Check if remaining debt is within the range of $0.01, otherwise use bisection search for a new guess
while abs(remainingBalance) > 0.01:
    remainingBalance = balance
    guess = (lowerBound + upperBound) / 2
    
    # Compute balance at the end of a year with guess
    for month in range(1, 13):
        monthlyUnpaidBalance = remainingBalance - (guess)
        remainingBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    
    # Set lower or upperbound according to results
    if remainingBalance > 0:
        lowerBound = guess
    elif remainingBalance < 0:
        upperBound = guess
        
# Print smallest monthly payment tha will pay off all debt within a year
print("Lowest Payment: " + str(round(guess, 2)))