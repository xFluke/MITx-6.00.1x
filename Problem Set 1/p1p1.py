# -*- coding: utf-8 -*-
"""
MITx: 6.00.1x
Problem Set 1
Problem 1
Miko Man

Specification:
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s
"""
vowelCount = 0
for letters in s:
    if letters == 'a' or letters == 'e' or letters == 'i' or letters == 'o' or letters == 'u':
        vowelCount += 1
print("Number of vowels: ", vowelCount)