# -*- coding: utf-8 -*-
"""
MITx: 6.00.1x
Problem Set 2
Problem 1
Miko Man

Specification:
Write a program to calculate the credit card balance after one year if a person 
only pays the minimum monthly payment required by the credit card company each 
month.

Input:
    balance: the outstanding balance on the credit card
    annualInterestRate: annual interest rate as a decimal
    monthlyPaymentRate: the minimum monthly payment rate as a decimal

Returns:
    Remaing balance at the end of a year
"""
# Initialize variables
remainingBalance = balance
monthlyInterestRate = annualInterestRate / 12.0

# Compute remaining balance after each month
for month in range(1,13):
    minimumMonthlyPayment = monthlyPaymentRate * remainingBalance
    monthlyUnpaidBalance = remainingBalance - (monthlyPaymentRate * remainingBalance)
    remainingBalance = round(monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance), 2)

# Print result
print("Remaining balance: " + str(round(remainingBalance, 2)))