# -*- coding: utf-8 -*-
"""
MITx: 6.00.1x
Problem Set 2
Problem 2
Miko Man

Specification:
Write a program that calculates the minimum fixed monthly payment needed in 
order to pay off a credit card balance within 12 months.

Input:
    balance: the outstanding balance on the credit card
    annualInterestRate: annual interest rate as a decimal
    
Returns:
    Lowest monthly payment that will pay off all debt in under a year
"""
# Initialize variables
monthlyInterestRate = annualInterestRate / 12.0
remainingBalance = balance
fixedPayment = 0

# Check if debt is paid off, otherwise increment fixed payment by 10
while remainingBalance >= 0:
    fixedPayment += 10
    remainingBalance = balance
    
    
    # Compute balance at the end of a year with monthly fixed payment
    for month in range(1, 13):
        monthlyUnpaidBalance = remainingBalance - (fixedPayment)
        remainingBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        
# Print lowest monthly payment that will pay off all debt
print("Lowest Payment: " + str(fixedPayment))