# -*- coding: utf-8 -*-
"""
MITx: 6.00.1x
Problem Set 1
Problem 3
Miko Man

Specification:
Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order.     
"""
longestSubstring = s[0]
newSubstring = ""

for letters in s:
    if newSubstring == "":
        newSubstring = letters
    elif letters >= newSubstring[-1]:
        newSubstring += letters
        if len(newSubstring) > len(longestSubstring):
            longestSubstring = newSubstring
    else:
        newSubstring = letters

print("Longest substring in alphabetical order is: " + longestSubstring)