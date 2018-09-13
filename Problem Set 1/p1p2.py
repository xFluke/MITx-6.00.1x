# -*- coding: utf-8 -*-
"""
MITx: 6.00.1x
Problem Set 1
Problem 2
Miko Man

Specification:
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s
"""
bobCount = 0

for i in range(len(s) - 1):
    if s[i:i+3] == 'bob':
        bobCount += 1
print("Number of times bob occurs is: ", bobCount)
